# ⚔️ Course Solutions & Progressive Game Hacking Academy (`Labs 01` → `10`)

Welcome to the **Hands-On Game Hacking & Memory Architecture Academy**!  
Instead of jumping blindly into massive 100 GB commercial games, this directory provides **10 custom-engineered, interactive C++ RPG Targets** that simulate real game engine architectures.

### 🧠 Philosophy: Cumulative Step-by-Step Progression
Every lab is designed around **Progressive Mastery**:
1. **No Sudden Walls:** Each lab introduces **one new reverse engineering concept** while actively requiring the skills you mastered in the previous lab.
2. **Two Play Modes in Every Binary:**
   * 🟢 **Apprentice Mode (Guided):** Displays memory addresses and structural hints on-screen so you can verify your scans in Cheat Engine, ReClass.NET, or x64dbg.
   * 🔴 **Hardcore Mode (Blind RE):** Hides all memory addresses and internal state, simulating a real black-box commercial game binary.
3. **100% Legal & Safe Offline Sandbox:** You have full C++ source code, PDB debug symbols (optional), and clean binaries to practice external trainers, AOB scripts, DLL injection, and anti-tamper bypasses safely.

---

## 🗺️ Progressive Curriculum Overview

| Lab | RPG Tier | Difficulty | Target Source & Binary | Skill Used from Previous Lab | 🆕 New Concept Unlocked |
| :---: | :---: | :---: | :--- | :--- | :--- |
| **01** | `Tier F-` | `0.1 / 10` | [`Lab01_Static_Scalars`](./Lab01_Static_Scalars/lab01_static_scalars.cpp) | *Starting Point (Zero Experience)* | Exact 4-Byte integer scans, memory addresses, & value freezing in Cheat Engine |
| **02** | `Tier F` | `0.5 / 10` | [`Lab02_Data_Types_and_Bitmasks`](./Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp) | Basic memory scanning | `Float` / `Double` IEEE-754 scans, Unknown Initial Value, & `Byte` Bitmask flags |
| **03** | `Tier E-` | `1.3 / 10` | [`Lab03_2D_Arrays_and_Structures`](./Lab03_2D_Arrays_and_Structures/lab03_grid_minesweeper.cpp) | Data types & byte inspection | Contiguous C structs & 2D grid arrays in Hex Memory Viewer (like `winmine.exe`) |
| **04** | `Tier E` | `1.8 / 10` | [`Lab04_MultiLevel_Pointers`](./Lab04_MultiLevel_Pointers/lab04_pointer_chains.cpp) | Struct offsets in RAM | Dynamic heap allocation (`new`/`delete`) & resolving 3-level pointer chains |
| **05** | `Tier E+` | `2.3 / 10` | [`Lab05_Code_Injection_and_NOP`](./Lab05_Code_Injection_and_NOP/lab05_code_injection.cpp) | Dynamic heap pointers | Hardware Breakpoints (*"What writes"*), `NOP` patching, & Auto Assembler (`alloc`/`jmp`) |
| **06** | `Tier D` | `3.0 / 10` | [`Lab06_Shared_Code_Disambiguation`](./Lab06_Shared_Code_Disambiguation/lab06_shared_code.cpp) | Auto Assembler injection | **Shared Engine Code:** Comparing `this` (`RCX`) / `faction_id` for God Mode + 1-Hit Kill |
| **07** | `Tier C-` | `3.8 / 10` | [`Lab07_ReClass_and_VMT_Hooking`](./Lab07_ReClass_and_VMT_Hooking/lab07_vtable_reclass.cpp) | Class pointers & offsets | C++ Polymorphism, Virtual Method Tables (`vptr` at `0x00`), & **ReClass.NET** |
| **08** | `Tier B-` | `5.0 / 10` | [`Lab08_3D_Math_and_WorldToScreen`](./Lab08_3D_Math_and_WorldToScreen/lab08_3d_w2s_simulator.cpp) | Reconstructed C++ classes | 3D Vectors (`Vec3`), Pitch/Yaw Euler angles, & $4\times 4$ `ViewMatrix` **WorldToScreen** |
| **09** | `Tier B+` | `5.8 / 10` | [`Lab09_Internal_DLL_and_Hooks`](./Lab09_Internal_DLL_and_Hooks/lab09_internal_hook_target.cpp) | External memory & engine structs | **Internal DLL Injection**, calling internal functions by address, & Trampoline Hooking |
| **10** | `Tier A+` | `7.2 / 10` | [`Lab10_Integrity_and_AntiTamper_Boss`](./Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp) | VMT hooks & assembly analysis | **Boss Fight:** Bypassing `.text` CRC32 Integrity Guards, XORed memory, & Anti-Debug |

