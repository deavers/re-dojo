// RE:DOJO map - headless Chrome end-to-end test for docs/dojo-map.html (CDP, no npm deps).
//
// Requires: Node 22+ (global fetch/WebSocket), Python 3.10+, Google Chrome or Chromium.
// Usage (from the repo root):
//   node Tools_and_Scripts/tests/e2e_dojo_map.mjs
//   CHROME_PATH=/path/to/chrome PYTHON=python3 node Tools_and_Scripts/tests/e2e_dojo_map.mjs
// It builds a FIXTURE page with test-stub hints in a temp dir (nothing is written to data/ or docs/),
// drives it through clicks, then smoke-tests the committed docs/dojo-map.html.
// Not part of CI (needs a browser). Screenshots are left in the printed temp folder.
import { spawn, spawnSync } from "node:child_process";
import { writeFileSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, existsSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const REAL_PAGE = path.join(ROOT, "docs", "dojo-map.html");
const outDir = mkdtempSync(path.join(os.tmpdir(), "re-dojo-e2e-"));
const PYTHON = process.env.PYTHON || (process.platform === "win32" ? "python" : "python3");
const CHROME = process.env.CHROME_PATH || [
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
].find((p) => existsSync(p));
if (!CHROME) { console.error("Chrome not found. Set CHROME_PATH."); process.exit(2); }

// --- fixture: test-stub hints (NOT real hints; they only exercise the UI)
const KIND = { 1: "nudge", 2: "concept", 3: "near_spoiler" };
const H = (level, text, source, refs = []) => ({ level, kind: KIND[level], text, source, refs });
const LAB10 = "Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp";
const hintsDir = path.join(outDir, "hints");
mkdirSync(hintsDir);
writeFileSync(path.join(hintsDir, "batch_test.json"), JSON.stringify({ batch: 0, entries: {
  g019: { status: "draft", hints: [
    H(1, "TEST STUB: start from an exact value scan.", "my_notes", ["Game_Hacking/README.md#1-plants-vs-zombies-goty-tier-e--21--10"]),
    H(2, "TEST STUB: notes mention +0x5560 on Board.", "my_notes", ["Game_Hacking/README.md"]),
    H(3, "TEST STUB: see the AOB script in the table.", "my_notes", ["Game_Hacking/PvZ.CT"])] },
  g199: { status: "draft", hints: [
    H(1, "TEST STUB: what does an integrity check protect?", "needs_verification"),
    H(2, "TEST STUB: hashing code pages vs a reference.", "repo_catalog"),
    H(3, "TEST STUB: practice on your own Lab 10 binary.", "needs_verification", [LAB10])] },
} }));
const run = (args) => {
  const r = spawnSync(PYTHON, args, { cwd: ROOT, encoding: "utf-8" });
  if (r.status !== 0) { console.error(r.stdout, r.stderr); process.exit(2); }
};
const fixtureGames = path.join(outDir, "games.json");
const pagePath = path.join(outDir, "fixture-map.html");
run(["Tools_and_Scripts/build_games_json.py", "--hints-dir", hintsDir, "--out", fixtureGames]);
run(["Tools_and_Scripts/validate_games.py", "--file", fixtureGames]);
run(["Tools_and_Scripts/build_dojo_map.py", "--games", fixtureGames, "--out", pagePath]);

const PORT = 9339;
const profile = path.join(outDir, "profile");
const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
  "--no-first-run", "--disable-extensions", "--window-size=1400,900", "about:blank"], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

let ws, seq = 0;
const pending = new Map();
const problems = [];
async function connect() {
  for (let i = 0; i < 50; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: "PUT" });
      const t = await r.json();
      ws = new WebSocket(t.webSocketDebuggerUrl);
      await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
      ws.onmessage = (ev) => {
        const m = JSON.parse(ev.data);
        if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
        if (m.method === "Runtime.exceptionThrown") problems.push("EXCEPTION " + JSON.stringify(m.params.exceptionDetails).slice(0, 400));
        if (m.method === "Runtime.consoleAPICalled" && ["error", "warning"].includes(m.params.type)) problems.push("CONSOLE " + JSON.stringify(m.params.args).slice(0, 300));
        if (m.method === "Log.entryAdded" && ["error", "warning"].includes(m.params.entry.level)) problems.push("LOG " + m.params.entry.text.slice(0, 300));
      };
      return;
    } catch (e) { await sleep(200); }
  }
  throw new Error("chrome did not start");
}
const send = (method, params = {}) => new Promise((res) => { const id = ++seq; pending.set(id, res); ws.send(JSON.stringify({ id, method, params })); });
async function ev(expr) {
  const r = await send("Runtime.evaluate", { expression: expr, awaitPromise: true, returnByValue: true });
  if (r.result.exceptionDetails) throw new Error("eval failed: " + expr + " -> " + JSON.stringify(r.result.exceptionDetails).slice(0, 300));
  return r.result.result.value;
}
async function nav(url) { await send("Page.navigate", { url }); await sleep(900); }
async function shot(name, w, h, mobile = false) {
  await send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 1, mobile });
  await sleep(400);
  const r = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(path.join(outDir, `${name}.png`), Buffer.from(r.result.data, "base64"));
}
const results = [];
function check(name, cond, detail = "") { results.push(`${cond ? "PASS" : "FAIL"} ${name}${detail ? " :: " + detail : ""}`); }
const click = (sel) => ev(`(() => { const e = document.querySelector(${JSON.stringify(sel)}); if (!e) return false; e.click(); return true; })()`);

