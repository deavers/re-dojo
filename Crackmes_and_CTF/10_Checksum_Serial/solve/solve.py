"""[Crackme 10] Reference key generator (SPOILER). Interactive: the binary prints "CHALLENGE: BBBB".

Rules: block B == challenge; digit sum of block A == 20; block C == (A * 7 + B * 3 + 1234) % 10000;
Luhn check digit over the 13 digits A B C D. Any serial that satisfies all of them is accepted.
"""
import random


def luhn_check_digit(payload: str) -> str:
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = int(ch)
        if i % 2 == 0:  # doubled once the check digit is appended
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return str((10 - total % 10) % 10)


def build(a: int, b: int, c: int | None = None, check: str | None = None) -> str:
    c = (a * 7 + b * 3 + 1234) % 10000 if c is None else c
    payload = f"{a:04d}{b:04d}{c:04d}"
    return f"DOJO-{a:04d}-{b:04d}-{c:04d}-{luhn_check_digit(payload) if check is None else check}"


def block_a(rng: random.Random, target_sum: int = 20) -> int:
    while True:
        a = rng.randrange(10000)
        if sum(map(int, f"{a:04d}")) == target_sum:
            return a


def keygen(challenge: str) -> str:
    return build(block_a(random.Random(int(challenge))), int(challenge))


def answer_for(challenge: str) -> str:
    return keygen(challenge) + "\n"


def expected_flag(challenge: str, answer: str) -> str:
    h = 0xCBF29CE484222325
    for byte in ("cm10|" + answer.strip()).encode("ascii"):
        h ^= byte
        h = (h * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return f"FLAG{{CM10_{h:016X}}}"


def _bad_luhn(ch: str) -> str:
    good = keygen(ch)
    return good[:-1] + str((int(good[-1]) + 1) % 10) + "\n"


WRONG = [
    # A valid serial for ANOTHER challenge (block B differs) - one found serial is not a key generator.
    lambda ch: build(block_a(random.Random(1)), (int(ch) + 1) % 10000) + "\n",
    # Only the Luhn check digit is wrong.
    _bad_luhn,
    # Block A does not sum to 20 (everything else recomputed).
    lambda ch: build(block_a(random.Random(2), target_sum=21), int(ch)) + "\n",
    # Block C off by one (Luhn recomputed).
    lambda ch: build(1955, int(ch), c=((1955 * 7 + int(ch) * 3 + 1234) + 1) % 10000) + "\n",
    # The old 16-digit layout: wrong format (exit 2).
    "1955-0000-5919-0000\n",
    # Letters: wrong format (exit 2).
    "DOJO-ABCD-EFGH-IJKL-M\n",
]
