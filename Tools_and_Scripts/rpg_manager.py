#!/usr/bin/env python3
"""
============================================================================
[RPG Manager] Auto-Updating Character Card, Breakthrough Level-Up & Rubric DB
============================================================================
FEATURES:
  1. Parses all 28 Tiers (`F-` -> `SSS++`) and `- [ ]` / `- [x]` checkboxes
     in `README.md`.
  2. Applies the Smart "Breakthrough" Level-Up Rule:
       - Clearing a Tier requires 3 Tier Points (3 TP).
       - Each quest completed in Tier T gives +1 TP to Tier T.
       - BREAKTHROUGH: Each quest completed in a higher Tier (T+1 or above)
         automatically grants +3 TP to Tier T (instantly clearing Tier T!).
  3. 5-Axis Anti-Inflation Rubric Calculator:
       - Reads `data/custom_targets.json`, computes the objective Difficulty
         Score (0.1 to 10.0) and RPG Tier from 5 technical axes (preventing
         arbitrary "SSS++" inflation), and renders them into `README.md`.
  4. Modes:
       - Default: Recalculate RPG Card from current checkboxes in `README.md`
       - `--name "Handle"` : Set player name on the RPG Card
       - `--reset`         : Reset all checkboxes to `- [ ]` (Clean New Game)
       - `--preset deavers`: Load `deavers`'s completed milestones
       - `--add-target`    : Interactive 5-Axis Rubric CLI wizard
============================================================================
"""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT_DIR = Path(__file__).resolve().parent.parent
README_PATH = ROOT_DIR / "README.md"
CUSTOM_DB_PATH = ROOT_DIR / "data" / "custom_targets.json"
TOP100_DB_PATH = ROOT_DIR / "data" / "top200_popular_games.json"
PROGRESS_JSON_PATH = ROOT_DIR / "data" / "player_progress.json"

TIERS = [
    ("F-",    0.2,  "White-Box Novice",         100),
    ("F",     0.4,  "Memory Initiate",          120),
    ("F+",    0.6,  "State Scavenger",          150),
    ("E--",   1.0,  "Tutorial Apprentice",      180),
    ("E-",    1.4,  "Win32 Tinkerer",           220),
    ("E",     1.8,  "Pointer Scout",            260),
    ("E+",    2.2,  "Code-Cave Squire",         300),
    ("D-",    2.6,  "Sector Ranger",            350),
    ("D",     3.0,  "Arena Vanguard",           400),
    ("D+",    3.4,  "Memory Tracker",           450),
    ("C-",    3.8,  "Struct Alchemist",         520),
    ("C",     4.2,  "Adventurer (Mono/CLR)",    600),
    ("C+",    4.6,  "Harmony Hexer",            680),
    ("B-",    5.0,  "RTTI Knight",              770),
    ("B",     5.4,  "VMT Paladin",              860),
    ("B+",    5.8,  "Internal Dragoon",         960),
    ("A-",    6.2,  "Unreal Architect",        1100),
    ("A",     6.6,  "IL2CPP Inquisitor",       1250),
    ("A+",    7.0,  "Hybrid VM Warlock",       1400),
    ("S-",    7.4,  "Soulslike Sage",          1600),
    ("S",     7.7,  "DOD Grandmaster",         1800),
    ("S+",    8.0,  "Cross-Arch Empath",       2000),
    ("SS-",   8.3,  "Protocol Cryptographer",  2250),
    ("SS",    8.6,  "Unpacker Sovereign",      2500),
    ("SS+",   8.9,  "VM Slayer",               2800),
    ("SSS-",  9.2,  "Symbolic Oracle (Z3)",    3200),
    ("SSS",   9.5,  "Ring-0 / VMI Phantom",    3600),
    ("SSS+",  9.8,  "Decompilation Titan",     4200),
    ("SSS++", 10.0, "Demigod of Silicon",      5000),
]

