#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
  Reverse Engineering RPG — Automated Artifact Tier & Difficulty Grader
  File: Tools_and_Scripts/auto_artifact_grader.py
================================================================================
  Automatically analyzes any reverse engineering artifact:
    - Cheat Engine Tables (.CT / .CEA / .ASM)
    - C / C++ / C# Trainers, Internal DLLs, VMT Hooks & SDK Dumpers (.cpp/.hpp/.cs)
    - Python RE Scripts, Unpackers, Keygens & Z3/angr Solvers (.py)
    - Markdown CTF Writeups (.md)

  How the Calculation Works (Deterministic 5-Axis Formula = 0.5 to 10.0):
    Axis 1: Architecture & Runtime Target      (0.2 - 2.0 pts)
    Axis 2: Memory Indirection & Struct Depth  (0.1 - 2.0 pts)
    Axis 3: Code, Hook & Math Complexity       (0.1 - 2.0 pts)
    Axis 4: Protection, Anti-Debug & Obfus.    (0.0 - 2.5 pts)
    Axis 5: Privilege & Execution Boundary     (0.0 - 1.5 pts)
    ----------------------------------------------------------
    Total Score = clamp(Axis1 + Axis2 + Axis3 + Axis4 + Axis5, 0.5, 10.0)
================================================================================
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

TIERS = [
    ("F-",  "Unranked Novice",            0.0, 0.4),
    ("F",   "White-Box Initiate",         0.5, 0.6),
    ("F+",  "Script Tinkerer",            0.7, 0.9),
    ("E--", "Memory Scanner",             1.0, 1.2),
    ("E-",  "Pointer Seeker",             1.3, 1.6),
    ("E",   "Assembly Apprentice",        1.7, 2.0),
    ("E+",  "Codecave Weaver",            2.1, 2.4),
    ("D-",  "Pointer Alchemist",          2.5, 2.8),
    ("D",   "Entity Filter Tactician",    2.9, 3.2),
    ("D+",  "Stealth & Logic Hacker",     3.3, 3.6),
    ("C-",  "Struct & Bitmask Scholar",   3.7, 4.0),
    ("C",   "Adventurer (Managed JIT)",   4.1, 4.5),
    ("C+",  "Harmony & Runtime Modder",   4.6, 4.9),
    ("B-",  "VMT & RTTI Investigator",    5.0, 5.3),
    ("B",   "Netvar & 3D Math Engineer",  5.4, 5.7),
    ("B+",  "Internal DLL Specialist",    5.8, 6.1),
    ("A-",  "UE4/5 SDK Architect",        6.2, 6.5),
    ("A",   "IL2CPP & VM Reverser",       6.6, 6.9),
    ("A+",  "LuaJIT & ECS Hacker",        7.0, 7.3),
    ("S-",  "Custom Engine Conqueror",    7.4, 7.6),
    ("S",   "DOD & MBA De-Obfuscator",    7.7, 7.9),
    ("S+",  "Cross-ISA Emulator Master",  8.0, 8.2),
    ("SS-", "JVM JNI & Protocol Cryptor", 8.3, 8.5),
    ("SS",  "Packer & OEP Unpacker",      8.6, 8.8),
    ("SS+", "VMProtect & Arxan Auditor",  8.9, 9.1),
    ("SSS-","Symbolic Z3 / angr Savant",  9.2, 9.4),
    ("SSS", "Ring-0 & VMI Hypervisor",    9.5, 9.7),
    ("SSS+","Matching Decomp Grandmaster",9.8, 9.9),
    ("SSS++","Demigod of Silicon",       10.0, 10.0),
]


def score_to_tier(score: float) -> tuple[str, str]:
    s = round(max(0.5, min(10.0, score)), 1)
    for code, title, lo, hi in TIERS:
        if lo <= s <= hi + 1e-6:
            return code, title
    return "SSS++", "Demigod of Silicon"


