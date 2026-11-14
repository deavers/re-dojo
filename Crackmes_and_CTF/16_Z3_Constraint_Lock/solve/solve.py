"""[Crackme 16] Reference solution (SPOILER): describe the five constraints to Z3 and let it find the key.

Needs z3-solver. The constants are read from crackme16_z3_lock.cpp - no key here.
Four 64-bit unknowns: one component still determines the others, but that is a search over 2^64 values
(at the review's measured 2^32 keys / 169 s that is ~23,000 years); Z3 solves the system in well under a second.
"""
import re
from pathlib import Path

import z3

SRC = Path(__file__).resolve().parents[1] / "crackme16_z3_lock.cpp"
BITS = 64


def consts() -> dict[str, int]:
    text = SRC.read_text(encoding="utf-8")
    return {m.group(1): int(m.group(2), 16)
            for m in re.finditer(r"constexpr std::uint64_t (k\w+) = 0x([0-9A-Fa-f]+)ULL;", text)}


def holds(key: tuple[int, int, int, int]) -> list[bool]:
    """Plain-Python evaluation of the five constraints (mirrors CheckKey)."""
    k, m = consts(), (1 << BITS) - 1
    a, b, c, d = key
    rot = ((b << 23) | (b >> (BITS - 23))) & m
    return [(a + b) & m == k["kK1"], a ^ c == k["kK2"], (rot + d) & m == k["kK3"],
            ((c * k["kGolden"]) & m) ^ d == k["kK4"], ((a & 0xFFFFFFFF) * 3 + (d >> 32)) & m == k["kK5"]]


def solve(skip_mul: bool = False, avoid: tuple[int, int, int, int] | None = None) -> tuple[int, int, int, int]:
    """skip_mul leaves out constraint 4 (multiplication); avoid excludes one key (fast plain disequality)."""
    k = consts()
    a, b, c, d = z3.BitVecs("a b c d", BITS)
    rules = [
        a + b == k["kK1"],
        a ^ c == k["kK2"],
        z3.RotateLeft(b, 23) + d == k["kK3"],
        (c * k["kGolden"]) ^ d == k["kK4"],
        (a & 0xFFFFFFFF) * 3 + z3.LShR(d, 32) == k["kK5"],
    ]
    s = z3.Solver()
    s.add(*[r for i, r in enumerate(rules) if not (skip_mul and i == 3)])
    if avoid is not None:
        s.add(a != avoid[0])
    assert s.check() == z3.sat
    m = s.model()
    return tuple(m.eval(v, model_completion=True).as_long() for v in (a, b, c, d))


def first_three_only(key: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    """A key that satisfies only constraints 1-3 (another a, the rest derived) - built without Z3."""
    k, m = consts(), (1 << BITS) - 1
    a = key[0] ^ 1
    b = (k["kK1"] - a) & m
    c = a ^ k["kK2"]
    d = (k["kK3"] - (((b << 23) | (b >> (BITS - 23))) & m)) & m
    return a, b, c, d


def fmt(key: tuple[int, int, int, int]) -> str:
    return "-".join(f"{x:016X}" for x in key)


def answer() -> str:
    return fmt(solve()) + "\n"


_KEY = solve()
_M = (1 << BITS) - 1
_NO_MUL = solve(skip_mul=True, avoid=_KEY)
assert not holds(_NO_MUL)[3]  # it breaks exactly the constraint that was left out
_ONLY_123 = first_three_only(_KEY)
assert holds(_ONLY_123)[:3] == [True, True, True] and not all(holds(_ONLY_123))
WRONG = [
    # Last component off by one.
    fmt((_KEY[0], _KEY[1], _KEY[2], (_KEY[3] + 1) & _M)) + "\n",
    # a and b swapped (constraint 1 still holds, the others do not).
    fmt((_KEY[1], _KEY[0], _KEY[2], _KEY[3])) + "\n",
    # A key of the system without the multiplication constraint.
    fmt(_NO_MUL) + "\n",
    # A key that satisfies only constraints 1-3.
    fmt(_ONLY_123) + "\n",
    # The old 32-bit layout: wrong format (exit 2).
    "1D5F8C2E-00000000-00000000-00000000\n",
    # Not hex: wrong format (exit 2).
    "XYZXYZXYZXYZXYZX-0000000000000000-0000000000000000-0000000000000000\n",
]
