#!/usr/bin/env python3
"""
RE:DOJO - lab autocheck runner (stdlib only). Called by CTest via cmake/DojoLab.cmake.

  python Tools_and_Scripts/lab_runner.py ok    --lab-dir <lab folder> --exe <binary>
  python Tools_and_Scripts/lab_runner.py wrong --lab-dir <lab folder> --exe <binary> [--real-exe <lab binary>]
  python Tools_and_Scripts/lab_runner.py selftest            # runner checks itself (no compiler needed)

Lab folder contract (docs/lab_plan.md, section 3):
  solve/solve.py        answer() -> str   stdin payload of the reference solution
                        WRONG: list[str]  stdin payloads that must NOT pass
  check/expected.json   {"flag_sha256": "<hex>", "runs": 1}   runs > 1 = fresh process each time
Interactive labs (the binary prints "CHALLENGE: <value>" and then reads the answer, e.g. a per-run block):
  solve/solve.py        answer_for(challenge) -> str             answer for this run
                        expected_flag(challenge, answer) -> str  independent re-implementation of the flag
                        WRONG entries may be callables challenge -> str
  check/expected.json   {"flag": "computed", "runs": N}
Exit-code contract of every new lab binary: 0 solved (prints FLAG{...}), 1 wrong, 2 usage, 3 quit.
'wrong' accepts only exit 1 or 2 for a wrong payload: a crash, a timeout or any other code is a FAIL
(a lab that crashes on bad input is broken, not "rejecting"). With --real-exe it also starts the real
lab binary with empty stdin (memory labs are otherwise only driven through their selftest binary):
it must end with 1, 2 or 3 and print no FLAG.
Output is ASCII-only; the flag itself is never printed by this runner.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import queue
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

# No bytecode cache: solve.py must always be read fresh (a .pyc keyed on mtime-seconds + size can go stale),
# and running the tests must not drop __pycache__ folders into lab directories.
sys.dont_write_bytecode = True

FLAG_RX = re.compile(r"FLAG\{[^}\r\n]*\}")
CHALLENGE_RX = re.compile(r"CHALLENGE:\s*(\S+)")
TIMEOUT_S = 20


def say(msg: str) -> None:
    print(msg.encode("ascii", "backslashreplace").decode("ascii"))


def load_solve(lab_dir: Path):
    path = lab_dir / "solve" / "solve.py"
    spec = importlib.util.spec_from_file_location(f"solve_{lab_dir.name}", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"[RUNNER] cannot load {path.name}")
    mod = importlib.util.module_from_spec(spec)
    code = compile(path.read_text(encoding="utf-8"), str(path), "exec")
    exec(code, mod.__dict__)
    interactive = callable(getattr(mod, "answer_for", None)) and callable(getattr(mod, "expected_flag", None))
    if not (callable(getattr(mod, "answer", None)) or interactive) or not isinstance(getattr(mod, "WRONG", None), list):
        raise SystemExit("[RUNNER] solve.py must define answer() (or answer_for + expected_flag) and WRONG = [...]")
    return mod


def run(exe: str, payload: str) -> tuple[int, str]:
    cmd = [sys.executable, exe] if exe.endswith(".py") else [exe]
    try:
        r = subprocess.run(cmd, input=payload, capture_output=True, text=True, timeout=TIMEOUT_S,
                           encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return 124, ""
    return r.returncode, r.stdout


def run_interactive(exe: str, respond) -> tuple[int, str, str | None, str]:
    """Start the binary, wait for 'CHALLENGE: <value>', send respond(value), collect the rest."""
    cmd = [sys.executable, exe] if exe.endswith(".py") else [exe]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                         text=True, encoding="utf-8", errors="replace")
    lines: queue.Queue = queue.Queue()

    def reader() -> None:
        for line in p.stdout:
            lines.put(line)
        lines.put(None)

    threading.Thread(target=reader, daemon=True).start()
    deadline = time.monotonic() + TIMEOUT_S
    out, challenge, payload = [], None, ""
    while challenge is None:
        try:
            line = lines.get(timeout=max(0.1, deadline - time.monotonic()))
        except queue.Empty:
            p.kill()
            return 124, "".join(out), None, ""
        if line is None:
            break
        out.append(line)
        m = CHALLENGE_RX.search(line)
        if m:
            challenge = m.group(1)
    if challenge is not None:
        payload = respond(challenge)
        try:
            p.stdin.write(payload)
            p.stdin.close()
        except OSError:
            pass
    while True:
        try:
            line = lines.get(timeout=max(0.1, deadline - time.monotonic()))
        except queue.Empty:
            p.kill()
            return 124, "".join(out), challenge, payload
        if line is None:
            break
        out.append(line)
    return p.wait(timeout=TIMEOUT_S), "".join(out), challenge, payload


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def mode_ok(lab_dir: Path, exe: str) -> int:
    solve = load_solve(lab_dir)
    exp = json.loads((lab_dir / "check" / "expected.json").read_text(encoding="utf-8"))
    runs = int(exp.get("runs", 1))
    interactive = callable(getattr(solve, "answer_for", None))
    for i in range(runs):
        if interactive:
            rc, out, challenge, payload = run_interactive(exe, solve.answer_for)
            flags = FLAG_RX.findall(out)
            want = solve.expected_flag(challenge, payload) if challenge is not None else None
            if rc != 0 or len(flags) != 1 or flags[0] != want:
                say(f"[FAIL] run {i + 1}/{runs}: exit={rc}, challenge seen={challenge is not None}, "
                    f"flags found={len(flags)}, matches independent flag={bool(flags) and flags[0] == want}")
                return 1
            continue
        rc, out = run(exe, solve.answer())
        flags = FLAG_RX.findall(out)
        if rc != 0 or len(flags) != 1 or sha(flags[0]) != exp["flag_sha256"]:
            say(f"[FAIL] run {i + 1}/{runs}: exit={rc}, flags found={len(flags)}, sha256 match="
                f"{bool(flags) and sha(flags[0]) == exp['flag_sha256']}")
            return 1
    say(f"[OK] reference solution accepted in {runs} fresh run(s)")
    return 0


def mode_wrong(lab_dir: Path, exe: str, real_exe: str | None = None) -> int:
    solve = load_solve(lab_dir)
    if not solve.WRONG:
        say("[FAIL] solve.py WRONG list is empty - a lab must prove that wrong input fails")
        return 1
    exp_path = lab_dir / "check" / "expected.json"
    runs = int(json.loads(exp_path.read_text(encoding="utf-8")).get("runs", 1)) if exp_path.exists() else 1
    for i, payload in enumerate(solve.WRONG, 1):
        for r in range(runs):  # a wrong answer must fail in EVERY fresh run, not just usually
            rc, out = run_interactive(exe, payload)[:2] if callable(payload) else run(exe, payload)
            if rc not in (1, 2) or FLAG_RX.search(out):
                say(f"[FAIL] wrong input #{i}, run {r + 1}/{runs}: exit={rc} (expected 1 or 2), "
                    f"flag printed={bool(FLAG_RX.search(out))}")
                return 1
    if real_exe:
        rc, out = run(real_exe, "")
        if rc not in (1, 2, 3) or FLAG_RX.search(out):
            say(f"[FAIL] real lab binary on empty input: exit={rc} (expected 1, 2 or 3), "
                f"flag printed={bool(FLAG_RX.search(out))}")
            return 1
    say(f"[OK] all {len(solve.WRONG)} wrong inputs rejected in {runs} run(s) each"
        + ("; real binary quits cleanly" if real_exe else ""))
    return 0


FAKE_EXE = '''import sys
data = sys.stdin.read().strip()
if data == "open sesame":
    print("FLAG{RUNNER_SELFTEST}")
    sys.exit(0)
if data == "boom":
    sys.exit(-11)
print("FAILED")
sys.exit(1 if data else 2)
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
        ok = mode_ok(lab, str(exe)) == 0 and mode_wrong(lab, str(exe), real_exe=str(exe)) == 0
        say("-- negative checks: the [FAIL] lines below are expected --")
        # A crash on a wrong payload is a failure, not a rejection.
        crash = FAKE_SOLVE.replace('"open\\n"', '"boom\\n"')
        assert crash != FAKE_SOLVE
        (lab / "solve" / "solve.py").write_text(crash, encoding="utf-8")
        ok &= mode_wrong(lab, str(exe)) == 1
        (lab / "solve" / "solve.py").write_text(FAKE_SOLVE, encoding="utf-8")
        # The runner itself must catch a broken lab: wrong expected hash, and a lab that accepts anything.
        (lab / "check" / "expected.json").write_text(json.dumps({"flag_sha256": "0" * 64}), encoding="utf-8")
        ok &= mode_ok(lab, str(exe)) == 1
        exe.write_text('print("FLAG{RUNNER_SELFTEST}")\n', encoding="utf-8")
        ok &= mode_wrong(lab, str(exe)) == 1
        # Interactive lab: challenge read from the binary, flag checked against an independent computation.
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import lab_runner_fakes as fakes
        ilab = Path(tmp) / "LabYY_Interactive"
        (ilab / "solve").mkdir(parents=True)
        (ilab / "check").mkdir()
        (ilab / "solve" / "solve.py").write_text(fakes.INTERACTIVE_SOLVE, encoding="utf-8")
        (ilab / "check" / "expected.json").write_text(json.dumps({"flag": "computed", "runs": 2}), encoding="utf-8")
        iexe = Path(tmp) / "fake_interactive.py"
        iexe.write_text(fakes.INTERACTIVE_EXE, encoding="utf-8")
        say("-- interactive checks (no FAIL expected below) --")
        ok &= mode_ok(ilab, str(iexe)) == 0 and mode_wrong(ilab, str(iexe)) == 0
    say("[OK] runner selftest passed" if ok else "[FAIL] runner selftest failed")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="RE:DOJO lab autocheck runner")
    ap.add_argument("mode", choices=["ok", "wrong", "selftest"])
    ap.add_argument("--lab-dir", type=Path)
    ap.add_argument("--exe")
    ap.add_argument("--real-exe")
    a = ap.parse_args()
    if a.mode == "selftest":
        return mode_selftest()
    if not (a.lab_dir and a.exe):
        ap.error("--lab-dir and --exe are required")
    return mode_ok(a.lab_dir, a.exe) if a.mode == "ok" else mode_wrong(a.lab_dir, a.exe, a.real_exe)


if __name__ == "__main__":
    sys.exit(main())
