"""[Lab 32] Reference solution (SPOILER). Commands for check/lab32_selftest (see dojo_selftest.hpp).

The Captain is g_Guards[2] (+0x20 in the guards array, sizeof(Guard) = 0x10); his vptr is at +0x00 of the
object. Copy the shared Guard table (4 slots) into your own memory, put the Merchant's slot 2 (IsBribable,
returns true) into slot 2 of the copy, and point only the Captain's vptr at the copy.
In Cheat Engine: alloc 0x20 bytes, copy the 4 pointers, overwrite +0x10 with the Merchant's [table+0x10],
write the new table address into the Captain's vptr.
"""

CAPTAIN = 0x20


def answer() -> str:
    return f"vcopy {hex(CAPTAIN)} 4\nvset {hex(CAPTAIN)} 2 donor 2\n"


WRONG = [
    # Patching the shared table in place: it is read-only (and would bribe every guard).
    f"vset {hex(CAPTAIN)} 2 donor 2\n",
    # Shadow table for the wrong guard (guard 1 at +0x10).
    "vcopy 0x10 4\nvset 0x10 2 donor 2\n",
    # Wrong slot: Greet (slot 1) replaced, IsBribable untouched.
    f"vcopy {hex(CAPTAIN)} 4\nvset {hex(CAPTAIN)} 1 donor 2\n",
    # Every guard bribed: the Marshal notices.
    "vcopy 0x00 4\nvset 0x00 2 donor 2\nvcopy 0x10 4\nvset 0x10 2 donor 2\n"
    f"vcopy {hex(CAPTAIN)} 4\nvset {hex(CAPTAIN)} 2 donor 2\n",
    # Whole-vptr swap to the Merchant's table: he takes bribes, but he is no longer a Captain.
    f"vswap {hex(CAPTAIN)} donor\n",
    # A shadow table with only 3 of the 4 slots: the game would call past its end.
    f"vcopy {hex(CAPTAIN)} 3\nvset {hex(CAPTAIN)} 2 donor 2\n",
    # Copying far past the end of the table: rejected, never a crash.
    f"vcopy {hex(CAPTAIN)} 64\n",
    # +0x24 is rank/gold, not a vptr: rejected.
    "vcopy 0x24 4\n",
]
