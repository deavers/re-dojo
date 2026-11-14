"""[Lab 39] Sources-only check (runs everywhere, no .NET SDK needed - this is what CI runs, ci: sources_only).

Checks: the project targets net8.0, has no NuGet PackageReference (offline build), Program.cs defines the
passphrase forge and the flag, solve.py derives a non-empty passphrase from the sources and has WRONG cases,
expected.json is a sha256. Exit 0 ok, 1 problem. ASCII output.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
LAB = Path(__file__).resolve().parents[1]


def main() -> int:
    problems = []
    proj = (LAB / "game" / "Lab39.csproj").read_text(encoding="utf-8")
    if "<TargetFramework>net8.0</TargetFramework>" not in proj:
        problems.append("csproj must target net8.0")
    if "PackageReference" in proj:
        problems.append("csproj must not use NuGet packages (offline build)")
    prog = (LAB / "game" / "Program.cs").read_text(encoding="utf-8")
    for needle in ("ForgePassphrase", "MakeFlag", "return 3;", "return 2;", "return 1;", "return 0;"):
        if needle not in prog:
            problems.append(f"Program.cs is missing {needle!r}")
    spec = importlib.util.spec_from_file_location("solve39", LAB / "solve" / "solve.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not mod.answer().strip() or len(mod.WRONG) < 5:
        problems.append("solve.py must derive a passphrase and list at least 5 wrong answers")
    exp = json.loads((LAB / "check" / "expected.json").read_text(encoding="utf-8"))
    if not re.fullmatch(r"[0-9a-f]{64}", exp.get("flag_sha256", "")):
        problems.append("expected.json flag_sha256 must be a sha256 hex digest")
    for p in problems:
        print("[FAIL] " + p)
    print("[OK] lab39 sources check passed" if not problems else f"[FAIL] {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