await connect();
await send("Runtime.enable"); await send("Log.enable"); await send("Page.enable");
const url = pathToFileURL(pagePath).href;
await nav(url);
await ev("localStorage.clear()"); await nav(url);

check("220 tiles rendered", (await ev("document.querySelectorAll('.tile').length")) === 220);
check("start rank F-", (await ev("document.getElementById('rankCode').textContent")) === "F-");
check("count label split by kind", (await ev("document.getElementById('shownCount').textContent")) === "Игры: 200 из 200 · Лабы и крякми: 18 из 18 · Квесты: 2 из 2");
check("tier headers render above dependency edges", (await ev("(() => { const h = getComputedStyle(document.querySelector('.band-head')); return Number(h.zIndex) > Number(getComputedStyle(document.getElementById('edges')).zIndex) && h.backgroundColor !== 'rgba(0, 0, 0, 0)'; })()")) === true);
const lockedGames = await ev("[...document.querySelectorAll('.tile.kind-game.locked')].length");
check("all 200 games locked at start (lowest game tier F+ > F)", lockedGames === 200, String(lockedGames));

// open g019 while locked
await click('.tile[data-id="g019"]');
check("panel opens with title", (await ev("document.getElementById('pTitle').textContent")) === "Plants vs. Zombies GOTY");
check("hint button disabled while locked", (await ev("document.getElementById('btnHint').disabled")) === true);
check("done button disabled while locked", (await ev("document.getElementById('btnDone').disabled")) === true);
check("my_notes badge shown", (await ev("[...document.querySelectorAll('#panelBody .src.mine')].length")) > 0);
const edges = await ev("document.querySelectorAll('#edgeLayer path').length");
check("dependency edges drawn to prereq labs", edges === 3, String(edges));

// free mode: reveal hints in order
await click("#btnFree");
check("free mode unlocks hint button", (await ev("document.getElementById('btnHint').disabled")) === false);
for (let i = 1; i <= 3; i++) {
  await click("#btnHint");
  const levels = await ev("[...document.querySelectorAll('#panelBody article.hint')].map(a => a.getAttribute('aria-label'))");
  check(`hint ${i} revealed in order`, levels.length === i && levels[i - 1] === `Подсказка ${i}`, JSON.stringify(levels));
}
check("no further hint button after 3", (await ev("!document.getElementById('btnHint')")) === true);
await shot("desktop-g019-hints", 1400, 900);
check("award reduced by hints (300*0.4=120)", (await ev("document.getElementById('btnDone').textContent")).includes("+120 EXP"));
await click("#btnDone");
check("EXP updated", (await ev("document.getElementById('statExp').textContent")) === "120");

// persistence
await nav(url);
check("progress persisted after reload", (await ev("document.getElementById('statExp').textContent")) === "120");
check("hint count persisted", (await ev("document.getElementById('statHints').textContent")) === "3");

// restricted node
await click('.tile[data-id="g199"]');
const banner = await ev("[...document.querySelectorAll('#panelBody .banner')].map(b => b.textContent).join(' | ')");
check("restricted banner on g199", banner.includes("Ограниченный уровень") && banner.includes("Lab 10"), banner.slice(0, 120));
await click('.tile[data-id="g176"]');
const b176 = await ev("[...document.querySelectorAll('#panelBody .banner')].map(b => b.textContent).join(' | ')");
const tools176 = await ev("[...document.querySelectorAll('#panelBody span.chip')].map(c => c.textContent).join(' ')");
check("g176 restricted, redirected to CM 03, no Il2CppDumper", b176.includes("Ограниченный уровень") && b176.includes("CM 03") && !tools176.includes("Il2CppDumper"), b176.slice(0, 120));
await click('.tile[data-id="g002"]');
const amb = await ev("(() => { const p = document.querySelector('#panelBody .engine-unknown'); return p ? p.textContent : ''; })()");
const g002 = await ev("[...document.querySelectorAll('#panelBody span.chip')].map(c => c.textContent).join(' ')");
check("ambiguous engine: 'unknown [нужна проверка]', no Mono Dissector", amb.includes("Техники движка: unknown") && amb.includes("[нужна проверка]") && !g002.includes("Mono Dissector"), amb.slice(0, 120));
await click('.tile[data-id="q_ss_legacy_drm"]');
check("restricted campaign quest present", (await ev("document.getElementById('pTitle').textContent")).includes("Legacy DRM"));

