#!/usr/bin/env python3
"""
RE:DOJO map - build data/games.json from what already exists in the repo.

Inputs (read-only):
  data/top200_popular_games.json   Top 200 catalog (left untouched; README render + CI depend on it)
  README.md                        In-Repo Dojo table (labs/crackmes) + campaign quest lines
  data/notes_index.json            hand-curated links to the author's real notes (.CT / writeups)
  data/safety_overrides.json       restricted nodes (commercial protection) + redirect labs
  data/labs_index.json             labs/crackmes: built vs planned, prerequisites, techniques trained
  data/hints/*.json                hint batches (stage 5); merged by node id, optional

Output:
  data/games.json                  deterministic (no timestamps, sorted ids, LF, UTF-8)

Usage:
  python Tools_and_Scripts/build_games_json.py            # write data/games.json
  python Tools_and_Scripts/build_games_json.py --check    # exit 1 if data/games.json is stale
  python Tools_and_Scripts/build_games_json.py --hints-dir <dir> --out <file>

Stdlib only. Console output is ASCII-only (Windows cp1251 consoles).
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
TOP200_PATH = ROOT / "data" / "top200_popular_games.json"
README_PATH = ROOT / "README.md"
NOTES_PATH = ROOT / "data" / "notes_index.json"
SAFETY_PATH = ROOT / "data" / "safety_overrides.json"
LABS_INDEX_PATH = ROOT / "data" / "labs_index.json"
DEFAULT_HINTS_DIR = ROOT / "data" / "hints"
DEFAULT_OUT = ROOT / "data" / "games.json"

LAB_ROW_RX = re.compile(
    r"^\| \*\*(Lab|CM) (\d+)\*\* \| `([^`]+)` \| `([\d.]+)` \| \[`[^`]+`\]\(\./([^)]+)\) \| (.*?) \| (.*?) \|\s*$"
)


class BuildError(Exception):
    pass


def rel(p: Path) -> str:
    """Repo-relative POSIX path (never leak absolute local paths into output or errors)."""
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.name


def load_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise BuildError(f"missing input: {rel(p)}")
    except json.JSONDecodeError as e:
        raise BuildError(f"invalid JSON in {rel(p)}: line {e.lineno}: {e.msg}")


def clean_md(text: str) -> str:
    text = text.replace("\\times", "x").replace("$", "")
    text = re.sub(r"\*\*?([^*]+)\*\*?", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def humanize_dir(path: str) -> str:
    folder = path.split("/")[1] if "/" in path else path
    folder = re.sub(r"^(Lab)?\d+_", "", folder)
    return folder.replace("_", " ")


def difficulty_1_5(raw: float) -> int:
    return max(1, min(5, math.ceil(raw / 2)))


def arch_of(engine: str) -> list[str]:
    found = [a for rx, a in S.ARCH_RULES if re.search(rx, engine)]
    return found or ["unknown"]


def add_item(items: dict, key: str, source: str) -> None:
    """Keep the strongest source: my_notes > repo_catalog > derived."""
    rank = {"my_notes": 0, "repo_catalog": 1, "derived": 2}
    if key not in items or rank[source] < rank[items[key]]:
        items[key] = source


def to_list(items: dict, order: list[str]) -> list[dict]:
    return [{"id": k, "source": items[k]} for k in sorted(items, key=order.index)]


def parse_labs(readme: str, index: dict) -> list[dict]:
    labs = []
    for line in readme.splitlines():
        m = LAB_ROW_RX.match(line)
        if not m:
            continue
        kind, num, tier, diff, path, prereq, concept = m.groups()
        lab_id = f"{'lab' if kind == 'Lab' else 'cm'}{int(num):02d}"
        if lab_id not in index:
            raise BuildError(f"README Dojo row {lab_id} is missing in data/labs_index.json")
        labs.append({
            "id": lab_id,
            "kind": "lab" if kind == "Lab" else "crackme",
            "label": f"{kind} {int(num):02d}",
            "title": humanize_dir(path),
            "tier": tier,
            "difficulty_raw": float(diff),
            "difficulty": difficulty_1_5(float(diff)),
            "exp": S.TIER_EXP[tier],
            "path": path,
            "prerequisite_text": clean_md(prereq),
            "concept": clean_md(concept),
            "prerequisites": {"labs": [], "games": [], "source": "derived"},
            "notes": [{"path": path, "kind": "lab_source"}],
            "hints": [],
            "hints_status": "pending",
            "safety": {"restricted": False},
        })
    # data/labs_index.json is the source of truth for which labs exist and how they connect.
    built = {k for k, v in index.items() if v["status"] == "built"}
    parsed = {l["id"] for l in labs}
    if len(parsed) != len(labs):
        raise BuildError("duplicate lab rows in README Dojo table")
    if parsed != built:
        raise BuildError("README Dojo table and data/labs_index.json (status 'built') disagree: "
                         f"only in README {sorted(parsed - built)}, only in index {sorted(built - parsed)}")
    for lab in labs:
        entry = index[lab["id"]]
        if (entry["tier"], entry["difficulty_raw"]) != (lab["tier"], lab["difficulty_raw"]):
            raise BuildError(f"{lab['id']}: tier/difficulty differ between README and data/labs_index.json")
        # A lab may be built ahead of its plan prerequisites: edges only to built labs,
        # the planned ones are listed as text (prerequisites_planned) until they exist.
        lab["prerequisites"]["labs"] = [p for p in entry["prereqs"] if p in built]
        planned = [p for p in entry["prereqs"] if p not in built]
        if planned:
            lab["prerequisites_planned"] = planned
        lab["check"] = entry["check"]
        lab["platform"] = dict(entry["platform"])
    return sorted(labs, key=lambda l: (S.TIER_INDEX[l["tier"]], index[l["id"]]["order"]))


def technique_labs(index: dict) -> dict[str, list[str]]:
    """Technique -> the two lowest-difficulty BUILT labs whose 'trains' lists it (entry + next step)."""
    out: dict[str, list[str]] = {}
    for tech in S.TECHNIQUES:
        cands = [(v["difficulty_raw"], v["order"], k) for k, v in index.items()
                 if v["status"] == "built" and tech in v["trains"]]
        if cands:
            out[tech] = [k for _, _, k in sorted(cands)[:2]]
    return out


def split_redirects(lab_ids: list[str], index: dict) -> tuple[list[str], list[str]]:
    """Redirect labs that exist now vs. ones that are only planned (shown as text, no edge, no hint ref)."""
    built = [i for i in lab_ids if index.get(i, {}).get("status") == "built"]
    planned = [i for i in lab_ids if index.get(i, {}).get("status") == "planned"]
    unknown = [i for i in lab_ids if i not in index]
    if unknown:
        raise BuildError(f"redirect labs not in data/labs_index.json: {unknown}")
    return built, planned


def load_hints(hints_dir: Path) -> dict:
    merged: dict = {}
    if not hints_dir.exists():
        return merged
    for p in sorted(hints_dir.glob("*.json")):
        data = load_json(p)
        entries = data.get("entries")
        if not isinstance(entries, dict):
            raise BuildError(f"{p.name}: top-level 'entries' object is required")
        for node_id, entry in entries.items():
            if node_id in merged:
                raise BuildError(f"{p.name}: hints for '{node_id}' already defined in {merged[node_id]['_file']}")
            merged[node_id] = {**entry, "_file": p.name}
    return merged


def apply_hints(node: dict, hints: dict, used: set) -> None:
    entry = hints.get(node["id"])
    if not entry:
        return
    used.add(node["id"])
    node["hints"] = entry.get("hints", [])
    node["hints_status"] = entry.get("status", "draft")
    node["hints_batch"] = entry["_file"]


def build(hints_dir: Path) -> dict:
    top200 = load_json(TOP200_PATH)
    readme = README_PATH.read_text(encoding="utf-8")
    notes_idx = load_json(NOTES_PATH)
    safety = load_json(SAFETY_PATH)
    index = load_json(LABS_INDEX_PATH)["labs"]
    tech_labs = technique_labs(index)
    hints = load_hints(hints_dir)
    used_hints: set = set()

    labs = parse_labs(readme, index)
    for lab in labs:
        for extra in notes_idx.get("labs", {}).get(lab["id"], []):
            lab["notes"].append(extra)
        apply_hints(lab, hints, used_hints)

    # Not restricted, but the game has an online mode: map shows an offline-only banner.
    online_ids = set(safety.get("online_note_games", []))
    games = []
    for g in top200:
        raw_title = g["title"]
        title = raw_title.replace(S.TITLE_STAR, "").replace(S.TITLE_CHECK, "")
        title = re.sub(r"\s+", " ", title).strip()
        gid = f"g{g['rank']}"
        engine = g["engine"]
        eng = S.derive_engine(engine)
        family = eng["family"]
        # Ambiguous engine -> nothing comes from the engine string: neither family-derived techniques
        # nor keyword hits inside it ('IL2CPP' in the engine). Only what_to_find and my_notes count.
        catalog_text = g["what_to_find"] if eng["status"] == "unknown" else f"{g['what_to_find']} {engine}"
        override = safety.get("games", {}).get(gid)

        techniques: dict = {}
        tools: dict = {}
        mine = notes_idx.get("games", {}).get(gid, {})
        for t in mine.get("techniques", []):
            add_item(techniques, t, "my_notes")
        for t in mine.get("tools", []):
            add_item(tools, t, "my_notes")
        for rx, t in S.CATALOG_TECHNIQUE_RULES:
            if re.search(rx, catalog_text, re.IGNORECASE):
                add_item(techniques, t, "repo_catalog")
        for t in S.ENGINE_DERIVED_TECHNIQUES.get(family, []):
            add_item(techniques, t, "derived")
        for rx, tool in S.CATALOG_TOOL_RULES:
            if re.search(rx, catalog_text):
                add_item(tools, tool, "repo_catalog")
        # Restricted nodes may exclude items outright (e.g. no Il2CppDumper for encrypted metadata).
        excluded = (override or {}).get("exclude_items", {})
        for t in excluded.get("techniques", []):
            techniques.pop(t, None)
        for t in techniques:
            if t in S.TECHNIQUE_DERIVED_TOOLS:
                add_item(tools, S.TECHNIQUE_DERIVED_TOOLS[t], "derived")
        for t in excluded.get("tools", []):
            tools.pop(t, None)

        prereq_labs: list[str] = []
        for t in sorted(techniques, key=S.TECHNIQUES.index):
            for lab_id in tech_labs.get(t, []):
                if lab_id not in prereq_labs:
                    prereq_labs.append(lab_id)

        raw_diff = float(g["diff"].split("/")[0])
        node = {
            "id": gid,
            "kind": "game",
            "rank": g["rank"],
            "title": title,
            "flags": {
                "steam_library": S.TITLE_STAR in raw_title,
                "author_completed": S.TITLE_CHECK in raw_title,
            },
            "engine": engine,
            "engine_family": family,
            "engine_family_candidates": eng["candidates"],
            "engine_derivation": ({"status": "unknown", "reason": eng["reason"]} if eng["status"] == "unknown"
                                  else {"status": "known"}),
            "arch": arch_of(engine),
            "tier": g["tier"],
            "difficulty_raw": raw_diff,
            "difficulty": difficulty_1_5(raw_diff),
            "exp": S.TIER_EXP[g["tier"]],
            "what_to_find": g["what_to_find"],
            "techniques": to_list(techniques, S.TECHNIQUES),
            "tools": to_list(tools, S.TOOLS),
            "prerequisites": {"labs": prereq_labs, "games": [], "source": "derived"},
            "notes": mine.get("notes", []),
            "hints": [],
            "hints_status": "pending",
            "safety": {"restricted": False},
        }
        if override:
            node["safety"] = dict(override)
            if "redirect_labs" in override:
                built_r, planned_r = split_redirects(override["redirect_labs"], index)
                node["safety"]["redirect_labs"] = built_r
                if planned_r:
                    node["safety"]["redirect_labs_planned"] = planned_r
            # Practice on restricted nodes is redirected to own labs: show them as prerequisites (map edges).
            for lab_id in node["safety"].get("redirect_labs", []):
                if lab_id not in prereq_labs:
                    prereq_labs.append(lab_id)
        if gid in online_ids:
            node["safety"] = {**node["safety"], "online_note": True}
        apply_hints(node, hints, used_hints)
        games.append(node)

    unknown_online = sorted(online_ids - {g["id"] for g in games})
    if unknown_online:
        raise BuildError(f"online_note_games lists unknown game ids: {', '.join(unknown_online)}")
    clash = sorted(i for i in online_ids if safety.get("games", {}).get(i, {}).get("restricted"))
    if clash:
        raise BuildError(f"online_note_games must not list restricted games: {', '.join(clash)}")

    quests = []
    readme_lines = readme.splitlines()
    for q in safety.get("quests", []):
        hits = [ln for ln in readme_lines if q["readme_match"] in ln]
        if len(hits) != 1:
            raise BuildError(f"quest {q['id']}: readme_match must hit exactly 1 README line, got {len(hits)}")
        q_built, q_planned = split_redirects(q["redirect_labs"], index)
        node = {
            "id": q["id"],
            "kind": "campaign_quest",
            "title": q["title"],
            "tier": q["tier"],
            "exp": S.TIER_EXP[q["tier"]],
            "readme_match": q["readme_match"],
            "readme_text": clean_md(re.sub(r"^- \[[ xX]\]\s*", "", hits[0])),
            "prerequisites": {"labs": list(q_built), "games": [], "source": "derived"},
            "notes": [],
            "hints": [],
            "hints_status": "pending",
            "safety": {"restricted": q["restricted"], "note": q["note"], "redirect_labs": q_built,
                       **({"redirect_labs_planned": q_planned} if q_planned else {})},
        }
        apply_hints(node, hints, used_hints)
        quests.append(node)

    unknown = sorted(set(hints) - used_hints)
    if unknown:
        raise BuildError(f"hints reference unknown node ids: {', '.join(unknown)}")

    return {
        "schema_version": S.SCHEMA_VERSION,
        "generated_by": "Tools_and_Scripts/build_games_json.py",
        "sources": [
            "data/top200_popular_games.json", "README.md", "data/notes_index.json",
            "data/safety_overrides.json", "data/labs_index.json", "data/hints/*.json",
        ],
        "source_labels": {
            "my_notes": "из моих заметок",
            "repo_catalog": "нужна проверка",
            "derived": "нужна проверка",
            "needs_verification": "нужна проверка",
        },
        "tiers": [
            {"code": c, "max_diff": d, "title": t, "exp": e} for c, d, t, e in S.TIERS
        ],
        "labs": labs,
        "quests": quests,
        "games": games,
    }


def serialize(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Build data/games.json for the RE:DOJO map")
    ap.add_argument("--check", action="store_true", help="fail if the output file is stale")
    ap.add_argument("--hints-dir", type=Path, default=DEFAULT_HINTS_DIR)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()

    try:
        data = build(args.hints_dir)
    except BuildError as e:
        print(f"[BUILD ERROR] {e}")
        return 1

    if args.check:
        try:
            current = json.loads(args.out.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            current = None
        if current != data:
            print(f"[STALE] {rel(args.out)} is out of date. Run: python Tools_and_Scripts/build_games_json.py")
            return 1
        print(f"[OK] {rel(args.out)} is up to date ({len(data['games'])} games, {len(data['labs'])} labs, {len(data['quests'])} quests).")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(serialize(data))
    hinted = sum(1 for n in data["games"] + data["labs"] + data["quests"] if n["hints"])
    print(f"[OK] wrote {rel(args.out)}: {len(data['games'])} games, {len(data['labs'])} labs, "
          f"{len(data['quests'])} quests, {hinted} nodes with hints.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
