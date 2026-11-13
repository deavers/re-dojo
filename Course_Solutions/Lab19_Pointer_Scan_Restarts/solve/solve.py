"""[Lab 19] Reference solution (SPOILER). Commands for check/lab19_selftest (see dojo_selftest.hpp).

Stable path (survives restarts): g_World +0x18 -> Registry, +0x08 -> Entity** list, +0x18 (index 3) -> hero,
+0x2C = gold. In Cheat Engine: pointer scan for the gold address, restart the program, find gold again,
rescan the pointer list with the new address; repeat until the g_World-based path is left.
The runner starts the selftest 3 times (check/expected.json "runs"), each with a different heap layout.
"""


def answer() -> str:
    return "chain obj 0x18 0x08 0x18 0x2C i32 777777\n"


WRONG = [
    # Decoy 1: lastSpawned is always some mob, never the hero.
    "chain obj 0x10 0x2C i32 777777\n",
    # Decoy 2: the snapshot is a copy of the hero; editing it changes nothing.
    "chain obj 0x20 0x2C i32 777777\n",
    # Neighbour in the list (index 2 instead of 3).
    "chain obj 0x18 0x08 0x10 0x2C i32 777777\n",
    # Registry +0x00 is count/capacity, not a pointer: rejected as a bad address.
    "chain obj 0x18 0x00 0x18 0x2C i32 777777\n",
    # Right entity, wrong field (+0x28 is flags).
    "chain obj 0x18 0x08 0x18 0x28 i32 777777\n",
]