---

## 🛠️ How to Compile All Labs

From the repository root, run the automated build script:
```powershell
.\build_all.bat
```
Or compile any individual lab manually with **MSVC (`cl.exe`)** or **MinGW/Clang (`g++`)**:
```powershell
# Using MSVC Developer Command Prompt:
cl /EHsc /O2 /Zi Course_Solutions\Lab01_Static_Scalars\lab01_static_scalars.cpp /Fe:lab01.exe

# Using g++ / clang++:
g++ -O1 -g Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp -o lab01.exe
```

---

## 📖 Walkthrough Hints & Learning Objectives

<details>
<summary><b>🐣 Lab 01: Static Scalars (Tier F-) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Slay the Slime King (`5,000 HP`) or buy the Dragon Slayer Sword (`99,999 Gold`).
* **Why You Can't Win Normally:** You start with `100 HP`, `10 Arrows`, and `50 Gold`. The Slime King deals `35` damage per turn.
* **Step-by-Step Solution:**
  1. Attach Cheat Engine to `lab01_static_scalars.exe`.
  2. Set Value Type to `4 Bytes` and scan for `50` (your Gold).
  3. Spend or earn gold in-game (`[3] Scavenge for Gold`), then click **Next Scan** with the new value.
  4. Double-click the found address, change its value to `999999`, and buy the Dragon Slayer Sword (`[4]`)!
</details>

<details>
<summary><b>📄 Lab 02: Data Types & Bitmasks (Tier F) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Open the Sanctuary Gate by purifying your `StatusFlags` byte and raising your `Mana` float above `500.0f`.
* **Step-by-Step Solution:**
  1. Scan for `Mana` using Value Type `Float` (Scan Type: `Value between...` or `Decreased value` after casting a spell).
  2. Your `StatusFlags` is a single `Byte` (`uint8_t`) where:
     * Bit 0 (`0x01`) = `POISONED`
     * Bit 1 (`0x02`) = `CURSED`
     * Bit 2 (`0x04`) = `SILENCED`
     * Bit 7 (`0x80` = `128` decimal) = `DIVINE_BLESSING`
  3. Set the status byte to exactly `128` (`0x80`) so all debuffs are `0` and `DIVINE_BLESSING` is `1`!
</details>

<details>
<summary><b>🪵 Lab 03: 2D Grid & Contiguous Structs (Tier E-) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Collect all 3 Ancient Relics (`0x77`) on a $6 \times 6$ Fog-of-War grid without stepping on the 8 hidden Spike Traps (`0x8F`).
* **Step-by-Step Solution:**
  1. Find your Player `X` or `Y` coordinate in Cheat Engine, then press `Ctrl+B` (**Browse this memory region**).
  2. Nearby in memory lies the 36-byte `grid[6][6]` array!
  3. Watch how bytes change to `0x01` (visited) as you move. Locate the 3 cells containing `0x77` (Relics) and either navigate to their `(row, col)` coordinates or overwrite all `0x8F` (Traps) with `0x00`!
</details>

<details>
<summary><b>🔰 Lab 04: Multi-Level Pointers (Tier E) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Survive all 5 Dungeon Floors. Every floor transition frees the old `Hero` struct on the heap and allocates a new one!
* **Step-by-Step Solution:**
  1. Find your `Health` on Floor 1.
  2. Right-click the address $\rightarrow$ *"Find out what accesses this address"* (or use **Pointer Scan for this address**).
  3. Follow the chain back to the green static address `g_WorldManager` (`module.exe + offset` $\rightarrow$ `+0x10` (`Floor*`) $\rightarrow$ `+0x18` (`Hero*`) $\rightarrow$ `+0x08` (`HP`)).
  4. You can also test `Tools_and_Scripts/01_External_Trainer_Template` against this lab!
</details>

<details>
<summary><b>🥉 Lab 05: Code Injection & NOP (Tier E+) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Reach `100,000 EXP` and attack without losing Stamina, even though a per-tick sanity check resets Stamina if it exceeds `MaxStamina (100)`.
* **Step-by-Step Solution:**
  1. Right-click `Stamina` $\rightarrow$ *"Find out what writes to this address"*. Attack once.
  2. Select the `sub [rcx+...], 25` instruction $\rightarrow$ **Show Disassembler** $\rightarrow$ Right-click $\rightarrow$ **Replace with code that does nothing (NOP)**.
  3. Right-click `EXP` $\rightarrow$ *"Find out what writes to this address"*. Open **Tools $\rightarrow$ Auto Assemble $\rightarrow$ Template $\rightarrow$ AOB Injection** and change the `add` instruction to add `50000` per action!
