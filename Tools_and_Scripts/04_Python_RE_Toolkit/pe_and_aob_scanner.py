#!/usr/bin/env python3
"""
============================================================================
[Tool 04-A] PE32/PE64 Section Entropy & Wildcard AOB Signature Scanner
============================================================================
PURPOSE:
  A zero-dependency Python utility for Static Binary Analysis:
    1. Parses Windows PE32 / PE64 headers (`.text`, `.rdata`, `.data`, `.vmp0`).
    2. Computes Shannon Entropy H(X) (bits/byte, 0.0 to 8.0) for each section
       to detect packed or encrypted code (e.g. UPX, VMProtect, ChaCha20 stubs).
    3. Scans the binary for Cheat Engine / IDA style wildcard Array-of-Bytes
       (AOB) signatures (e.g. `48 8B 05 ?? ?? ?? ??`) and prints File Offset,
       RVA, and Virtual Address!

USAGE:
  python pe_and_aob_scanner.py <path_to_exe> ["48 89 5C 24 ??"]
============================================================================
"""

import math
import struct
import sys
from pathlib import Path
from collections import Counter


def calculate_shannon_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    counts = Counter(data)
    total = len(data)
    return -sum((c / total) * math.log2(c / total) for c in counts.values())


def parse_pe_headers(data: bytes):
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise ValueError("Not a valid DOS/PE executable (missing MZ header).")

    pe_offset = struct.unpack_from("<I", data, 0x3C)[0]
    if data[pe_offset : pe_offset + 4] != b"PE\x00\x00":
        raise ValueError("Invalid PE signature.")

    machine, num_sections, _, _, _, opt_header_size, _ = struct.unpack_from(
        "<HHIIIHH", data, pe_offset + 4
    )
    opt_offset = pe_offset + 24
    magic = struct.unpack_from("<H", data, opt_offset)[0]
    is_pe64 = magic == 0x20B
    entry_rva = struct.unpack_from("<I", data, opt_offset + 16)[0]
    image_base = (
        struct.unpack_from("<Q", data, opt_offset + 24)[0]
        if is_pe64
        else struct.unpack_from("<I", data, opt_offset + 28)[0]
    )

    sec_table_offset = opt_offset + opt_header_size
    sections = []
    for i in range(num_sections):
        sec_off = sec_table_offset + i * 40
        name_raw, virt_size, virt_addr, raw_size, raw_ptr = struct.unpack_from(
            "<8sIIII", data, sec_off
        )
        flags = struct.unpack_from("<I", data, sec_off + 36)[0]
        name = name_raw.split(b"\x00", 1)[0].decode("ascii", errors="replace")
        sec_bytes = data[raw_ptr : raw_ptr + raw_size]
        entropy = calculate_shannon_entropy(sec_bytes)
        sections.append(
            {
                "name": name,
                "vaddr": virt_addr,
                "vsize": virt_size,
                "raw_ptr": raw_ptr,
                "raw_size": raw_size,
                "flags": flags,
                "entropy": entropy,
            }
        )

    return {
        "arch": "PE64 (x86_64)" if is_pe64 else "PE32 (x86)",
        "image_base": image_base,
        "entry_rva": entry_rva,
        "sections": sections,
    }


def scan_aob_pattern(data: bytes, pattern_str: str):
    tokens = pattern_str.strip().split()
    pattern = []
    for tok in tokens:
        if tok in ("?", "??", "*"):
            pattern.append(None)
        else:
            pattern.append(int(tok, 16))

    matches = []
    pat_len = len(pattern)
    limit = len(data) - pat_len + 1
    first_byte = pattern[0]

    i = 0
    while i < limit:
        if first_byte is not None:
            idx = data.find(bytes([first_byte]), i, limit)
            if idx == -1:
                break
            i = idx

        matched = True
        for j in range(1, pat_len):
            p = pattern[j]
            if p is not None and data[i + j] != p:
                matched = False
                break
        if matched:
            matches.append(i)
        i += 1

    return matches


def file_offset_to_rva(offset: int, sections: list) -> int:
    for s in sections:
        if s["raw_ptr"] <= offset < s["raw_ptr"] + s["raw_size"]:
            return s["vaddr"] + (offset - s["raw_ptr"])
    return offset


def main():
    if len(sys.argv) < 2:
        print("Usage: python pe_and_aob_scanner.py <binary.exe> [\"AOB PATTERN\"]")
        sys.exit(0)

    target_path = Path(sys.argv[1])
    raw_data = target_path.read_bytes()
    info = parse_pe_headers(raw_data)

    print("=" * 72)
    print(f"  PE BINARY AUDIT: {target_path.name}")
    print("=" * 72)
    print(f"  Architecture : {info['arch']}")
    print(f"  ImageBase    : 0x{info['image_base']:016X}")
    print(f"  Entry RVA    : 0x{info['entry_rva']:08X}")
    print("-" * 72)
    print(f"  {'Section':<10} {'RVA':<12} {'RawSize':<12} {'Entropy':<10} {'Assessment'}")
    print("-" * 72)
    for s in info["sections"]:
        status = "PACKED / ENCRYPTED!" if s["entropy"] > 7.2 else "Normal"
        print(
            f"  {s['name']:<10} 0x{s['vaddr']:08X}   0x{s['raw_size']:08X}   {s['entropy']:5.2f}/8.0  {status}"
        )
    print("=" * 72)

    if len(sys.argv) >= 3:
        aob = sys.argv[2]
        print(f"\n[*] Scanning for AOB Signature: {aob}")
        hits = scan_aob_pattern(raw_data, aob)
        print(f"[+] Found {len(hits)} match(es):")
        for off in hits[:20]:
            rva = file_offset_to_rva(off, info["sections"])
            va = info["image_base"] + rva
            print(f"    FileOffset: 0x{off:08X} | RVA: +0x{rva:08X} | VA: 0x{va:016X}")


if __name__ == "__main__":
    main()
