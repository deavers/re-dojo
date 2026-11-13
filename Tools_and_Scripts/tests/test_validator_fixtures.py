#!/usr/bin/env python3
"""
RE:DOJO map - regression test for Tools_and_Scripts/validate_games.py (stdlib only, no browser).

Builds games.json variants with test-stub hint batches in a temp dir (nothing is written to data/)
and asserts that the validator accepts the positive cases and rejects every negative case with the
expected message: invented hex / versions / AOB bytes / [reg+off], substring and laundered provenance,
my_notes without own notes, protection tiers, restricted-node rules, ambiguous-engine rules,
structural mutations; plus a table-driven test of dojo_schema.derive_engine().

Usage (from anywhere):  python Tools_and_Scripts/tests/test_validator_fixtures.py
Exit code 0 = all expectations met. Output is ASCII-only.
"""
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_tmp = tempfile.TemporaryDirectory(prefix="re-dojo-fixtures-")
sp = Path(_tmp.name)
fx = sp / "fx"
fx.mkdir()
KIND = {1: "nudge", 2: "concept", 3: "near_spoiler"}
def H(lvl, text, src="needs_verification", refs=None):
    return {"level": lvl, "kind": KIND[lvl], "text": text, "source": src, "refs": refs or []}
def three(t1, src="needs_verification", refs=None):
    return {"status": "draft", "hints": [H(1, t1, src, refs), H(2, "b"), H(3, "c")]}
GH = "Game_Hacking/README.md"
LAB02 = "Course_Solutions/Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp"
LAB10 = "Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp"
CM03 = "Crackmes_and_CTF/03_XOR_and_Rol_Cipher/crackme03_xor_rol.cpp"
G199_OK = {"status": "draft", "hints": [
    H(1, "What does an integrity check protect, conceptually?"),
    H(2, "Concept: hashing code pages and comparing to a reference.", "repo_catalog"),
    H(3, "Practice the same idea on your own Lab 10 binary.", "needs_verification", [LAB10])]}
G019_OK = {"status": "draft", "hints": [
    H(1, "Sun lives inside the board object; start from an exact value scan.", "my_notes", [GH + "#1-plants-vs-zombies-goty-tier-e--21--10"]),
    H(2, "Notes: sun counter at +0x5560 of Board.", "my_notes", [GH]),
    H(3, "See the AOB script in the table.", "my_notes", ["Game_Hacking/PvZ.CT"])]}