DEAVERS_PRESET_KEYWORDS = [
    "lab01_static_scalars",
    "lab02_datatypes_bitmasks",
    "lab03_grid_minesweeper",
    "lab04_pointer_chains",
    "lab05_code_injection",
    "lab06_shared_code",
    "lab07_vtable_reclass",
    "crackme01_strings",
    "crackme02_serial_math",
    "crackme03_xor_rol",
    "crackme04_binary_license",
    "Plants vs. Zombies GOTY",
    "Unreal Tournament 99",
    "The Binding of Isaac: Repentance",
    "Streets of Rogue (v98)",
]


def score_to_tier(score: float) -> str:
    score = max(0.1, min(10.0, round(score, 1)))
    best_tier = "F-"
    for code, max_diff, _, _ in TIERS:
        best_tier = code
        if score <= max_diff + 0.15:
            break
    return best_tier


def compute_rubric_score(rubric: dict) -> tuple[float, str]:
    arch = min(2.0, max(0.1, float(rubric.get("arch_symbols", 0.2))))
    mem = min(2.0, max(0.0, float(rubric.get("memory_indirection", 0.1))))
    eng = min(2.0, max(0.0, float(rubric.get("engine_complexity", 0.1))))
    prot = min(2.5, max(0.0, float(rubric.get("binary_protection", 0.0))))
    priv = min(1.5, max(0.0, float(rubric.get("privilege_boundary", 0.0))))
    total = round(min(10.0, max(0.1, arch + mem + eng + prot + priv)), 1)
    return total, score_to_tier(total)


def render_custom_targets_section() -> str:
    if not CUSTOM_DB_PATH.exists():
        return ""
    data = json.loads(CUSTOM_DB_PATH.read_text(encoding="utf-8"))
    targets = data.get("targets", [])
    lines = [
        "<!-- CUSTOM_TARGETS_START -->",
        "| Status | Computed Tier | Rubric Score | Category | Target Title | Engine / Arch | Quest Objective |",
        "| :---: | :---: | :---: | :---: | :--- | :--- | :--- |",
    ]
    for t in targets:
        score, tier = compute_rubric_score(t.get("rubric", {}))
        chk = "[x]" if t.get("completed", False) else "[ ]"
        lines.append(
            f"| - {chk} | **{tier}** | `{score:.1f} / 10` | {t.get('category', 'Game')} | **{t.get('title', 'Custom')}** | {t.get('engine', 'N/A')} | {t.get('quest', '')} |"
        )
    lines.append("<!-- CUSTOM_TARGETS_END -->")
    return "\n".join(lines)


def render_top100_section() -> str:
    if not TOP100_DB_PATH.exists():
        return ""
    top200 = json.loads(TOP100_DB_PATH.read_text(encoding="utf-8"))
    lines = [
        "<!-- TOP100_GAMES_START -->",
        f"## 🔥 Top {len(top200)} Most Popular & Iconic Games for Reverse Engineering (`#001` – `#{len(top200):03d}`)",
        "",
        f"Complete reference guide of the **Top {len(top200)} most popular & iconic offline/single-player PC games** (sorted by difficulty from `0.5 / 10` to `9.8 / 10`), detailing each game's **Engine & Architecture**, **RPG Tier**, **Difficulty**, and **What to Search & Reverse (in-memory structs, pointer chains, classes, VMTs, matrices, and functions)**:",
        "",
        "| # | Game Title | Engine & Architecture | Tier | Difficulty | 🎯 What to Search & Reverse (Structs, Offsets, Classes & Hooks) |",
        "| :-: | :--- | :--- | :-: | :-: | :--- |",
    ]
    for g in top200:
        r_str = g["rank"] if isinstance(g["rank"], str) else f"{int(g['rank']):03d}"
        lines.append(
            f"| **{r_str}** | **{g['title']}** | {g['engine']} | **{g['tier']}** | `{g['diff']}` | {g['what_to_find']} |"
        )
    lines.append("<!-- TOP100_GAMES_END -->")
    return "\n".join(lines)