def analyze_cheat_table(text: str, filename: str) -> dict:
    """Parse Cheat Engine .CT XML and extract objective complexity metrics."""
    evidence = {
        "axis1": [],
        "axis2": [],
        "axis3": [],
        "axis4": [],
        "axis5": [],
    }

    # Parse XML metrics
    max_ptr_depth = 0
    ptr_chains_count = 0
    aa_scripts = []
    var_types = set()
    addresses = []

    try:
        root = ET.fromstring(text)
        for entry in root.iter("CheatEntry"):
            vtype = entry.findtext("VariableType")
            if vtype:
                var_types.add(vtype.strip())
            addr = entry.findtext("Address")
            if addr:
                addresses.append(addr.strip())
            offsets_el = entry.find("Offsets")
            if offsets_el is not None:
                offs = [o.text for o in offsets_el.findall("Offset") if o.text]
                if offs:
                    ptr_chains_count += 1
                    max_ptr_depth = max(max_ptr_depth, len(offs))
            script = entry.findtext("AssemblerScript")
            if script:
                aa_scripts.append(script)
    except ET.ParseError:
        # Fallback if plain .CEA script
        aa_scripts = [text]

    all_scripts = "\n".join(aa_scripts)
    # Strip Cheat Engine { ... } comment blocks so we grade active [ENABLE] code rather than commented disassembly dumps
    active_scripts = re.sub(r"\{.*?\}", "", all_scripts, flags=re.S)
    low_all = (text + "\n" + all_scripts).lower()

    # --- AXIS 1: Architecture & Runtime Target (0.2 - 2.0) ---
    axis1 = 0.4
    if any(k in low_all for k in ["big endian", "cemu", "rpcs3", "ryujinx", "arm64", "powerpc"]):
        axis1 = 2.0
        evidence["axis1"].append("Cross-ISA Emulator / Big-Endian target (2.0)")
    elif any(k in low_all for k in ["gameassembly.dll", "il2cpp", "global-metadata"]):
        axis1 = 1.7
        evidence["axis1"].append("Unity IL2CPP AOT Native Assembly (1.7)")
    elif any(k in low_all for k in ["gobjects", "gnames", "uworld", "fnamepool", "processevent"]):
        axis1 = 1.5
        evidence["axis1"].append("Unreal Engine 4/5 Reflection (GWorld/GNames) (1.5)")
    elif any(k in low_all for k in ["unityplayer.dll", "mono_", "launchmonodatacollector"]) or (
        re.search(r"\b(rax|rcx|rdx|rsi|rdi|r8|r9|r10|r11|r12|r13|r14|r15|movsxd)\b", all_scripts, re.I)
        and re.search(r"call\s+r1[0-5]", all_scripts, re.I)
    ):
        axis1 = 1.15
        evidence["axis1"].append("64-bit Unity / Managed JIT Runtime (x64 registers + JIT trampolines) (1.15)")
    elif re.search(r"\b(rax|rcx|rdx|r8|r9|r10|r11|movsxd|qword ptr)\b", all_scripts, re.I):
        axis1 = 1.0
        evidence["axis1"].append("Native x86_64 Architecture (64-bit registers & RIP-relative addressing) (1.0)")
    elif any(k in low_all for k in ["isaac-ng.exe"]):
        axis1 = 0.95
        evidence["axis1"].append("Custom C++20 Game Engine (`isaac-ng.exe`) with deep class hierarchies (0.95)")
    elif any(k in low_all for k in ["engine.dll", "core.dll", "render.dll"]):
        axis1 = 0.75
        evidence["axis1"].append("Multi-module C++ Engine (`Engine.dll` / `Core.dll` / `Render.dll`) (0.75)")
    elif any(k in low_all for k in ["popcapgame1.exe", "plantsvszombies"]):
        axis1 = 0.55
        evidence["axis1"].append("32-bit C++ Framework (`popcapgame1.exe` x86) (0.55)")
    else:
        evidence["axis1"].append("Standard 32-bit x86 target binary (0.4)")

    # --- AXIS 2: Memory Indirection & Struct Depth (0.1 - 2.0) ---
    axis2 = 0.2
    # Detect struct offsets inside active assembly like [eax+0000134C] or [edi+00005578]
    hex_disp = [int(m, 16) for m in re.findall(r"\[(?:e?[a-z]{2,3}|r[a-z0-9]{1,2})\+([0-9a-fA-F]{2,8})\]", active_scripts)]
    all_disp = [int(m, 16) for m in re.findall(r"\[(?:e?[a-z]{2,3}|r[a-z0-9]{1,2})\+([0-9a-fA-F]{2,8})\]", all_scripts)]
    max_struct_disp = max(hex_disp) if hex_disp else 0
    max_context_disp = max(all_disp) if all_disp else 0

    if max_ptr_depth >= 5:
        axis2 = 1.05
        evidence["axis2"].append(f"Deep {max_ptr_depth}-level pointer chains ({ptr_chains_count} chains) (1.05)")
    elif max_ptr_depth >= 3:
        axis2 = 0.80
        evidence["axis2"].append(f"Multi-level {max_ptr_depth}-deep pointer chains ({ptr_chains_count} chains) (0.80)")
    elif max_context_disp >= 0x10000 and max_struct_disp >= 0x1000:
        axis2 = 1.00
        evidence["axis2"].append(f"Large C++ engine class offsets (active +0x{max_struct_disp:X}, context +0x{max_context_disp:X}) (1.00)")
    elif max_struct_disp >= 0x1000:
        axis2 = 0.65
        evidence["axis2"].append(f"C++ class member offsets (up to +0x{max_struct_disp:X}) (0.65)")
    elif max_ptr_depth >= 1 or max_struct_disp > 0:
        axis2 = 0.45
        evidence["axis2"].append(f"Pointer/struct displacement addressing (max offset +0x{max_struct_disp:X}) (0.45)")
    else:
        evidence["axis2"].append("Direct / static memory addressing (0.20)")

    # Check if dynamic pointer walk is done manually inside assembly (e.g. mov ecx, ["Engine.dll"+...]; mov ecx, [ecx+30])
    if re.search(r"mov\s+\w+,\s*\[[^\]]+\]\s*\n\s*test\s+\w+,\s*\w+\s*\n\s*jz", active_scripts, re.I):
        axis2 = round(min(2.0, axis2 + 0.20), 2)
        evidence["axis2"].append("Manual NULL-checked pointer chain traversal inside assembly (+0.20)")

    # --- AXIS 3: Code, Hook & Math Complexity (0.1 - 2.0) ---
    aob_count = len(re.findall(r"\baobscan(?:module|region)?\b", active_scripts, re.I))
    alloc_count = len(re.findall(r"\balloc\s*\(", active_scripts, re.I))
    lua_blocks = len(re.findall(r"\{\$lua\}|<LuaScript>", text, re.I))
    cmp_branches = len(re.findall(r"\b(cmp|test)\b.*?\n\s*\b(je|jne|jz|jnz|jg|jl|ja|jb|jge|jle|jbe|jnl|cmov\w+)\b", active_scripts, re.I))
    sse_fpu = len(re.findall(r"\b(movss|addss|subss|mulss|divss|comiss|ucomiss|cvt\w+|xmm[0-9]+|fld|fstp|fadd|fsub)\b", active_scripts, re.I))
    near_alloc_64 = len(re.findall(r"alloc\s*\(\s*\w+\s*,\s*\$?[0-9a-fA-F]+\s*,\s*\w+\s*\)", active_scripts, re.I))

    axis3 = 0.2
    if alloc_count >= 1:
        axis3 = 0.65
        evidence["axis3"].append(f"Auto Assembler codecave hooks ({alloc_count} allocs, {aob_count} AOB scans) (0.65)")
    if aob_count >= 5:
        axis3 += 0.25
        evidence["axis3"].append(f"Multi-feature AOB script suite ({aob_count} independent AOB injections) (+0.25)")
    if aob_count >= 8:
        axis3 += 0.45
        evidence["axis3"].append(f"Comprehensive 8+ AOB table covering multiple engine subsystems (+0.45)")
    if re.search(r"check_enemy|god\s*mode|one[\s-]*shot", active_scripts, re.I) or cmp_branches >= 4:
        axis3 += 0.30
        evidence["axis3"].append(f"Shared-code entity filter & conditional branching ({cmp_branches} branches) (+0.30)")
    if lua_blocks >= 1:
        axis3 += 0.20
        evidence["axis3"].append(f"Embedded Cheat Engine {{$lua}} automation blocks ({lua_blocks} scripts) (+0.20)")
    if near_alloc_64 >= 1:
        axis3 += 0.35
        evidence["axis3"].append(f"64-bit RIP-relative near-memory codecave allocation ({near_alloc_64} hooks) (+0.35)")
    if sse_fpu >= 1 or "Float" in var_types or "Double" in var_types:
        axis3 += 0.15
        evidence["axis3"].append("Floating-point / SSE state manipulation (+0.15)")

    axis3 = round(min(2.0, axis3), 2)

    # --- AXIS 4: Binary Protection, JIT & Obfuscation (0.0 - 2.5) ---
    axis4 = 0.0
    if any(k in low_all for k in ["vmprotect", "themida", "arxan", "vmp0"]):
        axis4 = 2.0
        evidence["axis4"].append("Commercial virtualizer / integrity guard target (2.0)")
    elif aob_count > 0 and near_alloc_64 > 0 and "aobscan(" in active_scripts.lower():
        # JIT dynamic code scanning without module base (raw JIT heap pages)
        axis4 = 0.55
        evidence["axis4"].append("Raw JIT heap AOB scanning (moduleless dynamic CLR/Mono JIT pages) (0.55)")
    elif re.search(r"\b(rol|ror|shl|shr|cmov\w+)\b", all_scripts, re.I):
        axis4 = 0.35
        evidence["axis4"].append("Bitwise / conditional-move (`cmov`) state logic in target (0.35)")
    else:
        evidence["axis4"].append("Unobfuscated target binary (0.0)")

    # --- AXIS 5: Privilege & Boundary (0.0 - 1.5) ---
    axis5 = 0.0
    if any(k in low_all for k in ["kernel", "dbk32", "dbvm", "ultimap", "cr3"]):
        axis5 = 1.2
        evidence["axis5"].append("Kernel-mode DBVM / Ultimap hardware tracing (1.2)")
    else:
        evidence["axis5"].append("Ring-3 User-Mode Cheat Engine table (0.0)")

    total = round(min(10.0, max(0.5, axis1 + axis2 + axis3 + axis4 + axis5)), 1)
    tier_code, tier_title = score_to_tier(total)

    return {
        "filename": filename,
        "artifact_type": "Cheat Engine Table (.CT)",
        "axes": {
            "axis1_arch_symbols": round(axis1, 2),
            "axis2_memory_indirection": round(axis2, 2),
            "axis3_code_complexity": round(axis3, 2),
            "axis4_protection": round(axis4, 2),
            "axis5_privilege_boundary": round(axis5, 2),
        },
        "metrics": {
            "aob_injections": aob_count,
            "codecave_allocs": alloc_count,
            "max_pointer_depth": max_ptr_depth,
            "pointer_chains": ptr_chains_count,
            "max_struct_offset": f"0x{max_struct_disp:X}",
            "lua_scripts": lua_blocks,
        },
        "evidence": evidence,
        "computed_difficulty": total,
        "assigned_tier": tier_code,
        "tier_title": tier_title,
    }