# name -> (entries, expect_ok, must_contain_in_output)
cases = {
    # --- positives (no false alarms)
    "p00_valid": ({"g019": G019_OK, "g199": G199_OK}, True, ""),
    "p01_ce_version_from_notes": ({"g019": three("Tested with Cheat Engine 7.5 per my notes.", "my_notes", [GH])}, True, ""),
    "p02_reg_offset_from_concept": ({"lab06": three("Filter on the faction field at [rcx+08].")}, True, ""),
    "p03_prose_no_literals": ({"g001": three("Ищи double, а не float: 8 байт. Бонус +20% к скорости — не адрес. Шаг 3 из 3.")}, True, ""),
    "p04_title_version": ({"g088": three("Table targets v98 of the game.")}, True, ""),
    "p05_catalog_hex": ({"g007": three("Catalog says the grid starts at 0x01005340.", "repo_catalog")}, True, ""),
    # --- negatives from the first round
    "n01_invented_hex": ({"g019": {**G019_OK, "hints": [G019_OK["hints"][0], H(2, "Sun counter at +0x5590.", "my_notes", [GH]), G019_OK["hints"][2]]}}, False, "0x5590"),
    "n02_invented_version_3part": ({"g001": three("Works on v2.0.52 of the game.")}, False, "v2.0.52"),
    "n03_my_notes_no_refs": ({"g001": three("a", "my_notes")}, False, "requires at least one ref"),
    "n04_my_notes_foreign_ref": ({"g001": three("a", "my_notes", ["Game_Hacking/PvZ.CT"])}, False, "not one of this node"),
    "n05_restricted_hex": ({"g199": {**G199_OK, "hints": [H(1, "Look for 0xE9 patches."), *G199_OK["hints"][1:]]}}, False, "no concrete addresses"),
    "n06_restricted_l3_no_lab": ({"g199": {**G199_OK, "hints": [*G199_OK["hints"][:2], H(3, "Trace the guard thread.")]}}, False, "level-3 hint must reference"),
    "n07_html": ({"g001": three("<img src=x onerror=alert(1)>")}, False, "no HTML"),
    "n08_wrong_order": ({"g001": {"status": "draft", "hints": [H(2, "b"), H(1, "a"), H(3, "c")]}}, False, "revealed in order"),
    "n10_module_offset": ({"g001": three("Base is Game.exe+1A2B3C")}, False, "Game.exe+1A2B3C"),
    # --- new holes
    "n18_two_part_version": ({"g001": three("Only works on 1.05, not later.")}, False, "'1.05'"),
    "n19_year_version": ({"g003": three("Unity 2019.4 build of the game.")}, False, "'2019.4'"),
    "n20_build_number": ({"g001": three("Use build 98 of the game.")}, False, "build 98"),
    "n21_aob_bytes": ({"g001": three("Signature: 8B 45 08 89 ?? ??")}, False, "8B 45 08 89"),
    "n22_reg_offset": ({"g001": three("Cookies live at [rcx+08].")}, False, "[rcx+08]"),
    "n23_masm_hex": ({"g001": three("Offset is 5560h from base.")}, False, "5560h"),
    "n24_short_plus_offset": ({"g001": three("Value sits at +08 in the object.")}, False, "'+08'"),
    "n25_substring_provenance": ({"g019": three("Notes: counter at 0x55.", "my_notes", [GH])}, False, "'0x55'"),
    "n26_laundered_ref": ({"g001": three("Counter at +0x5560.", "repo_catalog", [GH])}, False, "+0x5560"),
    "n27_laundered_top200": ({"g001": three("Grid at 0x01005340.", "repo_catalog", ["data/top200_popular_games.json"])}, False, "0x01005340"),
    "n28_protection_in_unrestricted": ({"g001": three("Unlike Denuvo games, this one is easy.")}, False, "commercial protection"),
    "n29_restricted_aob": ({"g199": {**G199_OK, "hints": [H(1, "Hooks look like E9 ?? ?? ?? ??"), *G199_OK["hints"][1:]]}}, False, "no concrete addresses"),
    "n30_restricted_reg_offset": ({"g199": {**G199_OK, "hints": [H(1, "Check [rax+10] in the guard."), *G199_OK["hints"][1:]]}}, False, "no concrete addresses"),
    "p06_lab_own_source_my_notes": ({"lab02": three("Bit 7 is 0x80 in my lab.", "my_notes", [LAB02])}, True, ""),
    "n32_lab_ref_earns_my_notes": ({"g001": three("See my lab.", "my_notes", ["Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp"])}, False, "THIS node's own notes"),
    "n33_literal_borrowed_from_lab": ({"g009": three("Power-up flag is 0x80.", "needs_verification", [LAB02])}, False, "'0x80'"),
    "n31_unknown_node": ({"g999": three("a")}, False, "unknown node ids"),
    # --- protection tiers (hard tier: named products, anti-cheat acronyms, license / online-check bypass)
    "n34_license_bypass_in_game": ({"g001": three("Bypass the license check first.")}, False, "commercial protection"),
    "n35_eac_acronym_in_game": ({"g001": three("Games with EAC are off-limits.")}, False, "commercial protection"),
    "n36_product_in_crackme": ({"cm04": three("Unlike Denuvo, this file check is simple.")}, False, "commercial protection"),
    "p07_keygen_in_own_crackme": ({"cm02": three("Write a keygen for your own crackme; patch the license check if stuck.")}, True, ""),
    "p08_offline_sandbox_wording": ({"g006": three("Use the offline sandbox mode for practice.")}, True, ""),
    # --- g176 / g177: restricted, conceptual only, practice redirected to own labs
    "p09_g176_conceptual": ({"g176": {"status": "draft", "hints": [
        H(1, "Why would a publisher encrypt IL2CPP metadata at all?"),
        H(2, "Concept: the metadata file maps names to code; encrypting it hides that map.", "repo_catalog"),
        H(3, "Practice string decryption on your own CM 03 cipher binary.", "needs_verification", [CM03])]}}, True, ""),
    "n37_g176_hex": ({"g176": {"status": "draft", "hints": [
        H(1, "The header key sits at 0x10."), H(2, "b"), H(3, "Use CM 03.", "needs_verification", [CM03])]}}, False, "no concrete addresses"),
    "n38_g177_l3_not_own_lab": ({"g177": {"status": "draft", "hints": [
        H(1, "a"), H(2, "b"), H(3, "Dump it with a public tool.")]}}, False, "level-3 hint must reference"),
}

def run(args):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=ROOT)
    return r.returncode, (r.stdout + r.stderr).strip()

bad = 0
for name, (entries, expect_ok, needle) in cases.items():
    d = fx / name; d.mkdir(exist_ok=True)
    for f in d.glob("*.json"): f.unlink()
    (d / "batch_test.json").write_text(json.dumps({"batch": 0, "entries": entries}, ensure_ascii=False), encoding="utf-8")
    out = sp / f"{name}.games.json"
    rc, o = run(["Tools_and_Scripts/build_games_json.py", "--hints-dir", str(d), "--out", str(out)])
    if rc == 0:
        rc, o = run(["Tools_and_Scripts/validate_games.py", "--file", str(out)])
    ok = (rc == 0) == expect_ok and (not needle or needle in o)
    bad += not ok
    first = next((l for l in o.splitlines() if "ERROR" in l), o.splitlines()[-1])
    print(f"{'PASS' if ok else 'FAIL'} {name}: rc={rc} | {first[:150]}".encode("ascii", "backslashreplace").decode())