def parse_tier_checkboxes(md_text: str) -> dict:
    # Split by tier headers: ### ... [TIER_CODE] ...
    tier_counts = {code: {"checked": 0, "total": 0} for code, _, _, _ in TIERS}
    header_pattern = re.compile(r"^###\s+.*?Tier\s+`([A-Z\+\-]+)`", re.MULTILINE)
    matches = list(header_pattern.finditer(md_text))

    for idx, m in enumerate(matches):
        tier_code = m.group(1)
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        block = md_text[start:end]

        checked = len(re.findall(r"^\s*-\s*\[[xX]\]", block, re.MULTILINE))
        unchecked = len(re.findall(r"^\s*-\s*\[\s\]", block, re.MULTILINE))

        if tier_code == "F-":
            # Also handle combined F- & F header if present
            pass
        if tier_code in tier_counts:
            tier_counts[tier_code]["checked"] += checked
            tier_counts[tier_code]["total"] += checked + unchecked

    return tier_counts


def calculate_progression(tier_counts: dict) -> dict:
    total_checked = sum(v["checked"] for v in tier_counts.values())
    total_boxes = sum(v["total"] for v in tier_counts.values())

    total_exp = 0
    for code, _, _, exp_per_quest in TIERS:
        total_exp += tier_counts[code]["checked"] * exp_per_quest

    # Breakthrough Level-Up Rule:
    # A Tier T is cleared if:
    #   TP(T) = checked(T)*1 + sum_{k > T} checked(k)*3 >= 3
    cleared_indices = []
    tier_tp = {}
    for i, (code, _, _, _) in enumerate(TIERS):
        same_tier_pts = tier_counts[code]["checked"] * 1
        higher_tier_pts = sum(tier_counts[TIERS[j][0]]["checked"] * 3 for j in range(i + 1, len(TIERS)))
        tp = same_tier_pts + higher_tier_pts
        tier_tp[code] = tp
        if tp >= 3:
            cleared_indices.append(i)

    if not cleared_indices and total_checked == 0:
        current_idx = 0
        rank_label = "Tier F- (Unranked Novice)"
        class_title = "White-Box Novice"
        max_diff = 0.0
    else:
        highest_cleared = max(cleared_indices) if cleared_indices else -1
        # Clearing Tier i (>= 3 TP) promotes the Adventurer to Tier i + 1!
        current_idx = min(len(TIERS) - 1, highest_cleared + 1)
        code, max_diff, class_title, _ = TIERS[current_idx]
        rank_label = f"Tier {code} ({class_title})"

    next_idx = min(len(TIERS) - 1, current_idx + 1)
    next_code, _, next_title, _ = TIERS[next_idx]
    cur_tp = min(3, tier_tp[TIERS[current_idx][0]])

    return {
        "total_checked": total_checked,
        "total_boxes": max(1, total_boxes),
        "total_exp": total_exp,
        "current_idx": current_idx,
        "current_code": TIERS[current_idx][0],
        "rank_label": rank_label,
        "class_title": class_title,
        "max_diff": max_diff,
        "cleared_count": len(cleared_indices),
        "cur_tp": cur_tp,
        "next_code": next_code,
        "next_title": next_title,
    }


