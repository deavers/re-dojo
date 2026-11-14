"""[Lab 13] Reference solution (SPOILER). Commands for check/lab13_selftest (see dojo_selftest.hpp).

In Cheat Engine: scan String "Apprentice" with UTF-16 enabled -> heroName at +0x00 of g_Card; write
DRAGONSLAYER as UTF-16. The guild tag "NEW" sits at +0x21 with its length byte at +0x20: set the
length to 4 and write DOJO.
"""


def answer() -> str:
    return "poke 0x00 str16 DRAGONSLAYER\npoke 0x20 u8 4\npoke 0x21 str8 DOJO\n"


WRONG = [
    # Name written as ASCII bytes: the game reads UTF-16, so it sees garbage.
    "poke 0x00 str8 DRAGONSLAYER\npoke 0x20 u8 4\npoke 0x21 str8 DOJO\n",
    # Tag letters changed but the length byte left at 3: the game reads "DOJ".
    "poke 0x00 str16 DRAGONSLAYER\npoke 0x21 str8 DOJO\n",
    # Tag written over the length byte: the length becomes 'D' (68).
    "poke 0x00 str16 DRAGONSLAYER\npoke 0x20 str8 DOJO\n",
    # Name written over the full buffer without its terminator: the game reads past it.
    "poke 0x00 str16 DRAGONSLAYERXXX\npoke 0x20 u8 4\npoke 0x21 str8 DOJO\n",
    # Wrong case.
    "poke 0x00 str16 dragonslayer\npoke 0x20 u8 4\npoke 0x21 str8 DOJO\n",
    # 20 UTF-16 letters + terminator do not fit: must be rejected, never crash.
    "poke 0x00 str16 AAAAAAAAAAAAAAAAAAAA\n",
]