// rank logic without free mode
await ev("localStorage.clear()"); await nav(url);
await click('.tile[data-id="lab01"]'); await click("#btnDone");
await click('.tile[data-id="lab02"]'); await click("#btnDone");
check("lab01 + lab02 -> rank F (breakthrough rule)", (await ev("document.getElementById('rankCode').textContent")) === "F");
check("F+ games now unlocked", (await ev("!document.querySelector('.tile[data-id=\"g001\"]').classList.contains('locked')")) === true);
check("E-- games still locked", (await ev("document.querySelector('.tile[data-id=\"g005\"]').classList.contains('locked')")) === true);

// filters
await ev(`(() => { const s = document.getElementById('fEngine'); s.value = 'unity_mono'; s.dispatchEvent(new Event('input', { bubbles: true })); })()`);
check("engine filter unity_mono -> 23", (await ev("document.querySelectorAll('.tile').length")) === 23);
check("counter under a game-only filter", (await ev("document.getElementById('shownCount').textContent")) === "Игры: 23 из 200 · Лабы и крякми: 0 из 18 · Квесты: 0 из 2");
await ev(`(() => { const s = document.getElementById('fEngine'); s.value = 'ambiguous'; s.dispatchEvent(new Event('input', { bubbles: true })); })()`);
check("engine filter ambiguous -> 17", (await ev("document.querySelectorAll('.tile').length")) === 17);
await ev(`(() => { document.getElementById('filters').reset(); const s = document.getElementById('fSearch'); s.value = 'isaac'; s.dispatchEvent(new Event('input', { bubbles: true })); })()`);
await sleep(50);
const isaac = await ev("[...document.querySelectorAll('.tile')].map(t => t.dataset.id)");
check("search 'isaac'", isaac.includes("g074"), JSON.stringify(isaac));
await ev(`(() => { const s = document.getElementById('fSearch'); s.value = 'pointer'; s.dispatchEvent(new Event('input', { bubbles: true })); })()`);
await sleep(50);
{
  const ids = await ev("[...document.querySelectorAll('.tile')].map(t => t.dataset.id)");
  const g = ids.filter((x) => x.startsWith("g")).length, l = ids.filter((x) => /^(lab|cm)/.test(x)).length;
  check("counter matches visible tiles per kind", (await ev("document.getElementById('shownCount').textContent")) === `Игры: ${g} из 200 · Лабы и крякми: ${l} из 18 · Квесты: 0 из 2` && l > 0 && g > 0, `${g} games, ${l} labs`);
}
await ev(`(() => { document.getElementById('filters').reset(); })()`); await sleep(50);
await ev(`(() => { const s = document.getElementById('fStatus'); s.value = 'notes'; s.dispatchEvent(new Event('input', { bubbles: true })); })()`);
check("status 'with my notes' -> 4 games", (await ev("document.querySelectorAll('.tile').length")) === 4);

// deep link + import sanitizing
await ev("localStorage.setItem('re_dojo_map_v1', JSON.stringify({v:1, done:{g001:{exp:999999}, nope:{exp:1}, lab01:{exp:100}}, hints:{g019:99}, free:'yes'}))");
await nav("about:blank"); await nav(url + "#g074");
check("deep link opens g074", (await ev("document.getElementById('pTitle') && document.getElementById('pTitle').textContent")) === "The Binding of Isaac: Repentance");
check("tampered storage sanitized", (await ev("document.getElementById('statExp').textContent")) === "100");
check("existing app key untouched", (await ev("localStorage.getItem('re_rpg_journey_state_v2') === null")) === true);
await shot("mobile-g074", 390, 844, true);
check("no horizontal scroll at 390px", (await ev("document.documentElement.scrollWidth")) <= 390, String(await ev("document.documentElement.scrollWidth")));
await send("Emulation.setDeviceMetricsOverride", { width: 1400, height: 900, deviceScaleFactor: 1, mobile: false }); await sleep(300);
await ev("window.scrollTo(0, 3000)"); await sleep(200);
check("sticky panel sits below filter bar", (await ev("document.getElementById('panel').getBoundingClientRect().top >= document.getElementById('filters').getBoundingClientRect().bottom - 1")) === true);
await send("Emulation.clearDeviceMetricsOverride");


