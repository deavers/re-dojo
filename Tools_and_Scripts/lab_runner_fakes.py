"""Fake labs used only by `lab_runner.py selftest` (interactive challenge mode). Not a lab."""

INTERACTIVE_EXE = r'''import sys
print("CHALLENGE: 4242", flush=True)
data = sys.stdin.readline().strip()
if data == "4242-ok":
    print("FLAG{I_4242}")
    sys.exit(0)
print("FAILED")
sys.exit(1)
'''

INTERACTIVE_SOLVE = r'''def answer_for(ch):
    return ch + "-ok\n"


def expected_flag(ch, answer):
    return "FLAG{I_" + ch + "}"


WRONG = [lambda ch: ch + "-no\n", "static wrong\n"]
'''
