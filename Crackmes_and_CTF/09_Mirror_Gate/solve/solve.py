"""[Crackme 09] Reference solution (SPOILER): invert "mirror, then shift every byte by +3"."""

ENCODED = [0x56, 0x56, 0x44, 0x4F, 0x4A, 0x62, 0x49, 0x52, 0x62, 0x52, 0x4B, 0x46, 0x48]
SHIFT = 3


def password() -> str:
    unshifted = [(b - SHIFT) & 0xFF for b in ENCODED]
    return bytes(reversed(unshifted)).decode("ascii")


def answer() -> str:
    return password() + "\n"


WRONG = [
    # Shift undone but the mirror forgotten.
    bytes((b - SHIFT) & 0xFF for b in ENCODED).decode("ascii") + "\n",
    # The stored bytes typed as they are.
    bytes(ENCODED).decode("ascii") + "\n",
    # Mirror undone, shift applied the wrong way.
    bytes(reversed([(b + SHIFT) & 0xFF for b in ENCODED])).decode("ascii") + "\n",
    # Right letters, wrong case.
    password().lower() + "\n",
    # One letter short: rejected as wrong length (exit 2).
    password()[:-1] + "\n",
]
