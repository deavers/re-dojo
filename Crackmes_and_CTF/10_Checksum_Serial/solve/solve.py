"""[Crackme 10] Reference key generator (SPOILER).

Rules: (1) Luhn over all 16 digits, (2) block 1 digit sum == 20, (3) block 3 == (block1 * 7 + 1234) % 10000.
Any serial that satisfies all three is accepted; the flag does not depend on the serial.
"""
import random


def luhn_check_digit(payload: str) -> str:
    """Digit that makes payload + digit pass the Luhn check."""
    total = 0
    for i, ch in enumerate(reversed(payload)):
        d = int(ch)
        if i % 2 == 0:  # these digits are doubled once the check digit is appended
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return str((10 - total % 10) % 10)


def keygen(rng: random.Random) -> str:
    while True:
        b1 = f"{rng.randrange(10000):04d}"
        if sum(map(int, b1)) == 20:
            break
    b2 = f"{rng.randrange(10000):04d}"
    b3 = f"{(int(b1) * 7 + 1234) % 10000:04d}"
    b4 = f"{rng.randrange(1000):03d}"
    payload = b1 + b2 + b3 + b4
    return f"{b1}-{b2}-{b3}-{b4}{luhn_check_digit(payload)}"


def _fix_luhn(serial15: str) -> str:
    """Formats 15 digits + the Luhn digit, so a serial can break ONLY the rule under test."""
    return f"{serial15[0:4]}-{serial15[4:8]}-{serial15[8:12]}-{serial15[12:15]}{luhn_check_digit(serial15)}"


def answer() -> str:
    return keygen(random.Random(1337)) + "\n"


_GOOD = keygen(random.Random(1337)).replace("-", "")
_BAD_SUM = "9992" + _GOOD[4:8] + f"{(9992 * 7 + 1234) % 10000:04d}" + _GOOD[12:15]  # block 1 sums to 29
_BAD_B3 = _GOOD[0:8] + f"{(int(_GOOD[8:12]) + 1) % 10000:04d}" + _GOOD[12:15]

WRONG = [
    # Last digit changed: only the Luhn rule breaks.
    f"{_GOOD[0:4]}-{_GOOD[4:8]}-{_GOOD[8:12]}-{_GOOD[12:15]}{(int(_GOOD[15]) + 1) % 10}\n",
    # Block 1 does not sum to 20 (block 3 and Luhn are recomputed so only rule 2 breaks).
    _fix_luhn(_BAD_SUM) + "\n",
    # Block 3 off by one (Luhn recomputed so only rule 3 breaks).
    _fix_luhn(_BAD_B3) + "\n",
    # No dashes: wrong format (exit 2).
    _GOOD + "\n",
    # Letters: wrong format (exit 2).
    "ABCD-EFGH-IJKL-MNOP\n",
]
