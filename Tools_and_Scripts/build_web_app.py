#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds docs/index.html in 100% English with Matte Dark Theme, Top 200 Games, Auto-Grader & RE Cheat Sheet."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
top200 = json.loads((ROOT / "data" / "top200_popular_games.json").read_text(encoding="utf-8"))
top200_json_str = json.dumps(top200, ensure_ascii=False)

dojo_ct = (ROOT / "Game_Hacking" / "Dojo_Labs_Reference.CT").read_text(encoding="utf-8")
pvz_ct = (ROOT / "Game_Hacking" / "PvZ.CT").read_text(encoding="utf-8")
ut99_ct = (ROOT / "Game_Hacking" / "UnrealTournament_UT99.CT").read_text(encoding="utf-8")
isaac_ct = (ROOT / "Game_Hacking" / "isaac-ng.CT").read_text(encoding="utf-8")
sor_ct = (ROOT / "Game_Hacking" / "StreetsOfRogue_v98.CT").read_text(encoding="utf-8")
dll_cpp = (ROOT / "Tools_and_Scripts" / "03_Internal_DLL_Skeleton" / "dllmain_internal_hook.cpp").read_text(encoding="utf-8")
z3_py = (ROOT / "Tools_and_Scripts" / "04_Python_RE_Toolkit" / "crackme_solvers_and_z3_lab.py").read_text(encoding="utf-8")

sample_artifacts = {
    "Dojo_Labs_Reference.CT": dojo_ct,
    "PvZ.CT": pvz_ct,
    "UnrealTournament_UT99.CT": ut99_ct,
    "isaac-ng.CT": isaac_ct,
    "StreetsOfRogue_v98.CT": sor_ct,
    "dllmain_internal_hook.cpp": dll_cpp,
    "crackme_solvers_and_z3_lab.py": z3_py,
}
samples_json_str = json.dumps(sample_artifacts, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dimmed">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="RE:DOJO — Awwwards-Inspired Reverse Engineering, Binary Auditing & Offline Game Hacking RPG Progression Engine (F- to SSS++)" />
  <meta name="theme-color" content="#14171c" />
  <title>🛡️ RE:DOJO — Reverse Engineering & Offline Game Hacking RPG</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>" />
  <style>
    /* =========================================================================
       1. AWWWARDS CYBER-TACTICAL DESIGN SYSTEM & OKLCH/MATTE COLOR TOKENS
       ========================================================================= */
    :root, [data-theme="dimmed"] {{
      --bg-dark: #12151a;
      --bg-elevated: #171b22;
      --bg-card: #1b2028;
      --bg-input: #101318;
      --bg-hover: #222833;
      --border: #2a313d;
      --border-subtle: rgba(255, 255, 255, 0.06);
      --border-glow: rgba(91, 155, 213, 0.42);
      --accent: #5b9bd5;
      --accent-bright: #79b8ff;
      --accent-soft: rgba(91, 155, 213, 0.14);
      --gold: #d4a74a;
      --gold-soft: rgba(212, 167, 74, 0.14);
      --green: #4ca960;
      --green-bright: #85e89d;
      --green-soft: rgba(76, 169, 96, 0.14);
      --purple: #9378c9;
      --text: #b4c0ce;
      --heading: #e4ecf4;
      --muted: #7f8c9b;
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.55), 0 1px 0 0 rgba(255, 255, 255, 0.04) inset;
      --radius-lg: 14px;
      --radius-md: 10px;
      --radius-sm: 6px;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
    }}
    [data-theme="carbon"] {{
      --bg-dark: #090b0e;
      --bg-elevated: #0f1217;
      --bg-card: #13171d;
      --bg-input: #07090b;
      --bg-hover: #1a2028;
      --border: #222832;
      --border-subtle: rgba(255, 255, 255, 0.05);
      --border-glow: rgba(88, 166, 255, 0.45);
      --accent: #4c8fd1;
      --accent-bright: #79c0ff;
      --accent-soft: rgba(76, 143, 209, 0.14);
      --gold: #c69739;
      --gold-soft: rgba(198, 151, 57, 0.14);
      --green: #429954;
      --green-bright: #7ee787;
      --green-soft: rgba(66, 153, 84, 0.13);
      --purple: #8468ba;
      --text: #a5b2c0;
      --heading: #dbe4ee;
      --muted: #727f8e;
      --shadow-card: 0 12px 34px -10px rgba(0, 0, 0, 0.78), 0 1px 0 0 rgba(255, 255, 255, 0.04) inset;
    }}
    [data-theme="sepia"] {{
      --bg-dark: #171512;
      --bg-elevated: #1e1b17;
      --bg-card: #221f1a;
      --bg-input: #12100e;
      --bg-hover: #2b2721;
      --border: #363028;
      --border-subtle: rgba(255, 245, 230, 0.05);
      --border-glow: rgba(114, 156, 184, 0.4);
      --accent: #729cb8;
      --accent-bright: #97bed8;
      --accent-soft: rgba(114, 156, 184, 0.15);
      --gold: #c79848;
      --gold-soft: rgba(199, 152, 72, 0.15);
      --green: #619c64;
      --green-bright: #94d297;
      --green-soft: rgba(97, 156, 100, 0.14);
      --purple: #9679a8;
      --text: #bfb6a9;
      --heading: #e2d9cc;
      --muted: #8c8377;
      --shadow-card: 0 10px 30px -10px rgba(0, 0, 0, 0.6), 0 1px 0 0 rgba(255, 245, 230, 0.04) inset;
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; color-scheme: dark; }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-dark);
      background-image:
        radial-gradient(ellipse 80% 50% at 50% -15%, var(--accent-soft), transparent),
        linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      background-size: 100% 100%, 36px 36px, 36px 36px;
      color: var(--text);
      min-height: 100vh;
      line-height: 1.58;
      padding-bottom: 80px;
      transition: background-color 0.2s, color 0.2s;
    }}

    /* Skip link & WCAG 2.2 AA Focus States */
    .skip-link {{
      position: absolute; top: -100px; left: 16px; z-index: 9999;
      background: var(--accent); color: #fff; padding: 8px 14px; border-radius: var(--radius-sm);
      font-weight: 700; text-decoration: none;
    }}
    .skip-link:focus {{ top: 12px; }}
    :focus-visible {{
      outline: 2px solid var(--accent-bright);
      outline-offset: 2px;
    }}

    .container {{ max-width: 1320px; margin: 0 auto; padding: 18px 20px; }}

    /* =========================================================================
       2. STICKY CYBER-HUD TOPBAR & COMMAND PALETTE TRIGGER
       ========================================================================= */
    header.hud-bar {{
      position: sticky; top: 0; z-index: 50;
      display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center;
      gap: 12px; margin-bottom: 22px; padding: 12px 16px;
      background: color-mix(in srgb, var(--bg-elevated) 86%, transparent);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-card);
    }}
    .brand-cluster {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
    .brand-emblem {{
      width: 38px; height: 38px; border-radius: 9px;
      background: linear-gradient(135deg, var(--accent-soft), rgba(212, 167, 74, 0.12));
      border: 1px solid var(--border-glow);
      display: flex; align-items: center; justify-content: center;
      font-size: 1.2rem;
    }}
    header h1 {{
      font-size: clamp(1.05rem, 1.8vw, 1.3rem);
      color: var(--heading);
      font-weight: 800;
      letter-spacing: -0.02em;
    }}
    .brand-sub {{
      font-size: 0.74rem; color: var(--muted); font-family: var(--font-mono);
      display: block; margin-top: 1px;
    }}
    .header-controls {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    .cmd-trigger {{
      display: inline-flex; align-items: center; gap: 8px;
      background: var(--bg-input); color: var(--text);
      border: 1px solid var(--border); padding: 6px 11px; border-radius: var(--radius-sm);
      font-size: 0.78rem; cursor: pointer; font-family: inherit;
      transition: border-color 0.15s, background 0.15s;
    }}
    .cmd-trigger:hover {{ border-color: var(--accent); background: var(--bg-hover); color: var(--heading); }}
    .cmd-trigger kbd {{
      font-family: var(--font-mono); font-size: 0.7rem; padding: 1px 5px;
      background: var(--bg-card); border: 1px solid var(--border); border-radius: 4px; color: var(--accent-bright);
    }}
    .privacy-pill {{
      font-size: 0.74rem; background: var(--green-soft); color: var(--green-bright);
      border: 1px solid rgba(76, 169, 96, 0.38); padding: 5px 10px; border-radius: var(--radius-sm);
      font-weight: 600;
    }}
    .theme-ctrl {{
      display: flex; align-items: center; gap: 7px; background: var(--bg-input);
      border: 1px solid var(--border); padding: 4px 10px; border-radius: var(--radius-sm);
      font-size: 0.76rem; color: var(--muted);
    }}
    .theme-ctrl select {{
      background: var(--bg-card); color: var(--heading); border: 1px solid var(--border);
      padding: 3px 6px; border-radius: 4px; font-size: 0.76rem; cursor: pointer;
    }}
    .theme-ctrl input[type="range"] {{ width: 68px; accent-color: var(--accent); cursor: pointer; }}

    /* =========================================================================
       3. BENTO TELEMETRY CHARACTER SHEET & 8-AXIS RADAR HUD
       ========================================================================= */
    .bento-hero {{
      display: grid;
      grid-template-columns: 1.3fr 1fr 0.85fr;
      gap: 16px;
      margin-bottom: 22px;
    }}
    @media (max-width: 1080px) {{ .bento-hero {{ grid-template-columns: 1fr 1fr; }} }}
    @media (max-width: 740px) {{ .bento-hero {{ grid-template-columns: 1fr; }} }}

    .bento-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px 20px;
      box-shadow: var(--shadow-card);
      position: relative;
      overflow: hidden;
    }}
    .bento-card::after {{
      content: "";
      position: absolute; top: 0; left: 0; right: 0; height: 2px;
      background: linear-gradient(90deg, transparent, var(--accent), var(--gold), transparent);
      opacity: 0.55;
    }}
    .char-header {{ display: flex; align-items: center; gap: 14px; margin-bottom: 14px; flex-wrap: wrap; }}
    .rank-orb {{
      width: 66px; height: 66px; border-radius: 14px;
      background: radial-gradient(circle at 30% 30%, var(--accent-soft), var(--bg-input));
      border: 2px solid var(--accent);
      box-shadow: 0 0 20px rgba(91, 155, 213, 0.22);
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      font-family: var(--font-mono);
    }}
    .rank-orb-label {{ font-size: 0.58rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; }}
    .rank-orb-code {{ font-size: 1.3rem; font-weight: 800; color: var(--heading); line-height: 1.1; }}
    .name-input {{
      background: var(--bg-input); border: 1px solid var(--border); color: var(--heading);
      font-size: 1.05rem; font-weight: 700; padding: 5px 10px; border-radius: var(--radius-sm);
      width: 230px; transition: border-color 0.15s;
    }}
    .name-input:focus {{ border-color: var(--accent); }}
    .stat-row {{ display: flex; justify-content: space-between; font-size: 0.84rem; margin: 5px 0; color: var(--muted); }}
    .stat-row strong {{ color: var(--heading); font-family: var(--font-mono); }}
    .progress-track {{
      width: 100%; height: 11px; background: var(--bg-input); border-radius: 999px;
      overflow: hidden; border: 1px solid var(--border); margin: 8px 0 12px;
    }}
    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--green));
      width: 0%;
      transition: width 0.35s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    .telemetry-pills {{
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 12px;
    }}
    .tele-pill {{
      background: var(--bg-input); border: 1px solid var(--border); border-radius: var(--radius-sm);
      padding: 7px 9px; text-align: center;
    }}
    .tele-pill .val {{ font-family: var(--font-mono); font-size: 0.96rem; font-weight: 800; color: var(--heading); display: block; }}
    .tele-pill .lbl {{ font-size: 0.68rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }}

    .skill-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 7px; align-content: start;
    }}
    .skill-chip {{
      font-size: 0.75rem; padding: 7px 10px; border-radius: var(--radius-sm);
      background: var(--bg-input); border: 1px solid var(--border); color: var(--muted);
      display: flex; align-items: center; gap: 6px; transition: transform 0.15s, border-color 0.15s;
    }}
    .skill-chip.unlocked {{
      border-color: rgba(76, 169, 96, 0.5); color: var(--green-bright); background: var(--green-soft);
      font-weight: 600;
    }}
    .radar-wrap {{
      display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;
    }}
    .radar-title {{
      font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.07em;
      color: var(--muted); margin-bottom: 6px; font-weight: 700;
    }}

    /* =========================================================================
       4. CSS ANCHOR POSITIONING TABS + SAME-DOCUMENT VIEW TRANSITIONS
          (Modern Web Guidance: anchor-positioning-tab-underline & same-document-transitions)
       ========================================================================= */
    nav.tabs-nav {{ margin-bottom: 18px; }}
    ul.tabs-list {{
      list-style: none;
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      position: relative;
      background: var(--bg-card);
      padding: 7px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-card);
    }}
    ul.tabs-list::before {{
      content: '';
      position: absolute;
      position-anchor: --active-tab;
      inset-block-start: calc(anchor(bottom) - 3px);
      inset-inline-start: anchor(left);
      inset-inline-end: anchor(right);
      block-size: 3px;
      background-color: var(--accent-bright);
      border-radius: 99px;
      z-index: 2;
      pointer-events: none;
    }}
    @media (prefers-reduced-motion: no-preference) {{
      ul.tabs-list::before {{
        transition: inset .2s cubic-bezier(0.22, 1, 0.36, 1);
      }}
    }}
    .tab-btn {{
      background: transparent; color: var(--text); border: 1px solid transparent;
      padding: 8px 13px; border-radius: var(--radius-sm); cursor: pointer;
      font-weight: 600; font-size: 0.83rem; font-family: inherit;
      transition: background 0.15s, color 0.15s;
    }}
    .tab-btn:hover {{ background: var(--bg-hover); color: var(--heading); }}
    .tab-btn[aria-selected="true"], .tab-btn.active {{
      anchor-name: --active-tab;
      background: var(--accent-soft);
      color: var(--heading);
      border-color: rgba(91, 155, 213, 0.35);
    }}
    @supports not (position-anchor: auto) {{
      ul.tabs-list::before {{ display: none; }}
      .tab-btn[aria-selected="true"], .tab-btn.active {{
        border-bottom: 3px solid var(--accent-bright);
      }}
    }}

    /* View Transitions for Tab Switching */
    .tab-panel {{ display: none; view-transition-name: active-dojo-panel; }}
    .tab-panel.active {{ display: block; }}
    @media (prefers-reduced-motion: reduce) {{
      ::view-transition-group(*),
      ::view-transition-old(*),
      ::view-transition-new(*) {{
        animation-duration: 0.01ms !important;
      }}
    }}

    /* =========================================================================
       5. FILTER BARS, ENGINE CHIPS & OFF-SCREEN DEFERRED TIER CARDS
          (Modern Web Guidance: defer-rendering-heavy-content & interactions-in-complex-layouts)
       ========================================================================= */
    .filter-bar {{
      display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 14px;
      background: var(--bg-card); padding: 12px 14px; border-radius: var(--radius-md);
      border: 1px solid var(--border); align-items: center;
    }}
    .filter-bar input, .filter-bar select {{
      background: var(--bg-input); color: var(--heading); border: 1px solid var(--border);
      padding: 8px 12px; border-radius: var(--radius-sm); font-size: 0.85rem; font-family: inherit;
    }}
    .filter-bar input {{ flex: 1; min-width: 220px; }}
    .chip-bar {{
      display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px; align-items: center;
    }}
    .chip-btn {{
      background: var(--bg-input); color: var(--muted); border: 1px solid var(--border);
      padding: 5px 11px; border-radius: 999px; font-size: 0.75rem; font-weight: 600;
      cursor: pointer; transition: all 0.15s; font-family: inherit;
    }}
    .chip-btn:hover {{ color: var(--heading); border-color: var(--accent); }}
    .chip-btn.active {{
      background: var(--accent-soft); color: var(--accent-bright); border-color: var(--accent);
    }}

    /* Tier Cards + Off-screen content-visibility: auto with mandatory contain-intrinsic-size */
    .tier-card {{
      background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius-md); padding: 16px 18px; margin-bottom: 12px;
      box-shadow: var(--shadow-card);
      transition: border-color 0.2s;
    }}
    .tier-card.deferred-tier {{
      content-visibility: auto;
      contain-intrinsic-size: auto none auto 220px;
    }}
    @supports not (content-visibility: auto) {{
      .tier-card.deferred-tier {{
        contain: layout style paint;
      }}
    }}
    .tier-card.cleared {{ border-color: rgba(76, 169, 96, 0.55); }}
    .tier-top {{
      display: flex; justify-content: space-between; align-items: center;
      flex-wrap: wrap; gap: 8px; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid var(--border);
    }}
    .tier-badge {{
      display: inline-block; padding: 3px 9px; border-radius: 5px;
      font-weight: 800; font-size: 0.78rem; font-family: var(--font-mono);
      background: var(--bg-input); color: var(--accent-bright); border: 1px solid var(--border);
    }}
    .tier-card.cleared .tier-badge {{
      background: var(--green-soft); color: var(--green-bright); border-color: rgba(76, 169, 96, 0.45);
    }}
    .tp-pill {{
      font-size: 0.76rem; font-weight: 700; font-family: var(--font-mono);
      padding: 4px 10px; border-radius: 999px;
      background: var(--bg-input); border: 1px solid var(--border);
    }}
    .quest-list {{ list-style: none; display: grid; gap: 7px; }}
    .quest-item {{
      display: flex; align-items: flex-start; gap: 10px; padding: 9px 12px;
      background: var(--bg-input); border: 1px solid var(--border); border-radius: var(--radius-sm);
      cursor: pointer; transition: background 0.14s, border-color 0.14s, transform 0.1s;
    }}
    .quest-item:hover {{ background: var(--bg-hover); border-color: rgba(91, 155, 213, 0.4); }}
    .quest-item.done {{ background: var(--green-soft); border-color: rgba(76, 169, 96, 0.42); }}
    .quest-item input[type="checkbox"] {{
      margin-top: 3px; width: 16px; height: 16px; accent-color: var(--green); cursor: pointer;
    }}
    .q-tag {{
      font-size: 0.69rem; font-weight: 700; padding: 2px 7px; border-radius: 4px;
      text-transform: uppercase; white-space: nowrap; border: 1px solid transparent;
      font-family: var(--font-mono);
    }}
    .tag-dojo {{ background: rgba(147, 120, 201, 0.16); color: #c8b5ed; border-color: rgba(147, 120, 201, 0.35); }}
    .tag-game {{ background: rgba(91, 155, 213, 0.15); color: #9ac8f5; border-color: rgba(91, 155, 213, 0.35); }}
    .tag-soft {{ background: rgba(212, 167, 74, 0.15); color: #e6c373; border-color: rgba(212, 167, 74, 0.35); }}
    .tag-tool {{ background: rgba(76, 169, 96, 0.15); color: #95e0a3; border-color: rgba(76, 169, 96, 0.35); }}

    /* =========================================================================
       6. RESPONSIVE CONTAINER-QUERY TABLES WITH STICKY HEADERS & STACKED FALLBACK
          (Modern Web Guidance: responsive-table)
       ========================================================================= */
    .table-wrapper {{
      container-type: inline-size;
      overflow: auto;
      max-inline-size: 100%;
      max-block-size: 680px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--bg-input);
    }}
    .table-wrapper table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
    }}
    .table-wrapper th,
    .table-wrapper td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--border);
      text-align: start;
      vertical-align: top;
    }}
    .table-wrapper thead {{
      position: sticky;
      inset-block-start: 0;
      background: var(--bg-elevated);
      z-index: 2;
    }}
    .table-wrapper thead th {{
      color: var(--heading);
      font-weight: 700;
      border-bottom: 2px solid var(--border);
    }}
    .table-wrapper tbody th {{
      position: sticky;
      inset-inline-start: 0;
      background: var(--bg-card);
      color: var(--heading);
      z-index: 1;
    }}
    .table-wrapper tbody tr:hover {{
      background: var(--bg-hover);
    }}
    @container (width < 600px) {{
      .table-wrapper thead {{
        display: none;
      }}
      .table-wrapper tr {{
        display: grid;
        padding: 0.75rem 1rem;
        border-block-end: 1px solid var(--border);
        gap: 4px;
      }}
      .table-wrapper td,
      .table-wrapper tbody th {{
        display: block;
        padding: 0.2rem 0;
        border: none;
        position: static;
        background: transparent;
      }}
      .table-wrapper td::before {{
        font-weight: 700;
        color: var(--accent-bright);
        font-family: var(--font-mono);
        font-size: 0.75rem;
      }}
      .table-wrapper.top200-wrapper {{
        --label-1: "Status";
        --label-2: "Rank";
        --label-3: "Game Title";
        --label-4: "Engine";
        --label-5: "Tier";
        --label-6: "Diff";
        --label-7: "RE Targets";
      }}
      .table-wrapper.top200-wrapper td:nth-child(1)::before {{ content: var(--label-1) ": "; }}
      .table-wrapper.top200-wrapper td:nth-child(2)::before {{ content: var(--label-2) ": "; }}
      .table-wrapper.top200-wrapper td:nth-child(4)::before {{ content: var(--label-4) ": "; }}
      .table-wrapper.top200-wrapper td:nth-child(5)::before {{ content: var(--label-5) ": "; }}
      .table-wrapper.top200-wrapper td:nth-child(6)::before {{ content: var(--label-6) ": "; }}
      .table-wrapper.top200-wrapper td:nth-child(7)::before {{ content: var(--label-7) ": "; }}
    }}

    /* =========================================================================
       7. BOXES, DRAG-AND-DROP AUTO-GRADER, COMMAND PALETTE & TOASTS
       ========================================================================= */
    .card-box {{
      background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 20px 22px; margin-bottom: 18px;
      box-shadow: var(--shadow-card);
    }}
    .card-box h2 {{ font-size: 1.18rem; color: var(--heading); margin-bottom: 6px; letter-spacing: -0.01em; }}
    .card-box h3 {{ font-size: 0.98rem; color: var(--heading); margin: 18px 0 8px; }}
    .form-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 12px; }}
    @media (max-width: 760px) {{ .form-grid {{ grid-template-columns: 1fr; }} }}
    .form-group label {{ display: block; font-size: 0.81rem; color: var(--muted); margin-bottom: 5px; font-weight: 600; }}
    .form-group input, .form-group select, textarea {{
      width: 100%; background: var(--bg-input); color: var(--heading); border: 1px solid var(--border);
      padding: 9px 11px; border-radius: var(--radius-sm); font-family: inherit; font-size: 0.86rem;
    }}
    textarea {{
      font-family: var(--font-mono); font-size: 0.79rem; min-height: 250px; resize: vertical; line-height: 1.5;
    }}
    .drop-zone {{
      border: 1.5px dashed var(--border);
      border-radius: var(--radius-md);
      padding: 12px 16px;
      margin-bottom: 14px;
      background: var(--bg-input);
      display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;
      transition: border-color 0.15s, background 0.15s;
    }}
    .drop-zone.dragover {{
      border-color: var(--accent-bright);
      background: var(--accent-soft);
    }}
    .btn {{
      background: var(--accent); color: #fff; border: 1px solid var(--accent); padding: 8px 14px;
      border-radius: var(--radius-sm); font-weight: 600; font-size: 0.83rem; cursor: pointer;
      display: inline-flex; align-items: center; gap: 6px; font-family: inherit;
      transition: filter 0.15s, transform 0.1s;
    }}
    .btn:hover {{ filter: brightness(1.1); }}
    .btn:active {{ transform: translateY(1px); }}
    .btn-outline {{
      background: var(--bg-input); color: var(--text); border: 1px solid var(--border);
    }}
    .btn-outline:hover {{ background: var(--bg-hover); border-color: var(--accent); color: var(--heading); filter: none; }}
    pre {{
      background: var(--bg-input); border: 1px solid var(--border); padding: 14px;
      border-radius: var(--radius-sm); overflow-x: auto; font-size: 0.8rem;
      font-family: var(--font-mono); color: var(--green-bright); margin-top: 10px; position: relative;
    }}
    code {{
      font-family: var(--font-mono); font-size: 0.8rem;
      background: var(--bg-input); padding: 2px 6px; border-radius: 4px; color: var(--accent-bright);
      border: 1px solid var(--border-subtle);
    }}
    .axis-bar-row {{
      display: grid; grid-template-columns: 195px 95px 1fr; gap: 10px; align-items: center;
      padding: 8px 11px; background: var(--bg-card); border: 1px solid var(--border);
      border-radius: var(--radius-sm); margin-bottom: 7px; font-size: 0.81rem;
    }}
    @media (max-width: 720px) {{ .axis-bar-row {{ grid-template-columns: 1fr; }} }}

    /* Command Palette Modal (<dialog>) */
    dialog.cmd-dialog {{
      margin: auto;
      width: min(640px, 92vw);
      background: var(--bg-elevated);
      color: var(--text);
      border: 1px solid var(--border-glow);
      border-radius: var(--radius-lg);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75);
      padding: 0;
      overflow: hidden;
    }}
    dialog.cmd-dialog::backdrop {{
      background: rgba(5, 7, 10, 0.72);
      backdrop-filter: blur(6px);
    }}
    .cmd-header {{
      display: flex; align-items: center; gap: 10px; padding: 12px 16px;
      border-bottom: 1px solid var(--border); background: var(--bg-input);
    }}
    .cmd-header input {{
      flex: 1; background: transparent; border: none; color: var(--heading);
      font-size: 0.95rem; font-family: inherit; outline: none;
    }}
    .cmd-results {{
      max-height: 360px; overflow-y: auto; padding: 8px; list-style: none;
    }}
    .cmd-item {{
      display: flex; justify-content: space-between; align-items: center; gap: 10px;
      padding: 9px 12px; border-radius: var(--radius-sm); cursor: pointer; font-size: 0.84rem;
    }}
    .cmd-item:hover, .cmd-item:focus {{
      background: var(--accent-soft); color: var(--heading); outline: none;
    }}

    /* Toast Notification */
    .toast-region {{
      position: fixed; bottom: 20px; right: 20px; z-index: 9000;
      display: flex; flex-direction: column; gap: 8px; pointer-events: none;
    }}
    .toast-msg {{
      background: var(--bg-elevated); color: var(--heading);
      border: 1px solid var(--accent); border-left: 4px solid var(--green);
      padding: 10px 14px; border-radius: var(--radius-sm);
      box-shadow: var(--shadow-card); font-size: 0.82rem; font-weight: 600;
      pointer-events: auto;
    }}
  </style>
