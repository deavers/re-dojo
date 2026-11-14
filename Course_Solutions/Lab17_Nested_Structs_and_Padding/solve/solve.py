"""[Lab 17] Reference solution (SPOILER). Commands for check/lab17_selftest (see dojo_selftest.hpp).

Layout of g_Hero: id +0x00, (4 pad), Stats at +0x08 -> crit double at +0x08 + 0x10 = +0x18;
Armor at +0x20 -> durability uint16 at +0x22 (1 pad after tier); packed loot at +0x28 -> gold uint32 at
+0x29 (no padding, unaligned).
"""

CRIT, DURABILITY, LOOT_GOLD = 0x18, 0x22, 0x29


def _edits(crit: int = CRIT, dur: int = DURABILITY, gold: int = LOOT_GOLD, crit_type: str = "f64") -> str:
    return f"poke {hex(crit)} {crit_type} 1.0\npoke {hex(dur)} u16 9999\npoke {hex(gold)} u32 1000000\n"


def answer() -> str:
    return _edits()


WRONG = [
    # No padding assumed anywhere: crit right after agility.
    _edits(crit=0x0B),
    # Loot assumed aligned: gold at the next 4-byte boundary.
    _edits(gold=0x2C),
    # Armor padding ignored: durability right after tier.
    _edits(dur=0x21),
    # Crit written as a 4-byte float.
    _edits(crit_type="f32"),
    # Crit above the goal: the legend wants exactly 1.0.
    "poke 0x18 f64 2.0\npoke 0x22 u16 9999\npoke 0x29 u32 1000000\n",
    # Past the end of the hero: must be rejected, never crash.
    "poke 0x30 u8 1\n",
]