def analyze_source_or_script(text: str, filename: str, ext: str) -> dict:
    """Analyze .cpp/.c/.hpp/.cs/.py RE tools, trainers, DLLs, and CTF solvers."""
    # Strip multi-line docstrings/comments first, then single-line comments
    code_only = re.sub(r"/\*[\s\S]*?\*/|\"\"\"[\s\S]*?\"\"\"", "", text)
    code_only = re.sub(r"//[^\n]*|#[^\n]*", "", code_only)
    low = code_only.lower()
    evidence = {"axis1": [], "axis2": [], "axis3": [], "axis4": [], "axis5": []}

    # --- AXIS 1: Architecture & Runtime ---
    axis1 = 0.5
    if re.search(r"remill|mcsema|sleigh|llvm::|irbuilder", low):
        axis1 = 2.0
        evidence["axis1"].append("Compiler IR / LLVM / Ghidra SLEIGH architecture specification (2.0)")
    elif re.search(r"jni_getcreatedjavavms|jvmti|cemu|arm64|powerpc", low):
        axis1 = 1.8
        evidence["axis1"].append("Cross-ISA / JVM Native Interface (JNI/JVMTI) target (1.8)")
    elif re.search(r"il2cpp|gameassembly\.dll|lua_state|lual_loadbuffer", low):
        axis1 = 1.6
        evidence["axis1"].append("IL2CPP / Embedded Lua VM runtime internals (1.6)")
    elif re.search(r"gobjects|gnames|uworld|processevent|dumper-7", low):
        axis1 = 1.5
        evidence["axis1"].append("Unreal Engine 4/5 Reflection SDK architecture (1.5)")
    elif re.search(r"dllmain|virtualprotect|vtable|__thiscall|worldtoscreen|calceulerangles|getprocaddress", low):
        axis1 = 1.35
        evidence["axis1"].append("Native x64 C++ Engine ABI / VMT / 3D Projection Math (1.35)")
    elif re.search(r"harmonypatch|bepinex|dnspy|mono", low):
        axis1 = 1.0
        evidence["axis1"].append("Managed .NET / Unity Mono runtime patching (1.0)")
    elif re.search(r"openprocess|readprocessmemory|writeprocessmemory|createtoolhelp32snapshot|e_lfanew|pe_header|inspect_pe", low):
        axis1 = 0.80
        evidence["axis1"].append("Win32 Process & PE Header Binary Structures (0.80)")
    else:
        evidence["axis1"].append("Standard user-mode binary / script target (0.5)")

    # --- AXIS 2: Memory Indirection ---
    axis2 = 0.4
    if re.search(r"\b(cr3|pml4|mmcopyvirtualmemory|eprocess|ept_pointer)\b", low):
        axis2 = 2.0
        evidence["axis2"].append("Physical memory / x64 CR3 Page Table hierarchy walk (2.0)")
    elif re.search(r"vtable|vmt|virtualprotect|getprocaddress|fnspawn", low):
        axis2 = 1.5
        evidence["axis2"].append("In-process function pointer / VMT resolution (`GetProcAddress`/RVA) (1.5)")
    elif re.search(r"viewmatrix|worldtoscreen|clipw|ndcx", low):
        axis2 = 1.45
        evidence["axis2"].append("4x4 View-Projection matrix & homogeneous clip-space vectors (1.45)")
    elif re.search(r"resolvepointerchain|offsets|entitylist|e_lfanew|section_table", low):
        axis2 = 0.90
        evidence["axis2"].append("Multi-level dynamic pointer chain / PE section header walk (0.90)")
    else:
        evidence["axis2"].append("Direct buffer / struct parsing (0.4)")

    # --- AXIS 3: Code & Algorithmic Complexity ---
    axis3 = 0.5
    if re.search(r"z3|solver\s*\(\)|bitvec|angr|claripy|triton|miasm|disassemble_crackme06_vm", low):
        axis3 = 2.0
        evidence["axis3"].append("Automated SMT Theorem Proving (Z3) & Custom VM Disassembler (2.0)")
    elif re.search(r"trampoline|minhook|mh_createhook|imgui|internalworkerthread", low):
        axis3 = 1.85
        evidence["axis3"].append("Internal DLL worker thread & native function invocation hook (1.85)")
    elif re.search(r"worldtoscreen|calceulerangles|atan2", low):
        axis3 = 1.75
        evidence["axis3"].append("3D Linear Algebra, Perspective Divide & Euler Aimbot Trigonometry (1.75)")
    elif re.search(r"aob|shannon_entropy|math\.log2", low):
        axis3 = 1.40
        evidence["axis3"].append("Wildcard AOB pattern scanner, PE parser & Shannon entropy analyzer (1.40)")
    elif re.search(r"readprocessmemory|writeprocessmemory", low):
        axis3 = 0.85
        evidence["axis3"].append("External Win32 RPM/WPM memory trainer loop (0.85)")
    else:
        evidence["axis3"].append("Standard control flow logic (0.5)")

    # --- AXIS 4: Protection, Obfuscation & Crypto ---
    axis4 = 0.0
    if re.search(r"\b(vmprotect|themida|arxan)\b", low):
        axis4 = 2.4
        evidence["axis4"].append("Commercial virtualizer / self-healing checksum analysis (2.4)")
    elif re.search(r"disassemble_crackme06_vm|z3|bitvec|claripy", low):
        axis4 = 2.5
        evidence["axis4"].append("Custom Stack VM Bytecode Disassembly & Z3 Symbolic Constraint Solving (2.5)")
    elif re.search(r"chacha20|blowfish|aes_decrypt|scylla", low):
        axis4 = 1.6
        evidence["axis4"].append("Stream/Block Cipher Crypto or Executable Packer Unpacking (1.6)")
    elif re.search(r"isdebuggerpresent|ntqueryinformationprocess|rdtsc|fnv1a|shannon_entropy", low):
        axis4 = 1.1
        evidence["axis4"].append("Anti-Debugging / Packer Entropy / Integrity Hash detection (1.1)")
    elif re.search(r"rol8|ror8", low):
        axis4 = 0.5
        evidence["axis4"].append("Bitwise XOR / ROL / ROR cipher routines (0.5)")
    else:
        evidence["axis4"].append("Unobfuscated target (0.0)")

    # --- AXIS 5: Privilege & Execution Boundary ---
    axis5 = 0.0
    if re.search(r"iocreatedevice|irp_mj_device_control|mmcopyvirtualmemory|memflow|libvmi", low):
        axis5 = 1.5
        evidence["axis5"].append("Ring-0 Kernel Driver / KVM Hypervisor VMI boundary (1.5)")
    elif re.search(r"disassemble_crackme06_vm", low):
        axis5 = 1.4
        evidence["axis5"].append("Full-spectrum multi-stage CTF & Symbolic Solver Workbench (1.4)")
    elif re.search(r"dllmain|dll_process_attach|disablethreadlibrarycalls", low):
        axis5 = 1.2
        evidence["axis5"].append("In-Process Injected Native DLL (`DLL_PROCESS_ATTACH`) (1.2)")
    elif re.search(r"openprocess|process_all_access", low):
        axis5 = 0.3
        evidence["axis5"].append("Cross-process Win32 Handle (`OpenProcess`) boundary (0.3)")
    else:
        evidence["axis5"].append("Standard Ring-3 utility (0.0)")

    total = round(min(10.0, max(0.5, axis1 + axis2 + axis3 + axis4 + axis5)), 1)
    tier_code, tier_title = score_to_tier(total)

    return {
        "filename": filename,
        "artifact_type": f"Source / Script ({ext})",
        "axes": {
            "axis1_arch_symbols": round(axis1, 2),
            "axis2_memory_indirection": round(axis2, 2),
            "axis3_code_complexity": round(axis3, 2),
            "axis4_protection": round(axis4, 2),
            "axis5_privilege_boundary": round(axis5, 2),
        },
        "evidence": evidence,
        "computed_difficulty": total,
        "assigned_tier": tier_code,
        "tier_title": tier_title,
    }


