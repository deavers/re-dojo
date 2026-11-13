#!/usr/bin/env python3
"""
RE:DOJO map - validate data/games.json (stdlib only, no jsonschema dependency).

Beyond structure, it enforces the project rules:
  * no invented addresses / offsets / bytes / versions in hint text: every hex literal (0x.., +08,
    5560h), module+offset, [reg+off], AOB byte string and version/build number in a hint must
    appear (token-boundary match) in that node's own text or in one of ITS OWN notes cited in refs.
    Citing README.md, the catalog or a lab source does not count as provenance;
  * 'my_notes' claims must cite at least one of the node's own notes (data/notes_index.json; for
    labs: the lab source). Lab sources may be cited as extra refs but never earn the label alone;
  * anything touching commercial protection must be safety.restricted, with redirect labs,
    conceptual-only hints (no addresses/bytes at all) and a level-3 hint that points to an own lab;
    hints of unrestricted nodes must not mention commercial protections;
  * hint text is plain text (rendered via textContent), <= 400 chars.

Usage:
  python Tools_and_Scripts/validate_games.py [--file data/games.json]
Exit code 0 = valid, 1 = errors. Output is ASCII-only.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dojo_schema as S  # noqa: E402

ROOT = S.ROOT


LAB_ID_RX = re.compile(r"^(?:lab|cm)\d+$")
LAB_CHECKS = ["quest", "flag", "checker", "selftest"]
LAB_PLATFORM_KEYS = ["windows_only", "msvc_only", "needs_unity", "needs_dotnet"]


def say(msg: str) -> None:
    print(msg.encode("ascii", "backslashreplace").decode("ascii"))


class Validator:
    def __init__(self, data: dict):
        self.d = data
        self.errors: list[str] = []
        self.lab_ids: set[str] = set()
        self.lab_paths: dict[str, list[str]] = {}
        self._file_cache: dict[str, str] = {}
        try:
            self.index = json.loads(self.read("data/labs_index.json"))["labs"]
        except (KeyError, TypeError, json.JSONDecodeError):
            self.index = {}

    # ------------------------------------------------------------------ helpers
    def err(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def safe_repo_path(self, where: str, path) -> bool:
        if not isinstance(path, str) or not path:
            self.err(where, "path must be a non-empty string")
            return False
        if path.startswith(("/", "\\")) or ":" in path or ".." in path.split("/") or "\\" in path:
            self.err(where, f"path '{path}' must be repo-relative POSIX without '..'")
            return False
        if not (ROOT / path).is_file():
            self.err(where, f"path '{path}' does not exist in the repo")
            return False
        return True

    def read(self, path: str) -> str:
        if path not in self._file_cache:
            try:
                self._file_cache[path] = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
            except OSError:
                self._file_cache[path] = ""
        return self._file_cache[path]

    def check_type(self, where, obj, key, typ) -> bool:
        if key not in obj:
            self.err(where, f"missing field '{key}'")
            return False
        if not isinstance(obj[key], typ) or (typ is int and isinstance(obj[key], bool)):
            self.err(where, f"field '{key}' has wrong type")
            return False
        return True

    # ------------------------------------------------------------------ top level
    def run(self) -> list[str]:
        d = self.d
        if d.get("schema_version") != S.SCHEMA_VERSION:
            self.err("root", f"schema_version must be {S.SCHEMA_VERSION}")
        for key in ("tiers", "labs", "quests", "games"):
            if not isinstance(d.get(key), list):
                self.err("root", f"'{key}' must be a list")
                return self.errors

        tiers = [t.get("code") for t in d["tiers"]]
        if tiers != S.TIER_CODES:
            self.err("root.tiers", "tier ladder differs from rpg_manager.TIERS")

        seen: set[str] = set()
        for lab in d["labs"]:
            self.lab_ids.add(lab.get("id", ""))
            self.lab_paths[lab.get("id", "")] = [n.get("path") for n in lab.get("notes", []) if isinstance(n, dict)]
        for kind, nodes in (("labs", d["labs"]), ("quests", d["quests"]), ("games", d["games"])):
            for i, node in enumerate(nodes):
                nid = node.get("id") if isinstance(node, dict) else None
                where = f"{kind}[{i}]({nid})"
                if not isinstance(node, dict) or not isinstance(nid, str):
                    self.err(where, "node must be an object with a string id")
                    continue
                if nid in seen:
                    self.err(where, "duplicate id")
                seen.add(nid)
                self.common(where, node)
                getattr(self, kind)(where, node)

        self.schema_drift()
        if len(d["games"]) != 200:
            self.err("root.games", f"expected 200 games, got {len(d['games'])}")
        built = sorted(k for k, v in self.index.items() if v.get("status") == "built")
        if sorted(n.get("id") for n in d["labs"]) != built:
            self.err("root.labs", f"labs differ from data/labs_index.json status 'built' ({len(built)} expected, "
                                  f"{len(d['labs'])} in file)")
        return self.errors

    def schema_drift(self) -> None:
        """data/schema/games.schema.json is hand-maintained for IDEs; its enums must match dojo_schema.py."""
        try:
            sch = json.loads(self.read("data/schema/games.schema.json"))
            defs = sch["$defs"]
            game = defs["game"]["allOf"][1]["properties"]
            pairs = {
                "tier": (defs["tier"]["enum"], S.TIER_CODES),
                "engine_family": (game["engine_family"]["enum"], S.ENGINE_FAMILIES),
                "arch": (game["arch"]["items"]["enum"], S.ARCH),
                "techniques": (game["techniques"]["items"]["allOf"][1]["properties"]["id"]["enum"], S.TECHNIQUES),
                "tools": (game["tools"]["items"]["allOf"][1]["properties"]["id"]["enum"], S.TOOLS),
                "hint.source": (defs["hint"]["properties"]["source"]["enum"], S.HINT_SOURCES),
            }
        except (KeyError, IndexError, TypeError, json.JSONDecodeError):
            self.err("schema", "data/schema/games.schema.json is missing or has an unexpected layout")
            return
        for name, (in_schema, in_code) in pairs.items():
            if list(in_schema) != list(in_code):
                self.err("schema", f"enum '{name}' in games.schema.json differs from dojo_schema.py")

    # ------------------------------------------------------------------ node kinds
    def common(self, w: str, n: dict) -> None:
        if self.check_type(w, n, "tier", str) and n["tier"] not in S.TIER_INDEX:
            self.err(w, f"unknown tier '{n['tier']}'")
        elif n.get("exp") != S.TIER_EXP.get(n.get("tier")):
            self.err(w, "exp does not match the tier EXP table")
        self.check_type(w, n, "title", str)

        if self.check_type(w, n, "prerequisites", dict):
            p = n["prerequisites"]
            for lab_id in p.get("labs", []):
                if lab_id not in self.lab_ids:
                    self.err(w, f"prerequisite lab '{lab_id}' does not exist")
            if p.get("source") not in S.ITEM_SOURCES:
                self.err(w, "prerequisites.source must be one of " + "/".join(S.ITEM_SOURCES))

        if self.check_type(w, n, "notes", list):
            for j, note in enumerate(n["notes"]):
                nw = f"{w}.notes[{j}]"
                if not isinstance(note, dict):
                    self.err(nw, "must be an object")
                    continue
                self.safe_repo_path(nw, note.get("path"))
                if note.get("kind") not in S.NOTE_KINDS:
                    self.err(nw, f"kind must be one of {S.NOTE_KINDS}")

        self.safety(w, n)
        self.hints(w, n)

    def games(self, w: str, g: dict) -> None:
        rank = g.get("rank")
        if not (isinstance(rank, str) and len(rank) == 3 and rank.isdigit()):
            self.err(w, "rank must be a 3-digit string")
        elif g["id"] != f"g{rank}":
            self.err(w, "id must be 'g' + rank")
        if any(m in g.get("title", "") for m in (S.TITLE_STAR, S.TITLE_CHECK)):
            self.err(w, "title must not contain star/check markers (use flags)")
        flags = g.get("flags", {})
        if not (isinstance(flags.get("steam_library"), bool) and isinstance(flags.get("author_completed"), bool)):
            self.err(w, "flags.steam_library / flags.author_completed must be booleans")
        if g.get("engine_family") not in S.ENGINE_FAMILIES:
            self.err(w, f"engine_family '{g.get('engine_family')}' not in enum")
        self.engine_derivation(w, g)
        arch = g.get("arch")
        if not (isinstance(arch, list) and arch and all(a in S.ARCH for a in arch)) or ("unknown" in (arch or []) and len(arch) > 1):
            self.err(w, "arch must be a non-empty list of x86/x64/arm, or exactly ['unknown']")
        raw = g.get("difficulty_raw")
        if not (isinstance(raw, (int, float)) and 0.1 <= raw <= 10.0):
            self.err(w, "difficulty_raw must be a number in 0.1..10")
        elif g.get("difficulty") != max(1, min(5, math.ceil(raw / 2))):
            self.err(w, "difficulty must equal clamp(ceil(difficulty_raw / 2), 1, 5)")
        self.check_type(w, g, "what_to_find", str)

        has_notes = bool(g.get("notes"))
        for field, enum in (("techniques", S.TECHNIQUES), ("tools", S.TOOLS)):
            items = g.get(field)
            if not isinstance(items, list):
                self.err(w, f"'{field}' must be a list")
                continue
            ids = [it.get("id") for it in items if isinstance(it, dict)]
            if len(ids) != len(set(ids)) or len(ids) != len(items):
                self.err(w, f"'{field}' has duplicates or malformed items")
            for it in items:
                if not isinstance(it, dict):
                    continue
                if it.get("id") not in enum:
                    self.err(w, f"{field} id '{it.get('id')}' not in enum")
                if it.get("source") not in S.ITEM_SOURCES:
                    self.err(w, f"{field} '{it.get('id')}' has invalid source")
                if it.get("source") == "my_notes" and not has_notes:
                    self.err(w, f"{field} '{it.get('id')}' claims my_notes but the game has no notes")

        catalog = f"{g.get('title', '')} {g.get('engine', '')} {g.get('what_to_find', '')}"
        if S.PROTECTION_RX.search(catalog) and not g.get("safety", {}).get("restricted"):
            self.err(w, "catalog text mentions commercial protection -> safety.restricted must be true "
                        "(add it to data/safety_overrides.json)")

        excl = g.get("safety", {}).get("exclude_items", {})
        if not isinstance(excl, dict):
            self.err(w, "safety.exclude_items must be an object")
        else:
            for field, enum in (("techniques", S.TECHNIQUES), ("tools", S.TOOLS)):
                ids = excl.get(field, [])
                if not (isinstance(ids, list) and all(i in enum for i in ids)):
                    self.err(w, f"safety.exclude_items.{field} must be a list of known {field} ids")
                    continue
                present = {it.get("id") for it in g.get(field, []) if isinstance(it, dict)} & set(ids)
                if present:
                    self.err(w, f"{field} {sorted(present)} are excluded by safety.exclude_items but still listed")

    def engine_derivation(self, w: str, g: dict) -> None:
        """engine_family / candidates / derivation must equal dojo_schema.derive_engine(engine), and an
        ambiguous engine may not contribute any technique or tool (family rules or engine keywords)."""
        der, cands = g.get("engine_derivation"), g.get("engine_family_candidates")
        if not (isinstance(der, dict) and der.get("status") in S.ENGINE_DERIVATION_STATUSES):
            self.err(w, f"engine_derivation.status must be one of {S.ENGINE_DERIVATION_STATUSES}")
            return
        if not (isinstance(cands, list) and all(c in S.ENGINE_FAMILIES and c not in ("ambiguous", "custom") for c in cands)):
            self.err(w, "engine_family_candidates must be a list of concrete engine families")
            return
        unknown = der["status"] == "unknown"
        if unknown != (g.get("engine_family") == "ambiguous"):
            self.err(w, "engine_family 'ambiguous' <=> engine_derivation.status 'unknown'")
        if unknown and not (cands and isinstance(der.get("reason"), str) and der["reason"].strip()):
            self.err(w, "unknown engine derivation needs candidates and a reason")
        expect = S.derive_engine(str(g.get("engine", "")))
        if (g.get("engine_family"), cands, der["status"]) != (expect["family"], expect["candidates"], expect["status"]):
            self.err(w, f"engine derivation differs from dojo_schema.derive_engine(): expected family "
                        f"'{expect['family']}', candidates {expect['candidates']}, status '{expect['status']}'")
        if not unknown:
            return
        wtf = str(g.get("what_to_find", ""))
        for t in g.get("techniques", []):
            if not isinstance(t, dict):
                continue
            if t.get("source") == "derived":
                self.err(w, f"ambiguous engine: technique '{t.get('id')}' must not be derived from the engine")
            elif t.get("source") == "repo_catalog" and not any(
                    tid == t.get("id") and re.search(rx, wtf, re.IGNORECASE) for rx, tid in S.CATALOG_TECHNIQUE_RULES):
                self.err(w, f"ambiguous engine: technique '{t.get('id')}' is not backed by what_to_find")
        for t in g.get("tools", []):
            if isinstance(t, dict) and t.get("source") == "repo_catalog" and not any(
                    tid == t.get("id") and re.search(rx, wtf) for rx, tid in S.CATALOG_TOOL_RULES):
                self.err(w, f"ambiguous engine: tool '{t.get('id')}' is not backed by what_to_find")

    def labs(self, w: str, lab: dict) -> None:
        if not (isinstance(lab["id"], str) and LAB_ID_RX.match(lab["id"])):
            self.err(w, "lab id must match lab<digits> or cm<digits>")
        if lab.get("kind") not in ("lab", "crackme"):
            self.err(w, "kind must be lab or crackme")
        self.safe_repo_path(w, lab.get("path"))
        entry = self.index.get(lab["id"], {})
        prereqs = entry.get("prereqs", [])
        built_pre = [p for p in prereqs if self.index.get(p, {}).get("status") == "built"]
        if lab.get("prerequisites", {}).get("labs") != built_pre:
            self.err(w, "prerequisites.labs must equal the BUILT prereqs from data/labs_index.json")
        if lab.get("prerequisites_planned", []) != [p for p in prereqs if p not in built_pre]:
            self.err(w, "prerequisites_planned must list the not-yet-built prereqs from data/labs_index.json")
        if lab.get("check") not in LAB_CHECKS:
            self.err(w, f"check must be one of {LAB_CHECKS}")
        plat = lab.get("platform")
        if not (isinstance(plat, dict) and set(plat) == set(LAB_PLATFORM_KEYS)
                and all(isinstance(v, bool) for v in plat.values())):
            self.err(w, f"platform must be an object of booleans {LAB_PLATFORM_KEYS}")

    def quests(self, w: str, q: dict) -> None:
        if q.get("kind") != "campaign_quest":
            self.err(w, "kind must be campaign_quest")
        match = q.get("readme_match")
        if not isinstance(match, str) or not match:
            self.err(w, "readme_match must be a non-empty string")
        else:
            hits = sum(1 for ln in self.read("README.md").splitlines() if match in ln)
            if hits != 1:
                self.err(w, f"readme_match must hit exactly 1 README.md line, got {hits}")
        if not q.get("safety", {}).get("restricted"):
            self.err(w, "campaign quests on the map are only the restricted ones -> restricted must be true")

    # ------------------------------------------------------------------ safety & hints
    def safety(self, w: str, n: dict) -> None:
        s = n.get("safety")
        if not isinstance(s, dict) or not isinstance(s.get("restricted"), bool):
            self.err(w, "safety.restricted must be a boolean")
            return
        if "online_note" in s:
            if not isinstance(s["online_note"], bool):
                self.err(w, "safety.online_note must be a boolean")
            elif s["online_note"] and (s["restricted"] or n.get("kind") != "game"):
                self.err(w, "safety.online_note is only for unrestricted games")
        if s["restricted"]:
            if not (isinstance(s.get("note"), str) and s["note"].strip()):
                self.err(w, "restricted node needs safety.note")
            red = s.get("redirect_labs")
            if not (isinstance(red, list) and red):
                self.err(w, "restricted node needs non-empty safety.redirect_labs")
            else:
                for lab_id in red:
                    if lab_id not in self.lab_ids:
                        self.err(w, f"redirect lab '{lab_id}' does not exist")
            planned = s.get("redirect_labs_planned", [])
            if not isinstance(planned, list):
                self.err(w, "safety.redirect_labs_planned must be a list")
            else:
                for lab_id in planned:
                    if self.index.get(lab_id, {}).get("status") != "planned":
                        self.err(w, f"planned redirect lab '{lab_id}' is not a planned lab in data/labs_index.json")

    def allowed_ref_paths(self, n: dict) -> set[str]:
        """Files that may back a 'my_notes' hint: the node's notes + sources of its labs."""
        paths = {x.get("path") for x in n.get("notes", []) if isinstance(x, dict)}
        lab_ids = list(n.get("prerequisites", {}).get("labs", [])) + list(n.get("safety", {}).get("redirect_labs", []) or [])
        if n.get("kind") in ("lab", "crackme"):
            lab_ids.append(n["id"])
        for lab_id in lab_ids:
            paths.update(self.lab_paths.get(lab_id, []))
        return {p for p in paths if p}

    def hints(self, w: str, n: dict) -> None:
        hints = n.get("hints")
        status = n.get("hints_status")
        if not isinstance(hints, list):
            self.err(w, "hints must be a list")
            return
        if status not in S.HINT_STATUSES:
            self.err(w, f"hints_status must be one of {S.HINT_STATUSES}")
        if not hints:
            if status != "pending":
                self.err(w, "empty hints require hints_status 'pending'")
            return
        if status == "pending":
            self.err(w, "hints present but hints_status is 'pending'")
        if len(hints) != 3:
            self.err(w, f"hints must contain exactly 3 levels, got {len(hints)}")

        restricted = bool(n.get("safety", {}).get("restricted"))
        own_text = "\n".join(str(n.get(k, "")) for k in
                             ("title", "engine", "what_to_find", "readme_text", "concept", "prerequisite_text"))
        allowed = self.allowed_ref_paths(n)
        own_notes = {x.get("path") for x in n.get("notes", []) if isinstance(x, dict) and x.get("path")}
        redirect_paths = set()
        for lab_id in n.get("safety", {}).get("redirect_labs", []) or []:
            redirect_paths.update(self.lab_paths.get(lab_id, []))

        for j, h in enumerate(hints):
            hw = f"{w}.hints[{j}]"
            if not isinstance(h, dict):
                self.err(hw, "must be an object")
                continue
            level = h.get("level")
            if level != j + 1:
                self.err(hw, f"level must be {j + 1} (hints are revealed in order)")
            if h.get("kind") != S.HINT_KINDS.get(level):
                self.err(hw, f"kind must be '{S.HINT_KINDS.get(level)}' for level {level}")
            text = h.get("text")
            if not (isinstance(text, str) and text.strip()):
                self.err(hw, "text must be a non-empty string")
                continue
            if len(text) > S.HINT_MAX_LEN:
                self.err(hw, f"text longer than {S.HINT_MAX_LEN} chars")
            if S.HTML_RX.search(text):
                self.err(hw, "text must be plain text (no HTML tags)")
            source = h.get("source")
            if source not in S.HINT_SOURCES:
                self.err(hw, f"source must be one of {S.HINT_SOURCES}")
            refs = h.get("refs", [])
            if not isinstance(refs, list) or not all(isinstance(r, str) for r in refs):
                self.err(hw, "refs must be a list of strings")
                refs = []
            ref_paths = []
            for r in refs:
                path = r.split("#", 1)[0]
                if self.safe_repo_path(hw, path):
                    ref_paths.append(path)
            if source == "my_notes":
                if not refs:
                    self.err(hw, "source my_notes requires at least one ref")
                for p in ref_paths:
                    if p not in allowed:
                        self.err(hw, f"my_notes ref '{p}' is not one of this node's notes or lab sources")
                if refs and not any(p in own_notes for p in ref_paths):
                    self.err(hw, "source my_notes needs at least one ref to THIS node's own notes "
                                 "(a lab source alone does not make a game hint 'my notes')")

            # --- protection topics only on restricted nodes. Labs/crackmes are the author's own binaries:
            # license-file / keygen talk is fine there, commercial product names are not.
            prot_rx = S.PROTECTION_PRODUCTS_RX if n.get("kind") in ("lab", "crackme") else S.PROTECTION_RX
            if not restricted and prot_rx.search(text):
                self.err(hw, "hint mentions a commercial protection but the node is not safety.restricted")
            if n.get("safety", {}).get("online_note") is True:
                m = S.ONLINE_CONTEXT_RX.search(text)
                if m:
                    self.err(hw, f"online_note game: hints must stay offline / single-player, found '{m.group(0)}'")

            # --- anti-hallucination: concrete literals must have provenance
            if restricted:
                found = S.byte_literals(text)
                if found:
                    self.err(hw, f"restricted node: no concrete addresses/bytes allowed in hints, found {sorted(found)}")
            # Provenance corpus = this node's own text + refs to THIS node's own notes. Citing README.md,
            # the Top 200 catalog or a lab source does not let a hint borrow a literal from somewhere else.
            backing = [p for p in ref_paths if p in own_notes]
            corpus = own_text + "\n" + "\n".join(self.read(p) for p in backing)
            for lit in sorted(S.concrete_literals(text)):
                if not S.literal_in(lit, corpus):
                    self.err(hw, f"literal '{lit}' is not backed by this node's own text or its own notes cited in refs "
                                 f"(possible invented address/offset/bytes/version)")

        if restricted and len(hints) == 3 and isinstance(hints[2], dict):
            l3_paths = {r.split("#", 1)[0] for r in hints[2].get("refs", []) if isinstance(r, str)}
            if not (l3_paths & redirect_paths):
                self.err(f"{w}.hints[2]", "restricted node: level-3 hint must reference a redirect lab source")


