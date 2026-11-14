"""[Lab 45] Reference name-pool dumper (SPOILER).

A learner's dumper reads the pool from process memory: g_NamePool -> chunks[] (+0x08, 8 bytes each) ->
entries (2-byte header = length << 6, then the characters, padded to an even offset);
FName index = (chunk << 16) | (offset / 2). The names are inserted in a seed-dependent order, so the dump
belongs to one seed (the game prints it). This reference dumper is independent of the binary: it decodes
the XOR-encoded table from lab45_core.hpp and replays the seeded insertion (xorshift32 + Fisher-Yates).
Checker input: "seed <N>" then "<index> <name>" lines.
"""
import re
from pathlib import Path

CORE = Path(__file__).resolve().parents[1] / "lab45_core.hpp"
CHUNK_SIZE, STRIDE, KEY = 0xC0, 2, 0x5C
SEED = 424242


def names() -> list[str]:
    text = CORE.read_text(encoding="utf-8")
    table = re.search(r"kEncodedNames\[\]\s*=\s*\{(.*?)\n\};", text, re.S).group(1)
    out = []
    for i, (length, body) in enumerate(re.findall(r"\{(\d+),\s*\{([^}]*)\}\}", table)):
        enc = [int(x, 16) for x in re.findall(r"0x[0-9A-Fa-f]{2}", body)][: int(length)]
        out.append("".join(chr(b ^ ((KEY + i * 7 + j * 3) & 0xFF)) for j, b in enumerate(enc)))
    return out


def order(seed: int, n: int) -> list[int]:
    s = (seed | 1) & 0xFFFFFFFF
    pos = list(range(n))
    for i in range(n - 1, 0, -1):
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= s >> 17
        s ^= (s << 5) & 0xFFFFFFFF
        j = s % (i + 1)
        pos[i], pos[j] = pos[j], pos[i]
    return pos


def pool(seed: int = SEED, stride: int = STRIDE, chunk_shift: int = 16) -> list[tuple[int, str]]:
    table = names()
    chunk, offset, have_chunk, entries = 0, 0, False, []
    for i in order(seed, len(table)):
        name = table[i]
        size = (2 + len(name) + 1) & ~1
        if have_chunk and offset + size > CHUNK_SIZE:
            chunk, offset = chunk + 1, 0
        have_chunk = True
        entries.append(((chunk << chunk_shift) | (offset // stride), name))
        offset += size
    return entries


def dump(entries: list[tuple[int, str]], seed: int = SEED) -> str:
    return f"seed {seed}\n" + "".join(f"0x{i:08X} {n}\n" for i, n in entries)


def answer() -> str:
    return dump(pool())


WRONG = [
    # A correct dump of ANOTHER seed's pool, presented as this seed.
    dump(pool(seed=SEED + 2)),  # +2: seed | 1 makes an even seed and seed + 1 identical
    # Seeded insertion order ignored: the real indices paired with the names in table order.
    dump([(idx, n) for (idx, _), n in zip(pool(), names())]),
    # Last entry missing.
    dump(pool()[:-1]),
    # Index = byte offset (forgot the /2 stride).
    dump(pool(stride=1)),
    # Chunk shifted by 8 instead of 16.
    dump(pool(chunk_shift=8)),
    # No seed line (exit 2).
    "".join(f"0x{i:08X} {n}\n" for i, n in pool()),
]