def grade_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    ext = path.suffix.lower()
    if ext in [".ct", ".cea"] or "<CheatTable" in text:
        return analyze_cheat_table(text, path.name)
    return analyze_source_or_script(text, path.name, ext)


def print_report(res: dict):
    a = res["axes"]
    print("=" * 76)
    print(f"  ARTIFACT  : {res['filename']}  [{res['artifact_type']}]")
    print(f"  TIER RANK : Tier {res['assigned_tier']} ({res['tier_title']})")
    print(f"  DIFFICULTY: {res['computed_difficulty']:.1f} / 10.0")
    print("-" * 76)
    print(f"  [Axis 1] Arch & Runtime     : {a['axis1_arch_symbols']:>4.2f} / 2.00  | {', '.join(res['evidence']['axis1'])}")
    print(f"  [Axis 2] Memory Indirection : {a['axis2_memory_indirection']:>4.2f} / 2.00  | {', '.join(res['evidence']['axis2'])}")
    print(f"  [Axis 3] Code & Hook Logic  : {a['axis3_code_complexity']:>4.2f} / 2.00  | {', '.join(res['evidence']['axis3'])}")
    print(f"  [Axis 4] Protection/Obfus.  : {a['axis4_protection']:>4.2f} / 2.50  | {', '.join(res['evidence']['axis4'])}")
    print(f"  [Axis 5] Privilege Boundary : {a['axis5_privilege_boundary']:>4.2f} / 1.50  | {', '.join(res['evidence']['axis5'])}")
    if "metrics" in res:
        m = res["metrics"]
        print("-" * 76)
        print(
            f"  Detected .CT Metrics: AOB Hooks={m['aob_injections']} | Codecave Allocs={m['codecave_allocs']} | "
            f"Pointer Chains={m['pointer_chains']} (Max Depth={m['max_pointer_depth']}) | "
            f"Max Struct Offset={m['max_struct_offset']} | Lua Blocks={m['lua_scripts']}"
        )
    print("=" * 76)


def main():
    parser = argparse.ArgumentParser(description="Automated RE Artifact Tier & Difficulty Grader")
    parser.add_argument("target", nargs="?", default="Game_Hacking", help="File or directory to analyze")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    p = Path(args.target)
    if not p.exists():
        print(f"[!] Target not found: {p}")
        sys.exit(1)

    results = []
    if p.is_dir():
        exts = {".ct", ".cea", ".cpp", ".hpp", ".c", ".cs", ".py"}
        for child in sorted(p.rglob("*")):
            if child.is_file() and child.suffix.lower() in exts and child.name != "auto_artifact_grader.py":
                results.append(grade_file(child))
    else:
        results.append(grade_file(p))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print_report(r)


if __name__ == "__main__":
    main()