base = json.loads((ROOT / "data" / "games.json").read_text(encoding="utf-8"))
muts = {
    "m11_restricted_no_redirect": (lambda d: d["games"][198]["safety"].update(redirect_labs=[]), "redirect_labs"),
    "m12_protection_not_restricted": (lambda d: d["games"][198].update(safety={"restricted": False}), "commercial protection"),
    "m13_bad_difficulty": (lambda d: d["games"][0].update(difficulty=4), "difficulty must equal"),
    "m14_star_in_title": (lambda d: d["games"][1].update(title=d["games"][1]["title"] + " \u2b50"), "star/check"),
    "m15_missing_note_file": (lambda d: d["games"][18]["notes"].append({"path": "Game_Hacking/nope.CT", "kind": "cheat_table"}), "does not exist"),
    "m16_abs_path": (lambda d: d["games"][18]["notes"].append({"path": "C:/x/y.CT", "kind": "cheat_table"}), "repo-relative"),
    "m17_my_notes_claim_without_notes": (lambda d: d["games"][0]["techniques"].append({"id": "aob_injection", "source": "my_notes"}), "claims my_notes"),
    # --- ambiguous engine: nothing may come from the engine string
    "m18_ambiguous_derived_technique": (lambda d: d["games"][1]["techniques"].append({"id": "mono_dissect", "source": "derived"}), "must not be derived from the engine"),
    "m19_ambiguous_engine_keyword": (lambda d: d["games"][5]["techniques"].append({"id": "il2cpp_dump", "source": "repo_catalog"}), "not backed by what_to_find"),
    "m20_family_differs_from_rule": (lambda d: d["games"][1].update(engine_family="unity_mono"), "engine derivation differs"),
    "m21_ambiguous_but_status_known": (lambda d: d["games"][1].update(engine_derivation={"status": "known"}), "'ambiguous' <=>"),
    "m22_excluded_tool_present": (lambda d: d["games"][175]["tools"].append({"id": "il2cppdumper", "source": "derived"}), "excluded by safety.exclude_items"),
    "m23_g176_not_restricted": (lambda d: d["games"][175].update(safety={"restricted": False}), "commercial protection"),
}
for name, (f, needle) in muts.items():
    d = copy.deepcopy(base); f(d); out = sp / f"{name}.games.json"
    out.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    rc, o = run(["Tools_and_Scripts/validate_games.py", "--file", str(out)])
    ok = rc == 1 and needle in o
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'} {name}: rc={rc}")

# --- engine classifier, table-driven (pure strings, independent of the catalog)
sys.path.insert(0, str(ROOT / "Tools_and_Scripts"))
import dojo_schema as S  # noqa: E402
ENGINE_TABLE = [
    # (engine string, expected family, expected status)
    ("Unity / ActionScript Wrapper", "ambiguous", "unknown"),           # wrapper + Unity without backend
    ("Unity / PopCap Hybrid", "ambiguous", "unknown"),
    ("JS / Electron Wrapper (x64)", "ambiguous", "unknown"),
    ("Unity IL2CPP / Mono", "ambiguous", "unknown"),                    # both backends named
    ("Unity Engine (x86/x64)", "ambiguous", "unknown"),                 # no backend
    ("Playdead Custom C++/C# Engine", "ambiguous", "unknown"),          # C++/C# without a named runtime
    ("GameMaker Studio & Unity Engine", "ambiguous", "unknown"),        # two games, different engines
    ("Unreal Engine 4 & Unity IL2CPP", "ambiguous", "unknown"),
    ("Modified Unity IL2CPP (Custom Metadata)", "ambiguous", "unknown"),
    ("Unity IL2CPP + Custom Metadata Encryption", "ambiguous", "unknown"),
    ("Unreal Engine 4 & Unreal Engine 5 (x64)", "unreal_5", "known"),   # same techniques -> not ambiguous
    ("PAIN Engine (x86 C++ & Lua)", "lua_hybrid", "known"),             # '&' inside parentheses
    ("Diesel Engine 2.0 (C++ & LuaJIT)", "lua_hybrid", "known"),
    ("Supergiant Custom C++ & Lua 5.2 Engine (x64)", "lua_hybrid", "known"),  # part without a family adds no candidate
    ("Unity Engine Mono (C#)", "unity_mono", "known"),                  # C# inside Unity is just Unity
    ("Unity IL2CPP (x64 Native Assembly)", "unity_il2cpp", "known"),
    (".NET / MonoGame (x64 C#)", "dotnet_xna", "known"),
    ("Modified Unreal Engine 2.5 (x64)", "unreal_2", "known"),          # bare 'Modified' does not fire
    ("Unreal Engine 3 (Modified x64)", "unreal_3", "known"),
    ("Custom 2D C++ Engines (x86)", "custom", "known"),                 # bare 'Custom' does not fire
    ("Custom Win32 OpenGL C++ (x86)", "native_win32", "known"),
]
for eng, fam, status in ENGINE_TABLE:
    r = S.derive_engine(eng)
    ok = (r["family"], r["status"]) == (fam, status)
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'} engine '{eng}' -> {r['family']}/{r['status']} (expected {fam}/{status})".encode("ascii", "backslashreplace").decode())

total = len(cases) + len(muts) + len(ENGINE_TABLE)
print(f"\n{total - bad}/{total} fixture expectations met")
_tmp.cleanup()
sys.exit(1 if bad else 0)