// ---------------- export / import / reset / theme
{
    const dl = path.join(outDir, "dl"); rmSync(dl, { recursive: true, force: true }); mkdirSync(dl, { recursive: true });
  await send("Browser.setDownloadBehavior", { behavior: "allow", downloadPath: dl });
  await nav("about:blank"); await ev("1"); await nav(url);
  await ev("localStorage.clear()"); await nav("about:blank"); await nav(url);
  await click('.tile[data-id="lab01"]'); await click("#btnDone");
  await click("#btnFree");
  await click("#btnExport");
  let file = null;
  for (let i = 0; i < 30 && !file; i++) { await sleep(200); const f = readdirSync(dl).filter((x) => x.endsWith(".json")); if (f.length) file = path.join(dl, f[0]); }
  check("export downloads a JSON file", !!file, file || "no file");
  if (file) {
    const j = JSON.parse(readFileSync(file, "utf-8"));
    check("export content", j.app === "re-dojo-map" && j.done.lab01 && j.done.lab01.exp === 100 && j.free === true, JSON.stringify(j).slice(0, 160));
  }
  // reset (confirm auto-accepted)
  await ev("window.confirm = () => true");
  await click("#btnReset");
  check("reset clears progress", (await ev("document.getElementById('statExp').textContent")) === "0" && (await ev("localStorage.getItem('re_dojo_map_v1')")).includes('"done":{}'));
  // import a valid file (with junk that must be dropped)
  const good = path.join(outDir, "import-good.json");
  writeFileSync(good, JSON.stringify({ app: "re-dojo-map", v: 1, done: { lab01: { exp: 100 }, lab02: { exp: 120 }, g001: { exp: 99999 }, evil: { exp: 5 } }, hints: { g019: 2, lab01: 7 }, free: false, theme: "light" }));
  const setFile = async (fp) => {
    const doc = await send("DOM.getDocument", {});
    const q = await send("DOM.querySelector", { nodeId: doc.result.root.nodeId, selector: "#fileImport" });
    await send("DOM.setFileInputFiles", { nodeId: q.result.nodeId, files: [fp] });
    await sleep(500);
  };
  await setFile(good);
  check("import valid file -> sanitized progress (lab01+lab02 only)", (await ev("document.getElementById('statExp').textContent")) === "220");
  check("import -> rank F", (await ev("document.getElementById('rankCode').textContent")) === "F");
  check("import -> theme light applied", (await ev("document.documentElement.getAttribute('data-theme')")) === "light");
  check("import -> hint counter clamped to existing hints", (await ev("document.getElementById('statHints').textContent")) === "2");
  await shot("desktop-light-theme", 1400, 900);
  await send("Emulation.clearDeviceMetricsOverride");
  // import an invalid file -> state unchanged, toast shown
  const badf = path.join(outDir, "import-bad.json");
  writeFileSync(badf, JSON.stringify({ done: { lab01: { exp: 1 } } }));
  await setFile(badf);
  check("import foreign JSON rejected", (await ev("document.getElementById('statExp').textContent")) === "220" && (await ev("document.getElementById('toast').textContent")).includes("Не удалось"));
  const notjson = path.join(outDir, "import-notjson.json");
  writeFileSync(notjson, "<script>alert(1)</script>");
  await setFile(notjson);
  check("import non-JSON rejected", (await ev("document.getElementById('statExp').textContent")) === "220");
  // theme toggle flips and persists
  const bg = () => ev("getComputedStyle(document.body).backgroundColor");
  const bgLight = await bg();
  await click("#btnTheme");
  const t1 = await ev("document.documentElement.getAttribute('data-theme')");
  const bgDark = await bg();
  check("theme toggle light -> dark", t1 === "dark" && bgDark !== bgLight, `${bgLight} -> ${bgDark}`);
  await nav("about:blank"); await nav(url);
  check("theme persists after reload", (await ev("document.documentElement.getAttribute('data-theme')")) === "dark");
  await click("#btnTheme");
  check("theme toggle dark -> light", (await ev("document.documentElement.getAttribute('data-theme')")) === "light");
}

// real (committed) page: no hints yet
await ev("localStorage.clear()");
await nav(pathToFileURL(REAL_PAGE).href + "#g019");
check("real page: empty-hints message", (await ev("document.getElementById('panelBody').textContent")).includes("ещё не написаны"));
await shot("desktop-real-overview", 1400, 900);
await ev("window.scrollTo(0, 0)");

check("no console errors / CSP violations / exceptions", problems.length === 0, problems.join("\n"));
const failed = results.filter((r) => r.startsWith("FAIL")).length;
console.log(results.join("\n"));
console.log(`\n${results.length - failed}/${results.length} checks passed. Screenshots: ${outDir}`);
ws.close(); chrome.kill();
await sleep(500);
try { rmSync(profile, { recursive: true, force: true }); } catch (e) { /* Chrome may still hold files */ }
process.exit(failed ? 1 : 0);
