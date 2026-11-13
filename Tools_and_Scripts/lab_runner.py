#!/usr/bin/env python3
"""
RE:DOJO - lab autocheck runner (stdlib only). Called by CTest via cmake/DojoLab.cmake.

  python Tools_and_Scripts/lab_runner.py ok    --lab-dir <lab folder> --exe <binary>
  python Tools_and_Scripts/lab_runner.py wrong --lab-dir <lab folder> --exe <binary>
  python Tools_and_Scripts/lab_runner.py selftest            # runner checks itself (no compiler needed)

Lab folder contract (docs/lab_plan.md, section 3):
  solve/solve.py        answer() -> str   stdin payload of the reference solution
                        WRONG: list[str]  stdin payloads that must NOT pass
  check/expected.json   {"flag_sha256": "<hex>", "runs": 1}   runs > 1 = fresh process each time
Exit-code contract of every new lab binary: 0 solved (prints FLAG{...}), 1 wrong, 2 usage, 3 quit.
Output is ASCII-only; the flag itself is never printed by this runner.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

FLAG_RX = re.compile(r"FLAG\{[^}\r\n]*\}")
TIMEOUT_S = 20


def say(msg: str) -> None:
    print(msg.encode("ascii", "backslashreplace").decode("ascii"))


def load_solve(lab_dir: Path):
    path = lab_dir / "solve" / "solve.py"
    spec = importlib.util.spec_from_file_location(f"solve_{lab_dir.name}", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"[RUNNER] cannot load {path.name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not callable(getattr(mod, "answer", None)) or not isinstance(getattr(mod, "WRONG", None), list):
        raise SystemExit("[RUNNER] solve.py must define answer() and WRONG = [...]")
    return mod


def run(exe: str, payload: str) -> tuple[int, str]:
    cmd = [sys.executable, exe] if exe.endswith(".py") else [exe]
    try:
        r = subprocess.run(cmd, input=payload, capture_output=True, text=True, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        return 124, ""
    return r.returncode, r.stdout


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def mode_ok(lab_dir: Path, exe: str) -> int:
    solve = load_solve(lab_dir)
    exp = json.loads((lab_dir / "check" / "expected.json").read_text(encoding="utf-8"))
    runs = int(exp.get("runs", 1))
    for i in range(runs):
        rc, out = run(exe, solve.answer())
        flags = FLAG_RX.findall(out)
        if rc != 0 or len(flags) != 1 or sha(flags[0]) != exp["flag_sha256"]:
            say(f"[FAIL] run {i + 1}/{runs}: exit={rc}, flags found={len(flags)}, sha256 match="
                f"{bool(flags) and sha(flags[0]) == exp['flag_sha256']}")
            return 1
    say(f"[OK] reference solution accepted in {runs} fresh run(s)")
    return 0


def mode_wrong(lab_dir: Path, exe: str) -> int:
    solve = load_solve(lab_dir)
    if not solve.WRONG:
        say("[FAIL] solve.py WRONG list is empty - a lab must prove that wrong input fails")
        return 1
    for i, payload in enumerate(solve.WRONG, 1):
        rc, out = run(exe, payload)
        if rc == 0 or FLAG_RX.search(out):
            say(f"[FAIL] wrong input #{i} was accepted (exit={rc})")
            return 1
    say(f"[OK] all {len(solve.WRONG)} wrong inputs rejected")
    return 0


FAKE_EXE = '''import sys
data = sys.stdin.read().strip()
if data == "open sesame":
    print("FLAG{RUNNER_SELFTEST}")
    sys.exit(0)
print("FAILED")
sys.exit(1)
'''
FAKE_SOLVE = '''def answer():
    return "open sesame\\n"
WRONG = ["", "open\\n", "OPEN SESAME\\n"]
'''


def mode_selftest() -> int:
    with tempfile.TemporaryDirectory(prefix="dojo-runner-") as tmp:
        lab = Path(tmp) / "LabXX_Fake"
        (lab / "solve").mkdir(parents=True)
        (lab / "check").mkdir()
        (lab / "solve" / "solve.py").write_text(FAKE_SOLVE, encoding="utf-8")
        (lab / "check" / "expected.json").write_text(
            json.dumps({"flag_sha256": sha("FLAG{RUNNER_SELFTEST}"), "runs": 2}), encoding="utf-8")
        exe = Path(tmp) / "fake_lab.py"
        exe.write_text(FAKE_EXE, encoding="utf-8")
        ok = mode_ok(lab, str(exe)) == 0 and mode_wrong(lab, str(exe)) == 0
        # The runner itself must catch a broken lab: wrong expected hash, and a lab that accepts anything.
        (lab / "check" / "expected.json").write_text(json.dumps({"flag_sha256": "0" * 64}), encoding="utf-8")
        ok &= mode_ok(lab, str(exe)) == 1
        exe.write_text('print("FLAG{RUNNER_SELFTEST}")\n', encoding="utf-8")
        ok &= mode_wrong(lab, str(exe)) == 1
    say("[OK] runner selftest passed" if ok else "[FAIL] runner selftest failed")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="RE:DOJO lab autocheck runner")
    ap.add_argument("mode", choices=["ok", "wrong", "selftest"])
    ap.add_argument("--lab-dir", type=Path)
    ap.add_argument("--exe")
    a = ap.parse_args()
    if a.mode == "selftest":
        return mode_selftest()
    if not (a.lab_dir and a.exe):
        ap.error("--lab-dir and --exe are required")
    return mode_ok(a.lab_dir, a.exe) if a.mode == "ok" else mode_wrong(a.lab_dir, a.exe)


if __name__ == "__main__":
    sys.exit(main())
