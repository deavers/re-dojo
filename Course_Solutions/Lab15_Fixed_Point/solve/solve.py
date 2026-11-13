"""[Lab 15] Reference solution (SPOILER). Commands for check/lab15_selftest (see dojo_selftest.hpp).

In Cheat Engine: fuel 12.50 is the 4-Byte integer 12.5 * 65536 = 819200 at +0x00 of g_Ship, thrust
1.75 is 114688 at +0x04. Write raw values: fuel 1000.0 -> 65536000, thrust 3.25 -> 212992.
"""

ONE = 65536


def answer() -> str:
    return f"poke 0x00 i32 {1000 * ONE}\npoke 0x04 i32 {int(3.25 * ONE)}\n"


WRONG = [
    # Fuel written as a Float: the bit pattern of 1000.0f is not 1000.0 in 16.16.
    f"poke 0x00 f32 1000.0\npoke 0x04 i32 {int(3.25 * ONE)}\n",
    # Raw value without the 65536 scale.
    f"poke 0x00 i32 1000\npoke 0x04 i32 {int(3.25 * ONE)}\n",
    # Thrust written as a Float.
    f"poke 0x00 i32 {1000 * ONE}\npoke 0x04 f32 3.25\n",
    # Thrust rounded to a whole number.
    f"poke 0x00 i32 {1000 * ONE}\npoke 0x04 i32 {3 * ONE}\n",
    # Out of bounds: must be rejected, never crash.
    "poke 0x0C i32 1\n",
]
