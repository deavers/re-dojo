"""
RE:DOJO map - shared schema constants for build_games_json.py / validate_games.py.

Single source of truth for enums and derivation rules. Stdlib only.
Source tags:
  my_notes            -> backed by a file listed in data/notes_index.json      (UI: [из моих заметок])
  repo_catalog        -> keyword literally present in Top 200 catalog text     (UI: [нужна проверка])
  derived             -> inferred by a rule in this file (engine family, etc.)  (UI: [нужна проверка])
  needs_verification  -> hint text that is not backed by notes or catalog      (UI: [нужна проверка])
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rpg_manager import TIERS  # noqa: E402  (tier code, max diff, title, EXP per quest)

SCHEMA_VERSION = 1

TIER_CODES = [t[0] for t in TIERS]
TIER_EXP = {t[0]: t[3] for t in TIERS}
TIER_INDEX = {code: i for i, code in enumerate(TIER_CODES)}

ARCH = ["x86", "x64", "arm", "unknown"]

ENGINE_FAMILIES = [
    "unity_mono", "unity_il2cpp", "unreal_1", "unreal_2", "unreal_3", "unreal_4", "unreal_5",
    "source", "goldsrc", "idtech", "native_win32", "dotnet_xna", "gamemaker", "godot",
    "lua_hybrid", "popcap", "renderware_gamebryo", "js_web", "emulator", "custom",
]

TECHNIQUES = [
    "exact_value_scan", "float_double_scan", "bitmask_flags", "struct_dissect", "pointer_scan",
    "pointer_chain", "aob_injection", "nop_patch", "code_cave", "shared_code_filter",
    "ce_lua_script", "speedhack", "mono_dissect", "dotnet_decompile", "il2cpp_dump",
    "harmony_bepinex", "vmt_hook", "detour_hook", "dll_injection", "sdk_dump", "w2s_math",
    "archive_format", "save_format", "lua_vm_hook", "emulator_memory", "integrity_concept",
]

TOOLS = [
    "cheat_engine", "x64dbg", "ghidra", "reclass_net", "dnspyex", "il2cppdumper", "dumper7",
    "bepinex_harmony", "system_informer", "hex_editor", "python", "z3",
]

ITEM_SOURCES = ["my_notes", "repo_catalog", "derived"]
HINT_SOURCES = ["my_notes", "repo_catalog", "needs_verification"]
HINT_KINDS = {1: "nudge", 2: "concept", 3: "near_spoiler"}
HINT_STATUSES = ["pending", "draft", "reviewed"]
NOTE_KINDS = ["cheat_table", "writeup", "lab_source"]
HINT_MAX_LEN = 400

# ---------------------------------------------------------------------------
# Derivation rules (ordered; first match wins for engine family)
# ---------------------------------------------------------------------------
ENGINE_FAMILY_RULES = [
    (r"IL2CPP", "unity_il2cpp"),
    (r"\bUnity\b", "unity_mono"),
    (r"Unreal Engine 5|\bUE5\b", "unreal_5"),
    (r"Unreal Engine 4|\bUE4\b", "unreal_4"),
    (r"Unreal Engine 3|\bUE3\b", "unreal_3"),
    (r"Unreal Engine 2|\bUE2", "unreal_2"),
    (r"Unreal Engine 1|\bUE1\b", "unreal_1"),
    (r"GoldSrc", "goldsrc"),
    (r"\bSource Engine\b|\bSource 2\b", "source"),
    (r"\bid Tech\b", "idtech"),
    (r"PopCap", "popcap"),
    (r"GameMaker", "gamemaker"),
    (r"\bGodot\b", "godot"),
    (r"RenderWare|Gamebryo|NetImmerse", "renderware_gamebryo"),
    (r"XNA|MonoGame|\bFNA\b|\.NET|\bC#", "dotnet_xna"),
    (r"\bLua(JIT)?\b|LÖVE", "lua_hybrid"),
    (r"Emulat|PCSX|Dolphin|RPCS3|Cemu|Yuzu|Ryujinx|PPSSPP", "emulator"),
    (r"\bJS\b|Electron|HTML5|JavaScript", "js_web"),
    (r"Native Win32|\bWin32\b", "native_win32"),
]

ARCH_RULES = [
    (r"\bx64\b|\bx86[-_]64\b|\bAMD64\b", "x64"),
    (r"\bx86\b(?![-_]64)", "x86"),
    (r"\bARM(64)?\b", "arm"),
]

# Technique keyword -> technique id, matched against catalog text (what_to_find + engine).
# Word boundaries on purpose: 'firecrackers' must not hit 'crack', 'Hook durability' / 'Red Hook' (studio) are not hooks.
CATALOG_TECHNIQUE_RULES = [
    (r"\bpointer[- ]scan", "pointer_scan"),
    (r"\bpointer[- ]chains?\b|\bmulti-level pointers?\b|\bpointers?\b", "pointer_chain"),
    (r"\b(float|floats|double|doubles|IEEE)\b", "float_double_scan"),
    (r"\bbit ?masks?\b|\bbit ?flags?\b|\bbitwise\b", "bitmask_flags"),
    (r"\bstructs?\b|\bstructures?\b|\bclass(es)?\b|\bRTTI\b", "struct_dissect"),
    (r"\bAOB\b|\bsignature scan|\bpattern scan", "aob_injection"),
    (r"\bNOP\b|\bpatch(es|ing)?\b", "nop_patch"),
    (r"\bcode ?caves?\b", "code_cave"),
    (r"\bshared[- ]code\b|\bdisambiguat", "shared_code_filter"),
    (r"\bspeed ?hack", "speedhack"),
    (r"\bMono Dissector\b", "mono_dissect"),
    (r"\bdnSpy(Ex)?\b|\bILSpy\b", "dotnet_decompile"),
    (r"\bIL2CPP\b|\bIl2CppDumper\b", "il2cpp_dump"),
    (r"\bBepInEx\b|\bHarmony\b", "harmony_bepinex"),
    (r"\bVMTs?\b|\bvtables?\b|\bvirtual method", "vmt_hook"),
    (r"(?<!grappling )(?<!grapple )(?<!Red )\bhook(s|ing|ed)?\b(?! durability)|\bdetours?\b|\bMinHook\b|\btrampoline", "detour_hook"),
    (r"\bDLL injection\b|\binternal DLL\b|\binject(ed|ion|ing)?\b", "dll_injection"),
    (r"\bGObjects\b|\bGNames\b|\bFNamePool\b|\bGWorld\b|\bUWorld\b|\bSDK\b|\bDumper-?7\b", "sdk_dump"),
    (r"\bView ?Matrix\b|\bWorldToScreen\b|\bW2S\b|\bEuler\b|\bbone matri", "w2s_math"),
    (r"\.pak\b|\.pck\b|\.wad\b|\.vpk\b|\.bsa\b|\.ba2\b|\barchives?\b|\bunpack(ing)?\b", "archive_format"),
    (r"\bsave[- ]?(state|file|game|data)s?\b|\.sav\b|\.ess\b", "save_format"),
    (r"\blua_State\b|\bLuaJIT\b|\bLua\b", "lua_vm_hook"),
    (r"\bemulat(or|ion|ed)\b|\bbig-endian\b|\bPowerPC\b|\bMIPS\b", "emulator_memory"),
    (r"\bArxan\b|\bintegrity (check|verif|guard|thread)|\bchecksums?\b|\bCRC(32)?\b", "integrity_concept"),  # not 'Hull integrity' (FTL)
    (r"\bcounters?\b|\bgold\b|\bcash\b|\bmoney\b|\bammo\b|\blives\b|\bHP\b|\bhealth\b|\bcoins?\b", "exact_value_scan"),
]

CATALOG_TOOL_RULES = [
    (r"\bCheat Engine\b", "cheat_engine"),
    (r"\bx64dbg\b|\bx32dbg\b", "x64dbg"),
    (r"\bGhidra\b", "ghidra"),
    (r"\bReClass", "reclass_net"),
    (r"\bdnSpy(Ex)?\b", "dnspyex"),
    (r"\bIl2CppDumper\b", "il2cppdumper"),
    (r"\bDumper-?7\b", "dumper7"),
    (r"\bBepInEx\b|\bHarmony\b", "bepinex_harmony"),
    (r"\bSystem Informer\b|\bProcess Hacker\b", "system_informer"),
    (r"\bHxD\b|\bhex editor\b", "hex_editor"),
    (r"\bPython\b", "python"),
    (r"\bZ3\b", "z3"),
]

# Engine family -> techniques that the family implies (source 'derived').
ENGINE_DERIVED_TECHNIQUES = {
    "unity_mono": ["mono_dissect", "dotnet_decompile"],
    "unity_il2cpp": ["il2cpp_dump"],
    "dotnet_xna": ["dotnet_decompile"],
    "unreal_4": ["sdk_dump"],
    "unreal_5": ["sdk_dump"],
    "lua_hybrid": ["lua_vm_hook"],
    "emulator": ["emulator_memory"],
}

# Technique -> tool that the technique implies (source 'derived').
TECHNIQUE_DERIVED_TOOLS = {
    "exact_value_scan": "cheat_engine",
    "float_double_scan": "cheat_engine",
    "pointer_chain": "cheat_engine",
    "pointer_scan": "cheat_engine",
    "aob_injection": "cheat_engine",
    "speedhack": "cheat_engine",
    "struct_dissect": "reclass_net",
    "vmt_hook": "reclass_net",
    "mono_dissect": "cheat_engine",
    "dotnet_decompile": "dnspyex",
    "il2cpp_dump": "il2cppdumper",
    "harmony_bepinex": "bepinex_harmony",
    "sdk_dump": "dumper7",
    "detour_hook": "x64dbg",
    "dll_injection": "x64dbg",
    "integrity_concept": "x64dbg",
    "archive_format": "hex_editor",
    "save_format": "hex_editor",
    "nop_patch": "x64dbg",
}

# Technique -> in-repo lab that teaches it (prerequisite recommendation, source 'derived').
TECHNIQUE_LABS = {
    "exact_value_scan": ["lab01"],
    "float_double_scan": ["lab02"],
    "bitmask_flags": ["lab02"],
    "struct_dissect": ["lab03"],
    "pointer_chain": ["lab04"],
    "pointer_scan": ["lab04"],
    "aob_injection": ["lab05"],
    "nop_patch": ["lab05"],
    "code_cave": ["lab05"],
    "shared_code_filter": ["lab06"],
    "vmt_hook": ["lab07"],
    "sdk_dump": ["lab07"],
    "w2s_math": ["lab08"],
    "dll_injection": ["lab09"],
    "detour_hook": ["lab09"],
    "integrity_concept": ["lab10", "cm05"],
    "archive_format": ["cm04"],
    "save_format": ["cm04"],
}

# Catalog text that touches commercial software protection -> node must be safety.restricted.
PROTECTION_RX = re.compile(
    r"\b(Arxan|Denuvo|SecuROM|SafeDisc|StarForce|VMProtect|Themida|WinLicense|anti-?cheat|EasyAntiCheat|BattlEye|DRM)\b",
    re.IGNORECASE,
)

# Literals that must never be invented in hint text (validator checks provenance).
HEX_RX = re.compile(
    r"\b0x[0-9A-Fa-f]+\b"                         # 0x5560
    r"|\+(?:0x)?[0-9A-Fa-f]{2,}\b(?![%\d])"       # +5560, +08 (but not +20%)
    r"|\b[0-9A-F]{8,16}\b"                        # 01005340, DEADBEEF
    r"|\b(?=[0-9A-Fa-f]*\d)[0-9A-Fa-f]{2,}h\b"    # 5560h (MASM style)
)
MODULE_OFFSET_RX = re.compile(r"\b[\w-]+\.(?:exe|dll)\s*\+\s*(?:0x)?[0-9A-Fa-f]+\b", re.IGNORECASE)
REG_OFFSET_RX = re.compile(r"\[\s*[A-Za-z]{1,3}\d{0,2}\s*[+-]\s*(?:0x)?[0-9A-Fa-f]+h?\s*\]")  # [rcx+08]
AOB_RX = re.compile(r"(?<![0-9A-Za-z?])(?:[0-9A-Fa-f]{2}|\?\?)(?:\s+(?:[0-9A-Fa-f]{2}|\?\??)){2,}(?![0-9A-Za-z?])")
VERSION_RX = re.compile(
    r"\bv\d+(?:\.\d+)*\b"                         # v98, v1.2
    r"|\b\d+\.\d+(?:\.\d+)*\b"                    # 7.5, 1.05, 2019.4, 1.2.3
    r"|\b(?:build|patch|update|version|ver|версия|патч|билд|сборка)\s*#?\s*\d+\b",
    re.IGNORECASE,
)
HTML_RX = re.compile(r"<[^>]*>")


def _aob_matches(text: str) -> list[str]:
    """AOB byte strings: 3+ byte tokens; must contain a digit / wildcard or be upper-case (skips prose)."""
    out = []
    for m in AOB_RX.finditer(text):
        s = m.group(0)
        if re.search(r"\d|\?", s) or s == s.upper():
            out.append(s)
    return out


def byte_literals(text: str) -> set[str]:
    """Concrete addresses, offsets and byte patterns in a text."""
    found = {m.group(0) for rx in (HEX_RX, MODULE_OFFSET_RX, REG_OFFSET_RX) for m in rx.finditer(text)}
    return found | set(_aob_matches(text))


def concrete_literals(text: str) -> set[str]:
    """Everything that must have provenance: addresses, offsets, byte patterns, versions/builds."""
    return byte_literals(text) | {m.group(0) for m in VERSION_RX.finditer(text)}


def literal_in(literal: str, corpus: str) -> bool:
    """Token-boundary match ('0x55' is NOT backed by '0x5560'); whitespace inside AOB strings is flexible."""
    body = r"\s+".join(re.escape(tok) for tok in literal.split())
    # Boundaries only where the literal itself starts/ends with a word char ('+08' inside '[rcx+08]' is fine).
    left = r"(?<![0-9A-Za-z_])" if re.match(r"\w", literal) else ""
    right = r"(?![0-9A-Za-z_])" if re.search(r"\w$", literal) else ""
    return re.search(left + body + right, corpus, re.IGNORECASE) is not None

TITLE_STAR = "⭐"   # in Steam library
TITLE_CHECK = "✅"  # completed by author
