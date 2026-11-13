"""[Lab 11] Reference solution (SPOILER). Commands for check/lab11_selftest (see dojo_selftest.hpp).

In Cheat Engine the same edits are: Morale 1 Byte at +0x00 = -100, Arrows 2 Bytes at +0x02 = 65535,
Gold 8 Bytes at +0x08 = 5000000000 (struct g_Treasury, 4 bytes of padding before gold).
"""


def answer() -> str:
    return "poke 0x00 i8 -100\npoke 0x02 u16 65535\npoke 0x08 i64 5000000000\n"


WRONG = [
    # Gold written as 4 bytes: only the low half changes, the value stays far below 5 billion.
    "poke 0x00 i8 -100\npoke 0x02 u16 65535\npoke 0x08 i32 705032704\n",
    # Gold placed right after arrows (padding ignored): the 8-byte write lands across padding and gold.
    "poke 0x00 i8 -100\npoke 0x02 u16 65535\npoke 0x04 i64 5000000000\n",
    # Positive morale instead of negative.
    "poke 0x00 i8 100\npoke 0x02 u16 65535\npoke 0x08 i64 5000000000\n",
    # Arrows written as one byte: 255 is not 65535.
    "poke 0x00 i8 -100\npoke 0x02 u8 255\npoke 0x08 i64 5000000000\n",
    # Out of bounds: must be rejected, never crash.
    "poke 0x40 i8 1\n",
]
