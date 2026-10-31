# 🔐 Crackmes, Keygenmes & Binary Auditing Dojo (`Crackmes 01` → `08`)

Welcome to the **Static Analysis, Keygenning & Binary Auditing Track**!  
While `Course_Solutions/` focuses on dynamic memory manipulation and live game engines, `Crackmes_and_CTF/` trains your **Static Disassembly (Ghidra / IDA Pro / Binary Ninja)**, **Dynamic Debugging (x64dbg / GDB)**, **Cryptographic Reversing**, **VM Bytecode Analysis**, and **Symbolic Execution (`Z3` / `angr`)** skills.

---

## 📈 Step-by-Step Crackme Progression Ladder

Every Crackme builds directly on the previous challenge, introducing **one new binary protection or algorithmic concept** at each step:

| # | RPG Tier | Difficulty | Crackme Challenge | Prerequisite Used | 🆕 New Skill Unlocked |
| :-: | :---: | :---: | :--- | :--- | :--- |
| **01** | `Tier F+` | `0.7 / 10` | [`01_Apprentice_Gate`](./01_Apprentice_Gate/crackme01_strings.cpp) | Basic terminal usage | `.rdata` strings, stack strings, `strcmp`, & `JE`/`JNE` conditional jump patching |
| **02** | `Tier E` | `1.9 / 10` | [`02_Mathematical_Lock`](./02_Mathematical_Lock/crackme02_serial_math.cpp) | Assembly jumps & `CMP` | Reading compiler arithmetic (`IMUL`, `XOR`, `SHR`) in Ghidra & writing a **Keygen** |
| **03** | `Tier D` | `3.1 / 10` | [`03_XOR_and_Rol_Cipher`](./03_XOR_and_Rol_Cipher/crackme03_xor_rol.cpp) | Decompiler pseudocode | Bitwise rotation (`ROL`/`ROR`) + loop inversion to decrypt a hidden flag |
| **04** | `Tier C` | `4.3 / 10` | [`04_Struct_License_File`](./04_Struct_License_File/crackme04_binary_license.cpp) | Bitwise checksums | **Binary File Format RE:** Reversing a packed `.dat` struct & forging `license.dat` |
| **05** | `Tier B` | `5.5 / 10` | [`05_AntiDebug_Sentinel`](./05_AntiDebug_Sentinel/crackme05_antidebug.cpp) | x64dbg breakpoints | Bypassing `IsDebuggerPresent`, `PEB`, `RDTSC` timing, & `0xCC` INT3 scans + FNV-1a |
| **06** | `Tier A` | `6.8 / 10` | [`06_Custom_Stack_VM`](./06_Custom_Stack_VM/crackme06_bytecode_vm.cpp) | Switch tables & structs | **Virtualization:** Reversing a custom 12-opcode Stack VM & writing a disassembler |
| **07** | `Tier S` | `7.8 / 10` | [`07_Control_Flow_Maze_and_MBA`](./07_Control_Flow_Maze_and_MBA/crackme07_cff_mba.cpp) | VM state dispatchers | **O-LLVM Control-Flow Flattening** + simplifying **Mixed Boolean-Arithmetic (MBA)** |
| **08** | `Tier SSS-` | `9.2 / 10` | [`08_Symbolic_Execution_Vault`](./08_Symbolic_Execution_Vault/crackme08_z3_symbolic.cpp) | Algebraic constraints | **Symbolic Execution:** Solving a 16-variable non-linear system with **Z3 / angr** |

---

## 🏆 Rules of the Dojo

1. **Goal #1 (Patching — Bronze Medal 🥉):** Modify the binary's conditional jump (`JNZ` $\rightarrow$ `JZ` or `NOP`) in x64dbg/Ghidra so it prints the victory banner.
2. **Goal #2 (Keygenning / Flag Recovery — Gold Medal 🥇):** Reverse the validation algorithm without modifying a single byte of the executable, and either recover the exact secret flag or write a Python keygen script in `Tools_and_Scripts/`!

---