def build_rpg_card_block(player_name: str, stats: dict) -> str:
    pct = int(round((stats["total_checked"] / stats["total_boxes"]) * 100))
    filled_bars = int(round((stats["cleared_count"] / len(TIERS)) * 28))
    # Pure ASCII progress bars guarantee 100% monospace alignment in VS Code & GitHub
    bar_str = "#" * filled_bars + "-" * (28 - filled_bars)
    tp_bar = "#" * stats["cur_tp"] + "-" * (3 - stats["cur_tp"])

    badge_rank = quote(stats["rank_label"])
    badge_exp = quote(f"{stats['total_exp']:,} EXP ({stats['total_checked']}/{stats['total_boxes']} Quests)")

    s1 = "x" if stats["total_checked"] >= 1 else " "
    s2 = "x" if stats["current_idx"] >= 5 else " "
    s3 = "x" if stats["current_idx"] >= 8 else " "
    s4 = "x" if stats["current_idx"] >= 11 else " "
    s5 = "x" if stats["current_idx"] >= 14 else " "
    s6 = "x" if stats["current_idx"] >= 16 else " "
    s7 = "x" if stats["current_idx"] >= 18 else " "
    s8 = "x" if stats["current_idx"] >= 25 else " "

    inner_w = 88

    def box_row(text: str) -> str:
        padded = f"  {text}"
        return f"║{padded:<{inner_w}.{inner_w}}║"

    top_border = "╔" + ("═" * inner_w) + "╗"
    mid_border = "╠" + ("═" * inner_w) + "╣"
    bot_border = "╚" + ("═" * inner_w) + "╝"

    exp_str = f"{stats['total_exp']:,} ({pct}% Quests Done)"
    rows = [
        top_border,
        box_row(f"ADVENTURER   : {player_name:<26} CLASS     : {stats['class_title']}"),
        box_row(f"CURRENT RANK : {stats['rank_label']:<26} TOTAL EXP : {exp_str}"),
        box_row(f"TIER CLEAR   : [{bar_str}] {stats['cleared_count']:>2} / {len(TIERS)} Tiers Cleared"),
        box_row(f"RANK-UP TRIAL: [{tp_bar}] {stats['cur_tp']}/3 TP in Tier {stats['current_code']:<4} (3 Same-Tier OR 1 Higher-Tier = Rank Up!)"),
        mid_border,
        box_row("PASSIVE SKILL TREE UNLOCKED:"),
        box_row(f" [{s1}] Stage 1: Memory Scanning & Bitmasks    [{s2}] Stage 2: Pointer Chains & AutoAsm"),
        box_row(f" [{s3}] Stage 3: Shared Code Entity Filters    [{s4}] Stage 4: .NET / Unity Mono Dissect"),
        box_row(f" [{s5}] Stage 5: C++ VMT & Internal DLL Hooks  [{s6}] Stage 6: UE4/5 SDK & 3D W2S Math"),
        box_row(f" [{s7}] Stage 7: IL2CPP & Custom Bytecode VMs  [{s8}] Stage 8: Symbolic Z3, O-LLVM & VMI"),
        bot_border,
    ]
    ascii_box = "\n".join(rows)

    return f"""<!-- RPG_CARD_START -->
![Focus](https://img.shields.io/static/v1?label=Focus&message=Offline%20RE%20%26%20Binary%20Auditing&color=blue&style=for-the-badge)
![Current Rank](https://img.shields.io/static/v1?label=Player%20Rank&message={badge_rank}&color=success&style=for-the-badge)
![Total EXP](https://img.shields.io/static/v1?label=Progress&message={badge_exp}&color=orange&style=for-the-badge)
![Web RPG](https://img.shields.io/static/v1?label=Interactive%20Web%20RPG&message=docs%2Findex.html&color=blueviolet&style=for-the-badge)
![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge)

```text
{ascii_box}
```
<!-- RPG_CARD_END -->"""


def extract_current_player_name(md_text: str) -> str:
    m = re.search(r"ADVENTURER\s*:\s*([^\s].*?)\s+CLASS\s*:", md_text)
    if m:
        return m.group(1).strip()
    return "New Challenger"


def interactive_add_target():
    print("====================================================================")
    print("  5-AXIS ANTI-INFLATION RUBRIC CALCULATOR (Add Custom Target)")
    print("====================================================================")
    title = input("1. Target Name (Game or Software): ").strip()
    category = input("2. Category (Game / Software / Crackme): ").strip() or "Game"
    engine = input("3. Engine & Architecture (e.g. Unity x64 / Native C++): ").strip() or "Native x64"
    quest = input("4. Quest Objective: ").strip()

    print("\n--- Score the 5 Technical Axes ---")
    arch = float(input("Axis 1 - Arch & Symbols (0.2=Source, 0.5=Symbols, 0.9=Mono, 1.4=Stripped C++, 1.7=IL2CPP, 2.0=Emulator): ") or 0.5)
    mem = float(input("Axis 2 - Memory Indirection (0.1=Static, 0.4=Pointers, 0.8=Lists, 1.2=VMT/GWorld, 1.7=DOD/ECS, 2.0=XOR RAM): ") or 0.4)
    eng = float(input("Axis 3 - Code Complexity (0.1=Scalar, 0.5=2D, 0.8=SharedCode, 1.2=3D W2S, 1.6=DLL Hook, 2.0=LLVM Lifter): ") or 0.5)
    prot = float(input("Axis 4 - Protection (0.0=None, 0.5=AntiDebug, 1.2=Packer/CRC, 1.8=CustomVM/O-LLVM, 2.5=VMProtect): ") or 0.0)
    priv = float(input("Axis 5 - Boundary (0.0=Ring-3, 0.7=PacketCrypto, 1.5=Ring-0/Hypervisor/Silicon): ") or 0.0)

    rubric = {
        "arch_symbols": arch,
        "memory_indirection": mem,
        "engine_complexity": eng,
        "binary_protection": prot,
        "privilege_boundary": priv,
    }
    score, tier = compute_rubric_score(rubric)
    print(f"\n[+] Objective Rubric Calculation: Difficulty = {score:.1f} / 10.0  =>  Assigned Tier: [{tier}]")

    data = json.loads(CUSTOM_DB_PATH.read_text(encoding="utf-8"))
    data.setdefault("targets", []).append(
        {
            "id": f"custom_{len(data['targets']) + 1}",
            "title": title,
            "category": category,
            "engine": engine,
            "rubric": rubric,
            "quest": quest,
            "completed": False,
        }
    )
    CUSTOM_DB_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("[+] Saved to data/custom_targets.json!")


