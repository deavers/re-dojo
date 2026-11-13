"""[Lab 45] Reference name-pool dumper (SPOILER).

A learner's dumper reads the pool from process memory: g_NamePool -> chunks[] (+0x08, 8 bytes each) ->
entries (2-byte header = length << 6, then the characters, padded to an even offset);
FName index = (chunk << 16) | (offset / 2). This reference dumper is independent of the binary: it decodes
the XOR-encoded table from lab45_core.hpp and replays the pool layout, then prints "<index> <name>" lines.
The checker (check/lab45_selftest) compares the dump with the real pool in its own memory.
"""
import re
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "lab45_core.hpp"
CHUNK_SIZE, STRIDE, KEY = 0xC0, 2, 0x5C


def names() -> list[str]:
    text = CORE.read_text(encoding="utf-8")
    table = re.search(r"kEncodedNames\[\]\s*=\s*\{(.*?)\n\};", text, re.S).group(1)
    out = []
    for i, (length, body) in enumerate(re.findall(r"\{(\d+),\s*\{([^}]*)\}\}", table)):
        enc = [int(x, 16) for x in re.findall(r"0x[0-9A-Fa-f]{2}", body)][: int(length)]
        out.append("".join(chr(b ^ ((KEY + i * 7 + j * 3) & 0xFF)) for j, b in enumerate(enc)))
    return out


def pool(stride: int = STRIDE, chunk_shift: int = 16) -> list[tuple[int, str]]:
    chunk, offset, have_chunk, entries = 0, 0, False, []
    for name in names():
        size = (2 + len(name) + 1) & ~1
        if have_chunk and offset + size > CHUNK_SIZE:
            chunk, offset = chunk + 1, 0
        have_chunk = True
        entries.append(((chunk << chunk_shift) | (offset // stride), name))
        offset += size
    return entries


def dump(entries: list[tuple[int, str]]) -> str:
    return "".join(f"0x{i:08X} {n}\n" for i, n in entries)


def answer() -> str:
    return dump(pool())


WRONG = [
    # Last entry missing.
    dump(pool()[:-1]),
    # Index = byte offset (forgot the /2 stride).
    dump(pool(stride=1)),
    # Chunk shifted by 8 instead of 16.
    dump(pool(chunk_shift=8)),
    # One name with the wrong case.
    dump([(i, n.lower() if k == 5 else n) for k, (i, n) in enumerate(pool())]),
    # Malformed line (exit 2).
    "hello\n",
]