## 💡 Hints & Spoilers (Click to Expand)

<details>
<summary><b>🔓 Crackme 01 (`Tier F+`): Apprentice Gate</b></summary>

* **Stage A:** Run `strings` or search for All Referenced Text Strings in x64dbg.
* **Stage B:** Notice the second passcode is built character-by-character on the stack (`mov byte ptr [rsp+...], ...`) so it won't show up in basic `strings`! View the function in Ghidra's decompiler or place a breakpoint on the comparison loop.
</details>

<details>
<summary><b>🔓 Crackme 02 (`Tier E`): Mathematical Lock (Keygenme)</b></summary>

* **Format:** Expects `AAAA-BBBB-CCCC` (three 4-digit numbers separated by hyphens).
* **Conditions in Ghidra:**
  1. `A + B == 10000`
  2. `B ^ A == 7744`
  3. `C == (A * 3) % 9973`
* Write a 5-line Python loop for `A in range(1000, 10000)` to find all valid serial keys!
</details>

<details>
<summary><b>🔓 Crackme 03 (`Tier D`): XOR & Bit-Rotation Cipher</b></summary>

* Each input byte `c` at index `i` is transformed by:
  `enc = ROL8(c ^ (0x5A + i * 7), 3)`
* To invert it in Python:
  `c = ROR8(target[i], 3) ^ (0x5A + i * 7)`
</details>

<details>
<summary><b>🔓 Crackme 04 (`Tier C`): Binary License File Format (`license.dat`)</b></summary>

* Instead of reading `stdin`, this program opens `license.dat` in binary mode (`rb`) and reads a 24-byte `#pragma pack(1)` struct:
  * `uint32_t magic` (`0x44454156` = `"DEAV"`)
  * `uint16_t version` (`0x0104`)
  * `uint16_t tierRank` (`0x0777`)
  * `uint64_t userId` (`>= 100000`)
  * `uint32_t featureFlags` (Bit `0x80000000` and `0x0000002A` must be set)
  * `uint32_t checksum` (`magic ^ userId_low ^ featureFlags ^ 0xA5A5A5A5`)
* Write a Python script with `struct.pack("<HHIQII", ...)` to generate `license.dat`!
</details>

<details>
<summary><b>🔓 Crackme 05 (`Tier B`): Anti-Debug Sentinel</b></summary>

* Checks `IsDebuggerPresent()`, manual `RDTSC` instruction cycle delta, and scans `VerifySerialHash()` for `0xCC` (`INT3` software breakpoint).
* **Bypass:** Use **Hardware Breakpoints** (`DR0`–`DR3`) in x64dbg instead of `F2` (`0xCC`), or use **ScyllaHide**!
</details>

<details>
<summary><b>🔓 Crackme 06 (`Tier A`): Custom Stack Virtual Machine</b></summary>

* Inspect `g_VmBytecode[]` and the `switch(opcode)` dispatcher in `ExecuteVM()`.
* Use `Tools_and_Scripts/04_Python_RE_Toolkit/vm_disassembler_and_z3_template.py` to disassemble the bytecode and invert the stack operations!
</details>

<details>
<summary><b>🔓 Crackme 07 (`Tier S`): O-LLVM Control-Flow Flattening & MBA</b></summary>

* Notice the convoluted expression:
  `(x ^ y) + 2 * (x & y)` $\equiv x + y$
  and `(x | y) - (x & ~y)` $\equiv y$!
* Once you collapse the MBA identities on paper, the state machine reduces to a simple 4-integer key check!
</details>

<details>
<summary><b>🔓 Crackme 08 (`Tier SSS-`): Symbolic Execution Vault (Z3 / angr)</b></summary>

* Expects a 16-character ASCII key satisfying 16 coupled linear & XOR equations.
* Open `Tools_and_Scripts/04_Python_RE_Toolkit/vm_disassembler_and_z3_template.py`, copy the constraints into a `z3.Solver()`, and let Z3 solve the exact ASCII key in $< 50\text{ ms}$!
</details>