</head>
<body>
  <a href="#mainContent" class="skip-link">Skip to main content</a>

  <div class="container" id="appRoot">
    <!-- TOP STICKY HUD BAR -->
    <header class="hud-bar" role="banner">
      <div class="brand-cluster">
        <div class="brand-emblem" aria-hidden="true">🛡️</div>
        <div>
          <h1>RE:DOJO &mdash; Reverse Engineering &amp; Offline Game Hacking RPG</h1>
          <span class="brand-sub">28-Tier Curriculum (F- to SSS++) • 5-Axis Artifact Evaluator • Top 200 Target Encyclopedia</span>
        </div>
      </div>
      <div class="header-controls">
        <button type="button" class="cmd-trigger" onclick="openCmdPalette()" aria-label="Open Quick Command Palette">
          <span>⚡ Quick Jump</span>
          <kbd>Ctrl+K</kbd>
        </button>
        <span class="privacy-pill" id="saveStatusPill" role="status" aria-live="polite">💾 Auto-Saved Locally</span>
        <div class="theme-ctrl">
          <label for="themeSelect">Theme:</label>
          <select id="themeSelect" onchange="changeTheme(this.value)">
            <option value="dimmed">🌙 Matte Dimmed</option>
            <option value="carbon">🌑 OLED Carbon</option>
            <option value="sepia">☕ Warm Sepia</option>
          </select>
          <label for="brightnessRange">Dimmer:</label>
          <input type="range" id="brightnessRange" min="65" max="100" value="95" oninput="changeBrightness(this.value)" title="Adjust screen brightness" />
        </div>
      </div>
    </header>

    <main id="mainContent">
      <!-- BENTO TELEMETRY CHARACTER SHEET -->
      <section class="bento-hero" aria-label="Adventurer Progression Telemetry">
        <!-- Card 1: Rank & Campaign Progress -->
        <div class="bento-card">
          <div class="char-header">
            <div class="rank-orb" aria-live="polite">
              <span class="rank-orb-label">RANK</span>
              <span class="rank-orb-code" id="uiRankOrb">F-</span>
            </div>
            <div>
              <label for="uiPlayerName" style="font-size:0.7rem; color:var(--muted); display:block; letter-spacing:0.05em;">ADVENTURER HANDLE (LOCAL STORAGE)</label>
              <input type="text" id="uiPlayerName" class="name-input" value="New Challenger" />
              <div id="uiClassTitle" style="font-size:0.86rem; color:var(--accent-bright); font-weight:700; margin-top:4px;">
                Rank: Tier F- &mdash; White-Box Novice
              </div>
            </div>
          </div>
          <div class="stat-row">
            <span>Campaign Tiers Cleared (<strong id="uiTiersCleared">0 / 29</strong>)</span>
            <span>Total EXP: <strong id="uiTotalExp" style="color:var(--gold);">0 EXP</strong> (<span id="uiQuestsDone">0</span> Quests)</span>
          </div>
          <div class="progress-track" role="progressbar" aria-label="Campaign Tier Completion" aria-valuemin="0" aria-valuemax="100" id="uiProgressTrack">
            <div class="progress-fill" id="uiCampaignBar"></div>
          </div>
          <div class="stat-row">
            <span id="uiTrialLabel">Current Tier Trial (3 Same-Tier OR 1 Higher-Tier Breakthrough):</span>
            <strong id="uiTpStatus" style="color:var(--green-bright);">0 / 3 TP</strong>
          </div>
          <div class="telemetry-pills">
            <div class="tele-pill">
              <span class="val" id="teleDojoDone">0 / 18</span>
              <span class="lbl">🧪 Dojo Labs</span>
            </div>
            <div class="tele-pill">
              <span class="val" id="teleTop200Done">0 / 200</span>
              <span class="lbl">🎮 Top 200 Targets</span>
            </div>
            <div class="tele-pill">
              <span class="val" id="teleNextRank">F</span>
              <span class="lbl">🚀 Next Breakthrough</span>
            </div>
          </div>
        </div>

        <!-- Card 2: 8-Stage Mastery Matrix -->
        <div class="bento-card">
          <div class="radar-title">🔓 8-Stage Reverse Engineering Mastery Matrix</div>
          <div class="skill-grid" id="uiSkillGrid"></div>
        </div>

        <!-- Card 3: Live SVG Skill Radar Telemetry -->
        <div class="bento-card radar-wrap">
          <div class="radar-title">📡 Live 5-Axis Capability Radar</div>
          <svg id="skillRadarSvg" viewBox="0 0 220 190" width="210" height="175" role="img" aria-label="5-Axis Reverse Engineering Capability Radar">
            <polygon points="110,20 190,75 160,162 60,162 30,75" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1" />
            <polygon points="110,48 162,84 142,142 78,142 58,84" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1" stroke-dasharray="3,3" />
            <line x1="110" y1="95" x2="110" y2="20" stroke="rgba(255,255,255,0.08)" />
            <line x1="110" y1="95" x2="190" y2="75" stroke="rgba(255,255,255,0.08)" />
            <line x1="110" y1="95" x2="160" y2="162" stroke="rgba(255,255,255,0.08)" />
            <line x1="110" y1="95" x2="60" y2="162" stroke="rgba(255,255,255,0.08)" />
            <line x1="110" y1="95" x2="30" y2="75" stroke="rgba(255,255,255,0.08)" />
            <polygon id="radarDataPoly" points="110,70 135,88 125,118 95,118 85,88" fill="rgba(91, 155, 213, 0.28)" stroke="#79b8ff" stroke-width="2" />
            <text x="110" y="13" text-anchor="middle" fill="#b4c0ce" font-size="9" font-family="monospace">ARCH/ABI</text>
            <text x="196" y="77" text-anchor="start" fill="#b4c0ce" font-size="9" font-family="monospace">PTR</text>
            <text x="166" y="176" text-anchor="middle" fill="#b4c0ce" font-size="9" font-family="monospace">HOOKS</text>
            <text x="54" y="176" text-anchor="middle" fill="#b4c0ce" font-size="9" font-family="monospace">OBFUS</text>
            <text x="24" y="77" text-anchor="end" fill="#b4c0ce" font-size="9" font-family="monospace">RING0</text>
          </svg>
        </div>
      </section>

      <!-- NAVIGATION TABS (CSS Anchor Positioning + Accessible ARIA Tablist) -->
      <nav class="tabs-nav" aria-label="Primary Workspace Sections">
        <ul class="tabs-list" role="tablist">
          <li role="presentation"><button type="button" role="tab" id="tabbtn-quests" aria-selected="true" aria-controls="tab-quests" class="tab-btn active" onclick="switchTab('quests', this)">⚔️ 28-Tier Campaign Quests</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-top200" aria-selected="false" aria-controls="tab-top200" class="tab-btn" onclick="switchTab('top200', this)">🔥 Top 200 Popular Games (#001–#200)</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-autograde" aria-selected="false" aria-controls="tab-autograde" class="tab-btn" onclick="switchTab('autograde', this)">🔬 Auto-Grade Script / .CT / Trainer</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-cheatsheet" aria-selected="false" aria-controls="tab-cheatsheet" class="tab-btn" onclick="switchTab('cheatsheet', this)">📖 RE &amp; Assembly Cheat Sheet</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-adder" aria-selected="false" aria-controls="tab-adder" class="tab-btn" onclick="switchTab('adder', this)">⚖️ 5-Axis Target Calculator</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-scoreboard" aria-selected="false" aria-controls="tab-scoreboard" class="tab-btn" onclick="switchTab('scoreboard', this)">🏅 Hall of Fame</button></li>
          <li role="presentation"><button type="button" role="tab" id="tabbtn-sync" aria-selected="false" aria-controls="tab-sync" class="tab-btn" onclick="switchTab('sync', this)">💾 Save &amp; README Sync</button></li>
        </ul>
      </nav>

      <!-- TAB 1: QUEST LOG -->
      <section id="tab-quests" role="tabpanel" aria-labelledby="tabbtn-quests" class="tab-panel active">
        <h2 id="heading-quests" tabindex="-1" style="position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0,0,0,0);">28-Tier Campaign Quests</h2>
        <div class="filter-bar">
          <input type="text" id="searchBox" aria-label="Search campaign quests" placeholder="🔍 Search quests, C++ labs, crackmes, games, engines..." oninput="renderTiers()" />
          <select id="catFilter" aria-label="Filter by quest category" onchange="renderTiers()">
            <option value="ALL">All Categories (Games + Software + Dojo Labs)</option>
            <option value="DOJO">🧪 In-Repo C++ Labs &amp; Crackmes (18)</option>
            <option value="GAME">🎮 Offline Games</option>
            <option value="SOFT">💻 Software &amp; Binary Auditing</option>
            <option value="TOOL">🛠️ Toolcraft &amp; Scripting</option>
          </select>
          <select id="statusFilter" aria-label="Filter by tier completion status" onchange="renderTiers()">
            <option value="ALL">All 29 Tiers (F- to SSS++)</option>
            <option value="LOCKED">Incomplete Tiers Only</option>
            <option value="CLEARED">Cleared Tiers Only</option>
          </select>
        </div>
        <div id="tiersContainer"></div>
      </section>

      <!-- TAB 2: TOP 200 POPULAR GAMES -->
      <section id="tab-top200" role="tabpanel" aria-labelledby="tabbtn-top200" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-top200" tabindex="-1">🔥 Top 200 Most Popular &amp; Iconic Games for Reverse Engineering (#001 – #200)</h2>
          <p style="color:var(--muted); font-size:0.86rem; margin-top:4px; margin-bottom:12px;">
            Check off any game from the Top 200 as you reverse engineer it! Every checked game automatically awards EXP for its Tier and counts toward your <strong>Breakthrough Rank-Up Trial (3 TP)</strong>.
          </p>
          <div class="filter-bar" style="margin-bottom:10px;">
            <input type="text" id="top200Search" aria-label="Filter Top 200 games" placeholder="🔍 Filter by game title, engine (Unity, Unreal, Source, C++, IL2CPP), or target struct..." oninput="renderTop200()" />
            <select id="top200TierFilter" aria-label="Filter Top 200 by tier bracket" onchange="renderTop200()">
              <option value="ALL">All Tiers (F+ to SSS+)</option>
              <option value="NOVICE">F+ / E-- / E- / E / E+ (Novice: 0.5 – 2.4)</option>
              <option value="FRONTIER">D- / D / D+ (32-Bit Frontier: 2.5 – 3.6)</option>
              <option value="MANAGED">C- / C / C+ (Managed / Mono: 3.7 – 4.9)</option>
              <option value="AAA">B- / B / B+ (AAA Engines: 5.0 – 6.1)</option>
              <option value="MODERN">A- / A / A+ (UE4/5 &amp; IL2CPP: 6.2 – 7.3)</option>
              <option value="ELITE">S- to SSS+ (Elite &amp; Symbolic: 7.4 – 9.8)</option>
            </select>
          </div>
          <!-- Quick Engine Filter Chips -->
          <div class="chip-bar" role="group" aria-label="Quick Engine Filter Chips">
            <span style="font-size:0.75rem; color:var(--muted); margin-right:4px;">Engine Filter:</span>
            <button type="button" class="chip-btn active" onclick="setEngineChip('', this)">All Engines (200)</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('Unity', this)">Unity / Mono</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('IL2CPP', this)">IL2CPP</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('Unreal', this)">Unreal Engine</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('Source', this)">Source Engine</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('Creation', this)">Creation / Bethesda</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('REDengine', this)">REDengine / CDPR</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('FromSoftware', this)">FromSoftware</button>
            <button type="button" class="chip-btn" onclick="setEngineChip('GameMaker', this)">GameMaker / XNA</button>
          </div>

          <div tabindex="0" role="region" aria-labelledby="heading-top200" class="table-wrapper top200-wrapper">
            <table>
              <thead>
                <tr>
                  <th scope="col" style="width:48px;">Done</th>
                  <th scope="col" style="width:58px;">#</th>
                  <th scope="col" style="width:210px;">Game Title</th>
                  <th scope="col" style="width:190px;">Engine &amp; Architecture</th>
                  <th scope="col" style="width:72px;">Tier</th>
                  <th scope="col" style="width:85px;">Difficulty</th>
                  <th scope="col">🎯 What to Search &amp; Reverse (Structs, Offsets, Classes &amp; Hooks)</th>
                </tr>
              </thead>
              <tbody id="top200Body"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 3: AUTO-GRADER FOR .CT / SCRIPTS / TRAINERS -->
      <section id="tab-autograde" role="tabpanel" aria-labelledby="tabbtn-autograde" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-autograde" tabindex="-1">🔬 Automated Artifact Tier &amp; Difficulty Grader (<code>.CT</code> / Trainers / DLLs / Scripts)</h2>
          <p style="color:var(--muted); font-size:0.86rem; margin-top:4px; margin-bottom:12px;">
            Drag &amp; drop or upload any file (<code>.CT</code>, <code>.CEA</code>, <code>.cpp</code>, <code>.hpp</code>, <code>.cs</code>, <code>.py</code>) or click one of the verified repository artifacts below. The static AST/regex analyzer inspects Cheat Engine XML pointer trees, struct displacements, assembly instructions (<code>aobscanmodule</code>, <code>alloc</code>, <code>movsxd</code>, shared-code <code>cmp</code> filters), Win32/VMT/Z3 calls, and computes the exact <strong>5-Axis Score (<code>0.5 – 10.0</code>)</strong> and <strong>RPG Tier</strong>!
          </p>

          <div class="drop-zone" id="artifactDropzone">
            <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
              <label class="btn" style="cursor:pointer;">
                📂 Upload or Drop Artifact (.CT / .cpp / .py / .cs)
                <input type="file" id="artifactFileInput" accept=".ct,.cea,.asm,.cpp,.c,.hpp,.h,.cs,.py,.txt" style="display:none;" onchange="handleArtifactUpload(this)" />
              </label>
              <span style="color:var(--muted); font-size:0.8rem;">Or inspect verified in-repo artifacts:</span>
            </div>
            <div style="display:flex; gap:6px; flex-wrap:wrap;">
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('Dojo_Labs_Reference.CT')">📄 Dojo_Labs.CT</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('PvZ.CT')">📄 PvZ.CT (E+)</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('UnrealTournament_UT99.CT')">📄 UT99.CT (D)</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('isaac-ng.CT')">📄 isaac-ng.CT (C-)</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('StreetsOfRogue_v98.CT')">📄 StreetsOfRogue.CT (C)</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('dllmain_internal_hook.cpp')">📄 Internal DLL (B+)</button>
              <button type="button" class="btn btn-outline" onclick="loadSampleArtifact('crackme_solvers_and_z3_lab.py')">📄 Z3 &amp; VM Solver (A)</button>
            </div>
          </div>

          <div class="form-grid" style="grid-template-columns: 1fr 1.15fr;">
            <div>
              <label for="artifactCodeBox" style="font-size:0.8rem; color:var(--muted); display:block; margin-bottom:4px;">
                Artifact Source / XML Content (<span id="gradedFileName" style="color:var(--accent-bright); font-family:var(--font-mono);">PvZ.CT</span>):
              </label>
              <textarea id="artifactCodeBox" oninput="runAutoGrader()" placeholder="Paste your .CT XML table, Auto Assembler script, C++ trainer/DLL, or Python solver here..."></textarea>
            </div>
            <div>
              <div style="background:var(--bg-input); border:1px solid var(--border); border-radius:var(--radius-md); padding:16px;">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:12px; padding-bottom:10px; border-bottom:1px solid var(--border);">
                  <div>
                    <div style="font-size:0.72rem; color:var(--muted); letter-spacing:0.05em;">AUTOMATED ARTIFACT EVALUATION</div>
                    <div id="gradeTierHeadline" style="font-size:1.22rem; font-weight:800; color:var(--heading);">Tier E+ (Codecave Weaver)</div>
                  </div>
                  <div style="text-align:right;">
                    <div style="font-size:0.72rem; color:var(--muted); letter-spacing:0.05em;">DIFFICULTY SCORE</div>
                    <div id="gradeScoreHeadline" style="font-size:1.3rem; font-weight:800; color:var(--gold); font-family:var(--font-mono);">2.1 / 10.0</div>
                  </div>
                </div>
                <div id="gradeAxesBreakdown"></div>
                <div id="gradeMetricsBox" style="font-size:0.79rem; font-family:var(--font-mono); color:var(--muted); margin-top:10px; padding-top:10px; border-top:1px solid var(--border);"></div>
                <div style="margin-top:14px; display:flex; justify-content:flex-end;">
                  <button type="button" class="btn" onclick="addGradedArtifactAsQuest()">➕ Claim &amp; Add Graded Artifact to My Progress</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- TAB 4: RE & ASSEMBLY CHEAT SHEET -->
      <section id="tab-cheatsheet" role="tabpanel" aria-labelledby="tabbtn-cheatsheet" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-cheatsheet" tabindex="-1">📖 Reverse Engineering, x86/x64 Calling Conventions &amp; Engine Cheat Sheet</h2>
          <p style="color:var(--muted); font-size:0.86rem; margin-top:4px;">
            Quick reference for ABI registers, opcode byte patches, Cheat Engine Auto Assembler templates, and game engine memory landmarks.
          </p>

          <h3 id="table-abi-heading">1. x86 &amp; x64 Calling Conventions (Where Function Arguments Live)</h3>
          <div tabindex="0" role="region" aria-labelledby="table-abi-heading" class="table-wrapper" style="margin-bottom:16px;">
            <table>
              <thead>
                <tr>
                  <th scope="col">ABI / Convention</th>
                  <th scope="col">Architecture</th>
                  <th scope="col">Integer / Pointer Args</th>
                  <th scope="col">Float / Vector Args</th>
                  <th scope="col">Return Value</th>
                  <th scope="col">Stack Cleanup &amp; Notes</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row"><code>__cdecl</code></th>
                  <td>x86 (32-bit)</td>
                  <td>Stack <code>[esp+4]</code>, <code>[esp+8]</code>...</td>
                  <td>Stack</td>
                  <td><code>EAX</code> / <code>ST(0)</code></td>
                  <td><strong>Caller</strong> cleans stack (<code>add esp, X</code>). Standard C default.</td>
                </tr>
                <tr>
                  <th scope="row"><code>__stdcall</code></th>
                  <td>x86 (32-bit)</td>
                  <td>Stack <code>[esp+4]</code>, <code>[esp+8]</code>...</td>
                  <td>Stack</td>
                  <td><code>EAX</code></td>
                  <td><strong>Callee</strong> cleans stack (<code>ret 0x0C</code>). Standard Win32 API.</td>
                </tr>
                <tr>
                  <th scope="row"><code>__thiscall</code></th>
                  <td>x86 (32-bit MSVC)</td>
                  <td><code>ECX</code> = <code>this</code> ptr; rest on Stack</td>
                  <td>Stack</td>
                  <td><code>EAX</code></td>
                  <td><strong>Callee</strong> cleans stack. Default for 32-bit C++ class member functions!</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Microsoft x64 ABI</strong></th>
                  <td>x64 (Windows)</td>
                  <td><code>RCX</code>, <code>RDX</code>, <code>R8</code>, <code>R9</code> (<code>RCX</code> = <code>this</code>)</td>
                  <td><code>XMM0</code>, <code>XMM1</code>, <code>XMM2</code>, <code>XMM3</code></td>
                  <td><code>RAX</code> / <code>XMM0</code></td>
                  <td>Caller reserves 32-byte <strong>Shadow Space</strong> on stack before <code>call</code>.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>System V AMD64 ABI</strong></th>
                  <td>x64 (Linux / PS4 / macOS)</td>
                  <td><code>RDI</code>, <code>RSI</code>, <code>RDX</code>, <code>RCX</code>, <code>R8</code>, <code>R9</code> (<code>RDI</code> = <code>this</code>)</td>
                  <td><code>XMM0</code> – <code>XMM7</code></td>
                  <td><code>RAX</code> / <code>XMM0</code></td>
                  <td>128-byte Red Zone below <code>RSP</code>; no shadow space required.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 id="table-opcode-heading">2. Essential Opcode Byte Patches (Hex Patching Quick Reference)</h3>
          <div tabindex="0" role="region" aria-labelledby="table-opcode-heading" class="table-wrapper" style="margin-bottom:16px;">
            <table>
              <thead>
                <tr>
                  <th scope="col">Patch Goal</th>
                  <th scope="col">Assembly Instruction</th>
                  <th scope="col">Hex Bytes</th>
                  <th scope="col">Typical Use Case</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row"><strong>No Operation (NOP)</strong></th>
                  <td><code>nop</code> / 2-byte <code>66 90</code></td>
                  <td><code>90</code></td>
                  <td>Erase ammo/stamina subtraction or unwanted function call</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Unconditional Short Jump</strong></th>
                  <td><code>jmp short +offset</code></td>
                  <td><code>EB &lt;rel8&gt;</code></td>
                  <td>Replace conditional branch <code>74</code> (<code>je</code>) or <code>75</code> (<code>jne</code>) with <code>EB</code> (always jump)</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Unconditional Near Jump</strong></th>
                  <td><code>jmp near +offset</code></td>
                  <td><code>E9 &lt;rel32&gt;</code></td>
                  <td>5-byte relative detour used by Cheat Engine codecaves &amp; MinHook</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Invert Conditional Near Jump</strong></th>
                  <td><code>je</code> &harr; <code>jne</code></td>
                  <td><code>0F 84</code> &harr; <code>0F 85</code></td>
                  <td>Flip license check or damage check condition (6-byte instruction)</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Force Function Return False (0)</strong></th>
                  <td><code>xor eax, eax; ret</code></td>
                  <td><code>31 C0 C3</code></td>
                  <td>Instantly return <code>0</code> / <code>false</code> at function prologue (e.g. <code>IsDebuggerPresent</code> / <code>destroyPlayer</code>)</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Force Function Return True (1)</strong></th>
                  <td><code>mov al, 1; ret</code></td>
                  <td><code>B0 01 C3</code></td>
                  <td>Instantly return <code>1</code> / <code>true</code> at validation function prologue (e.g. <code>HasDLC</code> / <code>CheckKey</code>)</td>
                </tr>
                <tr>
                  <th scope="row"><strong>64-Bit Absolute 14-Byte Jump</strong></th>
                  <td><code>jmp qword ptr [rip+0]; dq addr</code></td>
                  <td><code>FF 25 00 00 00 00 &lt;8-byte addr&gt;</code></td>
                  <td>Full 64-bit trampoline jump when target codecave is &gt;2 GB away</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 id="table-engine-heading">3. Game Engine Memory Landmarks (What to Look For First)</h3>
          <div tabindex="0" role="region" aria-labelledby="table-engine-heading" class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th scope="col">Game Engine</th>
                  <th scope="col">Signature Binaries / Files</th>
                  <th scope="col">Primary RE Tooling</th>
                  <th scope="col">Key Globals, Structures &amp; Entry Points</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row"><strong>Unity (Mono JIT)</strong></th>
                  <td><code>MonoBleedingEdge\</code>, <code>Assembly-CSharp.dll</code></td>
                  <td>dnSpyEx, ILSpy, CE Mono Dissector, BepInEx + Harmony</td>
                  <td>Decompile C# directly in <code>dnSpyEx</code>; enable <em>Mono &rarr; Activate Mono Features</em> in Cheat Engine.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Unity (IL2CPP AOT)</strong></th>
                  <td><code>GameAssembly.dll</code>, <code>global-metadata.dat</code></td>
                  <td>Il2CppDumper, Cpp2IL, Ghidra, MinHook</td>
                  <td>Run <code>Il2CppDumper</code> to generate <code>script.json</code> + dummy DLLs; hook native methods via RVA in <code>GameAssembly.dll</code>.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Unreal Engine 4 &amp; 5</strong></th>
                  <td><code>&lt;Game&gt;-Win64-Shipping.exe</code>, <code>.pak</code> / <code>.utoc</code></td>
                  <td>Dumper-7, UESDK, FModel, ReClass.NET</td>
                  <td>Locate <code>GWorld</code> (<code>UWorld*</code>), <code>GObjects</code> (<code>TUObjectArray</code>), <code>GNames</code> (<code>FNamePool</code>), and VMT index of <code>UObject::ProcessEvent</code>.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Source Engine (Valve)</strong></th>
                  <td><code>client.dll</code>, <code>engine.dll</code>, <code>tier0.dll</code></td>
                  <td>Source SDK, Netvar Dumper, ReClass.NET</td>
                  <td>Call exported <code>CreateInterface</code>, walk <code>IBaseClientDLL::GetAllClasses()</code> linked list for Netvars, hook <code>CreateMove</code>.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>Creation Engine (Bethesda)</strong></th>
                  <td><code>SkyrimSE.exe</code>, <code>Fallout4.exe</code>, <code>.esm</code></td>
                  <td>xEdit, SKSE64 / CommonLibSSE, Ghidra</td>
                  <td><code>PlayerCharacter</code> singleton, <code>ActorValueOwner</code> VMT, RTTI class descriptors, and Papyrus native function table.</td>
                </tr>
                <tr>
                  <th scope="row"><strong>GameMaker Studio</strong></th>
                  <td><code>data.win</code>, <code>audiogroup*.dat</code></td>
                  <td>UndertaleModTool (UTMT), Cheat Engine</td>
                  <td>Open <code>data.win</code> in UndertaleModTool to decompile GML scripts; scan dynamic <code>Double</code> values in RAM.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 5: 5-AXIS RUBRIC CALCULATOR & ADDER -->
      <section id="tab-adder" role="tabpanel" aria-labelledby="tabbtn-adder" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-adder" tabindex="-1">⚖️ Autonomous Target Builder (5-Axis Anti-Inflation Calculator)</h2>
          <p style="color:var(--muted); font-size:0.86rem; margin-top:4px;">
            To prevent anyone from assigning a fake <code>SSS++</code> rating to a trivial program, every custom game or application is evaluated across <strong>5 objective architectural axes</strong>:
          </p>
          <div class="form-grid">
            <div class="form-group">
              <label for="addTitle">Target Title (Game or Program)</label>
              <input type="text" id="addTitle" placeholder="e.g. Celeste / 7-Zip / Factorio" />
            </div>
            <div class="form-group">
              <label for="addCat">Category</label>
              <select id="addCat">
                <option value="GAME">🎮 Offline Game</option>
                <option value="SOFT">💻 Desktop Software / Binary Format</option>
                <option value="DOJO">🔐 Custom Crackme / CTF</option>
              </select>
            </div>
            <div class="form-group">
              <label for="axArch">Axis 1: Architecture &amp; Symbols (0.2 – 2.0)</label>
              <select id="axArch" onchange="updateRubricPreview()">
                <option value="0.2">+0.2 — Open Source / Plaintext Config / Full PDB Symbols</option>
                <option value="0.5">+0.5 — Standard Win32/x64 or .NET with Symbols</option>
                <option value="0.9" selected>+0.9 — Unity Mono / XNA / GameMaker / Lua VM</option>
                <option value="1.4">+1.4 — Stripped Native x86/x64 C++ Binary</option>
                <option value="1.7">+1.7 — Unity IL2CPP / Embedded LuaJIT / JNI</option>
                <option value="2.0">+2.0 — Console Emulator (Big-Endian PowerPC / ARM64)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="axMem">Axis 2: Memory &amp; Pointer Indirection (0.1 – 2.0)</label>
              <select id="axMem" onchange="updateRubricPreview()">
                <option value="0.1">+0.1 — Static Globals or Fixed 2D Array</option>
                <option value="0.4" selected>+0.4 — 1-to-3 Level Heap Pointer Chain</option>
                <option value="0.8">+0.8 — Dynamic Linked Lists / Scene Node Trees</option>
                <option value="1.2">+1.2 — Deep C++ VMTs / UE GWorld / Source Netvars</option>
                <option value="1.7">+1.7 — Data-Oriented SoA Slabs / ECS / 64-bit Coords</option>
                <option value="2.0">+2.0 — XOR/Encrypted Runtime RAM or VM Stack</option>
              </select>
            </div>
            <div class="form-group">
              <label for="axEng">Axis 3: Code &amp; Hook Complexity (0.1 – 2.0)</label>
              <select id="axEng" onchange="updateRubricPreview()">
                <option value="0.1">+0.1 — Basic Scalar Freeze / NOP Patch</option>
                <option value="0.5" selected>+0.5 — Codecave Injection / 2D Physics / Keygen Math</option>
                <option value="0.8">+0.8 — Shared Code Disambiguation Filter (Player vs Enemy)</option>
                <option value="1.2">+1.2 — 3D Vectors, Euler Angles &amp; 4x4 WorldToScreen</option>
                <option value="1.6">+1.6 — Internal C++ DLL, MinHook &amp; ImGui Overlay</option>
                <option value="2.0">+2.0 — Matching Decompilation / LLVM IR Binary Lifter</option>
              </select>
            </div>
            <div class="form-group">
              <label for="axProt">Axis 4: Binary Protection &amp; Obfuscation (0.0 – 2.5)</label>
              <select id="axProt" onchange="updateRubricPreview()">
                <option value="0.0" selected>+0.0 — Unprotected Offline Binary</option>
                <option value="0.5">+0.5 — Basic Anti-Debug (IsDebuggerPresent / PEB)</option>
                <option value="1.2">+1.2 — Executable Packer (UPX) or .text CRC32 Guard</option>
                <option value="1.8">+1.8 — Custom Stack VM / O-LLVM Flattening / MBA</option>
                <option value="2.5">+2.5 — Commercial Virtualizer (VMProtect / Themida)</option>
              </select>
            </div>
            <div class="form-group">
              <label for="axPriv">Axis 5: Privilege Boundary (0.0 – 1.5)</label>
              <select id="axPriv" onchange="updateRubricPreview()">
                <option value="0.0" selected>+0.0 — User-Mode Process (Ring-3)</option>
                <option value="0.7">+0.7 — Encrypted Network Protocol Emulation (Blowfish/RSA)</option>
                <option value="1.5">+1.5 — Ring-0 Kernel Driver / KVM Hypervisor VMI / Silicon</option>
              </select>
            </div>
            <div class="form-group">
              <label for="addQuest">Quest Objective Description</label>
              <input type="text" id="addQuest" placeholder="e.g. Reverse Player struct, hook stamina, and build AOB script" />
            </div>
          </div>
          <div style="margin-top:16px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
            <div id="rubricPreview" style="font-size:1.05rem; font-weight:800; color:var(--gold); font-family:var(--font-mono);">
              Computed Score: 1.8 / 10.0  ➔  Assigned Tier: [Tier E]
            </div>
            <button type="button" class="btn" onclick="addCustomTargetToLog()">➕ Add Target to My Quest Log &amp; Generate JSON</button>
          </div>
          <pre id="jsonOutput">// Generated JSON entry for data/custom_targets.json will appear here...</pre>
        </div>
      </section>

      <!-- TAB 6: SCOREBOARD -->
      <section id="tab-scoreboard" role="tabpanel" aria-labelledby="tabbtn-scoreboard" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-scoreboard" tabindex="-1">🏅 Global Artifact-Verified Hall of Fame</h2>
          <p style="color:var(--muted); font-size:0.86rem; margin-top:4px; margin-bottom:12px;">
            In your browser you see your personal progress privately. To rank on the <strong>Global Hall of Fame</strong>, quests must be backed by a verifiable artifact in the repository (<code>.CT</code> table, solver script, or technical writeup) evaluated by the automated 5-Axis Rubric.
          </p>
          <div tabindex="0" role="region" aria-labelledby="heading-scoreboard" class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th scope="col">Rank</th>
                  <th scope="col">Adventurer</th>
                  <th scope="col">Class Title</th>
                  <th scope="col">Verified Tier</th>
                  <th scope="col">Verified EXP</th>
                  <th scope="col">Proof Artifacts in Repository</th>
                </tr>
              </thead>
              <tbody id="scoreboardBody"></tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 7: HOW SAVING & SYNC WORKS -->
      <section id="tab-sync" role="tabpanel" aria-labelledby="tabbtn-sync" class="tab-panel">
        <div class="card-box">
          <h2 id="heading-sync" tabindex="-1">💾 How Your Progress is Saved (Browser <code>localStorage</code>, JSON &amp; <code>README.md</code>)</h2>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:12px;">
            <div style="background:var(--bg-input); border:1px solid var(--border); padding:14px; border-radius:var(--radius-md);">
              <h3 style="margin-top:0;">1. 🌐 Automatic Browser Save (<code>localStorage</code>)</h3>
              <p style="font-size:0.84rem; color:var(--muted);">
                Every time you check off a quest or a Top 200 game, edit your Adventurer handle, or change the theme/brightness, your browser <strong>instantly saves your state in <code>localStorage</code></strong> on your machine. Refreshing or closing the browser never loses progress, and your session is 100% private to you.
              </p>
            </div>
            <div style="background:var(--bg-input); border:1px solid var(--border); padding:14px; border-radius:var(--radius-md);">
              <h3 style="margin-top:0;">2. 📄 Syncing with <code>README.md</code> &amp; <code>data/player_progress.json</code></h3>
              <p style="font-size:0.84rem; color:var(--muted);">
                Locally, you can either mark <code>- [x]</code> directly inside <code>README.md</code> and run <code>.\\update_progress.bat</code>, OR click <strong>"💾 Export <code>player_progress.json</code>"</strong> below, place it in the <code>data/</code> folder, and run <code>python Tools_and_Scripts/rpg_manager.py --from-json</code>!
              </p>
            </div>
          </div>
          <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:16px;">
            <button type="button" class="btn" onclick="exportProgressJson()">💾 Export player_progress.json (Sync to README.md)</button>
            <label class="btn btn-outline" style="cursor:pointer;">
              📂 Import player_progress.json
              <input type="file" accept=".json" style="display:none;" onchange="importProgressJson(this)" />
            </label>
            <button type="button" class="btn btn-outline" onclick="applyDeaversPreset()">🧙‍♂️ Load Author deavers Preset (Tier C)</button>
            <button type="button" class="btn btn-outline" onclick="resetProfile()">🌱 Reset to Clean New Game (Tier F- | 0 EXP)</button>
          </div>
          <pre># 1. Update the RPG Card in README.md after checking - [x] boxes:
