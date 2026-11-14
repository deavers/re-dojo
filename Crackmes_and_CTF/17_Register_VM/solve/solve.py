"""[Crackme 17] Reference solution (SPOILER): dump the bytecode, disassemble it, invert the checks.

The program is read from kProgram in crackme17_register_vm.cpp (in a real binary: dump the array from .rdata).
Each check is  r0 = input[i]; r0 ^= k; r0 += acc; compare with e; acc = r0  ->  input[i] = (e - acc) ^ k.
The solver does not hard-code that: it tracks which register holds a value derived from an input byte,
records the operations applied to it, and inverts them at the compare.
"""
import re
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "crackme17_register_vm.cpp"
NAMES = {0x10: "LDI", 0x11: "LDB", 0x20: "ADD", 0x21: "XOR", 0x24: "MOV", 0x30: "CMP", 0x31: "JNE",
         0x40: "HALT_OK", 0x41: "HALT_FAIL"}
SIZE = {0x10: 6, 0x11: 3, 0x20: 3, 0x21: 3, 0x24: 3, 0x30: 3, 0x31: 3, 0x40: 1, 0x41: 1}
MASK = 0xFFFFFFFF


def program() -> list[int]:
    text = SRC.read_text(encoding="utf-8")
    body = re.search(r"kProgram\[\]\s*=\s*\{(.*?)\};", text, re.S).group(1)
    return [int(x, 16) for x in re.findall(r"0x[0-9A-Fa-f]{2}", body)]


def disassemble(code: list[int]) -> list[tuple[int, str, list[int]]]:
    out, pc = [], 0
    while pc < len(code):
        op = code[pc]
        args = code[pc + 1: pc + SIZE[op]]
        if op == 0x10:
            args = [args[0], args[1] | args[2] << 8 | args[3] << 16 | args[4] << 24]
        elif op == 0x31:
            args = [args[0] | args[1] << 8]
        out.append((pc, NAMES[op], args))
        pc += SIZE[op]
    return out


def key() -> str:
    regs: dict[int, object] = {}  # register -> int constant, or ("sym", index, [ops])
    solved: dict[int, int] = {}
    for _, name, a in disassemble(program()):
        if name == "LDI":
            regs[a[0]] = a[1]
        elif name == "LDB":
            regs[a[0]] = ("sym", a[1], [])
        elif name in ("XOR", "ADD"):
            dst, src = regs[a[0]], regs[a[1]]
            if isinstance(dst, tuple):
                dst[2].append((name, src))
            else:
                regs[a[0]] = (dst ^ src) if name == "XOR" else (dst + src) & MASK
        elif name == "MOV":
            regs[a[0]] = regs[a[1]]
        elif name == "CMP":
            sym, target = regs[a[0]], regs[a[1]]
            value = target
            for op, c in reversed(sym[2]):          # invert the recorded operations
                value = (value ^ c) if op == "XOR" else (value - c) & MASK
            solved[sym[1]] = value
            regs[a[0]] = target                     # after a passing compare the register equals the target
    return "".join(chr(solved[i]) for i in sorted(solved))


def answer() -> str:
    return key() + "\n"


WRONG = [
    # Last character off by one.
    key()[:-1] + chr(ord(key()[-1]) + 1) + "\n",
    # First character off by one: the accumulator makes every later check fail too.
    chr(ord(key()[0]) + 1) + key()[1:] + "\n",
    # Key reversed.
    key()[::-1] + "\n",
    # Lower case.
    key().lower() + "\n",
    # Seven characters: wrong length (exit 2).
    key()[:7] + "\n",
]
