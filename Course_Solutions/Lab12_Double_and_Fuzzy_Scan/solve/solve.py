"""[Lab 12] Reference solution (SPOILER). Commands for check/lab12_selftest (see dojo_selftest.hpp).

In Cheat Engine: essence is a Double at +0x00 of g_Alchemy, catalyst purity a Float at +0x08.
Find them with "Unknown initial value" + Increased / Decreased, then set essence = 1000000 and purity = 1.0.
"""


def answer() -> str:
    return "poke 0x00 f64 1000000\npoke 0x08 f32 1.0\n"


WRONG = [
    # Essence written as a 4-byte float: only the low half of the double changes.
    "poke 0x00 f32 1000000\npoke 0x08 f32 1.0\n",
    # Purity written as a double: its low 4 bytes (all zero for 1.0) land on the float.
    "poke 0x00 f64 1000000\npoke 0x08 f64 1.0\n",
    # Purity written as the integer 1: a tiny denormal float, not 1.0.
    "poke 0x00 f64 1000000\npoke 0x08 i32 1\n",
    # Essence just below the goal.
    "poke 0x00 f64 999999.9\npoke 0x08 f32 1.0\n",
    # Out of bounds: must be rejected, never crash.
    "poke 0x10 f32 1.0\n",
]