def protection_report(data: dict) -> None:
    """Report-only scan of all games for a human safety decision. Never changes data, never fails."""
    def ctx(text: str, m) -> str:
        a, b = max(0, m.start() - 35), min(len(text), m.end() + 35)
        return ("..." if a else "") + text[a:b] + ("..." if b < len(text) else "")

    say("== Hard tier (PROTECTION_RX: forces safety.restricted) ==")
    for g in data["games"]:
        hits = [(f, m.group(0)) for f in ("title", "engine", "what_to_find")
                for m in S.PROTECTION_RX.finditer(str(g.get(f, "")))]
        if hits:
            say(f"  {g['id']} restricted={g['safety']['restricted']} {g['title']}: "
                + "; ".join(f"{f}: '{h}'" for f, h in hits))
    say("== Review tier (PROTECTION_REVIEW_RX: broad words, human decision) ==")
    for g in data["games"]:
        for f in ("title", "engine", "what_to_find"):
            text = str(g.get(f, ""))
            for m in S.PROTECTION_REVIEW_RX.finditer(text):
                say(f"  {g['id']} restricted={g['safety']['restricted']} {f}: '{m.group(0)}' | {ctx(text, m)}")
    say("== Offline-qualified titles (online mode implied; protection NOT stated in the repo) ==")
    for g in data["games"]:
        m = S.OFFLINE_QUALIFIER_RX.search(g["title"])
        if m:
            say(f"  {g['id']} restricted={g['safety']['restricted']} '{m.group(0)}' | {g['title']}")
    say("Note: zero text hits does not mean a game ships without protection; the catalog simply does not say.")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate RE:DOJO data/games.json")
    ap.add_argument("--file", type=Path, default=ROOT / "data" / "games.json")
    ap.add_argument("--protection-report", action="store_true",
                    help="list protection-related wording in all games for a human decision (report only)")
    args = ap.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        say(f"[FAIL] {args.file.name} not found. Run build_games_json.py first.")
        return 1
    except json.JSONDecodeError as e:
        say(f"[FAIL] {args.file.name}: invalid JSON at line {e.lineno}: {e.msg}")
        return 1
    if args.protection_report:
        protection_report(data)
        return 0

    errors = Validator(data).run()
    if errors:
        for e in errors:
            say(f"[ERROR] {e}")
        say(f"[FAIL] {len(errors)} error(s) in {args.file.name}")
        return 1
    nodes = data["games"] + data["labs"] + data["quests"]
    say(f"[OK] {args.file.name} valid: {len(data['games'])} games, {len(data['labs'])} labs, "
        f"{len(data['quests'])} quests, {sum(1 for n in nodes if n['hints'])} with hints, "
        f"{sum(1 for n in nodes if n['safety']['restricted'])} restricted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
