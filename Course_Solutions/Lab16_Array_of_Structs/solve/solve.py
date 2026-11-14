"""[Lab 16] Reference solution (SPOILER). Commands for check/lab16_selftest (see dojo_selftest.hpp).

In Cheat Engine: find unit 0's HP (4 Bytes), then the HP of unit 1 - the distance between them is the
stride 0x18. HP is at +0x04 of every element, the alive flag (bit 0) at +0x14. Unit 5 is the fallen one.
"""

STRIDE = 0x18
HP, FLAGS = 0x04, 0x14


def _all_hp(stride: int, count: int = 8, field: int = HP) -> str:
    return "".join(f"poke {hex(field + i * stride)} i32 500\n" for i in range(count))


def answer() -> str:
    return _all_hp(STRIDE) + f"poke {hex(FLAGS + 5 * STRIDE)} u32 1\n"


WRONG = [
    # Stride guessed as 0x14 (one field forgotten): the writes drift across fields.
    _all_hp(0x14) + f"poke {hex(FLAGS + 5 * STRIDE)} u32 1\n",
    # Only 7 of 8 units.
    _all_hp(STRIDE, 7) + f"poke {hex(FLAGS + 5 * STRIDE)} u32 1\n",
    # All HP set, but the fallen unit is still flagged as fallen.
    _all_hp(STRIDE),
    # Max HP edited instead of HP.
    _all_hp(STRIDE, field=0x08) + f"poke {hex(FLAGS + 5 * STRIDE)} u32 1\n",
    # More than 500 HP: the squad wants exactly 500.
    "".join(f"poke {hex(HP + i * STRIDE)} i32 600\n" for i in range(8)) + f"poke {hex(FLAGS + 5 * STRIDE)} u32 1\n",
    # Past the end of the array: must be rejected, never crash.
    "poke 0xC0 i32 500\n",
]
