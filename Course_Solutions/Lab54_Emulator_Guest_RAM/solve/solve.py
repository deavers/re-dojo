"""[Lab 54] Reference solution (SPOILER). Commands for check/lab54_selftest (see dojo_selftest.hpp).

Host address of a guest variable = [g_Machine +0x08] (the guest RAM pointer) + guest address.
In Cheat Engine: find the score (2 Bytes) on the host, subtract guest 0x0302 -> RAM base; "find out what
accesses" / pointer scan for the base leads to g_Machine.ram at +0x08. Then: lives = [[g_Machine+0x08]+0x300],
score = [[g_Machine+0x08]+0x302]. The runner starts the selftest 3 times (new host placement each time).
"""


def answer() -> str:
    return "chain obj 0x08 0x0300 u8 99\nchain obj 0x08 0x0302 u16 50000\n"


WRONG = [
    # Guest address used as an offset inside the emulator object: outside it, rejected.
    "poke 0x0300 u8 99\n",
    # Score one byte off (0x0301): the u16 lands across lives and score.
    "chain obj 0x08 0x0300 u8 99\nchain obj 0x08 0x0301 u16 50000\n",
    # Score written big-endian (bytes C3 50): the console reads 0x50C3 = 20675.
    "chain obj 0x08 0x0300 u8 99\nchain obj 0x08 0x0302 u16 0x50C3\n",
    # ramSize (+0x10) taken for the RAM pointer: not an address, rejected.
    "chain obj 0x10 0x0300 u8 99\n",
    # Score above the goal: the table wants exactly 50000.
    "chain obj 0x08 0x0300 u8 99\nchain obj 0x08 0x0302 u16 60000\n",
    # One life too many.
    "chain obj 0x08 0x0300 u8 100\nchain obj 0x08 0x0302 u16 50000\n",
]
