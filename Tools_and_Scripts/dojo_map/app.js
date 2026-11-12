"use strict";
/* RE:DOJO map - offline single-page game. No network, no innerHTML: all text goes through textContent. */
(() => {
  const DATA = JSON.parse(document.getElementById("dojo-data").textContent);
  const STORAGE_KEY = "re_dojo_map_v1";
  const HINT_PENALTY = 0.2;   // each opened hint: -20% EXP for that level
  const MIN_FACTOR = 0.4;     // never below 40% of the tier EXP

  const TIERS = DATA.tiers;
  const TIER_IDX = Object.fromEntries(TIERS.map((t, i) => [t.code, i]));
  const NODES = [...DATA.labs, ...DATA.quests, ...DATA.games];
  const BY_ID = new Map(NODES.map((n) => [n.id, n]));
  const KIND_ORDER = { lab: 0, crackme: 1, campaign_quest: 2, game: 3 };
  const BY_TIER = TIERS.map(() => []);
  for (const n of NODES) BY_TIER[TIER_IDX[n.tier]].push(n);
  for (const list of BY_TIER) {
    list.sort((a, b) => (KIND_ORDER[a.kind] - KIND_ORDER[b.kind]) || String(a.rank || a.id).localeCompare(String(b.rank || b.id)));
  }
  const DEPENDENTS = new Map();
  for (const n of NODES) {
    for (const lab of n.prerequisites.labs) {
      if (!DEPENDENTS.has(lab)) DEPENDENTS.set(lab, []);
      DEPENDENTS.get(lab).push(n.id);
    }
  }

  const TECH_LABEL = {
    exact_value_scan: "Точный скан значений", float_double_scan: "Float/Double скан", bitmask_flags: "Битовые маски/флаги",
    struct_dissect: "Разбор структур", pointer_scan: "Pointer scan", pointer_chain: "Цепочки указателей",
    aob_injection: "AOB-инъекция", nop_patch: "NOP / патчинг", code_cave: "Code cave", shared_code_filter: "Фильтр общего кода",
    ce_lua_script: "CE Lua-скрипт", speedhack: "Speedhack", mono_dissect: "Mono Dissector", dotnet_decompile: ".NET декомпиляция",
    il2cpp_dump: "IL2CPP дамп", harmony_bepinex: "BepInEx + Harmony", vmt_hook: "VMT-хук", detour_hook: "Detour-хук",
    dll_injection: "DLL-инъекция", sdk_dump: "Дамп SDK (GObjects/GNames)", w2s_math: "3D-математика / W2S",
    archive_format: "Формат архивов", save_format: "Формат сохранений", lua_vm_hook: "Lua VM", emulator_memory: "Память эмулятора",
    integrity_concept: "Integrity (концепт)",
  };
  const TOOL_LABEL = {
    cheat_engine: "Cheat Engine", x64dbg: "x64dbg", ghidra: "Ghidra", reclass_net: "ReClass.NET", dnspyex: "dnSpyEx",
    il2cppdumper: "Il2CppDumper", dumper7: "Dumper-7", bepinex_harmony: "BepInEx/Harmony", system_informer: "System Informer",
    hex_editor: "Hex-редактор", python: "Python", z3: "Z3",
  };
  const FAMILY_LABEL = {
    unity_mono: "Unity Mono", unity_il2cpp: "Unity IL2CPP", unreal_1: "Unreal 1", unreal_2: "Unreal 2", unreal_3: "Unreal 3",
    unreal_4: "Unreal 4", unreal_5: "Unreal 5", source: "Source", goldsrc: "GoldSrc", idtech: "id Tech", native_win32: "Native Win32",
    dotnet_xna: ".NET / XNA", gamemaker: "GameMaker", godot: "Godot", lua_hybrid: "C++ + Lua", popcap: "PopCap",
    renderware_gamebryo: "RenderWare/Gamebryo", js_web: "JS / Web", emulator: "Эмулятор", custom: "Свой движок",
  };
  const KIND_HINT = { nudge: "Намёк", concept: "Концепт", near_spoiler: "Почти спойлер" };
  const SRC_DETAIL = { my_notes: "из моих заметок", repo_catalog: "каталог репо", derived: "выведено правилом", needs_verification: "не подтверждено" };

  // ------------------------------------------------------------------ state (localStorage, defensive)
  const defaultState = () => ({ v: 1, done: {}, hints: {}, free: false, theme: null });
  function sanitizeState(raw) {
    const s = defaultState();
    if (!raw || typeof raw !== "object") return s;
    if (raw.done && typeof raw.done === "object") {
      for (const [id, rec] of Object.entries(raw.done)) {
        const n = BY_ID.get(id);
        const exp = rec && Number.isFinite(rec.exp) ? Math.round(rec.exp) : NaN;
        if (n && exp >= 0 && exp <= n.exp) s.done[id] = { exp };
      }
    }
    if (raw.hints && typeof raw.hints === "object") {
      for (const [id, k] of Object.entries(raw.hints)) {
        const n = BY_ID.get(id);
        if (n && Number.isInteger(k) && k > 0) s.hints[id] = Math.min(k, n.hints.length);
      }
    }
    s.free = raw.free === true;
    s.theme = raw.theme === "light" || raw.theme === "dark" ? raw.theme : null;
    return s;
  }
  function loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? sanitizeState(JSON.parse(raw)) : defaultState();
    } catch (e) {
      return defaultState();
    }
  }
  function saveState() {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch (e) { /* private mode / blocked storage */ }
  }
  let state = loadState();
  let selectedId = null;

  // ------------------------------------------------------------------ progression (port of rpg_manager.calculate_progression)
  function progression() {
    const counts = TIERS.map(() => 0);
    let exp = 0;
    for (const [id, rec] of Object.entries(state.done)) {
      counts[TIER_IDX[BY_ID.get(id).tier]] += 1;
      exp += rec.exp;
    }
    const total = counts.reduce((a, b) => a + b, 0);
    const tp = counts.map((c, i) => c + 3 * counts.slice(i + 1).reduce((a, b) => a + b, 0));
    const cleared = tp.map((v, i) => (v >= 3 ? i : -1)).filter((i) => i >= 0);
    const idx = cleared.length ? Math.min(TIERS.length - 1, Math.max(...cleared) + 1) : 0;
    return { idx, exp, total, curTp: Math.min(3, tp[idx]), counts };
  }
  const tierIndex = (n) => TIER_IDX[n.tier];
  const isLocked = (n, prog) => !state.free && tierIndex(n) > prog.idx + 1;
  const hintsOpened = (n) => state.hints[n.id] || 0;
  const awardFor = (n) => Math.round(n.exp * Math.max(MIN_FACTOR, 1 - HINT_PENALTY * hintsOpened(n)));

  // ------------------------------------------------------------------ tiny DOM helper (textContent only)
  function el(tag, opts = {}, children = []) {
    const e = document.createElement(tag);
    if (opts.cls) e.className = opts.cls;
    if (opts.text != null) e.textContent = String(opts.text);
    if (opts.attrs) for (const [k, v] of Object.entries(opts.attrs)) if (v != null && v !== false) e.setAttribute(k, v === true ? "" : String(v));
    if (opts.on) for (const [k, v] of Object.entries(opts.on)) e.addEventListener(k, v);
    for (const c of children) if (c) e.append(c);
    return e;
  }
  const $ = (id) => document.getElementById(id);
  function srcBadge(source) {
    const mine = source === "my_notes";
    return el("span", {
      cls: "src " + (mine ? "mine" : "verify"),
      text: mine ? "[из моих заметок]" : "[нужна проверка]",
      attrs: { title: SRC_DETAIL[source] || source },
    });
  }
  function repoHref(path, anchor) {
    // docs/dojo-map.html lives in docs/, repo files are one level up (works offline from a local clone).
    const safe = String(path).split("/").map(encodeURIComponent).join("/");
    return "../" + safe + (anchor ? "#" + encodeURIComponent(anchor) : "");
  }
  function nodeKindLabel(n) {
    if (n.kind === "game") return "#" + n.rank;
    if (n.kind === "campaign_quest") return "Квест кампании";
    return n.label;
  }
  function pips(d) {
    const s = el("span", { cls: "pips", attrs: { "aria-hidden": "true" } });
    s.append(document.createTextNode("●".repeat(d)), el("span", { cls: "off", text: "●".repeat(5 - d) }));
    return s;
  }
  let toastTimer = 0;
  function toast(msg) {
    const t = $("toast");
    t.textContent = msg;
    t.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove("show"), 2600);
  }

  // ------------------------------------------------------------------ filters
  function fillSelect(sel, label, options) {
    sel.replaceChildren(el("option", { text: label, attrs: { value: "" } }), ...options.map(([v, t]) => el("option", { text: t, attrs: { value: v } })));
  }
  function initFilters() {
    const games = DATA.games;
    const count = (fn) => { const m = new Map(); for (const g of games) for (const k of fn(g)) m.set(k, (m.get(k) || 0) + 1); return m; };
    const fam = count((g) => [g.engine_family]);
    fillSelect($("fEngine"), "Движок: все", [...fam.entries()].sort((a, b) => b[1] - a[1]).map(([k, c]) => [k, `${FAMILY_LABEL[k] || k} (${c})`]));
    const arch = count((g) => g.arch);
    fillSelect($("fArch"), "Архитектура: все", ["x86", "x64", "arm", "unknown"].filter((a) => arch.has(a)).map((a) => [a, `${a === "unknown" ? "не указана" : a} (${arch.get(a)})`]));
    fillSelect($("fDiff"), "Сложность: все", [1, 2, 3, 4, 5].map((d) => [String(d), `${"●".repeat(d)} ${d}/5`]));
    const tech = count((g) => g.techniques.map((t) => t.id));
    fillSelect($("fTech"), "Техника: все", [...tech.entries()].sort((a, b) => b[1] - a[1]).map(([k, c]) => [k, `${TECH_LABEL[k] || k} (${c})`]));
    fillSelect($("fStatus"), "Статус: все", [
      ["available", "Доступные"], ["done", "Пройденные"], ["todo", "Не пройденные"], ["locked", "Закрытые"],
      ["notes", "С моими заметками"], ["hints", "С подсказками"], ["restricted", "Ограниченные (safety)"],
    ]);
    $("filters").addEventListener("input", renderMap);
    $("filters").addEventListener("submit", (e) => e.preventDefault());
    $("filters").addEventListener("reset", () => setTimeout(renderMap, 0));
  }
  function readFilters() {
    return {
      q: $("fSearch").value.trim().toLowerCase(), engine: $("fEngine").value, arch: $("fArch").value,
      diff: $("fDiff").value, tech: $("fTech").value, status: $("fStatus").value, steam: $("fSteam").checked,
    };
  }
  function matches(n, f, prog) {
    const gameOnly = f.engine || f.arch || f.tech || f.steam;
    if (gameOnly && n.kind !== "game") return false;
    if (f.engine && n.engine_family !== f.engine) return false;
    if (f.arch && !n.arch.includes(f.arch)) return false;
    if (f.tech && !n.techniques.some((t) => t.id === f.tech)) return false;
    if (f.steam && !n.flags.steam_library) return false;
    if (f.diff && String(n.difficulty || "") !== f.diff) return false;
    const done = !!state.done[n.id];
    switch (f.status) {
      case "available": if (done || isLocked(n, prog)) return false; break;
      case "done": if (!done) return false; break;
      case "todo": if (done) return false; break;
      case "locked": if (!isLocked(n, prog)) return false; break;
      case "notes": if (!n.notes.length || n.kind === "lab" || n.kind === "crackme") return false; break;
      case "hints": if (!n.hints.length) return false; break;
      case "restricted": if (!n.safety.restricted) return false; break;
    }
    if (f.q) {
      const hay = [n.title, n.engine, n.what_to_find, n.concept, n.readme_text, n.label, n.rank, n.tier].filter(Boolean).join(" ").toLowerCase();
      if (!hay.includes(f.q)) return false;
    }
    return true;
  }

  // ------------------------------------------------------------------ map
  function tile(n, prog) {
    const done = !!state.done[n.id];
    const locked = isLocked(n, prog);
    const cls = ["tile", "kind-" + (n.kind === "campaign_quest" ? "quest" : n.kind)];
    if (done) cls.push("done");
    if (locked) cls.push("locked");
    if (n.id === selectedId) cls.push("selected");
    const icons = el("span", { cls: "icons", attrs: { "aria-hidden": "true" } });
    if (locked) icons.append("🔒");
    if (n.safety.restricted) icons.append("⚠️");
    if (n.kind === "game" && n.notes.length) icons.append("📒");
    if (n.kind === "game" && n.flags.steam_library) icons.append("⭐");
    if (n.hints.length) icons.append("💡");
    const status = [done ? "пройдено" : null, locked ? "закрыто" : null, n.safety.restricted ? "ограничено" : null].filter(Boolean).join(", ");
    return el("button", {
      cls: cls.join(" "),
      attrs: { type: "button", "data-id": n.id, "aria-label": `${nodeKindLabel(n)} ${n.title}, тир ${n.tier}${status ? ", " + status : ""}` },
      on: { click: () => select(n.id) },
    }, [
      el("span", { cls: "kind", text: `${nodeKindLabel(n)} · ${n.exp} EXP` }),
      el("span", { cls: "name", text: n.title }),
      el("span", { cls: "foot" }, [n.difficulty ? pips(n.difficulty) : el("span"), icons]),
    ]);
  }
  function renderMap() {
    const prog = progression();
    const f = readFilters();
    const bands = $("bands");
    bands.replaceChildren();
    let shown = 0;
    const shownBy = { game: 0, lab: 0, quest: 0 };
    TIERS.forEach((t, i) => {
      const nodes = BY_TIER[i].filter((n) => matches(n, f, prog));
      if (!nodes.length) return;
      shown += nodes.length;
      for (const n of nodes) shownBy[n.kind === "game" ? "game" : n.kind === "campaign_quest" ? "quest" : "lab"] += 1;
      const stateLabel = state.free ? ["open", "свободный режим"] : i <= prog.idx ? ["open", "открыт"] : i === prog.idx + 1 ? ["next", "прорыв: +3 TP"] : ["", "закрыт"];
      bands.append(el("section", { cls: "band", attrs: { "aria-labelledby": "band-" + i } }, [
        el("div", { cls: "band-head" }, [
          el("h2", { text: `Tier ${t.code} — ${t.title}`, attrs: { id: "band-" + i } }),
          el("span", { cls: "meta", text: `${t.exp} EXP за уровень · ${nodes.length}` }),
          el("span", { cls: "band-state " + stateLabel[0], text: stateLabel[1] }),
        ]),
        el("div", { cls: "tiles" }, nodes.map((n) => tile(n, prog))),
      ]));
    });
    // Separate counters: games out of 200, labs/crackmes out of 18, restricted campaign quests.
    $("shownCount").textContent = `Игры: ${shownBy.game} из ${DATA.games.length} · Лабы и крякми: ${shownBy.lab} из ${DATA.labs.length}`
      + ` · Квесты: ${shownBy.quest} из ${DATA.quests.length}`;
    if (!shown) bands.append(el("p", { cls: "empty", text: "Ничего не найдено. Сбросьте фильтры." }));
    markRelations();
    scheduleEdges();
  }
  function markRelations() {
    const sel = selectedId && BY_ID.get(selectedId);
    const prereq = new Set(sel ? sel.prerequisites.labs : []);
    const deps = new Set(sel ? DEPENDENTS.get(sel.id) || [] : []);
    for (const t of document.querySelectorAll(".tile")) {
      const id = t.getAttribute("data-id");
      t.classList.toggle("selected", id === selectedId);
      t.classList.toggle("prereq", prereq.has(id));
      t.classList.toggle("dependent", deps.has(id));
    }
  }
  let edgeFrame = 0;
  function scheduleEdges() { cancelAnimationFrame(edgeFrame); edgeFrame = requestAnimationFrame(drawEdges); }
  function drawEdges() {
    const wrap = $("map"), svg = $("edges"), layer = $("edgeLayer");
    layer.replaceChildren();
    svg.setAttribute("width", 0);   // reset first: the SVG must not inflate the size it measures
    svg.setAttribute("height", 0);
    svg.setAttribute("width", wrap.scrollWidth);
    svg.setAttribute("height", wrap.scrollHeight);
    const sel = selectedId && BY_ID.get(selectedId);
    if (!sel) return;
    const w = wrap.getBoundingClientRect();
    const tileOf = (id) => wrap.querySelector(`.tile[data-id="${CSS.escape(id)}"]`);
    const target = tileOf(sel.id);
    if (!target) return;
    const NS = "http://www.w3.org/2000/svg";
    for (const labId of sel.prerequisites.labs) {
      const src = tileOf(labId);
      if (!src) continue;
      const a = src.getBoundingClientRect(), b = target.getBoundingClientRect();
      const down = a.top <= b.top;
      const x1 = a.left - w.left + a.width / 2, y1 = (down ? a.bottom : a.top) - w.top;
      const x2 = b.left - w.left + b.width / 2, y2 = (down ? b.top : b.bottom) - w.top;
      const my = (y1 + y2) / 2;
      const p = document.createElementNS(NS, "path");
      p.setAttribute("class", "edge");
      p.setAttribute("d", `M${x1},${y1} C${x1},${my} ${x2},${my} ${x2},${y2}`);
      p.setAttribute("marker-end", "url(#arrow)");
      layer.append(p);
    }
  }

  // ------------------------------------------------------------------ panel
  function section(title, ...children) {
    return [el("h3", { text: title }), ...children];
  }
  function labChip(id) {
    const lab = BY_ID.get(id);
    if (!lab) return null;
    const done = !!state.done[id];
    return el("button", { cls: "chip", attrs: { type: "button", title: lab.title }, on: { click: () => select(id) } },
      [document.createTextNode(`${done ? "✅" : "▫️"} ${lab.label}: ${lab.title}`)]);
  }
  function renderPanel() {
    const panel = $("panel"), body = $("panelBody");
    const n = selectedId && BY_ID.get(selectedId);
    document.querySelector(".layout").classList.toggle("has-panel", !!n);
    if (!n) { panel.hidden = true; body.replaceChildren(); return; }
    panel.hidden = false;
    const prog = progression();
    const locked = isLocked(n, prog);
    const done = state.done[n.id];
    const out = [];

    out.push(el("p", { cls: "meta", text: `${nodeKindLabel(n)} · Tier ${n.tier} (${TIERS[tierIndex(n)].title})` }));
    out.push(el("h2", { text: n.title, attrs: { id: "pTitle", tabindex: "-1" } }));
    const metaBits = [];
    if (n.engine) metaBits.push(n.engine);
    if (n.arch) metaBits.push("arch: " + n.arch.join(", "));
    if (n.difficulty_raw != null) metaBits.push(`сложность ${n.difficulty}/5 (${n.difficulty_raw}/10)`);
    if (metaBits.length) out.push(el("p", { cls: "meta", text: metaBits.join(" · ") }));
    if (n.flags) {
      const f = [n.flags.steam_library ? "⭐ в моей Steam-библиотеке" : null, n.flags.author_completed ? "✅ пройдено автором" : null].filter(Boolean);
      if (f.length) out.push(el("p", { cls: "meta", text: f.join(" · ") }));
    }
    if (locked) out.push(el("div", { cls: "banner" }, [el("strong", { text: "🔒 Закрыто. " }),
      document.createTextNode(`Нужен ранг Tier ${TIERS[Math.max(0, tierIndex(n) - 1)].code}. Пройдите уровни своего тира (или один уровень на тир выше), либо включите свободный режим.`)]));

    if (n.safety.restricted) {
      out.push(el("div", { cls: "banner", attrs: { role: "note" } }, [
        el("strong", { text: "⚠️ Ограниченный уровень. " }),
        document.createTextNode("Только концептуальные подсказки. Никакого обхода защиты коммерческого ПО. Практика — на собственных бинарниках."),
        el("p", { cls: "small", text: n.safety.note }),
        el("div", { cls: "chips" }, n.safety.redirect_labs.map(labChip)),
      ]));
    }

    // what to look for (catalog / README / lab concept) - collapsed, it is spoilery
    if (n.kind === "game") {
      out.push(el("details", {}, [el("summary", {}, [document.createTextNode("Что искать — каталог репо "), srcBadge("repo_catalog")]), el("p", { text: n.what_to_find })]));
    } else if (n.kind === "campaign_quest") {
      out.push(el("details", {}, [el("summary", {}, [document.createTextNode("Текст квеста из README "), srcBadge("repo_catalog")]), el("p", { text: n.readme_text })]));
    } else {
      out.push(el("p", { text: n.concept }));
      out.push(el("p", { cls: "small", text: "Опирается на: " + n.prerequisite_text }));
    }

    if (n.techniques && n.techniques.length) {
      out.push(...section("Техники", el("div", { cls: "chips" }, n.techniques.map((t) =>
        el("span", { cls: "chip" }, [document.createTextNode(TECH_LABEL[t.id] || t.id), srcBadge(t.source)])))));
    }
    if (n.tools && n.tools.length) {
      out.push(...section("Инструменты", el("div", { cls: "chips" }, n.tools.map((t) =>
        el("span", { cls: "chip" }, [document.createTextNode(TOOL_LABEL[t.id] || t.id), srcBadge(t.source)])))));
    }
    if (n.prerequisites.labs.length) {
      out.push(...section("Рекомендуемые лабы", el("div", { cls: "chips" }, n.prerequisites.labs.map(labChip)),
        el("p", { cls: "small" }, [document.createTextNode("Связи выведены правилом «техника → лаба» "), srcBadge("derived")])));
    }
    const deps = DEPENDENTS.get(n.id) || [];
    if (deps.length) out.push(el("p", { cls: "small", text: `Эта лаба рекомендована для ${deps.length} уровней — они подсвечены на карте.` }));
    if (n.notes.length) {
      out.push(...section("Мои материалы", el("ul", {}, n.notes.map((note) =>
        el("li", {}, [el("a", { text: note.path + (note.anchor ? " #" + note.anchor : ""), attrs: { href: repoHref(note.path, note.anchor), rel: "noopener noreferrer" } })])))));
    }

    // hints, revealed strictly in order
    out.push(el("h3", { text: "Подсказки" }));
    if (!n.hints.length) {
      out.push(el("p", { cls: "empty", text: "Подсказки для этого уровня ещё не написаны (этап 5)." }));
    } else {
      const opened = hintsOpened(n);
      n.hints.slice(0, opened).forEach((h) => {
        const refs = (h.refs || []).map((r) => {
          const [path, anchor] = r.split("#");
          return el("li", {}, [el("a", { text: r, attrs: { href: repoHref(path, anchor), rel: "noopener noreferrer" } })]);
        });
        out.push(el("article", { cls: "hint", attrs: { "aria-label": `Подсказка ${h.level}` } }, [
          el("div", { cls: "hint-head" }, [el("span", { text: `Подсказка ${h.level}/3 · ${KIND_HINT[h.kind] || h.kind}` }), srcBadge(h.source)]),
          el("p", { text: h.text }),
          refs.length ? el("ul", { cls: "refs" }, refs) : null,
        ]));
      });
      if (opened < n.hints.length) {
        const next = n.hints[opened];
        out.push(el("div", { cls: "row" }, [
          el("button", {
            cls: "btn", text: `Открыть подсказку ${opened + 1}/3 — ${KIND_HINT[next.kind] || next.kind}`,
            attrs: { type: "button", disabled: locked, id: "btnHint" },
            on: { click: () => revealHint(n) },
          }),
          done ? null : el("span", { cls: "small", text: `−${HINT_PENALTY * 100}% EXP за подсказку (минимум ${MIN_FACTOR * 100}%)` }),
        ]));
      }
    }

    // completion
    out.push(el("div", { cls: "row" }, done
      ? [el("span", { text: `✅ Пройдено: +${done.exp} EXP` }), el("button", { cls: "btn", text: "Отменить", attrs: { type: "button" }, on: { click: () => toggleDone(n) } })]
      : [el("button", { cls: "btn primary", text: `Отметить пройденным (+${awardFor(n)} EXP)`, attrs: { type: "button", disabled: locked, id: "btnDone" }, on: { click: () => toggleDone(n) } })]));

    body.replaceChildren(...out.filter(Boolean));
  }

  // ------------------------------------------------------------------ actions
  function select(id, opts = {}) {
    selectedId = id && BY_ID.has(id) ? id : null;
    try { history.replaceState(null, "", selectedId ? "#" + selectedId : location.pathname + location.search); } catch (e) { /* file:// quirks */ }
    renderPanel();
    markRelations();
    scheduleEdges();
    if (selectedId && opts.scroll) {
      const t = document.querySelector(`.tile[data-id="${CSS.escape(selectedId)}"]`);
      if (t) t.scrollIntoView({ block: "center" });
    }
    if (selectedId && !opts.keepFocus) { const h = $("pTitle"); if (h) h.focus({ preventScroll: true }); }
  }
  function revealHint(n) {
    if (isLocked(n, progression())) return;
    state.hints[n.id] = Math.min(n.hints.length, hintsOpened(n) + 1);
    saveState();
    renderAll();
    const b = $("btnHint") || $("btnDone");
    if (b) b.focus({ preventScroll: true });
  }
  function toggleDone(n) {
    const before = progression();
    if (state.done[n.id]) {
      delete state.done[n.id];
    } else {
      if (isLocked(n, before)) return;
      state.done[n.id] = { exp: awardFor(n) };
    }
    saveState();
    const after = progression();
    renderAll();
    if (after.idx > before.idx) toast(`🎉 Новый ранг: Tier ${TIERS[after.idx].code} — ${TIERS[after.idx].title}`);
    else if (state.done[n.id]) toast(`+${state.done[n.id].exp} EXP`);
  }
  function renderStats() {
    const p = progression();
    const t = TIERS[p.idx];
    $("rankCode").textContent = t.code;
    $("rankTitle").textContent = t.title;
    $("tpText").textContent = `${p.curTp}/3 TP`;
    $("tpFill").style.width = (p.curTp / 3) * 100 + "%";
    $("statExp").textContent = p.exp.toLocaleString("ru-RU");
    const doneOf = (list) => list.filter((n) => state.done[n.id]).length;
    $("statGames").textContent = `${doneOf(DATA.games)}/${DATA.games.length}`;
    $("statLabs").textContent = `${doneOf(DATA.labs)}/${DATA.labs.length}`;
    $("statHints").textContent = String(Object.values(state.hints).reduce((a, b) => a + b, 0));
    $("btnFree").setAttribute("aria-pressed", String(state.free));
  }
  function applyTheme() {
    if (state.theme) document.documentElement.setAttribute("data-theme", state.theme);
    else document.documentElement.removeAttribute("data-theme");
  }
  function renderAll() { renderStats(); renderMap(); renderPanel(); }

  function exportProgress() {
    const blob = new Blob([JSON.stringify({ app: "re-dojo-map", ...state }, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = el("a", { attrs: { href: url, download: "re-dojo-map-progress.json" } });
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function importProgress(file) {
    if (!file || file.size > 512 * 1024) { toast("Файл слишком большой или не выбран"); return; }
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(String(reader.result));
        if (!parsed || parsed.app !== "re-dojo-map") throw new Error("not a re-dojo-map export");
        state = sanitizeState(parsed);
        saveState();
        applyTheme();
        renderAll();
        toast("Прогресс загружен");
      } catch (e) {
        toast("Не удалось прочитать файл прогресса");
      }
    };
    reader.readAsText(file);
  }

  function init() {
    applyTheme();
    initFilters();
    $("btnFree").addEventListener("click", () => { state.free = !state.free; saveState(); renderAll(); });
    $("btnTheme").addEventListener("click", () => {
      const dark = state.theme ? state.theme === "dark" : !matchMedia("(prefers-color-scheme: light)").matches;
      state.theme = dark ? "light" : "dark";
      saveState(); applyTheme(); scheduleEdges();
    });
    $("btnExport").addEventListener("click", exportProgress);
    $("fileImport").addEventListener("change", (e) => { importProgress(e.target.files[0]); e.target.value = ""; });
    $("btnReset").addEventListener("click", () => {
      if (!confirm("Сбросить весь прогресс карты? Это нельзя отменить.")) return;
      state = defaultState(); saveState(); applyTheme(); select(null); renderAll();
    });
    $("btnClose").addEventListener("click", () => {
      const prev = selectedId;
      select(null);
      const t = prev && document.querySelector(`.tile[data-id="${CSS.escape(prev)}"]`);
      if (t) t.focus();
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && selectedId) $("btnClose").click();
      if (e.key === "/" && document.activeElement === document.body) { e.preventDefault(); $("fSearch").focus(); }
    });
    const syncFiltersHeight = () => document.documentElement.style.setProperty("--filters-h", $("filters").offsetHeight + "px");
    if (typeof ResizeObserver === "function") {
      new ResizeObserver(scheduleEdges).observe($("map"));
      new ResizeObserver(syncFiltersHeight).observe($("filters"));
    }
    syncFiltersHeight();
    window.addEventListener("resize", scheduleEdges);
    renderAll();
    const openFromHash = () => {
      let id = "";
      try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { id = ""; }
      if (BY_ID.has(id) && id !== selectedId) select(id, { scroll: true, keepFocus: true });
    };
    window.addEventListener("hashchange", openFromHash);
    openFromHash();
  }
  init();
})();
