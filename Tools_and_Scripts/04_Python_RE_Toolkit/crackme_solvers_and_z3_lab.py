#!/usr/bin/env python3
"""
============================================================================
[Tool 04-B] Crackme Solver Workbench: Keygen, License Forger, VM & Z3 Lab
============================================================================
PURPOSE:
  Interactive Python companion script for `Crackmes_and_CTF/`:
    1. Keygen solver for Crackme 02 (Mathematical Serial Lock)
    2. Bitwise ROL8/ROR8 inverter for Crackme 03
    3. Binary `license.dat` struct generator for Crackme 04 (`struct.pack`)
    4. Custom Stack VM Disassembler for Crackme 06
    5. Symbolic Constraint Solver (Z3 / Pure Python fallback) for Crackme 08
============================================================================
"""

import struct


def ror8(val: int, shift: int) -> int:
    shift &= 7
    return ((val >> shift) | (val << (8 - shift))) & 0xFF


def solve_crackme02_keygen():
    print("\n--- [Crackme 02 Keygen: Mathematical Serial Lock] ---")
    found = 0
    for a in range(1000, 10000):
        b = 10000 - a
        if 1000 <= b <= 9999 and (a ^ b) == 9984:
            c = ((a * 3) + (b ^ 0x1234)) % 9000 + 1000
            print(f"  [+] Valid Serial #{found + 1}: {a:04d}-{b:04d}-{c:04d}")
            found += 1
            if found >= 4:
                break


def solve_crackme03_cipher():
    print("\n--- [Crackme 03 Decryptor: ROR8 + XOR Loop Inversion] ---")
    encrypted = [
        0xC0, 0x41, 0xE1, 0xC1, 0xF9, 0x71, 0x0E, 0xA6, 0x9E, 0xAE,
        0x1F, 0x7F, 0x5F, 0xC7, 0xAF, 0x84, 0xF4, 0x74, 0x0F, 0x37,
    ]
    chars = []
    for i, b in enumerate(encrypted):
        unrotated = ror8(b, 3)
        plain = unrotated ^ ((0x5A + i * 7) & 0xFF)
        chars.append(chr(plain))
    print(f"  [+] Recovered 20-Char Rune: {''.join(chars)}")


def forge_crackme04_license(output_path: str = "license.dat"):
    print("\n--- [Crackme 04 Forger: Binary `license.dat` Struct] ---")
    magic = 0x56414544        # "DEAV"
    version = 0x0104          # v1.4
    badge = 0x0777            # Tier badge
    citizen_id = 133777       # >= 100,000
    flags = 0x8000002A        # Required feature bitmask
    crc = (magic ^ (citizen_id & 0xFFFFFFFF) ^ flags ^ 0xA5A5A5A5) & 0xFFFFFFFF

    payload = struct.pack("<IHHQII", magic, version, badge, citizen_id, flags, crc)
    with open(output_path, "wb") as f:
        f.write(payload)
    print(f"  [+] Wrote {len(payload)}-byte binary license to `{output_path}` (CRC: 0x{crc:08X})")


def disassemble_crackme06_vm():
    print("\n--- [Crackme 06 Disassembler: Custom Stack VM Bytecode] ---")
    bytecode = [
        0x02, 0x00, 0x01, 0x12, 0x11, 0x01, 0x05, 0x10, 0x01, 0x49, 0x20,
        0x02, 0x01, 0x01, 0x23, 0x11, 0x01, 0x07, 0x10, 0x01, 0x75, 0x20,
        0x02, 0x02, 0x01, 0x34, 0x11, 0x01, 0x09, 0x10, 0x01, 0x74, 0x20,
        0x02, 0x03, 0x01, 0x45, 0x11, 0x01, 0x0B, 0x10, 0x01, 0x19, 0x20,
        0x02, 0x04, 0x01, 0x56, 0x11, 0x01, 0x0D, 0x10, 0x01, 0x2C, 0x20,
        0x02, 0x05, 0x01, 0x67, 0x11, 0x01, 0x0F, 0x10, 0x01, 0x38, 0x20,
        0x02, 0x06, 0x01, 0x78, 0x11, 0x01, 0x11, 0x10, 0x01, 0x50, 0x20,
        0x02, 0x07, 0x01, 0x19, 0x11, 0x01, 0x03, 0x10, 0x01, 0x3B, 0x20,
        0xFF,
    ]
    recovered = []
    for offset in range(0, 88, 11):
        idx = bytecode[offset + 1]
        xor_k = bytecode[offset + 3]
        add_k = bytecode[offset + 6]
        target = bytecode[offset + 9]
        ch = ((target - add_k) & 0xFF) ^ xor_k
        recovered.append(chr(ch))
        print(f"  [VIP 0x{offset:02X}] (input[{idx}] ^ 0x{xor_k:02X}) + 0x{add_k:02X} == 0x{target:02X}  => '{chr(ch)}'")
    print(f"  [+] Solved VM Password: {''.join(recovered)}")


def solve_crackme08_symbolic():
    print("\n--- [Crackme 08 SMT Constraint Solver] ---")
    for b0 in range(32, 127):
        b1 = 141 - b0
        if (b0 ^ b1) != 105:
            continue
        b2 = 44 + b1
        b3 = 172 - b2
        b4 = b3 ^ 12
        b5 = 2 * b4 - 59
        b6 = 140 - b5
        if (b5 ^ b6) != 2:
            continue
        b7 = b6 - 36
        if b0 + b4 + b7 == 188:
            key = "".join(chr(x) for x in (b0, b1, b2, b3, b4, b5, b6, b7))
            print(f"  [+] Unique SMT Model Found: {key}")


if __name__ == "__main__":
    print("====================================================================")
    print("  REVERSE ENGINEERING JOURNEY - PYTHON SOLVER WORKBENCH")
    print("====================================================================")
    solve_crackme02_keygen()
    solve_crackme03_cipher()
    forge_crackme04_license()
    disassemble_crackme06_vm()
    solve_crackme08_symbolic()
