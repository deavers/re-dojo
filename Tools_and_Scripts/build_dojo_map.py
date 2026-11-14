#!/usr/bin/env python3
"""
RE:DOJO map - build the self-contained offline page docs/dojo-map.html.

Inlines Tools_and_Scripts/dojo_map/{template.html,style.css,app.js} + data/games.json into ONE file:
  * no external requests (CSP default-src 'none'; scripts/styles allowed only by sha256 hash)
  * data is embedded as <script type="application/json"> with '<' escaped, rendered via textContent
  * progress lives in the browser's localStorage under 're_dojo_map_v1' (separate from index.html)

Usage:
  python Tools_and_Scripts/build_dojo_map.py                 # write docs/dojo-map.html
  python Tools_and_Scripts/build_dojo_map.py --check         # exit 1 if docs/dojo-map.html is stale
  python Tools_and_Scripts/build_dojo_map.py --games <games.json> --out <page.html>   # e.g. test fixtures
Stdlib only, ASCII console output.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(__file__).resolve().parent / "dojo_map"
DEFAULT_GAMES = ROOT / "data" / "games.json"
DEFAULT_OUT = ROOT / "docs" / "dojo-map.html"


def rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return p.name


def sha256_b64(text: str) -> str:
    return base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode("ascii")


def build(games_path: Path) -> str:
    template = (SRC / "template.html").read_text(encoding="utf-8")
    style = (SRC / "style.css").read_text(encoding="utf-8")
    script = (SRC / "app.js").read_text(encoding="utf-8")
    data = json.loads(games_path.read_text(encoding="utf-8"))

    # Compact JSON; escape '<' so the data block can never close the <script> element.
    data_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    data_json = data_json.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

    csp = "; ".join([
        "default-src 'none'",
        f"script-src 'sha256-{sha256_b64(script)}'",
        f"style-src 'sha256-{sha256_b64(style)}'",
        "img-src data:",
        "base-uri 'none'",
        "form-action 'none'",
    ])
    for marker in ("__CSP__", "__STYLE__", "__SCRIPT__", "__DATA__"):
        if template.count(marker) != 1:
            raise SystemExit(f"[BUILD ERROR] template must contain {marker} exactly once")
    # Replace data last so marker-like text inside the data can never be substituted.
    page = (template.replace("__CSP__", csp)
                    .replace("__STYLE__", style)
                    .replace("__SCRIPT__", script)
                    .replace("__DATA__", data_json))
    return page


def main() -> int:
    ap = argparse.ArgumentParser(description="Build docs/dojo-map.html (offline RE:DOJO map)")
    ap.add_argument("--games", type=Path, default=DEFAULT_GAMES)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--check", action="store_true", help="fail if the output page is stale")
    args = ap.parse_args()

    if not args.games.is_file():
        print(f"[BUILD ERROR] {rel(args.games)} not found. Run build_games_json.py first.")
        return 1
    page = build(args.games)

    if args.check:
        current = args.out.read_text(encoding="utf-8") if args.out.is_file() else ""
        if current != page:
            print(f"[STALE] {rel(args.out)} is out of date. Run: python Tools_and_Scripts/build_dojo_map.py")
            return 1
        print(f"[OK] {rel(args.out)} is up to date.")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    print(f"[OK] wrote {rel(args.out)} ({len(page.encode('utf-8')) // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
