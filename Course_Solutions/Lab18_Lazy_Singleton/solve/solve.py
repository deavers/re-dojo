"""[Lab 18] Reference solution (SPOILER). Commands for check/lab18_selftest (see dojo_selftest.hpp).

In Cheat Engine: enter the dungeon once so the manager exists, then use the pointer
[g_pGameManager] -> +0x08 (Player*) -> +0x08 (Inventory*) -> +0x10 = gems (4 Bytes) and set 99999.
"""


def answer() -> str:
    return "act enter\nchain ptr 0x08 0x08 0x10 i32 99999\n"


WRONG = [
    # Chain used before the lazy init: the static pointer is still NULL.
    "chain ptr 0x08 0x08 0x10 i32 99999\n",
    # One level skipped: gems read straight from the Player object (outside it).
    "act enter\nchain ptr 0x08 0x10 i32 99999\n",
    # First offset wrong: reads the ticks/floor ints as a pointer.
    "act enter\nchain ptr 0x00 0x08 0x10 i32 99999\n",
    # Right chain, last offset off by 4 (weight instead of gems).
    "act enter\nchain ptr 0x08 0x08 0x0C i32 99999\n",
    # Too many gems: the room wants exactly 99999.
    "act enter\nchain ptr 0x08 0x08 0x10 i32 100000\n",
    # Not enough gems.
    "act enter\nchain ptr 0x08 0x08 0x10 i32 9999\n",
    # A plain poke has no static object to write into here: rejected, never a crash.
    "act enter\npoke 0x00 i32 99999\n",
]
