"""[Lab 19] Reference solution (SPOILER). Stdin for lab19_pointer_scan: mode 1, play a turn, submit the path.

Stable path: g_World +0x18 -> Registry, +0x08 -> Entity** list, +0x18 (index 3) -> hero, +0x2C = gold.
In Cheat Engine: pointer scan for the gold address, restart, find gold again, rescan the pointer list with the
new address; repeat until the g_World-based path is left. The program then rebuilds the world three times
and checks the submitted path in each.
"""


def answer() -> str:
    return "1\n1\n5\n0x18 0x08 0x18 0x2C\n"


WRONG = [
    # Decoy 1: lastSpawned - its gold mirrors the hero's, but it is another entity.
    "1\n1\n5\n0x10 0x2C\n",
    # Decoy 2: heroSnapshot - a copy refreshed every turn, not the hero.
    "1\n1\n5\n0x20 0x2C\n",
    # Neighbour in the list (index 2 instead of 3).
    "1\n1\n5\n0x18 0x08 0x10 0x2C\n",
    # Registry +0x00 is count/capacity, not a pointer.
    "1\n1\n5\n0x18 0x00 0x18 0x2C\n",
    # Right entity, wrong field (+0x28 is flags).
    "1\n1\n5\n0x18 0x08 0x18 0x28\n",
    # Malformed path (exit 2).
    "1\n1\n5\nhello\n",
]
