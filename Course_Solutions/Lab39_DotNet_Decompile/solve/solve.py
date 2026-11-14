"""[Lab 39] Reference solution (SPOILER): read ForgePassphrase() from the decompiled code and replay it.

chars[i] = (Gears[i] ^ (0x2A + i * 5)) - i. The solver parses Gears from game/Program.cs (in practice: copy it
out of dnSpyEx / ILSpy) - no passphrase is hard-coded here.
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "game" / "Program.cs"


def gears() -> list[int]:
    body = re.search(r"Gears\s*=\s*\{([^}]*)\}", SRC.read_text(encoding="utf-8")).group(1)
    return [int(x) for x in body.split(",")]


def passphrase(xor: bool = True, minus: bool = True) -> str:
    out = []
    for i, g in enumerate(gears()):
        v = g ^ (0x2A + i * 5) if xor else g
        out.append(chr(v - i if minus else v))
    return "".join(out)


def answer() -> str:
    return passphrase() + "\n"


WRONG = [
    # "- i" forgotten.
    passphrase(minus=False) + "\n",
    # Lower case (the comparison is ordinal).
    passphrase().lower() + "\n",
    # Reversed.
    passphrase()[::-1] + "\n",
    # Only the first half.
    passphrase()[:7] + "\n",
    # Empty line: exit 2.
    "\n",
]