.\\update_progress.bat --name "YourHandle"

# 2. Automatically grade any .CT table, trainer, DLL, or script from CLI:
python Tools_and_Scripts/auto_artifact_grader.py Game_Hacking/PvZ.CT
python Tools_and_Scripts/rpg_manager.py --analyze Game_Hacking

# 3. Sync exported data/player_progress.json from browser into README.md:
python Tools_and_Scripts/rpg_manager.py --from-json</pre>
        </div>
      </section>
    </main>
  </div>

  <!-- COMMAND PALETTE MODAL (Ctrl+K / Cmd+K) -->
  <dialog id="cmdDialog" class="cmd-dialog" aria-label="Quick Command Palette">
    <div class="cmd-header">
      <span aria-hidden="true">⚡</span>
      <input type="text" id="cmdSearchInput" placeholder="Jump to any tab, Top 200 game, Dojo lab, or preset action..." oninput="renderCmdResults()" />
      <button type="button" class="btn btn-outline" style="padding:4px 8px; font-size:0.74rem;" onclick="closeCmdPalette()">ESC</button>
    </div>
    <ul id="cmdResultsList" class="cmd-results"></ul>
  </dialog>

  <!-- TOAST NOTIFICATION REGION -->
  <div id="toastRegion" class="toast-region" aria-live="polite"></div>

  <script>
    const TOP200_GAMES = {top200_json_str};
    const SAMPLE_ARTIFACTS = {samples_json_str};

    const TIER_META = [
      {{ code: "F-",    diff: 0.2,  lo: 0.0, hi: 0.4,  title: "Unranked Novice",           exp: 100,  act: "Act I: Novice Grounds" }},
      {{ code: "F",     diff: 0.5,  lo: 0.5, hi: 0.6,  title: "White-Box Initiate",        exp: 120,  act: "Act I: Novice Grounds" }},
      {{ code: "F+",    diff: 0.8,  lo: 0.7, hi: 0.9,  title: "Script Tinkerer",           exp: 150,  act: "Act I: Novice Grounds" }},
      {{ code: "E--",   diff: 1.1,  lo: 1.0, hi: 1.2,  title: "Memory Scanner",            exp: 180,  act: "Act I: Novice Grounds" }},
      {{ code: "E-",    diff: 1.5,  lo: 1.3, hi: 1.6,  title: "Pointer Seeker",            exp: 220,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "E",     diff: 1.8,  lo: 1.7, hi: 2.0,  title: "Assembly Apprentice",       exp: 260,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "E+",    diff: 2.2,  lo: 2.1, hi: 2.4,  title: "Codecave Weaver",           exp: 300,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "D-",    diff: 2.6,  lo: 2.5, hi: 2.8,  title: "Pointer Alchemist",         exp: 350,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "D",     diff: 3.0,  lo: 2.9, hi: 3.2,  title: "Entity Filter Tactician",   exp: 400,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "D+",    diff: 3.4,  lo: 3.3, hi: 3.6,  title: "Stealth & Logic Hacker",    exp: 450,  act: "Act II: 32-Bit Frontier" }},
      {{ code: "C-",    diff: 3.8,  lo: 3.7, hi: 4.0,  title: "Struct & Bitmask Scholar",  exp: 520,  act: "Act III: Managed Realms" }},
      {{ code: "C",     diff: 4.2,  lo: 4.1, hi: 4.5,  title: "Adventurer (Managed JIT)",  exp: 600,  act: "Act III: Managed Realms" }},
      {{ code: "C+",    diff: 4.7,  lo: 4.6, hi: 4.9,  title: "Harmony & Runtime Modder",  exp: 680,  act: "Act III: Managed Realms" }},
      {{ code: "B-",    diff: 5.1,  lo: 5.0, hi: 5.3,  title: "VMT & RTTI Investigator",   exp: 770,  act: "Act IV: AAA Architecture" }},
      {{ code: "B",     diff: 5.5,  lo: 5.4, hi: 5.7,  title: "Netvar & 3D Math Engineer", exp: 860,  act: "Act IV: AAA Architecture" }},
      {{ code: "B+",    diff: 5.9,  lo: 5.8, hi: 6.1,  title: "Internal DLL Specialist",   exp: 960,  act: "Act IV: AAA Architecture" }},
      {{ code: "A-",    diff: 6.3,  lo: 6.2, hi: 6.5,  title: "UE4/5 SDK Architect",       exp: 1100, act: "Act V: Modern Reflection" }},
      {{ code: "A",     diff: 6.7,  lo: 6.6, hi: 6.9,  title: "IL2CPP & VM Reverser",      exp: 1250, act: "Act V: Modern Reflection" }},
      {{ code: "A+",    diff: 7.1,  lo: 7.0, hi: 7.3,  title: "LuaJIT & ECS Hacker",       exp: 1400, act: "Act V: Modern Reflection" }},
      {{ code: "S-",    diff: 7.5,  lo: 7.4, hi: 7.6,  title: "Custom Engine Conqueror",   exp: 1600, act: "Act VI: DOD & Emulation" }},
      {{ code: "S",     diff: 7.8,  lo: 7.7, hi: 7.9,  title: "DOD & MBA De-Obfuscator",   exp: 1800, act: "Act VI: DOD & Emulation" }},
      {{ code: "S+",    diff: 8.1,  lo: 8.0, hi: 8.2,  title: "Cross-ISA Emulator Master", exp: 2000, act: "Act VI: DOD & Emulation" }},
      {{ code: "SS-",   diff: 8.4,  lo: 8.3, hi: 8.5,  title: "JVM JNI & Protocol Cryptor",exp: 2250, act: "Act VI: DOD & Emulation" }},
      {{ code: "SS",    diff: 8.7,  lo: 8.6, hi: 8.8,  title: "Packer & OEP Unpacker",     exp: 2500, act: "Act VI: DOD & Emulation" }},
      {{ code: "SS+",   diff: 9.0,  lo: 8.9, hi: 9.1,  title: "VMProtect & Arxan Auditor", exp: 2800, act: "Act VI: DOD & Emulation" }},
      {{ code: "SSS-",  diff: 9.3,  lo: 9.2, hi: 9.4,  title: "Symbolic Z3 / angr Savant", exp: 3200, act: "Act VII: Pantheon of Silicon" }},
      {{ code: "SSS",   diff: 9.6,  lo: 9.5, hi: 9.7,  title: "Ring-0 & VMI Hypervisor",   exp: 3600, act: "Act VII: Pantheon of Silicon" }},
      {{ code: "SSS+",  diff: 9.8,  lo: 9.8, hi: 9.9,  title: "Matching Decomp Titan",     exp: 4200, act: "Act VII: Pantheon of Silicon" }},
      {{ code: "SSS++", diff: 10.0, lo: 10.0,hi: 10.0, title: "Demigod of Silicon",        exp: 5000, act: "Act VII: Pantheon of Silicon" }}
    ];

    const DEFAULT_QUESTS = [
      {{ id: "q_f_1", tier: "F-", cat: "DOJO", kw: "lab01_static_scalars", text: "[In-Repo Lab 01 Bronze] Run lab01_static_scalars.exe in Apprentice Mode & freeze HP/Arrows", deavers: true }},
      {{ id: "q_f_2", tier: "F-", cat: "DOJO", kw: "Slime King in Hardcore", text: "[In-Repo Lab 01 Gold] Beat Slime King in Hardcore Blind Mode by scanning Gold (50 -> 999,999)", deavers: true }},
      {{ id: "q_f_3", tier: "F-", cat: "GAME", kw: "Bulánci-Kitty", text: "Bulánci-Kitty / Bonanza-Clone (Own C/C++17 SDL2) — Inspect own player structs in Cheat Engine", deavers: true }},
      {{ id: "q_f_4", tier: "F-", cat: "SOFT", kw: "System Informer", text: "Windows Calculator / CLI Process — Inspect .text, .rdata, .data & Heap regions in System Informer", deavers: false }},
      {{ id: "q_f0_1", tier: "F", cat: "DOJO", kw: "lab02_floats_and_bitmasks", text: "[In-Repo Lab 02 Bronze] Scan Float Mana Pool using Decreased Value after casting Arcane Bolt", deavers: true }},
      {{ id: "q_f0_2", tier: "F", cat: "DOJO", kw: "DIVINE_BLESSING", text: "[In-Repo Lab 02 Gold] Clear Poison/Curse bits & set 0x80 DIVINE_BLESSING bitmask to open Sanctuary", deavers: true }},
      {{ id: "q_f0_3", tier: "F", cat: "TOOL", kw: "IEEE-754", text: "Write a Python struct.pack('<f', val) converter to inspect IEEE-754 float hex representations", deavers: false }},
      {{ id: "q_fp_1", tier: "F+", cat: "DOJO", kw: "crackme01_apprentice_gate", text: "[In-Repo Crackme 01 Bronze] Extract Stage 1 .rdata passcode in x64dbg / Ghidra", deavers: true }},
      {{ id: "q_fp_2", tier: "F+", cat: "DOJO", kw: "STACK_ALCHEMY", text: "[In-Repo Crackme 01 Gold] Recover Stage 2 runtime Stack String ('STACK_ALCHEMY') without patching", deavers: true }},
      {{ id: "q_fp_3", tier: "F+", cat: "GAME", kw: "Clicker Heroes", text: "Banana / Clicker Heroes / Zup! S — Scan Double counters, boolean win flags & Speedhack timers", deavers: false }},
      {{ id: "q_fp_4", tier: "F+", cat: "GAME", kw: "SEGA Mega Drive", text: "SEGA Mega Drive Classics (Bonanza Bros / Golden Axe) — Lock lives inside 64KB 68000 RAM bank", deavers: false }},
      {{ id: "q_emm_1", tier: "E--", cat: "DOJO", kw: "Tutorial-x86_64.exe", text: "Cheat Engine Built-in Tutorial (Tutorial-x86_64.exe) — Complete Steps 1 through 9", deavers: true }},
      {{ id: "q_emm_2", tier: "E--", cat: "GAME", kw: "PwnAdventure", text: "Squally / PwnAdventure 3 — Solve live x86 assembly puzzles & UE3 GameLogic.dll speed patches", deavers: false }},
      {{ id: "q_emm_3", tier: "E--", cat: "SOFT", kw: "Microcorruption", text: "Microcorruption Embedded CTF — Solve Tutorial, New Orleans, Sydney & Hanoi MSP430 locks", deavers: false }},
      {{ id: "q_em_1", tier: "E-", cat: "DOJO", kw: "lab03_2d_grid_maze", text: "[In-Repo Lab 03] Locate the 36-byte board[6][6] in Hex View & collect all 3 Relics (0x77) avoiding Traps (0x8F)", deavers: true }},
      {{ id: "q_em_2", tier: "E-", cat: "GAME", kw: "winmine.exe", text: "Windows Minesweeper (winmine.exe) & 3D Pinball Space Cadet — Reveal static 2D mine grid & lock balls", deavers: false }},
      {{ id: "q_em_3", tier: "E-", cat: "SOFT", kw: "Scintilla.dll", text: "Notepad++ / HxD (Scintilla.dll) — Locate active text buffer in RAM & trace Win32 SendMessageW IDs", deavers: false }},
      {{ id: "q_e_1", tier: "E", cat: "DOJO", kw: "lab04_multilevel_pointers", text: "[In-Repo Lab 04] Build a 3-level pointer chain from g_WorldManager that survives 5 Heap floor reallocations", deavers: true }},
      {{ id: "q_e_2", tier: "E", cat: "DOJO", kw: "crackme02_serial_math", text: "[In-Repo Crackme 02] Reverse ValidateSerialKey() in Ghidra & write a Python Keygen for AAAA-BBBB-CCCC", deavers: true }},
      {{ id: "q_e_3", tier: "E", cat: "TOOL", kw: "external_memory_trainer", text: "[Tool 01] Compile & run external_memory_trainer.exe (OpenProcess + RPM/WPM + ResolvePointerChain)", deavers: false }},
      {{ id: "q_e_4", tier: "E", cat: "GAME", kw: "AssaultCube", text: "Aim Hero & AssaultCube — Locate LocalPlayer, EntityList, 3D target coords (X,Y,Z) & ViewAngles", deavers: false }},
      {{ id: "q_ep_1", tier: "E+", cat: "DOJO", kw: "lab05_code_injection", text: "[In-Repo Lab 05] NOP ConsumeStamina() subtraction & inject Auto Assembler code cave into GainExperience()", deavers: true }},
      {{ id: "q_ep_2", tier: "E+", cat: "GAME", kw: "PvZ.CT", text: "Plants vs. Zombies GOTY (PvZ.CT) — AOB Infinite Sun, Instant Recharge, Immortal Plants & Lua Speedhack", deavers: true }},
      {{ id: "q_ep_3", tier: "E+", cat: "GAME", kw: "Castle Crashers", text: "Castle Crashers & Deponia — Character XP/Stat structs, juggle physics & Visionaire 2D inventory arrays", deavers: false }},
      {{ id: "q_ep_4", tier: "E+", cat: "TOOL", kw: "pe_and_aob_scanner", text: "[Tool 04-A] Scan binaries for wildcard AOB signatures & section entropy with pe_and_aob_scanner.py", deavers: false }},
      {{ id: "q_dm_1", tier: "D-", cat: "GAME", kw: "DOOM + DOOM II", text: "DOOM + DOOM II (id Tech 1 / KEX) — Fixed-point (16.16) physics, mobj_t actor structs & god-mode bitflags", deavers: false }},
      {{ id: "q_dm_2", tier: "D-", cat: "GAME", kw: "Duke Nukem 3D", text: "POSTAL (Classic/Redux) & Duke Nukem 3D — Isometric coordinate vectors & Build Engine sector arrays", deavers: false }},
      {{ id: "q_dm_3", tier: "D-", cat: "SOFT", kw: "7-Zip", text: "7-Zip (7z.exe / 7za.dll) — Reverse 32-byte .7z signature header, CRC32 check & LZMA2 stream structs", deavers: false }},
      {{ id: "q_d_1", tier: "D", cat: "DOJO", kw: "lab06_shared_code_filter", text: "[In-Repo Lab 06] Write a shared-code factionId ([rcx+08]) filter in ApplySharedDamage for God Mode + 1-Hit Kill", deavers: true }},
      {{ id: "q_d_2", tier: "D", cat: "DOJO", kw: "crackme03_xor_rol", text: "[In-Repo Crackme 03] Invert the ROL8 + position-XOR loop in Python to decrypt the 20-char rune", deavers: true }},
      {{ id: "q_d_3", tier: "D", cat: "GAME", kw: "UnrealTournament_UT99.CT", text: "Unreal Tournament 99 (UnrealTournament_UT99.CT) — UObject/APawn hierarchy & smart shared damage filter", deavers: true }},
      {{ id: "q_d_4", tier: "D", cat: "GAME", kw: "Half-Life 1", text: "Half-Life 1 / CS 1.6 / POSTAL 2 — GoldSrc cl_entity_s array, recoil punch angles & UE2 UPawn linked lists", deavers: false }},
      {{ id: "q_d_5", tier: "D", cat: "SOFT", kw: "WinRAR", text: "WinRAR (rar.exe) — Audit RAR5 magic header parser & Win32 DialogBoxParamW trial evaluation flow", deavers: false }},
      {{ id: "q_dp_1", tier: "D+", cat: "GAME", kw: "Chaos Theory", text: "Splinter Cell: Chaos Theory & Far Cry 1 — Lock stealth light/acoustic floats & CryEngine 1 stamina", deavers: false }},
      {{ id: "q_dp_2", tier: "D+", cat: "GAME", kw: "SPORE", text: "SPORE / SimCity 4 / LEGO Star Wars & Batman — Bypass creature complexity limit & 64-bit stud counters", deavers: false }},
      {{ id: "q_dp_3", tier: "D+", cat: "SOFT", kw: "IOLI Crackme", text: "IOLI Crackme Suite (0x00 to 0x09) — Solve all 10 academic x86 crackmes in Ghidra/IDA", deavers: false }},
      {{ id: "q_cm_1", tier: "C-", cat: "DOJO", kw: "lab07_rtti_and_vmt", text: "[In-Repo Lab 07] Map AdventurerAccount in ReClass.NET & swap vptr (+0x00) to GrandmasterAccount VMT", deavers: true }},
      {{ id: "q_cm_2", tier: "C-", cat: "GAME", kw: "isaac-ng.CT", text: "The Binding of Isaac: Repentance (isaac-ng.CT) — Entity_Player struct, heart bitmasks & stat lock", deavers: true }},
      {{ id: "q_cm_3", tier: "C-", cat: "GAME", kw: "Geometry Dash", text: "Geometry Dash / Barony / Chasm / UBERMOSH — Cocos2d-x PlayLayer::destroyPlayer noclip & voxel stats", deavers: false }},
      {{ id: "q_cm_4", tier: "C-", cat: "SOFT", kw: "Bomb Lab", text: "CMU CS:APP Binary Bomb Lab (bomb) — Defuse all 6 x86_64 assembly phases in GDB/Ghidra", deavers: false }},
      {{ id: "q_c_1", tier: "C", cat: "DOJO", kw: "crackme04_binary_license", text: "[In-Repo Crackme 04] Reverse 24-byte BinaryLicenseHeader struct & forge license.dat with struct.pack", deavers: true }},
      {{ id: "q_c_2", tier: "C", cat: "GAME", kw: "StreetsOfRogue_v98.CT", text: "Streets of Rogue v98 (StreetsOfRogue_v98.CT) — Unity Mono Dissector, Agent/Stat classes & EXP hooks", deavers: true }},
      {{ id: "q_c_3", tier: "C", cat: "GAME", kw: "Punch Club", text: "Punch Club 1&2 / Graveyard Keeper / Enter the Gungeon — Decompile Assembly-CSharp.dll in dnSpyEx", deavers: false }},
      {{ id: "q_c_4", tier: "C", cat: "GAME", kw: "Stardew Valley", text: "Stardew Valley & Terraria — JIT signature scanning for Terraria.Player::Update & wing flight time", deavers: false }},
      {{ id: "q_cp_1", tier: "C+", cat: "GAME", kw: "Lethal Company", text: "Lethal Company & Unturned — Write custom BepInEx + Harmony C# runtime hooks (PlayerControllerB)", deavers: false }},
      {{ id: "q_cp_2", tier: "C+", cat: "GAME", kw: "Subnautica", text: "Subnautica: Below Zero / RimWorld / ULTRAKILL — LiveMixin health, OxygenManager & Harmony prefixes", deavers: false }},
      {{ id: "q_cp_3", tier: "C+", cat: "SOFT", kw: "KeePass", text: "KeePass 2.x (KDBX v4 Vault) — Audit KDBX 4.0 binary header, Argon2d params & ProtectedBinary XOR RAM", deavers: false }},
      {{ id: "q_bm_1", tier: "B-", cat: "DOJO", kw: "lab08_3d_aim_and_w2s", text: "[In-Repo Lab 08] Compute 3D Camera Pitch/Yaw Euler angles & 4x4 ViewMatrix W2S to hit all 3 Phantom Drones", deavers: false }},
      {{ id: "q_bm_2", tier: "B-", cat: "GAME", kw: "Skyrim Special Edition", text: "Skyrim Special Edition & Mount & Blade: Warband — PlayerCharacter singleton, ActorValueOwner VMT & SKSE", deavers: false }},
      {{ id: "q_bm_3", tier: "B-", cat: "SOFT", kw: "sqlite3.dll", text: "SQLite3 Engine (sqlite3.dll) — Reverse 100-byte DB header, B-Tree pages & sqlite3VdbeExec bytecode VM", deavers: false }},
      {{ id: "q_b_1", tier: "B", cat: "DOJO", kw: "crackme05_antidebug_crc", text: "[In-Repo Crackme 05] Bypass IsDebuggerPresent, PEB & 0xCC INT3 scanner using Hardware Breakpoints (DR0-DR3)", deavers: false }},
      {{ id: "q_b_2", tier: "B", cat: "GAME", kw: "Garry's Mod", text: "CS: Source / Garry's Mod / Half-Life 2 — Dump Source Netvars, hook CreateMove VMT & extract [3][4] bones", deavers: false }},
      {{ id: "q_b_3", tier: "B", cat: "GAME", kw: "Spec Ops: The Line", text: "Spec Ops: The Line / A Story About My Uncle / Injustice — UE3 GObjects & GNames SDK scanning", deavers: false }},
      {{ id: "q_b_4", tier: "B", cat: "SOFT", kw: "PuTTY", text: "PuTTY & WinSCP (SSH Client) — Locate in-memory SSH session keys & hook cleartext send/recv buffers", deavers: false }},
      {{ id: "q_bp_1", tier: "B+", cat: "DOJO", kw: "lab09_internal_hook", text: "[In-Repo Lab 09] Inject internal_hook_lab09.dll to invoke Engine_SpawnMythicChest(0x1337BEEF) internally", deavers: false }},
      {{ id: "q_bp_2", tier: "B+", cat: "GAME", kw: "Euro Truck Simulator 2", text: "Euro Truck Simulator 2 & Assetto Corsa — SCS Telemetry shared memory, speed limiter & physics structs", deavers: false }},
      {{ id: "q_bp_3", tier: "B+", cat: "GAME", kw: "Grand Theft Auto V", text: "GTA V Legacy (Story Mode) & HITMAN 2 — RAGE WorldPtr/ReplayInterface & Glacier 2 ZActor RTTI", deavers: false }},
      {{ id: "q_bp_4", tier: "B+", cat: "SOFT", kw: "libavcodec", text: "VLC Media Player & FFmpeg (libavcodec) — Audit MP4/MKV moov/trak box demuxers & SIMD decode loops", deavers: false }},
      {{ id: "q_am_1", tier: "A-", cat: "GAME", kw: "KovaaK", text: "KovaaK's & Escape the Backrooms — Dump UE4 SDK with Dumper-7, traverse GWorld->Actors & hook ProcessEvent", deavers: false }},
      {{ id: "q_am_2", tier: "A-", cat: "GAME", kw: "Palworld", text: "Palworld & Manor Lords & PEAK — UE5 FNamePool decryption, Pal capture formulas & regional wealth", deavers: false }},
      {{ id: "q_am_3", tier: "A-", cat: "SOFT", kw: "NtQuerySystemInformation", text: "Sysinternals Procmon / System Informer — Audit undocumented ntdll.dll (NtQuerySystemInformation) calls", deavers: false }},
      {{ id: "q_a_1", tier: "A", cat: "DOJO", kw: "crackme06_custom_vm", text: "[In-Repo Crackme 06] Disassemble g_BytecodeProgram[] in our 12-opcode Custom Stack VM to recover 'VM_KING!'", deavers: false }},
      {{ id: "q_a_2", tier: "A", cat: "GAME", kw: "Aimlabs", text: "Aimlabs & Slime Rancher 2 — Run Il2CppDumper on GameAssembly.dll & hook stripped native methods with MinHook", deavers: false }},
      {{ id: "q_a_3", tier: "A", cat: "SOFT", kw: "libwireshark", text: "Wireshark (libwireshark.dll) — Reverse dissector tables & write a custom game protocol dissector", deavers: false }},
      {{ id: "q_ap_1", tier: "A+", cat: "DOJO", kw: "lab10_integrity_boss", text: "[In-Repo Lab 10 BOSS] Defeat Archon of Silicon without tripping .text CRC32 Guard (VMT hook or XOR math)", deavers: false }},
      {{ id: "q_ap_2", tier: "A+", cat: "GAME", kw: "PAYDAY 2", text: "PAYDAY 2 & Don't Starve Together — Hook LuaJIT / lua_State* bridges (SuperBLT / ThePlayer structs)", deavers: false }},
      {{ id: "q_ap_3", tier: "A+", cat: "GAME", kw: "Civilization VI", text: "Civilization VI / SAO: Hollow Realization / Dragon Age: Inquisition — Frostbite 3 TypeInfo & Fog of War", deavers: false }},
      {{ id: "q_ap_4", tier: "A+", cat: "SOFT", kw: "UPX", text: "UPX Manual Unpacking Lab — Trace tail-jump to OEP in x64dbg, dump process & rebuild IAT with Scylla", deavers: false }},
      {{ id: "q_sm_1", tier: "S-", cat: "GAME", kw: "Elden Ring", text: "Dark Souls III / Sekiro / Elden Ring (Offline) — WorldChrMan, CSChrIns, i-frame flags & Param tables", deavers: false }},
      {{ id: "q_sm_2", tier: "S-", cat: "GAME", kw: "Armored Core VI", text: "Armored Core VI & Monster Hunter: World — Dantelion ACS stagger gauges & MT Framework part thresholds", deavers: false }},
      {{ id: "q_sm_3", tier: "S-", cat: "SOFT", kw: "Blender", text: "Blender (.blend SDNA) & Godot Engine (ClassDB) — Reverse serialized C struct DNA blocks & reflection", deavers: false }},
      {{ id: "q_s_1", tier: "S", cat: "DOJO", kw: "crackme07_ollvm_mba", text: "[In-Repo Crackme 07] Simplify Mixed Boolean-Arithmetic (MBA) & deflatten the O-LLVM state machine", deavers: false }},
      {{ id: "q_s_2", tier: "S", cat: "GAME", kw: "Factorio", text: "Factorio / Noita / Teardown / Dwarf Fortress — Custom SoA slab allocators & cellular automata pixel grids", deavers: false }},
      {{ id: "q_s_3", tier: "S", cat: "SOFT", kw: "PyInstaller", text: "PyInstaller & Electron V8 Snapshots — Extract CArchive .pyc code objects & repair magic headers", deavers: false }},
      {{ id: "q_sp_1", tier: "S+", cat: "GAME", kw: "Breath of the Wild", text: "Zelda: BOTW (Cemu PowerPC Big-Endian) & TOTK (Ryujinx ARM64) — Cross-arch memory & instruction patching", deavers: false }},
      {{ id: "q_sp_2", tier: "S+", cat: "GAME", kw: "Bloodborne", text: "Bloodborne (shadPS4) & Persona 5 (RPCS3 Cell SPU) — System V AMD64 .sprx modules & 0x300000000 RAM", deavers: false }},
      {{ id: "q_sp_3", tier: "S+", cat: "SOFT", kw: "QEMU", text: "QEMU / Unicorn Engine (TCG JIT) — Trace how guest ARM64/MIPS blocks translate to host x86_64 code", deavers: false }},
      {{ id: "q_ssm_1", tier: "SS-", cat: "GAME", kw: "Lineage 2", text: "Lineage 2 Chronicle 2 (L2.exe & Study Server) — Blowfish/RSA packet crypto & opcode reconstruction", deavers: false }},
      {{ id: "q_ssm_2", tier: "SS-", cat: "GAME", kw: "osu!", text: "osu! (Offline Framework) & Minecraft Java (JNI/JVMTI) — .osr LZMA replay parser & C++ JVM attachment", deavers: false }},
      {{ id: "q_ssm_3", tier: "SS-", cat: "SOFT", kw: "OpenSSL", text: "OpenSSL (libcrypto) & libsodium — Identify AES-NI, SHA-256 constants & ChaCha20 quarter-rounds in stripped bins", deavers: false }},
      {{ id: "q_ss_1", tier: "SS", cat: "TOOL", kw: "ChaCha20 Packer", text: "Custom ELF64/PE64 ChaCha20 Packer & Reflective Loader — Trace memfd_create/VirtualAlloc & auto-unpack", deavers: false }},
      {{ id: "q_ss_2", tier: "SS", cat: "GAME", kw: "No Man's Sky", text: "No Man's Sky & Vintage SecuROM/SafeDisc Binaries — Procedural voxel seeds, OEP recovery & IAT fixing", deavers: false }},
      {{ id: "q_ss_3", tier: "SS", cat: "SOFT", kw: "FLARE-On", text: "Mandiant FLARE-On CTF Challenges (Stages 1–5) — Multi-layered PE, custom encoding & shellcode analysis", deavers: false }},
      {{ id: "q_ssp_1", tier: "SS+", cat: "GAME", kw: "Red Dead Redemption 2", text: "Red Dead Redemption 2 (Offline Checksum Study) — Analyze Arxan .text integrity threads & stealth VMT hooks", deavers: false }},
      {{ id: "q_ssp_2", tier: "SS+", cat: "DOJO", kw: "VMProtect", text: "VMProtect v2/v3 & Themida CrackMes — Trace VM_Enter, log VIP handler dispatches & recover stolen OEP bytes", deavers: false }},
      {{ id: "q_ssp_3", tier: "SS+", cat: "TOOL", kw: "Frida", text: "Write a Dynamic Binary Instrumentation (Frida / Pin) tracer to log virtualized API exits", deavers: false }},
      {{ id: "q_sssm_1", tier: "SSS-", cat: "DOJO", kw: "crackme08_z3_symbolic", text: "[In-Repo Crackme 08 BOSS] Solve the 10 coupled algebraic/XOR equations using Python Z3 SMT Solver ('Z3_MAGE!')", deavers: false }},
      {{ id: "q_sssm_2", tier: "SSS-", cat: "TOOL", kw: "Miasm", text: "Write an automated O-LLVM Control-Flow Deflattener & MBA Simplifier using Miasm / Triton / Z3", deavers: false }},
      {{ id: "q_sssm_3", tier: "SSS-", cat: "SOFT", kw: "angr", text: "Automated CrackMe & Bomb-Lab Solver with angr & AFL++ — Symbolic bitvectors (claripy.BVS) & path pruning", deavers: false }},
      {{ id: "q_sss_1", tier: "SSS", cat: "SOFT", kw: "QEMU/KVM", text: "QEMU/KVM Virtual Machine Memory Introspection (Linux Host -> Guest) — Walk x64 CR3->PML4 page tables", deavers: false }},
      {{ id: "q_sss_2", tier: "SSS", cat: "TOOL", kw: "MmCopyVirtualMemory", text: "Custom Windows Kernel Driver (Ring-0 WDK) — Implement IOCTL, MmCopyVirtualMemory & EPROCESS walking", deavers: false }},
      {{ id: "q_sss_3", tier: "SSS", cat: "TOOL", kw: "EPT Shadow", text: "Custom Tiny Hypervisor (Intel VT-x / AMD-V EPT Shadow Page Hooking) — Split Execute-Only vs Read views", deavers: false }},
      {{ id: "q_sssp_1", tier: "SSS+", cat: "SOFT", kw: "decomp.me", text: "Matching Decompilation (decomp.me / DevilutionX / SM64) — Achieve a 100% byte-for-byte identical C++ match", deavers: false }},
      {{ id: "q_sssp_2", tier: "SSS+", cat: "GAME", kw: "Star Citizen", text: "OpenMW / OpenRCT2 / Star Citizen (64-bit Planetary Coords) — Reimplement proprietary formats & physics", deavers: false }},
      {{ id: "q_sssp_3", tier: "SSS+", cat: "TOOL", kw: "SLEIGH", text: "Ghidra Custom SLEIGH Processor Module — Author a .slaspec specification for an undocumented CPU/VM", deavers: false }},
      {{ id: "q_ssspp_1", tier: "SSS++", cat: "TOOL", kw: "Remill", text: "Automated Binary Lifter (x86_64 / VM Bytecode -> LLVM IR) — Strip obfuscation with LLVM opt -O3 passes", deavers: false }},
      {{ id: "q_ssspp_2", tier: "SSS++", cat: "SOFT", kw: "Glitching", text: "Silicon/Firmware Glitching & BootROM RE (ESP32-S3 / ARM Cortex-M) — SPI/JTAG dump & fault injection", deavers: false }},
      {{ id: "q_ssspp_3", tier: "SSS++", cat: "GAME", kw: "Lindbergh", text: "Arcade Crypto Dongle Emulation & GPU Shader Decompiler (d3d11.dll proxy / HLSL DXBC/SPIR-V)", deavers: false }}
    ];

    const STORAGE_KEY = "re_rpg_journey_state_v2";
    let state = {{
      playerName: "New Challenger",
      theme: "dimmed",
      brightness: 95,
      checked: {{}},
      customQuests: []
    }};

    let lastGradedResult = null;

    function changeTheme(themeName) {{
      document.documentElement.setAttribute("data-theme", themeName);
      state.theme = themeName;
      saveState();
    }}

    function changeBrightness(val) {{
      document.getElementById("appRoot").style.filter = `brightness(${{val}}%)`;
      state.brightness = parseInt(val, 10);
      try {{ localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }} catch(e) {{}}
    }}

    function loadState() {{
      try {{
        const raw = localStorage.getItem(STORAGE_KEY) || localStorage.getItem("re_rpg_journey_state_v1");
        if (raw) state = Object.assign(state, JSON.parse(raw));
      }} catch (e) {{}}
      document.getElementById("uiPlayerName").value = state.playerName || "New Challenger";
      document.getElementById("themeSelect").value = state.theme || "dimmed";
      document.documentElement.setAttribute("data-theme", state.theme || "dimmed");
      const br = state.brightness || 95;
      document.getElementById("brightnessRange").value = br;
      document.getElementById("appRoot").style.filter = `brightness(${{br}}%)`;
    }}

    function saveState() {{
      state.playerName = document.getElementById("uiPlayerName").value.trim() || "New Challenger";
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
        const pill = document.getElementById("saveStatusPill");
        pill.textContent = "💾 Saved in Browser (" + new Date().toLocaleTimeString() + ")";
      }} catch (e) {{}}
      recalcAndRender();
    }}

    document.getElementById("uiPlayerName").addEventListener("input", saveState);

    function getAllQuests() {{
      const top200Quests = TOP200_GAMES.map(g => ({{
        id: "top200_" + g.rank,
        tier: g.tier,
        cat: "GAME",
        kw: g.title.split(" ")[0],
        text: `[Top #${{g.rank}}] ${{g.title}} (${{g.engine}}) — ${{g.what_to_find}}`,
        isTop200: true
      }}));
      return DEFAULT_QUESTS.concat(state.customQuests || []).concat(top200Quests);
    }}

    function scoreToTierObj(score) {{
      const s = Math.max(0.5, Math.min(10.0, Math.round(score * 10) / 10));
      for (const t of TIER_META) {{
        if (s >= t.lo - 0.01 && s <= t.hi + 0.01) return t;
      }}
      return TIER_META[TIER_META.length - 1];
    }}

    function updateRubricPreview() {{
      const a1 = parseFloat(document.getElementById("axArch").value);
      const a2 = parseFloat(document.getElementById("axMem").value);
      const a3 = parseFloat(document.getElementById("axEng").value);
      const a4 = parseFloat(document.getElementById("axProt").value);
      const a5 = parseFloat(document.getElementById("axPriv").value);
      const total = Math.min(10.0, Math.max(0.5, +(a1 + a2 + a3 + a4 + a5).toFixed(1)));
      const tObj = scoreToTierObj(total);
      document.getElementById("rubricPreview").textContent =
        `Computed Score: ${{total.toFixed(1)}} / 10.0  ➔  Assigned Tier: [Tier ${{tObj.code}} — ${{tObj.title}}]`;
      return {{ total, tier: tObj.code, rubric: {{ arch_symbols: a1, memory_indirection: a2, engine_complexity: a3, binary_protection: a4, privilege_boundary: a5 }} }};
    }}

    function addCustomTargetToLog() {{
      const title = document.getElementById("addTitle").value.trim() || "Custom RE Target";
      const cat = document.getElementById("addCat").value;
      const quest = document.getElementById("addQuest").value.trim() || "Reverse structures, memory pointers, and control flow";
      const {{ total, tier, rubric }} = updateRubricPreview();

      const newQ = {{
        id: "cust_" + Date.now(),
        tier: tier,
        cat: cat,
        kw: title,
        text: `[Custom ${{total.toFixed(1)}}/10] ${{title}} — ${{quest}}`
      }};
      state.customQuests.push(newQ);
      state.checked[newQ.id] = true;
      saveState();

      const jsonSnippet = {{
        id: newQ.id,
        title: title,
        category: cat === "GAME" ? "Game" : "Software",
        computed_tier: tier,
        computed_score: total,
        rubric: rubric,
        quest: quest,
        completed: true
      }};
      document.getElementById("jsonOutput").textContent = JSON.stringify(jsonSnippet, null, 2);
    }}

    /* =========================================================================
       AUTOMATED ARTIFACT GRADER (.CT / .CEA / .CPP / .CS / .PY)
       ========================================================================= */
    function gradeArtifactText(text, filename) {{
      const lowerName = (filename || "").toLowerCase();
      const isCT = lowerName.endsWith(".ct") || lowerName.endsWith(".cea") || text.includes("<CheatTable") || text.includes("[ENABLE]");
      const ev = {{ a1: [], a2: [], a3: [], a4: [], a5: [] }};
      let a1 = 0.4, a2 = 0.2, a3 = 0.2, a4 = 0.0, a5 = 0.0;
      let metricsText = "";

      if (isCT) {{
        const activeText = text.replace(/\\{{[\\s\\S]*?\\}}/g, "");
        const lowAll = text.toLowerCase();

        const offsetBlocks = text.match(/<Offsets>[\\s\\S]*?<\\/Offsets>/gi) || [];
        let maxPtrDepth = 0;
        offsetBlocks.forEach(blk => {{
          const offs = blk.match(/<Offset>/gi) || [];
          if (offs.length > maxPtrDepth) maxPtrDepth = offs.length;
        }});

        const dispMatches = [...activeText.matchAll(/\\[(?:e?[a-z]{{2,3}}|r[a-z0-9]{{1,2}})\\+([0-9a-fA-F]{{2,8}})\\]/g)];
        const allDispMatches = [...text.matchAll(/\\[(?:e?[a-z]{{2,3}}|r[a-z0-9]{{1,2}})\\+([0-9a-fA-F]{{2,8}})\\]/g)];
        const maxDisp = dispMatches.reduce((m, x) => Math.max(m, parseInt(x[1], 16)), 0);
        const maxContextDisp = allDispMatches.reduce((m, x) => Math.max(m, parseInt(x[1], 16)), 0);

        const aobCount = (activeText.match(/\\baobscan(?:module|region)?\\b/gi) || []).length;
        const allocCount = (activeText.match(/\\balloc\\s*\\(/gi) || []).length;
        const luaCount = (text.match(/\\{{\\$lua\\}}|<LuaScript>/gi) || []).length;
        const nearAlloc64 = (activeText.match(/alloc\\s*\\(\\s*\\w+\\s*,\\s*\\$?[0-9a-fA-F]+\\s*,\\s*\\w+\\s*\\)/gi) || []).length;
        const cmpBranches = (activeText.match(/\\b(cmp|test)\\b[\\s\\S]*?\\b(je|jne|jz|jnz|jg|jl|ja|jb|jle|jge|jbe|jnl)\\b/gi) || []).length;

        if (/big endian|cemu|rpcs3|ryujinx|arm64|powerpc/i.test(lowAll)) {{
          a1 = 2.0; ev.a1.push("Cross-ISA Emulator / Big-Endian target (2.0)");
        }} else if (/gameassembly\\.dll|il2cpp|global-metadata/i.test(lowAll)) {{
          a1 = 1.7; ev.a1.push("Unity IL2CPP Native Assembly (1.7)");
        }} else if (/gobjects|gnames|uworld|fnamepool|processevent/i.test(lowAll)) {{
          a1 = 1.5; ev.a1.push("Unreal Engine 4/5 Reflection (1.5)");
        }} else if (/unityplayer\\.dll|mono_|launchmonodatacollector/i.test(lowAll) || (/\\b(rax|rcx|rdx|r8|r9|r11|movsxd)\\b/i.test(text) && /call\\s+r1[0-5]/i.test(text))) {{
          a1 = 1.15; ev.a1.push("64-bit Unity / Managed JIT Runtime (x64 + JIT trampolines) (1.15)");
        }} else if (/\\b(rax|rcx|rdx|r8|r9|r11|movsxd|qword ptr)\\b/i.test(text)) {{
          a1 = 1.0; ev.a1.push("Native x86_64 Architecture (64-bit registers) (1.0)");
        }} else if (/isaac-ng\\.exe/i.test(lowAll)) {{
          a1 = 0.95; ev.a1.push("Custom C++20 Game Engine (`isaac-ng.exe`) (0.95)");
        }} else if (/engine\\.dll|core\\.dll|render\\.dll/i.test(lowAll)) {{
          a1 = 0.75; ev.a1.push("Multi-module C++ Engine (`Engine.dll` / `Core.dll`) (0.75)");
        }} else if (/popcapgame1\\.exe|plantsvszombies/i.test(lowAll)) {{
          a1 = 0.55; ev.a1.push("32-bit C++ Framework (`popcapgame1.exe` x86) (0.55)");
        }} else {{
          a1 = 0.4; ev.a1.push("Standard 32-bit x86 target (0.4)");
        }}

        if (maxPtrDepth >= 5) {{
          a2 = 1.05; ev.a2.push(`Deep ${{maxPtrDepth}}-level pointer chains (${{offsetBlocks.length}} chains) (1.05)`);
        }} else if (maxPtrDepth >= 3) {{
          a2 = 0.80; ev.a2.push(`Multi-level ${{maxPtrDepth}}-deep pointer chains (0.80)`);
        }} else if (maxContextDisp >= 0x10000 && maxDisp >= 0x1000) {{
          a2 = 1.00; ev.a2.push(`Large C++ engine class offsets (active +0x${{maxDisp.toString(16).toUpperCase()}}, context +0x${{maxContextDisp.toString(16).toUpperCase()}}) (1.00)`);
        }} else if (maxDisp >= 0x1000) {{
          a2 = 0.65; ev.a2.push(`C++ class member offsets (up to +0x${{maxDisp.toString(16).toUpperCase()}}) (0.65)`);
        }} else if (maxPtrDepth >= 1 || maxDisp > 0) {{
          a2 = 0.45; ev.a2.push(`Struct displacement addressing (+0x${{maxDisp.toString(16).toUpperCase()}}) (0.45)`);
        }} else {{
          a2 = 0.20; ev.a2.push("Direct / static addressing (0.20)");
        }}
        if (/mov\\s+\\w+,\\s*\\[[^\\]]+\\][\\s\\S]*?test\\s+\\w+,\\s*\\w+[\\s\\S]*?jz/i.test(activeText)) {{
          a2 = +(Math.min(2.0, a2 + 0.20)).toFixed(2);
          ev.a2.push("Manual NULL-checked pointer walk inside assembly (+0.20)");
        }}

        if (allocCount >= 1) {{
          a3 = 0.65; ev.a3.push(`Auto Assembler codecave hooks (${{allocCount}} allocs, ${{aobCount}} AOB scans) (0.65)`);
        }}
        if (aobCount >= 5) {{
          a3 += 0.25; ev.a3.push(`Multi-feature AOB script suite (${{aobCount}} injections) (+0.25)`);
        }}
        if (aobCount >= 8) {{
          a3 += 0.45; ev.a3.push("Comprehensive 8+ AOB table covering multiple subsystems (+0.45)");
        }}
        if (/check_enemy|enemy_hit|god\\s*mode|one[\\s-]*shot/i.test(activeText) || cmpBranches >= 3) {{
          a3 += 0.30; ev.a3.push("Shared-code entity filter (Player vs Enemy disambiguation) (+0.30)");
        }}
        if (luaCount >= 1) {{
          a3 += 0.20; ev.a3.push(`Embedded Cheat Engine {{$lua}} automation (${{luaCount}} blocks) (+0.20)`);
        }}
        if (nearAlloc64 >= 1) {{
          a3 += 0.35; ev.a3.push(`64-bit RIP-relative near-memory codecaves (${{nearAlloc64}} hooks) (+0.35)`);
        }}
        if (/Float|Double|movss|addss|subss|mulss|xmm/i.test(text)) {{
          a3 += 0.15; ev.a3.push("Floating-point / SSE state manipulation (+0.15)");
        }}
        a3 = +(Math.min(2.0, a3)).toFixed(2);

        if (/vmprotect|themida|arxan|vmp0/i.test(lowAll)) {{
          a4 = 2.0; ev.a4.push("Commercial virtualizer / integrity guard target (2.0)");
        }} else if (aobCount > 0 && nearAlloc64 > 0 && /aobscan\\(/i.test(activeText)) {{
          a4 = 0.55; ev.a4.push("Raw JIT heap AOB scanning (moduleless dynamic CLR/Mono JIT pages) (0.55)");
        }} else if (/\\b(rol|ror|shl|shr|cmov\\w+)\\b/i.test(text)) {{
          a4 = 0.35; ev.a4.push("Bitwise / conditional-move (`cmov`) state logic (0.35)");
        }} else {{
          a4 = 0.0; ev.a4.push("Unobfuscated target binary (0.0)");
        }}

        a5 = 0.0; ev.a5.push("Ring-3 User-Mode Cheat Engine table (0.0)");
        metricsText = `Detected .CT Metrics: AOB Injections = ${{aobCount}} | Codecave Allocs = ${{allocCount}} | Pointer Chains = ${{offsetBlocks.length}} (Max Depth = ${{maxPtrDepth}}) | Max Struct Offset = +0x${{maxDisp.toString(16).toUpperCase()}} | Lua Blocks = ${{luaCount}}`;
      }} else {{
        const clean = text.replace(/\\/\\*[\\s\\S]*?\\*\\/|\"\"\"[\\s\\S]*?\"\"\"/g, "").replace(/\\/\\/[^\\n]*|#[^\\n]*/g, "").toLowerCase();

        if (/remill|mcsema|sleigh|llvm::|irbuilder/.test(clean)) {{ a1 = 2.0; ev.a1.push("Compiler IR / LLVM / SLEIGH lifter (2.0)"); }}
        else if (/jni_getcreatedjavavms|jvmti|cemu|arm64/.test(clean)) {{ a1 = 1.8; ev.a1.push("Cross-ISA / JVM Native Interface (1.8)"); }}
        else if (/il2cpp|gameassembly\\.dll|lua_state/.test(clean)) {{ a1 = 1.6; ev.a1.push("IL2CPP / Embedded Lua VM internals (1.6)"); }}
        else if (/dllmain|virtualprotect|vtable|worldtoscreen|calceulerangles|getprocaddress/.test(clean)) {{ a1 = 1.35; ev.a1.push("Native x64 C++ Engine ABI / VMT / 3D Math (1.35)"); }}
        else if (/harmonypatch|bepinex|dnspy/.test(clean)) {{ a1 = 1.0; ev.a1.push("Managed .NET / Harmony runtime patching (1.0)"); }}
        else if (/openprocess|readprocessmemory|writeprocessmemory|e_lfanew|inspect_pe/.test(clean)) {{ a1 = 0.80; ev.a1.push("Win32 Process & PE Header APIs (0.80)"); }}
        else {{ a1 = 0.50; ev.a1.push("Standard user-mode binary / script (0.50)"); }}

        if (/\\b(cr3|pml4|mmcopyvirtualmemory|eprocess)\\b/.test(clean)) {{ a2 = 2.0; ev.a2.push("x64 CR3 Page Table / Kernel memory walk (2.0)"); }}
        else if (/vtable|vmt|virtualprotect|getprocaddress|fnspawn/.test(clean)) {{ a2 = 1.5; ev.a2.push("In-process function pointer / VMT resolution (1.5)"); }}
        else if (/viewmatrix|worldtoscreen|clipw|ndcx/.test(clean)) {{ a2 = 1.45; ev.a2.push("4x4 View-Projection matrix & clip-space vectors (1.45)"); }}
        else if (/resolvepointerchain|offsets|e_lfanew/.test(clean)) {{ a2 = 0.90; ev.a2.push("Multi-level dynamic pointer chain / PE header walk (0.90)"); }}
        else {{ a2 = 0.40; ev.a2.push("Direct buffer / struct parsing (0.40)"); }}

        if (/z3|solver\\s*\\(\\)|bitvec|angr|claripy|disassemble_crackme06_vm/.test(clean)) {{ a3 = 2.0; ev.a3.push("Automated SMT Theorem Proving (Z3) & Custom VM Disassembler (2.0)"); }}
        else if (/trampoline|minhook|mh_createhook|internalworkerthread/.test(clean)) {{ a3 = 1.85; ev.a3.push("Internal DLL worker thread & native function hook (1.85)"); }}
        else if (/worldtoscreen|calceulerangles|atan2/.test(clean)) {{ a3 = 1.75; ev.a3.push("3D Linear Algebra, Perspective Divide & Aimbot Trig (1.75)"); }}
        else if (/aob|shannon_entropy|math\\.log2/.test(clean)) {{ a3 = 1.40; ev.a3.push("Wildcard AOB scanner & Shannon entropy analyzer (1.40)"); }}
        else if (/readprocessmemory|writeprocessmemory/.test(clean)) {{ a3 = 0.85; ev.a3.push("External Win32 RPM/WPM trainer loop (0.85)"); }}
        else {{ a3 = 0.50; ev.a3.push("Standard control flow logic (0.50)"); }}

        if (/disassemble_crackme06_vm|z3|bitvec|claripy/.test(clean)) {{ a4 = 2.5; ev.a4.push("Custom Stack VM Bytecode & Z3 Symbolic Constraint Solving (2.5)"); }}
        else if (/isdebuggerpresent|ntqueryinformationprocess|rdtsc|shannon_entropy/.test(clean)) {{ a4 = 1.1; ev.a4.push("Anti-Debugging / Packer Entropy / Hash detection (1.1)"); }}
        else if (/rol8|ror8/.test(clean)) {{ a4 = 0.5; ev.a4.push("Bitwise XOR / ROL / ROR cipher inversion (0.5)"); }}
        else {{ a4 = 0.0; ev.a4.push("Unobfuscated target (0.0)"); }}

        if (/iocreatedevice|mmcopyvirtualmemory|memflow/.test(clean)) {{ a5 = 1.5; ev.a5.push("Ring-0 Kernel / KVM VMI boundary (1.5)"); }}
        else if (/disassemble_crackme06_vm/.test(clean)) {{ a5 = 1.4; ev.a5.push("Multi-stage CTF & Symbolic Solver Workbench (1.4)"); }}
        else if (/dllmain|dll_process_attach/.test(clean)) {{ a5 = 1.2; ev.a5.push("In-Process Injected Native DLL (`DLL_PROCESS_ATTACH`) (1.2)"); }}
        else if (/openprocess/.test(clean)) {{ a5 = 0.3; ev.a5.push("Cross-process Win32 Handle (`OpenProcess`) (0.3)"); }}
        else {{ a5 = 0.0; ev.a5.push("Standard Ring-3 utility (0.0)"); }}

        metricsText = `Detected Source/Script Metrics: Lines = ${{text.split("\\n").length}} | File = ${{filename}}`;
      }}

      const total = +(Math.min(10.0, Math.max(0.5, a1 + a2 + a3 + a4 + a5))).toFixed(1);
      const tObj = scoreToTierObj(total);
      return {{ filename, total, tier: tObj.code, tierTitle: tObj.title, a1, a2, a3, a4, a5, ev, metricsText }};
    }}

    let activeEngineChip = "";

    function showToast(msg) {{
      const region = document.getElementById("toastRegion");
      if (!region) return;
      const el = document.createElement("div");
      el.className = "toast-msg";
      el.textContent = msg;
      region.appendChild(el);
      setTimeout(() => {{ el.remove(); }}, 3200);
    }}

    function loadSampleArtifact(name) {{
      document.getElementById("gradedFileName").textContent = name;
      document.getElementById("artifactCodeBox").value = SAMPLE_ARTIFACTS[name] || "";
      runAutoGrader();
      showToast(`Loaded verified artifact: ${{name}}`);
    }}

    function handleArtifactUpload(input) {{
      const file = input.files && input.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        document.getElementById("gradedFileName").textContent = file.name;
        document.getElementById("artifactCodeBox").value = e.target.result;
        runAutoGrader();
        showToast(`Analyzed uploaded file: ${{file.name}}`);
      }};
      reader.readAsText(file);
    }}

    // Drag and Drop on #artifactDropzone
    (function initDropzone() {{
      const dz = document.getElementById("artifactDropzone");
      if (!dz) return;
      dz.addEventListener("dragover", e => {{ e.preventDefault(); dz.classList.add("dragover"); }});
      dz.addEventListener("dragleave", () => dz.classList.remove("dragover"));
      dz.addEventListener("drop", e => {{
        e.preventDefault();
        dz.classList.remove("dragover");
        const file = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = function(ev) {{
          document.getElementById("gradedFileName").textContent = file.name;
          document.getElementById("artifactCodeBox").value = ev.target.result;
          runAutoGrader();
          showToast(`Dropped & analyzed: ${{file.name}}`);
        }};
        reader.readAsText(file);
      }});
    }})();

    function runAutoGrader() {{
      const fname = document.getElementById("gradedFileName").textContent || "artifact.CT";
      const code = document.getElementById("artifactCodeBox").value || "";
      const res = gradeArtifactText(code, fname);
      lastGradedResult = res;

      document.getElementById("gradeTierHeadline").textContent = `Tier ${{res.tier}} (${{res.tierTitle}})`;
      document.getElementById("gradeScoreHeadline").textContent = `${{res.total.toFixed(1)}} / 10.0`;
      document.getElementById("gradeMetricsBox").textContent = res.metricsText;

      const rows = [
        {{ name: "Axis 1: Arch & Runtime", val: res.a1, max: 2.0, desc: res.ev.a1.join(", ") }},
        {{ name: "Axis 2: Memory Indirection", val: res.a2, max: 2.0, desc: res.ev.a2.join(", ") }},
        {{ name: "Axis 3: Code & Hook Logic", val: res.a3, max: 2.0, desc: res.ev.a3.join(", ") }},
        {{ name: "Axis 4: Protection & Obfus.", val: res.a4, max: 2.5, desc: res.ev.a4.join(", ") }},
        {{ name: "Axis 5: Privilege Boundary", val: res.a5, max: 1.5, desc: res.ev.a5.join(", ") }}
      ];
      document.getElementById("gradeAxesBreakdown").innerHTML = rows.map(r => `
        <div class="axis-bar-row">
          <strong style="color:var(--heading);">${{r.name}}</strong>
          <span style="color:var(--gold); font-weight:700; font-family:var(--font-mono);">+${{r.val.toFixed(2)}} / ${{r.max.toFixed(1)}}</span>
          <span style="color:var(--muted);">${{r.desc}}</span>
        </div>
      `).join("");
    }}

    function addGradedArtifactAsQuest() {{
      if (!lastGradedResult) return;
      const newQ = {{
        id: "graded_" + Date.now(),
        tier: lastGradedResult.tier,
        cat: "TOOL",
        kw: lastGradedResult.filename,
        text: `[Auto-Graded ${{lastGradedResult.total.toFixed(1)}}/10] ${{lastGradedResult.filename}} — Verified ${{lastGradedResult.tierTitle}} Artifact`
      }};
      state.customQuests.push(newQ);
      state.checked[newQ.id] = true;
      saveState();
      showToast(`Claimed ${{lastGradedResult.filename}} (Tier ${{lastGradedResult.tier}} | ${{lastGradedResult.total.toFixed(1)}}/10)!`);
    }}

    function setEngineChip(engineKeyword, btn) {{
      activeEngineChip = engineKeyword.toLowerCase();
      document.querySelectorAll(".chip-btn").forEach(b => b.classList.remove("active"));
      if (btn) btn.classList.add("active");
      renderTop200();
    }}

    function renderTop200() {{
      const q = (document.getElementById("top200Search").value || "").toLowerCase().trim();
      const tf = document.getElementById("top200TierFilter").value;
      const tbody = document.getElementById("top200Body");
      if (!tbody) return;

      const groupMap = {{
        NOVICE: ["F+", "E--", "E-", "E", "E+"],
        FRONTIER: ["D-", "D", "D+"],
        MANAGED: ["C-", "C", "C+"],
        AAA: ["B-", "B", "B+"],
        MODERN: ["A-", "A", "A+"],
        ELITE: ["S-", "S", "S+", "SS-", "SS", "SS+", "SSS-", "SSS", "SSS+", "SSS++"]
      }};

      const filtered = TOP200_GAMES.filter(g => {{
        if (tf !== "ALL" && groupMap[tf] && !groupMap[tf].includes(g.tier)) return false;
        if (activeEngineChip && !g.engine.toLowerCase().includes(activeEngineChip) && !g.what_to_find.toLowerCase().includes(activeEngineChip)) return false;
        if (q && !(g.title.toLowerCase().includes(q) || g.engine.toLowerCase().includes(q) || g.what_to_find.toLowerCase().includes(q) || g.tier.toLowerCase() === q)) return false;
        return true;
      }});

      tbody.innerHTML = filtered.map(g => {{
        const qid = "top200_" + g.rank;
        const done = !!state.checked[qid];
        return `
          <tr style="${{done ? 'background:var(--green-soft);' : ''}} cursor:pointer;" onclick="toggleQuest('${{qid}}')">
            <td><input type="checkbox" aria-label="Mark ${{g.title}} as completed" ${{done ? 'checked' : ''}} onclick="event.stopPropagation(); toggleQuest('${{qid}}')" /></td>
            <td><strong style="font-family:var(--font-mono);">#${{g.rank}}</strong></td>
            <th scope="row"><strong style="color:var(--heading);">${{g.title}}</strong></th>
            <td style="color:var(--muted);">${{g.engine}}</td>
            <td><span class="tier-badge">${{g.tier}}</span></td>
            <td style="color:var(--gold); font-weight:700; font-family:var(--font-mono);">${{g.diff}}</td>
            <td>${{g.what_to_find}}</td>
          </tr>
        `;
      }}).join("");
    }}

    function calculateProgression() {{
      const quests = getAllQuests();
      const counts = {{}};
      TIER_META.forEach(t => counts[t.code] = {{ checked: 0, total: 0, tp: 0, cleared: false }});

      let totalChecked = 0;
      let totalExp = 0;
      let dojoDone = 0;
      let top200Done = 0;

      quests.forEach(q => {{
        if (!counts[q.tier]) return;
        counts[q.tier].total++;
        if (state.checked[q.id]) {{
          counts[q.tier].checked++;
          totalChecked++;
          if (q.cat === "DOJO") dojoDone++;
          if (String(q.id).startsWith("top200_")) top200Done++;
          const meta = TIER_META.find(m => m.code === q.tier);
          if (meta) totalExp += meta.exp;
        }}
      }});

      const clearedIndices = [];
      TIER_META.forEach((t, i) => {{
        let samePts = counts[t.code].checked * 1;
        let higherPts = 0;
        for (let j = i + 1; j < TIER_META.length; j++) {{
          higherPts += counts[TIER_META[j].code].checked * 3;
        }}
        counts[t.code].tp = samePts + higherPts;
        if (counts[t.code].tp >= 3) {{
          counts[t.code].cleared = true;
          clearedIndices.push(i);
        }}
      }});

      let curIdx = 0;
      if (clearedIndices.length > 0) {{
        const highestCleared = Math.max(...clearedIndices);
        curIdx = Math.min(TIER_META.length - 1, highestCleared + 1);
      }}

      return {{
        counts,
        totalChecked,
        dojoDone,
        top200Done,
        totalQuests: DEFAULT_QUESTS.length + (state.customQuests || []).length,
        totalExp,
        clearedCount: clearedIndices.length,
        curIdx,
        curTier: TIER_META[curIdx]
      }};
    }}

    function renderCharacterSheet(prog) {{
      document.getElementById("uiRankOrb").textContent = prog.curTier.code;
      document.getElementById("uiClassTitle").textContent =
        `Rank: Tier ${{prog.curTier.code}} — ${{prog.curTier.title}}`;
      document.getElementById("uiTiersCleared").textContent =
        `${{prog.clearedCount}} / ${{TIER_META.length}}`;
      document.getElementById("uiTotalExp").textContent =
        `${{prog.totalExp.toLocaleString()}} EXP`;
      document.getElementById("uiQuestsDone").textContent =
        `${{prog.totalChecked}}`;

      const pct = Math.round((prog.clearedCount / TIER_META.length) * 100);
      document.getElementById("uiCampaignBar").style.width = `${{pct}}%`;
      const track = document.getElementById("uiProgressTrack");
      if (track) track.setAttribute("aria-valuenow", String(pct));

      const curTp = Math.min(3, prog.counts[prog.curTier.code].tp);
      document.getElementById("uiTrialLabel").textContent =
        `Tier ${{prog.curTier.code}} Rank-Up Trial (3 Same-Tier OR 1 Higher-Tier Breakthrough):`;
      document.getElementById("uiTpStatus").textContent = `${{curTp}} / 3 TP`;

      const nextTierObj = TIER_META[Math.min(TIER_META.length - 1, prog.curIdx + 1)];
      const elDojo = document.getElementById("teleDojoDone");
      const elTop = document.getElementById("teleTop200Done");
      const elNext = document.getElementById("teleNextRank");
      if (elDojo) elDojo.textContent = `${{prog.dojoDone}} / 18`;
      if (elTop) elTop.textContent = `${{prog.top200Done}} / 200`;
      if (elNext) elNext.textContent = nextTierObj ? nextTierObj.code : "MAX";

      // Update 5-Axis SVG Capability Radar
      const poly = document.getElementById("radarDataPoly");
      if (poly) {{
        const ratio = Math.max(0.18, Math.min(1.0, (prog.curIdx + 2) / TIER_META.length));
        const rArch = Math.min(1.0, ratio * 1.15);
        const rPtr  = Math.min(1.0, ratio * 1.10);
        const rHook = Math.min(1.0, ratio * 1.05);
        const rObf  = Math.min(1.0, Math.max(0.15, ratio * 0.85));
        const rRing = Math.min(1.0, Math.max(0.15, ratio * 0.75));
        const p1 = `110,${{(95 - 75 * rArch).toFixed(1)}}`;
        const p2 = `${{(110 + 80 * rPtr).toFixed(1)}},${{(95 - 20 * rPtr).toFixed(1)}}`;
        const p3 = `${{(110 + 50 * rHook).toFixed(1)}},${{(95 + 67 * rHook).toFixed(1)}}`;
        const p4 = `${{(110 - 50 * rObf).toFixed(1)}},${{(95 + 67 * rObf).toFixed(1)}}`;
        const p5 = `${{(110 - 80 * rRing).toFixed(1)}},${{(95 - 20 * rRing).toFixed(1)}}`;
        poly.setAttribute("points", `${{p1}} ${{p2}} ${{p3}} ${{p4}} ${{p5}}`);
      }}

      const skills = [
        {{ name: "Stage 1: Memory & Bitmasks", ok: prog.totalChecked >= 1 }},
        {{ name: "Stage 2: Pointers & AutoAsm", ok: prog.curIdx >= 5 }},
        {{ name: "Stage 3: Shared Code Filters", ok: prog.curIdx >= 8 }},
        {{ name: "Stage 4: Unity Mono & .NET", ok: prog.curIdx >= 11 }},
        {{ name: "Stage 5: C++ VMT & DLL Hooks", ok: prog.curIdx >= 14 }},
        {{ name: "Stage 6: UE4/5 SDK & 3D W2S", ok: prog.curIdx >= 16 }},
        {{ name: "Stage 7: IL2CPP & Custom VMs", ok: prog.curIdx >= 18 }},
        {{ name: "Stage 8: Z3, O-LLVM & VMI", ok: prog.curIdx >= 25 }}
      ];
      document.getElementById("uiSkillGrid").innerHTML = skills.map(s =>
        `<div class="skill-chip ${{s.ok ? 'unlocked' : ''}}">${{s.ok ? '✅' : '🔒'}} ${{s.name}}</div>`
      ).join("");
    }}

    function renderTiers() {{
      const prog = calculateProgression();
      renderCharacterSheet(prog);

      const query = document.getElementById("searchBox").value.toLowerCase().trim();
      const catF = document.getElementById("catFilter").value;
      const statF = document.getElementById("statusFilter").value;
      const quests = DEFAULT_QUESTS.concat(state.customQuests || []);

      const container = document.getElementById("tiersContainer");
      container.innerHTML = "";

      let renderedIdx = 0;
      TIER_META.forEach(t => {{
        const c = prog.counts[t.code];
        if (statF === "LOCKED" && c.cleared) return;
        if (statF === "CLEARED" && !c.cleared) return;

        const tierQuests = quests.filter(q => {{
          if (q.tier !== t.code) return false;
          if (catF !== "ALL" && q.cat !== catF) return false;
          if (query && !q.text.toLowerCase().includes(query) && !t.title.toLowerCase().includes(query)) return false;
          return true;
        }});

        if (tierQuests.length === 0) return;

        const tpDisplay = Math.min(3, c.tp);
        const card = document.createElement("div");
        // Apply deferred-tier (content-visibility: auto + contain-intrinsic-size) ONLY to off-screen cards below the initial fold
        const deferClass = renderedIdx >= 3 ? "deferred-tier" : "";
        renderedIdx++;
        card.className = `tier-card ${{c.cleared ? 'cleared' : ''}} ${{deferClass}}`.trim();
        card.innerHTML = `
          <div class="tier-top">
            <div>
              <span class="tier-badge">Tier ${{t.code}}</span>
              <strong style="margin-left:8px; color:var(--heading);">${{t.title}}</strong>
              <span style="color:var(--muted); font-size:0.8rem; margin-left:8px;">(${{t.act}} • Diff ${{t.diff.toFixed(1)}}/10 • +${{t.exp}} EXP)</span>
            </div>
            <span class="tp-pill" style="color:${{c.cleared ? 'var(--green-bright)' : 'var(--gold)'}}">
              ${{c.cleared ? '✅ TIER CLEARED' : `⚡ ${{tpDisplay}}/3 TP`}}
            </span>
          </div>
          <ul class="quest-list">
            ${{tierQuests.map(q => {{
              const isDone = !!state.checked[q.id];
              const tagClass = q.cat === "DOJO" ? "tag-dojo" : q.cat === "GAME" ? "tag-game" : q.cat === "SOFT" ? "tag-soft" : "tag-tool";
              const tagLabel = q.cat === "DOJO" ? "🧪 Dojo Lab" : q.cat === "GAME" ? "🎮 Game" : q.cat === "SOFT" ? "💻 Software" : "🛠️ Toolcraft";
              return `
                <li class="quest-item ${{isDone ? 'done' : ''}}" onclick="toggleQuest('${{q.id}}')">
                  <input type="checkbox" aria-label="${{q.text}}" ${{isDone ? 'checked' : ''}} onclick="event.stopPropagation(); toggleQuest('${{q.id}}')" />
                  <span class="q-tag ${{tagClass}}">${{tagLabel}}</span>
                  <span style="flex:1; font-size:0.86rem;">${{q.text}}</span>
                </li>
              `;
            }}).join("")}}
          </ul>
        `;
        container.appendChild(card);
      }});

      renderTop200();
      renderScoreboard(prog);
    }}

    function toggleQuest(id) {{
      state.checked[id] = !state.checked[id];
      if (!state.checked[id]) delete state.checked[id];
      saveState();
    }}

    function renderScoreboard(prog) {{
      const tbody = document.getElementById("scoreboardBody");
      const userName = state.playerName || "New Challenger";
      tbody.innerHTML = `
        <tr>
          <td>🥇 <strong>#1</strong></td>
          <th scope="row"><strong style="color:var(--heading);">deavers</strong> <span style="color:var(--accent-bright); font-size:0.75rem;">[Author / Verified]</span></th>
          <td>Adventurer (Managed JIT)</td>
          <td><span class="tier-badge">Tier C</span></td>
          <td style="color:var(--gold); font-weight:700; font-family:var(--font-mono);">6,850 EXP</td>
          <td><code>PvZ.CT</code> (2.1 E+), <code>UnrealTournament_UT99.CT</code> (2.9 D), <code>isaac-ng.CT</code> (3.8 C-), <code>StreetsOfRogue_v98.CT</code> (4.1 C)</td>
        </tr>
        <tr style="background:var(--accent-soft);">
          <td>⚡ <strong>YOU</strong></td>
          <th scope="row"><strong style="color:var(--heading);">${{userName}}</strong> <span style="color:var(--green-bright); font-size:0.75rem;">[Browser Session]</span></th>
          <td>${{prog.curTier.title}}</td>
          <td><span class="tier-badge">Tier ${{prog.curTier.code}}</span></td>
          <td style="color:var(--gold); font-weight:700; font-family:var(--font-mono);">${{prog.totalExp.toLocaleString()}} EXP</td>
          <td>${{prog.totalChecked}} Quests Checked</td>
        </tr>
      `;
    }}

    function exportProgressJson() {{
      const prog = calculateProgression();
      const allQ = getAllQuests();
      const completedKeywords = allQ.filter(q => state.checked[q.id] && q.kw).map(q => q.kw);
      const payload = {{
        player_name: state.playerName,
        rank_label: `Tier ${{prog.curTier.code}} (${{prog.curTier.title}})`,
        current_tier: prog.curTier.code,
        total_exp: prog.totalExp,
        quests_completed: prog.totalChecked,
        completed_keywords: completedKeywords,
        browser_state: state
      }};
      const blob = new Blob([JSON.stringify(payload, null, 2)], {{ type: "application/json" }});
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "player_progress.json";
      a.click();
      showToast("Exported player_progress.json");
    }}

    function importProgressJson(input) {{
      const file = input.files && input.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {{
        try {{
          const data = JSON.parse(e.target.result);
          if (data.browser_state) {{
            state = Object.assign(state, data.browser_state);
          }} else if (data.player_name) {{
            state.playerName = data.player_name;
          }}
          document.getElementById("uiPlayerName").value = state.playerName;
          saveState();
          showToast("Profile imported successfully!");
        }} catch (err) {{
          showToast("Error reading JSON file");
        }}
      }};
      reader.readAsText(file);
    }}

    function applyDeaversPreset() {{
      state.playerName = "deavers";
      state.checked = {{}};
      DEFAULT_QUESTS.forEach(q => {{ if (q.deavers) state.checked[q.id] = true; }});
      document.getElementById("uiPlayerName").value = "deavers";
      saveState();
      showToast("Loaded verified deavers preset (Tier C | 6,850 EXP)");
    }}

    function resetProfile() {{
      state.playerName = "New Challenger";
      state.checked = {{}};
      state.customQuests = [];
      document.getElementById("uiPlayerName").value = "New Challenger";
      saveState();
      showToast("Reset profile to Tier F- (0 EXP)");
    }}

    function recalcAndRender() {{
      renderTiers();
    }}

    // Same-Document View Transition + Accessible ARIA Tab Selection & Focus Routing
    function switchTab(name, btn, focusTargetHeading = false) {{
      const applyDomSwitch = () => {{
        document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
        document.querySelectorAll(".tab-btn").forEach(b => {{
          b.classList.remove("active");
          b.setAttribute("aria-selected", "false");
        }});
        const targetPanel = document.getElementById("tab-" + name);
        if (targetPanel) targetPanel.classList.add("active");
        const activeBtn = btn || document.getElementById("tabbtn-" + name);
        if (activeBtn) {{
          activeBtn.classList.add("active");
          activeBtn.setAttribute("aria-selected", "true");
        }}
      }};

      const routeFocus = () => {{
        if (!focusTargetHeading) return;
        const heading = document.getElementById("heading-" + name);
        if (heading) heading.focus({{ preventScroll: true }});
      }};

      if (!document.startViewTransition) {{
        applyDomSwitch();
        routeFocus();
        return;
      }}
      const transition = document.startViewTransition(() => {{
        applyDomSwitch();
      }});
      transition.finished.then(routeFocus);
    }}

    // Command Palette (Ctrl+K / Cmd+K)
    function openCmdPalette() {{
      const dlg = document.getElementById("cmdDialog");
      if (!dlg) return;
      if (!dlg.open) dlg.showModal();
      const inp = document.getElementById("cmdSearchInput");
      inp.value = "";
      renderCmdResults();
      inp.focus();
    }}

    function closeCmdPalette() {{
      const dlg = document.getElementById("cmdDialog");
      if (dlg && dlg.open) dlg.close();
    }}

    function renderCmdResults() {{
      const q = (document.getElementById("cmdSearchInput").value || "").toLowerCase().trim();
      const list = document.getElementById("cmdResultsList");
      if (!list) return;

      const actions = [
        {{ label: "⚔️ Go to 28-Tier Campaign Quests", sub: "Navigation", act: () => switchTab("quests", null, true) }},
        {{ label: "🔥 Go to Top 200 Popular Games (#001–#200)", sub: "Navigation", act: () => switchTab("top200", null, true) }},
        {{ label: "🔬 Go to Automated .CT / Script Grader", sub: "Navigation", act: () => switchTab("autograde", null, true) }},
        {{ label: "📖 Go to x86/x64 & Engine Cheat Sheet", sub: "Navigation", act: () => switchTab("cheatsheet", null, true) }},
        {{ label: "⚖️ Go to 5-Axis Target Calculator", sub: "Navigation", act: () => switchTab("adder", null, true) }},
        {{ label: "🧙‍♂️ Load Verified Author Preset (deavers — Tier C)", sub: "Preset", act: () => applyDeaversPreset() }},
        {{ label: "🌱 Reset Profile to Clean New Game (Tier F-)", sub: "Preset", act: () => resetProfile() }}
      ];

      TOP200_GAMES.slice(0, 60).forEach(g => {{
        actions.push({{
          label: `🎮 #${{g.rank}} ${{g.title}} (${{g.engine}})`,
          sub: `Tier ${{g.tier}} • ${{g.diff}}`,
          act: () => {{
            switchTab("top200", null, true);
            const sb = document.getElementById("top200Search");
            if (sb) {{ sb.value = g.title; renderTop200(); }}
          }}
        }});
      }});

      const matches = actions.filter(a => !q || a.label.toLowerCase().includes(q) || a.sub.toLowerCase().includes(q)).slice(0, 12);
      list.innerHTML = matches.map((m, idx) => `
        <li class="cmd-item" tabindex="0" data-cmd-idx="${{idx}}">
          <span>${{m.label}}</span>
          <span class="tier-badge">${{m.sub}}</span>
        </li>
      `).join("");

      list.querySelectorAll(".cmd-item").forEach(el => {{
        const idx = Number(el.getAttribute("data-cmd-idx"));
        el.onclick = () => {{ closeCmdPalette(); matches[idx].act(); }};
        el.onkeydown = (ev) => {{
          if (ev.key === "Enter" || ev.key === " ") {{
            ev.preventDefault();
            closeCmdPalette();
            matches[idx].act();
          }}
        }};
      }});
    }}

    document.addEventListener("keydown", e => {{
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {{
        e.preventDefault();
        openCmdPalette();
      }}
    }});

    loadState();
    updateRubricPreview();
    loadSampleArtifact("PvZ.CT");
    recalcAndRender();
  </script>
</body>
</html>
"""

(ROOT / "docs" / "index.html").write_text(html, encoding="utf-8")
print(f"[+] Generated 100%-English docs/index.html ({len(html):,} bytes)!")