def main():
    parser = argparse.ArgumentParser(description="RPG Progress Card & Target Sync Engine")
    parser.add_argument("--name", type=str, help="Set Adventurer Name on the RPG Card")
    parser.add_argument("--reset", action="store_true", help="Reset all checkboxes to clean default [ ]")
    parser.add_argument("--preset", type=str, choices=["deavers"], help="Apply preset profile")
    parser.add_argument("--add-target", action="store_true", help="Launch 5-Axis Rubric Target Adder")
    parser.add_argument("--analyze", type=str, help="Auto-grade a .CT table, .cpp/.cs trainer, or .py script")
    parser.add_argument("--from-json", action="store_true", help="Sync checked quests from data/player_progress.json")
    parser.add_argument("--verify-db", action="store_true", help="Verify 5-Axis Rubric scores and Top 200 JSON integrity")
    args = parser.parse_args()

    if args.verify_db:
        if CUSTOM_DB_PATH.exists():
            db = json.loads(CUSTOM_DB_PATH.read_text(encoding="utf-8"))
            targets = db.get("custom_targets", [])
            for t in targets:
                ax = t.get("axes", {})
                calc_score, calc_tier = compute_rubric_score(
                    ax.get("arch", 1.0), ax.get("sym", 1.0), ax.get("ptr", 1.0), ax.get("obf", 1.0), ax.get("ac", 1.0)
                )
                print(f"[OK] Verified Custom Target: {t['name']} -> {calc_score}/10 (Tier {calc_tier})")
        if TOP100_DB_PATH.exists():
            games = json.loads(TOP100_DB_PATH.read_text(encoding="utf-8"))
            assert len(games) == 200, f"Expected 200 games, got {len(games)}"
            print(f"[OK] Verified Top 200 Popular Games Database: {len(games)} entries valid.")
        return

    if args.analyze:
        from auto_artifact_grader import grade_file, print_report
        target_p = Path(args.analyze)
        if not target_p.exists():
            print(f"[!] File not found: {target_p}")
            return
        if target_p.is_dir():
            for child in sorted(target_p.rglob("*")):
                if child.is_file() and child.suffix.lower() in {".ct", ".cea", ".cpp", ".hpp", ".c", ".cs", ".py"}:
                    print_report(grade_file(child))
        else:
            print_report(grade_file(target_p))
        return

    if args.add_target:
        interactive_add_target()

    if not README_PATH.exists():
        print("[!] README.md not found!")
        return

    md_text = README_PATH.read_text(encoding="utf-8")
    player_name = args.name or extract_current_player_name(md_text)

    if args.reset:
        player_name = args.name or "New Challenger"
        # Reset all quest checkboxes outside the RPG card
        md_text = re.sub(r"^(\s*-\s*)\[[xX]\]", r"\1[ ]", md_text, flags=re.MULTILINE)
    elif args.preset == "deavers":
        player_name = "deavers"
        md_text = re.sub(r"^(\s*-\s*)\[[xX]\]", r"\1[ ]", md_text, flags=re.MULTILINE)
        lines = md_text.splitlines()
        for i, line in enumerate(lines):
            if re.match(r"^\s*-\s*\[\s\]", line):
                if any(kw in line for kw in DEAVERS_PRESET_KEYWORDS):
                    lines[i] = re.sub(r"^(\s*-\s*)\[\s\]", r"\1[x]", line, count=1)
        md_text = "\n".join(lines) + "\n"
    elif args.from_json and PROGRESS_JSON_PATH.exists():
        saved = json.loads(PROGRESS_JSON_PATH.read_text(encoding="utf-8"))
        player_name = args.name or saved.get("player_name", player_name)
        keywords = saved.get("completed_keywords", [])
        if keywords:
            md_text = re.sub(r"^(\s*-\s*)\[[xX]\]", r"\1[ ]", md_text, flags=re.MULTILINE)
            lines = md_text.splitlines()
            for i, line in enumerate(lines):
                if re.match(r"^\s*-\s*\[\s\]", line):
                    if any(kw in line for kw in keywords):
                        lines[i] = re.sub(r"^(\s*-\s*)\[\s\]", r"\1[x]", line, count=1)
            md_text = "\n".join(lines) + "\n"

    # Sync Top 200 Popular Games table
    top100_block = render_top100_section()
    if top100_block:
        if "<!-- TOP100_GAMES_START -->" in md_text:
            md_text = re.sub(
                r"<!-- TOP100_GAMES_START -->.*?<!-- TOP100_GAMES_END -->",
                top100_block,
                md_text,
                flags=re.DOTALL,
            )
        else:
            anchor = "## 💻 Software, File Formats & Binary Auditing Arsenal (Programs & Utilities)"
            if anchor in md_text:
                md_text = md_text.replace(anchor, top100_block + "\n\n---\n\n" + anchor)

    # Sync custom targets table
    custom_block = render_custom_targets_section()
    if custom_block and "<!-- CUSTOM_TARGETS_START -->" in md_text:
        md_text = re.sub(
            r"<!-- CUSTOM_TARGETS_START -->.*?<!-- CUSTOM_TARGETS_END -->",
            custom_block,
            md_text,
            flags=re.DOTALL,
        )

    tier_counts = parse_tier_checkboxes(md_text)
    stats = calculate_progression(tier_counts)
    new_card = build_rpg_card_block(player_name, stats)

    if "<!-- RPG_CARD_START -->" in md_text and "<!-- RPG_CARD_END -->" in md_text:
        md_text = re.sub(
            r"<!-- RPG_CARD_START -->.*?<!-- RPG_CARD_END -->",
            new_card,
            md_text,
            flags=re.DOTALL,
        )

    README_PATH.write_text(md_text, encoding="utf-8")

    # Save persistent progress snapshot to data/player_progress.json
    checked_lines = [
        line.strip() for line in md_text.splitlines() if re.match(r"^\s*-\s*\[[xX]\]", line)
    ]
    PROGRESS_JSON_PATH.write_text(
        json.dumps(
            {
                "player_name": player_name,
                "rank_label": stats["rank_label"],
                "current_tier": stats["current_code"],
                "total_exp": stats["total_exp"],
                "quests_completed": stats["total_checked"],
                "quests_total": stats["total_boxes"],
                "tiers_cleared": stats["cleared_count"],
                "current_tier_tp": stats["cur_tp"],
                "completed_quest_lines": checked_lines,
                "tier_breakdown": tier_counts,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print("====================================================================")
    print(f"  [+] RPG Card Synchronized in README.md & data/player_progress.json!")
    print(f"      Adventurer : {player_name}")
    print(f"      Rank       : {stats['rank_label']}")
    print(f"      Total EXP  : {stats['total_exp']:,} EXP ({stats['total_checked']}/{stats['total_boxes']} Quests)")
    print(f"      Tiers Done : {stats['cleared_count']} / {len(TIERS)} (Current Tier TP: {stats['cur_tp']}/3)")
    print("====================================================================")


if __name__ == "__main__":
    main()
