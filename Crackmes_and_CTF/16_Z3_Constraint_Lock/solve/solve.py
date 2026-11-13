"""[Crackme 16] Reference solution (SPOILER): describe the five constraints to Z3 and let it find the key.

Needs z3-solver (pip install z3-solver). The constants are read from crackme16_z3_lock.cpp - no key here.
"""
import re
from pathlib import Path

import z3

SRC = Path(__file__).resolve().parents[1] / "crackme16_z3_lock.cpp"


def consts() -> dict[str, int]:
    text = SRC.read_text(encoding="utf-8")
    return {m.group(1): int(m.group(2), 16)
            for m in re.finditer(r"constexpr std::uint32_t (k\w+) = 0x([0-9A-Fa-f]+)U;", text)}


def solve(drop: int | None = None) -> tuple[int, int, int, int]:
    """drop = index of a constraint to leave out (used to build a 'weakened system' wrong answer)."""
    k = consts()
    a, b, c, d = z3.BitVecs("a b c d", 32)
    rules = [
        a + b == k["kC1"],
        a ^ c == k["kC2"],
        z3.RotateLeft(b, 7) + d == k["kC3"],
        (c * k["kGolden"]) ^ d == k["kC4"],
        (a & 0xFFFF) * 3 + z3.LShR(d, 16) == k["kC5"],
    ]
    s = z3.Solver()
    for i, r in enumerate(rules):
        if i != drop:
            s.add(r)
    if drop is not None:
        s.add(z3.Not(rules[drop]))  # a key of the weakened system that the real lock rejects
    assert s.check() == z3.sat
    m = s.model()
    return tuple(m.eval(v, model_completion=True).as_long() for v in (a, b, c, d))


def fmt(k: tuple[int, int, int, int]) -> str:
    return "-".join(f"{x:08X}" for x in k)


def answer() -> str:
    return fmt(solve()) + "\n"


_KEY = solve()
WRONG = [
    # Last component off by one.
    fmt((_KEY[0], _KEY[1], _KEY[2], (_KEY[3] + 1) & 0xFFFFFFFF)) + "\n",
    # a and b swapped (constraint 1 still holds, the others do not).
    fmt((_KEY[1], _KEY[0], _KEY[2], _KEY[3])) + "\n",
    # A key of the system without the multiplication constraint.
    fmt(solve(drop=3)) + "\n",
    # A key of the system without the masked mix.
    fmt(solve(drop=4)) + "\n",
    # Not hex: wrong format (exit 2).
    "XYZXYZXY-00000000-00000000-00000000\n",
]