</details>

<details>
<summary><b>🛡️ Lab 06: Shared Code Disambiguation (Tier D) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Defeat the Shadow Dragon (`250,000 HP`). Both your Hero and the Dragon share `CombatEngine::DealDamage(Entity* victim, int dmg)`.
* **Step-by-Step Solution:**
  1. Break on the `sub [rcx+10], edx` instruction inside `DealDamage`.
  2. Right-click the instruction in Cheat Engine's *"What writes"* window $\rightarrow$ *"Find out what addresses this instruction accesses"*.
  3. Open **Structure Dissect** (`Ctrl+D`) on the two `RCX` pointers. Notice offset `+0x08` is `factionId` (`1` = Player, `2` = Dragon Boss)!
  4. Write an Auto Assembler script:
     ```x86asm
     cmp dword ptr [rcx+08], 1
     jne enemy_hit
     xor edx, edx          // Player takes 0 damage!
     jmp code
     enemy_hit:
     mov edx, #999999      // Boss takes 999,999 damage!
     code:
     sub [rcx+10], edx
     ```
</details>

<details>
<summary><b>🔮 Lab 07: ReClass.NET & VMT Hooking (Tier C-) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Unlock the Grandmaster Vault by reconstructing the polymorphic `Character` class and hijacking its Virtual Method Table (`vptr`).
* **Step-by-Step Solution:**
  1. Open the `Character` instance address in **ReClass.NET** (or CE Structure Dissect).
  2. Offset `0x00` is the `vptr` pointing to an array of 4 virtual function pointers in `.rdata`.
  3. Look at the class's virtual table or search for the unused `AdminCharacter` vtable / `SecretAdminOverride` function in Ghidra, and overwrite the 4th VMT entry (`IsAuthorizedAdmin()`) or patch its return value (`mov al, 1; ret`)!
</details>

<details>
<summary><b>⚔️ Lab 08: 3D Math & WorldToScreen Simulator (Tier B-) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Calculate the exact Pitch/Yaw aim angles and 2D screen coordinates `(ScreenX, ScreenY)` of 4 cloaked 3D Phantom drones.
* **Step-by-Step Solution:**
  1. Inspect `g_Camera` (`Vec3 pos`, `float pitch`, `float yaw`, `float viewProjMatrix[16]`) and `g_Phantoms[4]` (`Vec3 worldPos`).
  2. Use the formulas in `Tools_and_Scripts/02_3D_Math_and_W2S_Lib/w2s_math_lab.hpp` to compute clip coordinates $W = X \cdot M_{12} + Y \cdot M_{13} + Z \cdot M_{14} + M_{15}$ and NDC coordinates, or write a small external C++ tool to lock `g_Camera.pitch` and `g_Camera.yaw` onto each active Phantom!
</details>

<details>
<summary><b>🔥 Lab 09: Internal DLL & Function Hooking Target (Tier B+) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Call the unreferenced internal function `GrantMythicRelic(int magicCode)` with `0x1337` from an injected DLL.
* **Step-by-Step Solution:**
  1. Compile `Tools_and_Scripts/03_Internal_DLL_Skeleton` into a `.dll`.
  2. Find the RVA offset of `GrantMythicRelic` in Ghidra/x64dbg (or read it from Apprentice Mode), cast `(BaseAddress + RVA)` to a function pointer inside your DLL's worker thread, and invoke it directly!
</details>

<details>
<summary><b>👑 Lab 10: Integrity Guardian & XOR Encryption Boss (Tier A+) — Click for Quest Briefing & Hints</b></summary>

* **Objective:** Defeat the Archon of Silicon (`1,000,000 HP`) while a live `.text` CRC32 checker scans `ApplyCombatDamage` for any `0x90` (`NOP`), `0xE9` (`JMP`), or `0xCC` (`INT3`) modifications, and Player HP is XOR-encrypted in RAM!
* **Step-by-Step Solution:**
  1. Notice that patching instructions inside `ApplyCombatDamage` triggers `[INTEGRITY VIOLATION: .text modified!]`.
  2. **Bypass Method A (VMT Hook):** The Archon and Player call `ApplyCombatDamage` via a function pointer / VMT stored in writable data memory outside `.text`! Swapping that pointer redirects execution without altering a single byte of `.text`.
  3. **Bypass Method B (XOR Key Recovery):** In Ghidra, observe that `real_hp = encrypted_hp ^ xor_cookie`. Find both `encrypted_hp` and `xor_cookie` in `.data` and write `(999999 ^ xor_cookie)` to `encrypted_hp`!
</details>
