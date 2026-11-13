<div align="center">

```text
  ____  _____     ____   ___     _  ___  
 |  _ \| ____|   |  _ \ / _ \   | |/ _ \ 
 | |_) |  _|     | | | | | | |_ | | | | |
 |  _ <| |___ _  | |_| | |_| | || | |_| |
 |_| \_\_____(_) |____/ \___/ \__/ \___/ 
```

# 🥋 RE:DOJO
### *The Interactive Reverse Engineering & Offline Game Hacking RPG Academy*
**From Tier F- (Unranked Novice) to SSS++ (Silicon Demigod)**

[![Live Web RPG](https://img.shields.io/badge/LIVE%20WEB%20RPG-deavers.github.io%2Fre--dojo-blueviolet?style=for-the-badge&logo=googlechrome&logoColor=white)](https://deavers.github.io/re-dojo/)
[![Stars](https://img.shields.io/github/stars/deavers/re-dojo?style=for-the-badge&color=gold)](https://github.com/deavers/re-dojo/stargazers)
[![Forks](https://img.shields.io/github/forks/deavers/re-dojo?style=for-the-badge&color=informational)](https://github.com/deavers/re-dojo/network/members)
[![OPSEC Audited](https://img.shields.io/badge/OPSEC-Strictly%20Offline-success?style=for-the-badge&logo=shield)](./SECURITY.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

<br/>

**[🌐 Launch Interactive Web RPG](https://deavers.github.io/re-dojo/)** • 
**[🧪 C++20 Practice Dojo](./Course_Solutions/)** • 
**[🔥 Top 200 Games Masterlist](#-top-200-most-popular--iconic-games-for-reverse-engineering-001--200)** • 
**[🔬 Auto-Grader](./Tools_and_Scripts/auto_artifact_grader.py)** • 
**[📖 RE Cheat Sheet](https://deavers.github.io/re-dojo/)**

<br/>

</div>

<!-- RPG_CARD_START -->
![Focus](https://img.shields.io/static/v1?label=Focus&message=Offline%20RE%20%26%20Binary%20Auditing&color=blue&style=for-the-badge)
![Current Rank](https://img.shields.io/static/v1?label=Player%20Rank&message=Tier%20F-%20%28Unranked%20Novice%29&color=success&style=for-the-badge)
![Total EXP](https://img.shields.io/static/v1?label=Progress&message=0%20EXP%20%280/142%20Quests%29&color=orange&style=for-the-badge)
![Web RPG](https://img.shields.io/static/v1?label=Live%20Web%20RPG&message=deavers.github.io%2Fre--dojo&color=blueviolet&style=for-the-badge)
![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge)

```text
╔════════════════════════════════════════════════════════════════════════════════════════╗
║  ADVENTURER   : New Challenger             CLASS     : White-Box Novice                ║
║  CURRENT RANK : Tier F- (Unranked Novice)  TOTAL EXP : 0 (0% Quests Done)              ║
║  TIER CLEAR   : [----------------------------]  0 / 29 Tiers Cleared                   ║
║  RANK-UP TRIAL: [---] 0/3 TP in Tier F-   (3 Same-Tier OR 1 Higher-Tier = Rank Up!)    ║
╠════════════════════════════════════════════════════════════════════════════════════════╣
║  PASSIVE SKILL TREE UNLOCKED:                                                          ║
║   [ ] Stage 1: Memory Scanning & Bitmasks    [ ] Stage 2: Pointer Chains & AutoAsm     ║
║   [ ] Stage 3: Shared Code Entity Filters    [ ] Stage 4: .NET / Unity Mono Dissect    ║
║   [ ] Stage 5: C++ VMT & Internal DLL Hooks  [ ] Stage 6: UE4/5 SDK & 3D W2S Math      ║
║   [ ] Stage 7: IL2CPP & Custom Bytecode VMs  [ ] Stage 8: Symbolic Z3, O-LLVM & VMI    ║
╚════════════════════════════════════════════════════════════════════════════════════════╝
```
<!-- RPG_CARD_END -->

> **⚠️ Educational, Ethical & Legal Safe-Harbor Disclaimer ([`SECURITY.md`](./SECURITY.md)):** This repository is an interactive, open-source **Reverse Engineering & Low-Level Systems Architecture RPG Academy** conducted under **17 U.S.C. § 1201(f)** and **EU Directive 2009/24/EC** interoperability & educational research exemptions. All custom C++ practice binaries, Cheat Engine tables (`.CT`), crackmes, and tools target **strictly local, single-player, offline games, open-source software, emulators, and self-written binaries**. There is zero involvement with multiplayer cheats, anti-cheat bypasses, online competitive services, or software piracy. See [`SECURITY.md`](./SECURITY.md) for our full legal policy and Reverse Engineer's OPSEC guide.

---

## 🧭 Quick Navigation (RPG Player's Handbook)

* 🏅 **[Global Hall of Fame Scoreboard & Author Milestones](#-verified-hall-of-fame-scoreboard--author-milestones)**
* ⚙️ **[How This RPG Works (Auto-Updating Card, Breakthrough Level-Up & Web App)](#-how-this-rpg-works-auto-updating-card-breakthrough-level-up--web-app)**
* 🧪 **[In-Repo Interactive Dojo (18 Compilable C++ Labs & Crackmes)](#-in-repo-interactive-dojo-18-custom-c-labs--crackmes)**
* 🎮 **[Personal Steam Target Arsenal (65+ Offline Games)](#-personal-steam-target-arsenal-curated-high-value-games)**
* 🔥 **[Top 200 Most Popular & Iconic Games for RE (#001 – #200 + What to Search)](#-top-200-most-popular--iconic-games-for-reverse-engineering-001--200)**
* 💻 **[Software, File Formats & Binary Auditing Arsenal (45+ Programs)](#-software-file-formats--binary-auditing-arsenal-programs--utilities)**
* 🌳 **[The 6-Stage Reverse Engineering Skill Tree](#-the-6-stage-reverse-engineering-skill-tree)**
* 🏆 **[The Complete 28-Tier RPG Campaign (`F-` $\rightarrow$ `SSS++`)](#-the-complete-28-tier-rpg-campaign-f--sss)**
  * [Act I: Novice Grounds (`F-` to `E--`)](#-act-i-the-novice-grounds-tiers-f--to-e--) | [Act II: 32-Bit Frontier (`E-` to `D+`)](#-act-ii-the-32-bit-frontier-tiers-e--to-d) | [Act III: Managed Realms (`C-` to `C+`)](#-act-iii-bytecode--managed-realms-tiers-c--to-c)
  * [Act IV: AAA Architecture (`B-` to `B+`)](#-act-iv-aaa-engine-architecture-tiers-b--to-b) | [Act V: Modern Reflection (`A-` to `A+`)](#-act-v-modern-reflection--native-transpilation-tiers-a--to-a)
  * [Act VI: DOD, Emulation & VMs (`S-` to `SS+`)](#-act-vi-elite-systems-dod--console-emulation-tiers-s--to-ss) | [Act VII: Pantheon of Silicon (`SSS-` to `SSS++`)](#-act-vii-the-pantheon-of-silicon--symbolic-execution-tiers-sss--to-sss)
* 🛠️ **[Autonomous Community & Custom Targets (`data/custom_targets.json`)](#️-autonomous-community--custom-targets-5-axis-rubric-verified)**

---

## 🏅 Verified Hall of Fame Scoreboard & Author Milestones

To prevent scoreboard spoofing (e.g., someone rating a simple program `SSS++`), the **Verified Hall of Fame** (`data/leaderboard.json`) only counts quests backed by a **verifiable proof artifact in the repository** (`.CT` table, keygen script, or writeup) and scored by our deterministic **5-Axis Technical Rubric Calculator**.

| Rank | Adventurer | RPG Class | Verified Tier | Max Diff | Verified EXP | Proof Artifacts in Repo |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 🥇 **#1** | **`deavers`** *(Author)* | Low-Level Systems Alchemist | **Tier C** *(Adventurer)* | `4.1 / 10` | `6,850 EXP` | [`PvZ.CT`](./Game_Hacking/PvZ.CT), [`UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT), [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT), [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT) |
| 🥈 **#2** | *Your Name Here!* | *Clone, solve quests & submit PR* | `Tier F-` $\rightarrow$ `SSS++` | — | — | *Add your `.CT` / writeup / keygen to [`data/leaderboard.json`](./data/leaderboard.json)* |

### 🎯 `deavers`'s Completed `.CT` Artifacts in [`Game_Hacking/`](./Game_Hacking/)

| Target Binary | Game Title | Engine / Arch | Tier | Difficulty | Status | Artifact |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `PlantsVsZombies.exe` | **Plants vs. Zombies GOTY** | PopCap Framework (x86) | **E+** | `2.1 / 10` | ✅ Done | [`PvZ.CT`](./Game_Hacking/PvZ.CT) |
| `UnrealTournament.exe` | **Unreal Tournament 99** | Unreal Engine 1 (x86) | **D** | `2.9 / 10` | ✅ Done | [`UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT) |
| `isaac-ng.exe` | **The Binding of Isaac: Repentance** | Custom C++20 Engine (x86) | **C-** | `3.8 / 10` | ✅ Done | [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT) |
| `StreetsOfRogue.exe` | **Streets of Rogue (v98)** | Unity Engine Mono (x64) | **C** | `4.1 / 10` | ✅ Done | [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT) |

---

## ⚙️ How This RPG Works (Auto-Updating Card, Breakthrough Level-Up & Web App)

This repository is designed so **anyone can clone it and start playing from zero immediately**—either inside `README.md` or inside our standalone **Web RPG Dashboard (`docs/index.html`)**!

### 1. 🌐 Play in Your Browser (`docs/index.html` / GitHub Pages)
* Open [`docs/index.html`](./docs/index.html) in any browser (or visit the GitHub Pages deployment).
* **100% Isolated Personal Progress:** Your character name, checked quests, EXP, and custom targets are saved privately in your own browser's `localStorage`—you only see **your own progression**, never mixed with anyone else's!

### 2. 📝 Play Locally in `README.md` (Auto-Updating Character Sheet)
1. By default, all quest checkboxes `- [ ]` in `README.md` are unchecked so you can start right away.
2. Whenever you complete a quest, change `- [ ]` to `- [x]` in `README.md` and run:
   ```powershell
   # Windows one-click updater (or set your name with --name "YourHandle")
   .\update_progress.bat --name "YourHandle"

   # Load author deavers's preset profile at any time:
   python Tools_and_Scripts/rpg_manager.py --preset deavers

   # Reset back to a clean New Game template:
   python Tools_and_Scripts/rpg_manager.py --reset
   ```
3. *(Optional)* If you edit `- [x]` directly on GitHub, the included **GitHub Action** (`.github/workflows/update_rpg_card.yml`) automatically recalculates your EXP and updates the Character Card on push!

### 3. ⚡ The Smart "Breakthrough" Level-Up Rule (`3 TP` per Tier)
How do you advance from `Tier F-` to `Tier F`, `Tier E`, and beyond?
* Every Tier requires **3 Tier Points (`3 TP`)** to clear:
  * **Standard Mastery (`+1 TP`):** Every quest completed at your **current Tier ($T$)** gives **`+1 TP`**. Completing **3 quests** at Tier $T$ clears the tier and ranks you up!
  * **Breakthrough Bonus (`+3 TP`):** If you jump ahead and complete **1 quest at a higher Tier ($T+1$ or above)**, it automatically awards **`+3 TP`** to Tier $T$, clearing your current tier immediately!

### 4. 🛡️ Adding New Games & Programs Without Inflation (`5-Axis Rubric`)
Want to add a new game or software target? Edit [`data/custom_targets.json`](./data/custom_targets.json) or run:
```powershell
python Tools_and_Scripts/rpg_manager.py --add-target
```
Instead of letting users type a fake `"SSS++"` rating for an easy game, our engine computes the exact difficulty (`0.1` to `10.0`) from **5 objective technical axes** (*Architecture/Symbols*, *Pointer Indirection*, *Engine/Math Complexity*, *Binary Protection/VM*, and *Privilege Boundary*) and automatically renders the target into `README.md`!

---

## 📂 Repository Architecture & In-Repo Interactive Dojo

```text
re-dojo/
├── 📁 Course_Solutions/       # 10 Progressive C++ Game Hacking & Memory Labs (Tier F- to A+)
├── 📁 Crackmes_and_CTF/       # 8 Progressive Binary Auditing, Keygen & VM Crackmes (Tier F+ to SSS-)
├── 📁 Game_Hacking/           # Real-World Cheat Engine tables (.CT), AOB scripts, & Lua trainers
├── 📁 Tools_and_Scripts/      # C++20 External Trainer, W2S Math, DLL Skeleton, Python AOB/Z3 & RPG Engine
├── 📁 data/                   # Autonomous custom_targets.json (5-Axis Rubric) & leaderboard.json
├── 📁 docs/                   # Interactive GitHub Pages Web RPG App (docs/index.html)
├── 📄 build_all.bat           # One-click MSVC/MinGW compiler for all 18 C++ labs & crackmes
├── 📄 update_progress.bat     # One-click RPG Character Sheet & Checkbox synchronizer
└── 📄 README.md               # Main RPG Player's Handbook & 28-Tier Campaign
```

### 🧪 In-Repo Interactive Dojo (18 Custom C++ Labs & Crackmes)
Compile all 18 practice binaries into `build/bin/` with a single command (`.\build_all.bat`). Every lab builds smoothly on the previous one (`N + 1` learning) and includes **Apprentice Mode** (guided addresses) and **Hardcore Mode** (blind RE):

| ID | Tier | Diff | In-Repo Source & Binary | Prerequisite Used | 🆕 New Concept Unlocked & Practiced |
| :-: | :-: | :-: | :--- | :--- | :--- |
| **Lab 01** | `F-` | `0.1` | [`lab01_static_scalars.cpp`](./Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp) | *Zero Experience* | Exact 4-Byte integer scanning (`HP`, `Gold`, `Arrows`) & freezing memory |
| **Lab 11** | `F` | `0.3` | [`lab11_integer_widths.cpp`](./Course_Solutions/Lab11_Integer_Widths/lab11_integer_widths.cpp) | Exact value scans | Scan widths `1` / `2` / `8` Bytes, signed vs unsigned overflow (`int8` morale, `uint16` arrows, `int64` gold) |
| **Lab 02** | `F` | `0.5` | [`lab02_datatypes_bitmasks.cpp`](./Course_Solutions/Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp) | Exact value scans | IEEE-754 `Float` mana, `Int16` durability, & 8-bit status **Bitmask** (`0x80`) |
| **Lab 12** | `F+` | `0.6` | [`lab12_double_fuzzy.cpp`](./Course_Solutions/Lab12_Double_and_Fuzzy_Scan/lab12_double_fuzzy.cpp) | Float & Int16 scans | Rounded display defeats exact scans: `Unknown initial value` + Increased / Decreased, `double` vs `float` |
| **CM 01** | `F+` | `0.7` | [`crackme01_strings.cpp`](./Crackmes_and_CTF/01_Apprentice_Gate/crackme01_strings.cpp) | Basic terminal I/O | `.rdata` plaintext strings vs runtime **Stack Strings** in Ghidra/x64dbg |
| **Lab 13** | `E--` | `0.8` | [`lab13_strings.cpp`](./Course_Solutions/Lab13_Strings_in_Memory/lab13_strings.cpp) | Fuzzy scans | Strings in memory: UTF-16 (`char16_t`) names, length-prefixed ASCII tags, fixed buffers |
| **CM 09** | `E--` | `0.9` | [`crackme09_mirror.cpp`](./Crackmes_and_CTF/09_Mirror_Gate/crackme09_mirror.cpp) | String recovery | Password stored after a reversible transform (mirror + byte shift); invert the compare loop |
| **Lab 15** | `E-` | `1.1` | [`lab15_fixed_point.cpp`](./Course_Solutions/Lab15_Fixed_Point/lab15_fixed_point.cpp) | Fuzzy scans | 16.16 fixed point: fractions stored as a 4-byte int (`raw / 65536`), Float scans find nothing |
| **Lab 03** | `E-` | `1.3` | [`lab03_grid_minesweeper.cpp`](./Course_Solutions/Lab03_2D_Arrays_and_Structures/lab03_grid_minesweeper.cpp) | Byte inspection | Contiguous C structs & revealing a hidden $6\times 6$ trap grid in Hex View |
| **Lab 16** | `E-` | `1.4` | [`lab16_array_of_structs.cpp`](./Course_Solutions/Lab16_Array_of_Structs/lab16_array_of_structs.cpp) | Struct offsets | Array of structs: entity list, element stride, the same field in every element |
| **Lab 17** | `E` | `1.6` | [`lab17_nested_padding.cpp`](./Course_Solutions/Lab17_Nested_Structs_and_Padding/lab17_nested_padding.cpp) | Array stride | Nested structs, alignment padding before `double` / `uint16`, `#pragma pack(1)` unaligned fields |
| **Lab 04** | `E` | `1.8` | [`lab04_pointer_chains.cpp`](./Course_Solutions/Lab04_MultiLevel_Pointers/lab04_pointer_chains.cpp) | Struct offsets | Dynamic Heap reallocation (`new`/`delete`) & 3-level **Pointer Chains** |
| **CM 02** | `E` | `1.9` | [`crackme02_serial_math.cpp`](./Crackmes_and_CTF/02_Mathematical_Lock/crackme02_serial_math.cpp) | Assembly jumps | Reversing `AAAA-BBBB-CCCC` arithmetic & writing a **Python Keygen** |
| **Lab 18** | `E+` | `2.0` | [`lab18_lazy_singleton.cpp`](./Course_Solutions/Lab18_Lazy_Singleton/lab18_lazy_singleton.cpp) | Pointer chains | Lazy singleton: static pointer stays `NULL` until first use, then a 3-level chain to the inventory |
| **Lab 05** | `E+` | `2.3` | [`lab05_code_injection.cpp`](./Course_Solutions/Lab05_Code_Injection_and_NOP/lab05_code_injection.cpp) | Heap pointers | Hardware Breakpoints (*"What writes"*), `NOP` (`0x90`), & Auto Assembler `alloc` |
| **Lab 06** | `D` | `3.0` | [`lab06_shared_code.cpp`](./Course_Solutions/Lab06_Shared_Code_Disambiguation/lab06_shared_code.cpp) | Auto Assembler | **Shared Engine Code:** Filtering `victim->factionId` (`[rcx+08]`) for 1-Hit Kill |
| **CM 03** | `D` | `3.1` | [`crackme03_xor_rol.cpp`](./Crackmes_and_CTF/03_XOR_and_Rol_Cipher/crackme03_xor_rol.cpp) | Decompiler math | Bitwise rotation (`ROL8`/`ROR8`) + index-dependent `XOR` cipher inversion |
| **Lab 07** | `C-` | `3.8` | [`lab07_vtable_reclass.cpp`](./Course_Solutions/Lab07_ReClass_and_VMT_Hooking/lab07_vtable_reclass.cpp) | Class pointers | C++ Polymorphism, **ReClass.NET**, & hijacking Virtual Method Tables (`vptr`) |
| **CM 04** | `C` | `4.3` | [`crackme04_binary_license.cpp`](./Crackmes_and_CTF/04_Struct_License_File/crackme04_binary_license.cpp) | Bitwise checksums | **File Format RE:** Reversing a packed 24-byte `license.dat` struct (`struct.pack`) |
| **Lab 08** | `B-` | `5.0` | [`lab08_3d_w2s_simulator.cpp`](./Course_Solutions/Lab08_3D_Math_and_WorldToScreen/lab08_3d_w2s_simulator.cpp) | Reconstructed classes | 3D Vectors (`Vec3`), Camera Pitch/Yaw Euler angles (`atan2`), & $4\times 4$ `ViewMatrix` |
| **CM 05** | `B` | `5.5` | [`crackme05_antidebug.cpp`](./Crackmes_and_CTF/05_AntiDebug_Sentinel/crackme05_antidebug.cpp) | x64dbg breakpoints | Bypassing `IsDebuggerPresent`, `PEB`, & `0xCC` (`INT3`) scans + FNV-1a |
| **Lab 09** | `B+` | `5.8` | [`lab09_internal_hook_target.cpp`](./Course_Solutions/Lab09_Internal_DLL_and_Hooks/lab09_internal_hook_target.cpp) | Engine structs | **Internal DLL Injection:** Calling internal engine functions by RVA pointer |
| **CM 06** | `A` | `6.8` | [`crackme06_bytecode_vm.cpp`](./Crackmes_and_CTF/06_Custom_Stack_VM/crackme06_bytecode_vm.cpp) | Switch dispatchers | **Virtualization:** Reversing a custom 12-opcode Stack VM & writing a disassembler |
| **Lab 10** | `A+` | `7.2` | [`lab10_integrity_boss.cpp`](./Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp) | VMT & assembly hooks | **Boss Fight:** Bypassing `.text` CRC32 Integrity Hashing + XOR-encrypted RAM |
| **CM 07** | `S` | `7.8` | [`crackme07_cff_mba.cpp`](./Crackmes_and_CTF/07_Control_Flow_Maze_and_MBA/crackme07_cff_mba.cpp) | VM state loops | **O-LLVM Control-Flow Flattening** + simplifying **Mixed Boolean-Arithmetic (MBA)** |
| **CM 08** | `SSS-` | `9.2` | [`crackme08_z3_symbolic.cpp`](./Crackmes_and_CTF/08_Symbolic_Execution_Vault/crackme08_z3_symbolic.cpp) | Algebraic systems | **Symbolic Execution:** Solving coupled SMT equations with **Z3 Theorem Prover** |


---

## 🎮 Personal Steam Target Arsenal (Curated High-Value Games)

To maximize practical learning and keep motivation at $100\%$, this roadmap filters out trivial shovelware and card-farming fillers, focusing exclusively on **high-value, non-filler offline games** from my personal Steam library (`⭐`) plus iconic industry benchmarks across every engine architecture.

| Game Title | Genre / Category | Engine & Architecture | Tier | Difficulty | Key Reverse Engineering Focus |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Aim Hero** ⭐ | 3D Aim Trainer | Unity Engine (x86/x64) | **E** | `1.8 / 10` | Target sphere 3D coordinates $(X,Y,Z)$, ViewMatrix $4\times 4$, camera Pitch/Yaw Euler angles. |
| **Plants vs. Zombies GOTY** ⭐ | Casual Tower Defense | PopCap Framework (x86 C++) | **E+** | `2.1 / 10` | 🏆 [`PvZ.CT`](./Game_Hacking/PvZ.CT). Multi-level pointer chains, projectile ID swapping, instant recharge. |
| **Castle Crashers** ⭐ | 2D Hack-and-Slash | Custom 2D C++ Engine (x86) | **E+** | `2.2 / 10` | Character XP/stat blocks, gold counter, juggle physics, potion quantities. |
| **Deponia: Complete Journey** ⭐ | 2D Point-and-Click | Visionaire 2D Engine (x86) | **E+** | `2.2 / 10` | Inventory item combination arrays, dialogue bitmasks, puzzle completion flags. |
| **DOOM + DOOM II** ⭐ | Retro 2.5D FPS | id Tech 1 / KEX Engine (x86/x64) | **D-** | `2.5 / 10` | Fixed-point ($16.16$) physics, `mobj_t` actor structs, ammo/armor pointers, sector lighting. |
| **POSTAL (Classic / Redux)** ⭐ | Isometric Shooter | Custom C++ / UE4 (Redux x64) | **D-** | `2.6 / 10` | Isometric coordinate vectors, weapon ammo arrays, execute state machine flags. |
| **Unreal Tournament 99** ⭐ | 3D Arena Shooter | Unreal Engine 1 (x86 C++) | **D** | `2.9 / 10` | 🏆 [`UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT). `UObject`/`APawn` hierarchy, smart AOB filters. |
| **Half-Life 1 / CS 1.6 / CZ** ⭐ | Tactical FPS (Offline Bots) | GoldSrc Engine (x86 C++) | **D** | `3.0 / 10` | `cl_entity_s` array, `cl_enginefunc_t` function table, recoil vectors, bunnyhop ground flags. |
| **POSTAL 2** ⭐ | Open-World Action / FPS | Unreal Engine 2 (x86 C++) | **D** | `3.1 / 10` | `UPawn` inventory linked list, weapon cat-silencer counters, health pipes, NPC aggression AI. |
| **Splinter Cell: Chaos Theory** ⭐ | Tactical Stealth | Lead Engine (UE2.5 x86 C++) | **D+** | `3.3 / 10` | Acoustic noise meter float, light-visibility meter float, night-vision battery, AI detection cones. |
| **Far Cry 1** ⭐ | Open-World Tactical FPS | CryEngine 1 (x86 C++ & Lua) | **D+** | `3.3 / 10` | Binocular tag ranges, stamina/breath floats, weapon recoil vectors, CryEngine entity tables. |
| **SimCity 4 Deluxe / Evil Genius** ⭐ | Management Strategy | Custom 32-bit C++ Engines | **D+** | `3.4 / 10` | Treasury gold/simoleons, minion attention bars, power grid capacity, instant construction hooks. |
| **SPORE** ⭐ | Evolution Sandbox RPG | Maxis Custom C++ (x86) | **D+** | `3.5 / 10` | Creature Editor complexity limit bypass, stage DNA pools, spaceship energy/cargo holds. |
| **LEGO Star Wars / Batman / LOTR** ⭐ | Action Adventure | TT Games Nu2x Engine (x86/x64) | **D+** | `3.5 / 10` | True Jedi stud meter thresholds, 64-bit stud counters, Red Brick multiplier bitflags. |
| **UBERMOSH series (Black / Wraith)** ⭐ | Precision Arcade Slicer | GameMaker Studio (x86) | **C-** | `3.7 / 10` | Bullet-cutting reflection window frames, Brain-Power meter lock, countdown timer freeze. |
| **The Binding of Isaac: Repentance** ⭐ | 2D Action Roguelike | Custom C++20 + Lua 5.3 (x86) | **C-** | `3.8 / 10` | 🏆 [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT). `Entity_Player` struct, heart bitmasks, room-transition stat lock. |
| **Geometry Dash** ⭐ | Precision Rhythm Platformer | Cocos2d-x C++ (x86/x64) | **C-** | `3.8 / 10` | Reversing `PlayLayer::destroyPlayer` (noclip), `PlayerObject` gravity/speed floats, Cocos2d nodes. |
| **Chasm & Secrets of Grindea** ⭐ | Metroidvania / Action RPG | Custom C# / XNA (.NET) | **C-** | `3.8 / 10` | Procedural map room reveal bitmasks, perfect parry window timers, drop rate multiplier tables. |
| **Barony** ⭐ | 3D First-Person Roguelike | Custom C++ Voxel Engine | **C-** | `3.9 / 10` | Character stat blocks (`HP`, `MP`, `DEX`), cursed item identification flags, hunger timers. |
| **Streets of Rogue (v98)** ⭐ | Roguelike Stealth/Action | Unity Engine Mono (x64) | **C** | `4.1 / 10` | 🏆 [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT). Mono Dissector, `Agent`/`Stat` classes, EXP hooks. |
| **Punch Club 1 & 2** ⭐ | Fighter Management RPG | Unity Engine Mono (Lazy Bear) | **C** | `4.1 / 10` | Decompiling in **dnSpyEx**, daily stat decay bypass, locking Energy/Hunger/Mood bars. |
| **Graveyard Keeper** ⭐ | Cemetery Sim / RPG | Unity Engine Mono (Lazy Bear) | **C** | `4.2 / 10` | `WorldGameObject` / `PlayerComponent`, Red/Green/Blue tech points, corpse white skulls. |
| **Enter the Gungeon & Broforce** ⭐ | Bullet-Hell / Action | Unity Engine Mono (x86/x64) | **C** | `4.2 / 10` | `PlayerController` & `HealthHaver`, infinite Blanks/airstrikes, dodge-roll i-frame duration. |
| **Kingdom: Two Crowns & Moonlighter** ⭐ | Strategy / Action RPG | Unity Engine Mono (x86/x64) | **C** | `4.3 / 10` | Coin pouch (`Wallet`), steed stamina, shop item customer price satisfaction thresholds. |
| **Slime Rancher 1 & Poly Bridge** ⭐ | Sandbox / Physics Puzzle | Unity Engine Mono (x64) | **C** | `4.3 / 10` | Vacpack slot capacity, jetpack energy, hydraulic joint stress tensors (`unbreakable joints`). |
| **Stardew Valley & Terraria** ⭐ | Farming / Survival Sandbox | .NET MonoGame & C# XNA/FNA | **C** | `4.5 / 10` | JIT signature scanning for `Terraria.Player::Update`, stamina/luck floats, wing flight time. |
| **Lethal Company & Unturned** ⭐ | Horror / Zombie Sandbox | Unity Mono (x64) | **C+** | `4.6 / 10` | Custom **BepInEx + Harmony** C# plugin (`PlayerControllerB`), `SDG.Unturned` recoil/stamina. |
| **Subnautica: Below Zero** ⭐ | Underwater Survival | Unity Engine (x64) | **C+** | `4.7 / 10` | `OxygenManager`, `LiveMixin` health component, body temperature floats, Seatruck depth limits. |
| **Skyrim Special Edition** ⭐ | Open-World Action RPG | Creation Engine (x64 C++) | **B-** | `5.0 / 10` | `PlayerCharacter` singleton, `ActorValueOwner` VMT, Papyrus VM hooks, SKSE Address Library. |
| **Mount & Blade: Warband / WF&S** ⭐ | Medieval Warfare / Sandbox | TaleWorlds C++ Engine (x86) | **B-** | `5.0 / 10` | Party size limits, renown/morale pointers, troop XP tables, agent horse/combat speed. |
| **Dragon Age: Origins & II** ⭐ | Party Tactical RPG | BioWare Eclipse & Lycium (x86) | **B-** | `5.1 / 10` | Party stat arrays (`Strength`, `Willpower`), spell cooldown timers, companion approval offsets. |
| **Far Cry 2 & Xenus 2: White Gold** ⭐ | Open-World FPS / RPG | Dunia Engine & Vital Engine ZL | **B-** | `5.1 / 10` | Weapon degradation/jamming counters, malaria timers, RPG perk bitflags, faction reputation. |
| **Half-Life 2 & CS: Source & GMod** ⭐ | Physics FPS / Sandbox | Source Engine (`client.dll`) | **B** | `5.4 / 10` | Netvars dumping (`ClientClass` linked list), `CreateMove` VMT hooking, bone matrix `[3][4]`. |
| **Spec Ops: The Line & Story About My Uncle** ⭐ | TPS / Grapple Platformer | Unreal Engine 3 (x86 C++) | **B** | `5.5 / 10` | UE3 `GObjects` & `GNames` scanning, grapple impulse velocity vectors, squad ammo pointers. |
| **Injustice: Gods Among Us** ⭐ | 2.5D Fighting Game | Modified Unreal Engine 3 (x86) | **B** | `5.6 / 10` | Combat hitbox/hurtbox bounding boxes, Super Meter gauge lock, frame data recovery. |
| **Euro Truck Simulator 2** ⭐ | Heavy Vehicle Simulator | SCS Prism3D Engine (x64 C++) | **B+** | `5.8 / 10` | SCS Telemetry SDK shared memory (`scs-telemetry.dll`), speed limiter removal, economy structs. |
| **Assetto Corsa & GRID 2** ⭐ | Motorsport Physics Sim | Kunos Custom C++ / EGO 3.0 | **B+** | `5.8 / 10` | Live physics shared memory (`acpmf_physics`), tire temperature/grip multipliers, KERS battery. |
| **Grand Theft Auto V Legacy** ⭐ | Open-World Crime Action | RAGE Engine (x64 C++) | **B+** | `5.9 / 10` | `CPedFactory` (`WorldPtr`), `CReplayInterface` entity list, Native Invoker, handling flags. |
| **Just Cause 2 & 3 / Dying Light** ⭐ | Sandbox / Parkour Action | Avalanche 3.0 & Chrome Engine 6 | **B+** | `6.0 / 10` | Grappling hook tensile strength, wingsuit boost, parkour stamina, weapon durability. |
| **Metro 2033 / Exodus & HITMAN 2** ⭐ | Survival FPS / Stealth Sim | 4A Engine & IO Glacier 2 (x64) | **B+** | `6.1 / 10` | Gas mask filter timers, `ZHitman5` / `ZActor` RTTI classes, AI suspicion timers, Silent Assassin. |
| **KovaaK's & Escape the Backrooms** ⭐ | 3D Aim / Liminal Survival | Unreal Engine 4 (x64 C++) | **A-** | `6.2 / 10` | Dumping UE4 SDK with **Dumper-7**, `UWorld` $\rightarrow$ `Actors` traversal, `FNamePool` entity ESP. |
| **Manor Lords & Palworld & PEAK** ⭐ | Strategy / Creature Survival | Unreal Engine 4 & 5 (x64 C++) | **A-** | `6.3 / 10` | Regional wealth, `GWorld` traversal, Pal capture rate formulas, climbing grip stamina. |
| **Aimlabs & Slime Rancher 2** ⭐ | 3D Aim / IL2CPP Sandbox | Unity IL2CPP (x64 Assembly) | **A** | `6.6 / 10` | Running **Il2CppDumper**, analyzing stripped native x64 camera matrices & MinHook detours. |
| **PAYDAY 2 & Don't Starve Together** ⭐ | Heist / Survival Sandbox | Diesel 2.0 LuaJIT & Klei Lua VM | **A+** | `7.0 / 10` | Reversing **SuperBLT** C++ bridge, hooking `lua_State*` / `luaL_loadbuffer`, `ThePlayer` structs. |
| **Civilization VI & SAO: Hollow Realization** ⭐ | Grand Strategy / JRPG | Firaxis LORE & PhyreEngine (x64) | **A+** | `7.1 / 10` | Fog of War (`MapVisibility`) bitmasks, SP bar locks, Burst Gauge, sword skill cooldowns. |
| **Dragon Age: Inquisition (GOTY)** ⭐ | Action RPG | EA Frostbite 3 Engine (x64) | **A+** | `7.2 / 10` | Navigating Frostbite's `ClientGameContext`, `PlayerManager`, `TypeInfo` class reflection lists. |
| **Lineage 2 Chronicle 2 (Client/Server)** ⭐ | MMORPG Architecture Lab | Modified UE2 + Blowfish Crypto | **SS-** | `8.3 / 10` | Reversing `L2.exe` packet serialization, Blowfish/RSA login exchange, matching server emulator. |
| **osu! (Offline Framework)** ⭐ | Precision Rhythm Game | .NET C# + Mixed-Mode Native | **SS-** | `8.4 / 10` | `.osr` LZMA replay format, cursor trajectory smoothing math, audio offset sync timers. |

---

<!-- TOP100_GAMES_START -->
## 🔥 Top 200 Most Popular & Iconic Games for Reverse Engineering (`#001` – `#200`)

Complete reference guide of the **Top 200 most popular & iconic offline/single-player PC games** (sorted by difficulty from `0.5 / 10` to `9.8 / 10`), detailing each game's **Engine & Architecture**, **RPG Tier**, **Difficulty**, and **What to Search & Reverse (in-memory structs, pointer chains, classes, VMTs, matrices, and functions)**:

| # | Game Title | Engine & Architecture | Tier | Difficulty | 🎯 What to Search & Reverse (Structs, Offsets, Classes & Hooks) |
| :-: | :--- | :--- | :-: | :-: | :--- |
| **001** | **Cookie Clicker** | JS / Electron Wrapper (x64) | **F+** | `0.5 / 10` | IEEE-754 Double (`8 Bytes`) cookie counter (`Game.cookies`), CPS multipliers, plaintext/Base64 save state, and Golden Cookie spawn timers. |
| **002** | **Clicker Heroes ⭐** | Unity / ActionScript Wrapper | **F+** | `0.6 / 10` | Double / BigNumber gold counter, boss HP floats, 30-second boss fight countdown timer, and Cheat Engine Speedhack tick acceleration. |
| **003** | **AdVenture Capitalist** | Unity Engine Mono (x86/x64) | **F+** | `0.7 / 10` | Double cash balance, Angel Investor count, business revenue multiplier floats, and offline profit timer deltas. |
| **004** | **Plague Inc: Evolved** | Unity Engine Mono (x64) | **F+** | `0.9 / 10` | 4-byte integer DNA Points counter, infectivity/severity/lethality floats, and Cure research progress freeze (`0.0f`). |
| **005** | **Plants vs. Zombies: Fusion / Mods** | Unity / PopCap Hybrid | **E--** | `1.1 / 10` | Sun counter, instant seed packet cooldown timer reset, and projectile damage/ID overrides in memory. |
| **006** | **Bloons TD 6 (Offline Sandbox)** | Unity IL2CPP / Mono | **E--** | `1.2 / 10` | In-round Cash (Double/Float), shield/lives counter, tower XP values, and ability cooldown timer freeze. |
| **007** | **Windows Minesweeper (winmine.exe)** | Native Win32 C (x86) | **E-** | `1.3 / 10` | Static 2D minefield byte array at `0x01005340` (`0x8F` = mine, `0x0F` = safe tile), 1-second timer freeze, and direct win-function call. |
| **008** | **3D Pinball: Space Cadet** | Native Win32 C (x86) | **E-** | `1.4 / 10` | 4-byte Score counter, remaining balls (`Balls Left`), plunger spring impulse float, and Tilt penalty flag patch. |
| **009** | **DX-Ball 2 & Ricochet Infinity** | Native Win32 C++ (x86) | **E-** | `1.5 / 10` | Extra lives counter, paddle width float, ball velocity vector, and power-up drop bitflags. |
| **010** | **Chicken Invaders 4 & 5** | Custom Win32 OpenGL C++ (x86) | **E-** | `1.6 / 10` | Weapon overheat gauge float (`0.0f`), Firepower upgrade level, lives, and missile stock counters. |
| **011** | **AssaultCube** | Cube Engine (x86 Open-Source C++) | **E** | `1.7 / 10` | Classic beginner benchmark: static `LocalPlayer` (`0x50F4F4`), `EntityList`, HP/Armor/Ammo, recoil instructions, 4x4 `ViewMatrix`, and Pitch/Yaw angles. |
| **012** | **Aim Hero ⭐** | Unity Engine (x86/x64) | **E** | `1.8 / 10` | Target sphere 3D coordinates `(X, Y, Z)` (Floats), target lifetime timers, camera `ViewMatrix`, and Pitch/Yaw Euler aim angles. |
| **013** | **Worms Armageddon & World Party** | Team17 2D Engine (x86 C++) | **E** | `1.8 / 10` | Worm health array, infinite Banana Bombs / Holy Hand Grenades, wind direction/strength floats, and turn countdown timer. |
| **014** | **CS2D & Soldat (Offline Bots)** | BlitzMax / Custom Delphi 2D | **E** | `1.9 / 10` | 2D player coordinates `(X, Y)`, HP, cash, jetpack fuel float in Soldat, and zero weapon spread/recoil. |
| **015** | **Quake III Arena (ioquake3)** | id Tech 3 (x86/x64 C) | **E** | `1.9 / 10` | `centity_t` & `clientInfo_t` struct arrays, velocity vectors for strafe/bunnyhop physics, and OpenGL `wglSwapBuffers` overlay hook. |
| **016** | **Serious Sam: The First & Second Encounter** | Serious Engine 1 (`Engine.dll` x86) | **E** | `2.0 / 10` | Health, Armor, Cannonball/Serious Bomb ammo counters, movement speed float, and gravity modifiers in `Engine.dll`. |
| **017** | **SuperTuxKart** | Antarctica Engine (C++) | **E** | `2.0 / 10` | Nitro energy reserve float, kart mass/acceleration physics struct, lap counter, and race timer. |
| **018** | **Bejeweled 3 & Feeding Frenzy 2** | PopCap Framework (x86 C++) | **E+** | `2.1 / 10` | Score counter, level timer freeze, and player fish size scale float (`Scale`) in Feeding Frenzy to eat sharks immediately. |
| **019** | **Plants vs. Zombies GOTY ⭐ ✅** | PopCap Framework (x86 C++) | **E+** | `2.1 / 10` | Pointer chain `LawnApp -> Board -> Sun` (`+0x5560` / `+0x5578`), seed slot recharge timers, projectile ID swapping (pea -> cob cannon), and Crazy Dave coins. |
| **020** | **Castle Crashers ⭐** | The Behemoth 2D C++ Engine (x86) | **E+** | `2.2 / 10` | Character stat struct (`XP`, `Level`, `Gold`, `Strength`, `Magic`, `Defense`, `Agility`), sandwich/potion quantities, and aerial juggle gravity. |
| **021** | **Neighbours from Hell 1 & 2** | JoWooD 2D Engine (x86 C++) | **E+** | `2.2 / 10` | Neighbor anger meter percentage, Woody stealth invisibility flag when sharing a room, and inventory item array. |
| **022** | **Peggle Deluxe & Zuma Deluxe** | PopCap Framework (x86 C++) | **E+** | `2.2 / 10` | Ball counter, aim-guide trajectory line length float, rolling ball linked list in Zuma, and frog rotation angle. |
| **023** | **Alien Shooter 1 & 2 / Zombie Shooter** | Sigma Team 2D Isometric C++ (x86) | **E+** | `2.3 / 10` | Cash, HP, Armor, ammo pools, implant durability, and character attribute structs (`Accuracy`, `Speed`, `Strength`). |
| **024** | **Angry Birds Classic (PC)** | Box2D + Lua C++ Wrapper (x86) | **E+** | `2.3 / 10` | Box2D slingshot impulse multiplier, world gravity vector, remaining bird counter, and Lua level unlock tables. |
| **025** | **Braid & Super Meat Boy** | Custom 2D C++ Engines (x86) | **E+** | `2.4 / 10` | Time-rewind ring buffer frames in Braid, and horizontal acceleration / jump velocity vectors in Super Meat Boy. |
| **026** | **Limbo & Inside** | Playdead Custom C++/C# Engine | **E+** | `2.4 / 10` | Player `(X, Y)` world coordinates, gravity/jump vectors, and disabling hazard death trigger callbacks. |
| **027** | **Papers, Please** | OpenFL / NME (x86/x64) | **E+** | `2.4 / 10` | Family savings balance, Citations counter (freeze at `0` to prevent penalties), workday clock timer, and heat/food status flags. |
| **028** | **DOOM (1993) + DOOM II ⭐** | id Tech 1 / KEX Engine (C/C++) | **D-** | `2.5 / 10` | `mobj_t` actor structs, `16.16` fixed-point coordinates & momentum, invulnerability bitflags, and ammo/armor pointers. |
| **029** | **Return to Castle Wolfenstein** | id Tech 3 (`WolfSP.exe` x86 C) | **D-** | `2.5 / 10` | `gentity_t` actor structs, health, armor, stamina float, Venom gun overheat timer, and secret gold bars. |
| **030** | **Duke Nukem 3D (EDuke32)** | Build Engine (C/C++) | **D-** | `2.6 / 10` | Static `sprite[]`, `wall[]`, and `sector[]` arrays, Jetpack fuel timer, Steroids duration, and weapon ammo tables. |
| **031** | **Medal of Honor: Allied Assault** | id Tech 3 + F.A.K.K.2 (x86) | **D-** | `2.6 / 10` | Health, ammo counters, weapon recoil suppression, and reading enemy coordinates from the entity array. |
| **032** | **Painkiller: Black Edition** | PAIN Engine (x86 C++ & Lua) | **D-** | `2.7 / 10` | Soul counter for Demon Morph (`66 Souls`), gold for Black Tarot cards, Stakegun ammo, and Havok ragdoll impulses. |
| **033** | **Wolfenstein 3D & Quake II** | Wolf3D Raycaster & id Tech 2 | **D-** | `2.7 / 10` | 64x64 tile map grid in RAM (secret push-walls), `edict_t` entity structs in Quake II, and QuakeC VM stack. |
| **034** | **Age of Empires II (HD / Definitive)** | Genie Engine (C++) | **D-** | `2.8 / 10` | Player resource float array (`Food`, `Wood`, `Gold`, `Stone`), Population Cap limit, and instant building construction hook. |
| **035** | **Command & Conquer: Red Alert 2 & Generals** | Westwood 2D / SAGE 3D Engine (x86) | **D-** | `2.8 / 10` | Credits balance, base Power grid capacity, Map Shroud (Fog of War) reveal flag, and instant unit production hook. |
| **036** | **StarCraft: Brood War** | Blizzard Storm 2D Engine (x86) | **D-** | `2.8 / 10` | Minerals, Vespene Gas, Psi/Supply cap, `CUnit` doubly-linked entity list, and unit HP/Shield fixed-point values. |
| **037** | **Gothic I & Gothic II: Night of the Raven** | Piranha Bytes ZenGin (`Gothic2.exe` x86) | **D** | `2.9 / 10` | `oCNpc` player class: Learning Points (`LP`), Strength, Dexterity, Mana, Magic Circle level, and Gold ore/coins. |
| **038** | **Unreal Tournament 99 GOTY ⭐ ✅** | Unreal Engine 1 (x86 C++) | **D** | `2.9 / 10` | `UObject -> AActor -> APawn` hierarchy in `Engine.dll`, shared damage instruction filter (Player God Mode + Bot One-Hit Kill). |
| **039** | **Counter-Strike 1.6 (Offline Bots) ⭐** | GoldSrc Engine (x86 C++) | **D** | `3.0 / 10` | Bot bone coordinates, recoil `punchangle` vectors, `$16000` cash, FOV float, and OpenGL `glBegin` model rendering hook. |
| **040** | **Deus Ex (2000 GOTY)** | Unreal Engine 1 (`DeusEx.dll` x86) | **D** | `3.0 / 10` | Bioelectric energy float for augmentations, Skill Points, lockpicks, multitools, weapon accuracy, and credits. |
| **041** | **Half-Life 1 (1998) ⭐** | GoldSrc Engine (`hw.dll` / `client.dll`) | **D** | `3.0 / 10` | `cl_entity_s` entity array, `cl_enginefunc_t` engine pointer table, HEV suit armor, and `FL_ONGROUND` bunnyhop bitflag. |
| **042** | **The Elder Scrolls III: Morrowind** | NetImmerse / Gamebryo (x86 C++) | **D** | `3.0 / 10` | `MACP` player actor struct: Health, Magicka, Fatigue (controls hit/cast success probability!), attributes, and Gold. |
| **043** | **Hitman: Codename 47 / Silent Assassin / Blood Money** | IO Glacier 1 Engine (x86 C++) | **D** | `3.1 / 10` | Agent 47 health, weapon upgrade money balance, suspicion/noise meter, and locking the `Silent Assassin` rating flag. |
| **044** | **Max Payne 1 & Max Payne 2** | MAX-FX Engine (x86 C++) | **D** | `3.1 / 10` | Bullet Time hourglass float, Painkillers counter, projectile velocity vectors, and camera FOV. |
| **045** | **POSTAL 2 ⭐** | Unreal Engine 2 (`Postal2.exe` x86) | **D** | `3.1 / 10` | `UPawn` inventory linked list, cat-silencer counter, health pipes, and NPC aggression AI state flags. |
| **046** | **System Shock 2 & Thief: Deadly Shadows** | Dark Engine / Modified UE2 (x86) | **D** | `3.1 / 10` | Cyber Modules, Psi Points, weapon degradation, Nanites, and the stealth visibility `Light Gem` float in Thief. |
| **047** | **Baldur's Gate I & II (Enhanced Edition)** | Infinity Engine (x86/x64 C++) | **D** | `3.2 / 10` | AD&D 2e character stats (`THAC0`, `Armor Class`, `HP`), spell memorization slots without resting, Gold, and party XP. |
| **048** | **Diablo II (Offline Singleplayer)** | Blizzard Custom 2D/Isometric C++ | **D** | `3.2 / 10` | `UnitAny` (`pPlayerUnit`) struct, fixed-point stats (HP/Mana shifted by `<< 8` bits), gold, stamina, and map seed. |
| **049** | **Fallout 1 & Fallout 2** | Interplay 2D Isometric Engine (x86) | **D** | `3.2 / 10` | Turn-based combat Action Points (`AP`), S.P.E.C.I.A.L. stat block, Skill Points, carry weight limit, and Bottle Caps. |
| **050** | **Warcraft III (Classic Offline)** | Blizzard Storm / JASS VM (C++) | **D** | `3.2 / 10` | Gold, Lumber, Food cap, Hero ability cooldown timers, unit structs in `Game.dll`, and the JASS scripting VM. |
| **051** | **F.E.A.R. (First Encounter Assault Recon)** | LithTech Jupiter EX Engine (x86 C++) | **D+** | `3.3 / 10` | Slow-Mo Reflexes charge float, Medkit/Reflex boosters, armor, and Penetrator / Type-7 particle weapon ammo. |
| **052** | **Far Cry 1 (2004) ⭐** | CryEngine 1 (`CryGame.dll` C++/Lua) | **D+** | `3.3 / 10` | Stamina, sniper breath-hold float, binocular tagging distance limit, weapon recoil vectors, and CryEngine 1 entity tables. |
| **053** | **Splinter Cell: Chaos Theory ⭐** | Lead Engine (Modified UE2.5 x86) | **D+** | `3.3 / 10` | Light visibility meter float (`0.0f` = total darkness), acoustic footstep noise float, night-vision battery, and SC-20K ammo. |
| **054** | **Vampire: The Masquerade – Bloodlines** | Source Engine Early Branch (`vampire.dll`) | **D+** | `3.3 / 10` | Blood Pool reserve, XP points for Disciplines, Humanity/Masquerade counters, cash, and computer hacking bypass. |
| **055** | **GTA III & Bully: Scholarship Edition** | RenderWare / Gamebryo (x86 C++) | **D+** | `3.4 / 10` | `CPed` pool in GTA III; cash, slingshot/firecrackers, Prefect `Trouble Meter`, and curfew clock freeze in Bully. |
| **056** | **GTA: Vice City & San Andreas (Original)** | RenderWare Engine (x86 C++) | **D+** | `3.4 / 10` | Static `CPed` (`0xB6F5F0`) and `CVehicle` pools, weapon slots, Wanted Level (`0–6`), vehicle gravity, and calling `CHud::SetHelpMessage`. |
| **057** | **Mafia: The City of Lost Heaven & Mafia II** | LS3D Engine & Illusion Engine (x86) | **D+** | `3.4 / 10` | Race car damage/timer patch in the iconic 'Fair Play' mission, Tommy Gun ammo, cash, and speed limiter removal. |
| **058** | **FlatOut 2 & Burnout Paradise** | Bugbear Engine & Criterion RenderWare | **D+** | `3.5 / 10` | Nitro gauge float, opponent chassis health in demolition derbies, cash, and driver ejection impulse vectors in stunts. |
| **059** | **LEGO Star Wars: The Complete Saga ⭐** | TT Games Nu2x Engine (x86 C++) | **D+** | `3.5 / 10` | 64-bit Studs counter, `True Jedi` meter threshold, and Red Brick score multiplier bitflags (`x2`, `x4`, `x6`, `x8`, `x10`). |
| **060** | **Need for Speed: Most Wanted (2005)** | EA EAGL Engine (x86 C++) | **D+** | `3.5 / 10` | `N2O` nitrous and `Speedbreaker` slow-motion floats, Bounty rating points, cash, and vehicle mass/torque multipliers. |
| **061** | **Prince of Persia: Sands of Time / Warrior Within** | Ubisoft Jade Engine (x86 C++) | **D+** | `3.5 / 10` | Sand Tanks counter (for time rewind), Eye of the Storm slow-motion charges, and Prince / Dahaka health. |
| **062** | **SPORE ⭐** | Maxis Custom C++ Engine (x86) | **D+** | `3.5 / 10` | DNA Points in Creature/Tribe stages, bypassing the `Complexity Meter` limit in the Creature Editor, and Space Stage ship energy. |
| **063** | **Devil May Cry 3 & 4 Special Edition** | MT Framework (x86/x64 C++) | **D+** | `3.6 / 10` | Red Orbs & Proud Souls counters, `Devil Trigger` gauge float, instant `SSS` Style Rank multiplier, and HP. |
| **064** | **Heroes of Might and Magic III (HD/HotA)** | New World Computing C++ (x86) | **D+** | `3.6 / 10` | Hero struct (`Movement Points` on the adventure map, `Mana`, primary stats), 7 kingdom resource array, and creature stack counts. |
| **065** | **Resident Evil 4 (2005 Classic / UHD)** | Capcom Custom C++ Engine (x86) | **D+** | `3.6 / 10` | Pesetas (`PTAS`), Leon & Ashley HP/MaxHP, Attaché Case 2D grid inventory items, and knife durability. |
| **066** | **Star Wars: Knights of the Old Republic (KOTOR)** | BioWare Odyssey Engine (x86 C++) | **D+** | `3.6 / 10` | Hooking the `d20` combat/persuasion RNG roll (always natural 20), Force Points, Light/Dark alignment, and Credits. |
| **067** | **Stronghold Crusader & Warcraft II** | Firefly 2D Isometric C++ (x86) | **D+** | `3.6 / 10` | Treasury Gold, Castle Popularity (`100`), stockpile goods (stone, iron, bread, weapons), and troop population cap. |
| **068** | **The Sims 2 / The Sims 3 (Offline)** | Maxis Custom C++ / Mono Sims3 | **D+** | `3.6 / 10` | Household Simoleons balance, the 6 Sim Motive floats (`Hunger`, `Energy`, `Bladder`, `Fun`, `Social`, `Hygiene`), and Lifetime Happiness. |
| **069** | **Shovel Knight & Katana ZERO** | Yacht Club C++ & GameMaker Studio | **C-** | `3.7 / 10` | Chronos slow-motion battery float in Katana ZERO (`data.win`), and relic Magic / Gold pouches in Shovel Knight. |
| **070** | **Bastion & Transistor** | Supergiant Custom C# / MonoGame | **C-** | `3.8 / 10` | Fragments currency, Spirit tonics, Function `MEM` slot capacity limit in Transistor, and Turn() planning energy. |
| **071** | **FTL: Faster Than Light** | Subset Custom C++ Engine | **C-** | `3.8 / 10` | Ship `Hull` integrity, `Scrap` currency, Fuel, Missiles, Drone Parts, and reactor power bar allocation across subsystems. |
| **072** | **Geometry Dash ⭐** | Cocos2d-x C++ (`libcocos2d.dll`) | **C-** | `3.8 / 10` | Patching `PlayLayer::destroyPlayer` (Noclip), `PlayerObject` gravity/speed floats, and traversing `CCNode` scene trees. |
| **073** | **Loop Hero & Inscryption** | GameMaker Studio & Unity Engine | **C-** | `3.8 / 10` | Camp resource structs and card deck arrays in Loop Hero (`data.win`), and card Attack/HP & scale teeth in Inscryption. |
| **074** | **The Binding of Isaac: Repentance ⭐ ✅** | Custom C++20 + Lua 5.3 (x86) | **C-** | `3.8 / 10` | `Entity_Player` struct, Red/Soul/Black heart bitmasks, `Tear Delay` fire-rate formula, active item charge, and pedestal item IDs. |
| **075** | **Barony ⭐** | Custom 3D Voxel C++ Engine | **C-** | `3.9 / 10` | `Stat` struct (`HP`, `MP`, `STR`, `DEX`), cursed/blessed item `beatitude` flags, hunger timer, and zero spell mana cost. |
| **076** | **Darkest Dungeon 1** | Red Hook Custom C++ Engine (x64) | **C-** | `3.9 / 10` | Locking hero Stress at `0` (preventing Afflictions/Heart Attacks), Torchlight at `100`, Gold, and Heirloom crests. |
| **077** | **Rogue Legacy 1 & 2** | C# MonoGame (RL1) & Unity Engine (RL2) | **C-** | `3.9 / 10` | Manor upgrade Gold, double-jump/dash runes, Mana pool, and armor `Resolve` weight capacity. |
| **078** | **Spelunky HD & Spelunky 2** | Custom C++ Engine (x86/x64) | **C-** | `3.9 / 10` | Rope & Bomb counters, Ghost spawn timer freeze (`0`), Jetpack/Kapala equipment bitflags, and teleport coordinates. |
| **079** | **Brotato & Halls of Torment** | Godot Engine 3/4 (GDScript / C++) | **C-** | `4.0 / 10` | Unpacking Godot `.pck` archives, Materials currency, primary stats (`Harvesting`, `Luck`, `Attack Speed`, `Armor`), and HP. |
| **080** | **Celeste** | C# XNA / FNA / Monocle Engine | **C-** | `4.0 / 10` | `Player.Dashes` field (infinite mid-air dashes), `Player.Stamina` (infinite wall-climb grip), and sub-pixel velocity vectors. |
| **081** | **Core Keeper & Forager** | Unity Engine & GameMaker Studio | **C-** | `4.0 / 10` | Pickaxe durability, food saturation, and skill points in Core Keeper; infinite energy and coins in Forager. |
| **082** | **Dead Cells** | Heaps.io Engine (Haxe -> HashLink VM) | **C-** | `4.0 / 10` | HashLink VM bytecode (`hlboot.dat`), Cells, Gold, `Brutality`/`Tactics`/`Survival` scroll counts, and skill cooldowns. |
| **083** | **Hotline Miami 1 & 2** | GameMaker / SilverWare C++ | **C-** | `4.0 / 10` | Equipped weapon magazine ammo, `Combo Window` expiration timer freeze, and patching bullet collision checks on the player. |
| **084** | **Undertale & Deltarune** | GameMaker Studio (`data.win` VM) | **C-** | `4.0 / 10` | GameMaker dynamic `double` hash-table variables (`global.hp`, `global.gold`, battle box Soul `(X,Y)` coords) and `data.win` bytecode. |
| **085** | **Blasphemous 1 & 2** | Unity Engine Mono (x64) | **C** | `4.1 / 10` | Tears of Atonement currency, `Fervour` prayer bar, Bile Flask charges, and Penitent One health. |
| **086** | **Ori and the Blind Forest & Will of the Wisps** | Unity Engine (Moon Studios x64) | **C** | `4.1 / 10` | Life & Energy cells, `Spirit Light` currency, Spirit Shard slots, and infinite mid-air jumps/dashes. |
| **087** | **Punch Club 1 & 2 ⭐** | Unity Engine Mono (C#) | **C** | `4.1 / 10` | Decompiling `Assembly-CSharp.dll` in `dnSpyEx`, disabling daily `Stat Decay`, and locking Energy/Hunger/Mood bars. |
| **088** | **Streets of Rogue (v98) ⭐ ✅** | Unity Engine Mono (x64) | **C** | `4.1 / 10` | Cheat Engine Mono Dissector: `Agent`, `InvDatabase`, and `Stat` classes, infinite weapon durability, EXP hook, and trait points. |
| **089** | **Cult of the Lamb** | Unity Engine Mono (x64) | **C** | `4.2 / 10` | Follower `Faith`, Hunger, and Village Hygiene bars, Gold coins, and Crusade Fervour / Tarot card multipliers. |
| **090** | **Disco Elysium** | Unity Engine Mono (x64) | **C** | `4.2 / 10` | Skill Points, `Morale` & `Health` pips, Réal currency, and patching `2d6` skill check rolls to always succeed. |
| **091** | **Enter the Gungeon ⭐** | Unity Engine Mono (x64) | **C** | `4.2 / 10` | `PlayerController` & `HealthHaver` classes, infinite `Blanks`, Keys, Hegemony Credits, zero spread, and dodge-roll i-frames. |
| **092** | **Graveyard Keeper ⭐** | Unity Engine Mono (C#) | **C** | `4.2 / 10` | `WorldGameObject` & `PlayerComponent` classes, infinite Energy, Red/Green/Blue tech points, and corpse `White Skulls` quality. |
| **093** | **Slay the Spire** | Java / LibGDX Framework (JVM) | **C** | `4.2 / 10` | Decompiling `desktop-1.0.jar` (`Jadx`/`Recaf`) or scanning `AbstractPlayer.currentHealth`, combat `EnergyManager`, and Gold. |
| **094** | **Balatro** | LÖVE 2D Framework (LuaJIT) | **C** | `4.3 / 10` | Extracting the ZIP archive appended to `Balatro.exe`, inspecting Lua state tables (`G.GAME.dollars`, `hands_left`, `discards_left`), and Joker multipliers. |
| **095** | **Subnautica (Original)** | Unity Engine Mono (x64) | **C** | `4.3 / 10` | `Oxygen` manager, `LiveMixin` health component, battery/power-cell charge, Cyclops `CrushDamage` depth, and blueprint unlocks. |
| **096** | **The Forest** | Unity Engine Mono (x64) | **C** | `4.3 / 10` | `LocalPlayer -> Stats` class: Energy, Stamina, Fullness, Thirst, Creepy Armor, and instant blueprint construction. |
| **097** | **Cuphead** | Unity Engine Mono (x64) | **C** | `4.4 / 10` | `PlayerStatsManager` (HP & `SuperMeter` Ex-cards), `LevelPlayerWeaponManager` damage multipliers, and Gold coins. |
| **098** | **Hollow Knight** | Unity Engine Mono (x64) | **C** | `4.4 / 10` | `HeroController.instance` & `PlayerData`: infinite Soul (`MPCharge`), `Geo`, `charmSlots` notch capacity, and Shade Cloak cooldown. |
| **099** | **Kerbal Space Program** | Unity Engine Mono (x64) | **C** | `4.4 / 10` | Infinite LiquidFuel/Oxidizer/MonoPropellant in `PartResource`, ElectricCharge, R&D `Science` points, and career Funds. |
| **100** | **Raft & Green Hell** | Unity Engine Mono (x64) | **C** | `4.4 / 10` | Thirst/Hunger & Hook durability in Raft; Macronutrients (Proteins/Fats/Carbs), `Sanity`, and Stamina in Green Hell. |
| **101** | **Cities: Skylines** | Unity Engine Mono (x64) | **C** | `4.5 / 10` | `EconomyManager` treasury balance, eliminating ground/water pollution, and unlocking all 25/81 map tiles. |
| **102** | **Pillars of Eternity & Pathfinder: Wrath of the Righteous** | Unity Engine Mono (x64) | **C** | `4.5 / 10` | Party attribute blocks, per-rest spell casts, Gold, Crusade army morale, and `d20` attack/saving-throw roll hooks. |
| **103** | **Stardew Valley ⭐** | .NET / MonoGame (x64 C#) | **C** | `4.5 / 10` | `StardewValley.Game1.player` singleton: infinite `stamina`, Gold, `DailyLuck` max roll, watering can water, and clock freeze. |
| **104** | **Terraria ⭐** | C# XNA / FNA (.NET JIT) | **C** | `4.5 / 10` | JIT signature scanning `Terraria.Player::Update`: infinite wing flight (`wingTime`), mana, pickaxe `blockRange`, and item IDs. |
| **105** | **Lethal Company (Offline Solo) ⭐** | Unity Mono + Netcode (x64) | **C+** | `4.6 / 10` | Authoring a `BepInEx + Harmony` C# plugin for `PlayerControllerB`: infinite `sprintMeter`, battery charge, zero carry weight, and Quota. |
| **106** | **Unturned (Offline Sandbox) ⭐** | Unity Engine Mono (x64) | **C+** | `4.6 / 10` | `SDG.Unturned` namespace: `PlayerLife` (HP/Food/Water/Virus), `UseableGun` (zero recoil/spread), and vehicle fuel/health. |
| **107** | **Valheim (Offline Solo World)** | Unity Engine Mono (x64) | **C+** | `4.6 / 10` | BepInEx/Harmony hooks on `Player`: infinite `m_stamina` & `m_eitr`, `m_maxCarryWeight`, and unrestricted metal portal teleportation. |
| **108** | **7 Days to Die (Offline Singleplayer)** | Unity Engine Mono (x64) | **C+** | `4.7 / 10` | Skill Points, Stamina, core temperature, stealth meter, and `BlockDamage` multiplier for instant mining. |
| **109** | **Project Zomboid (Solo Sandbox)** | Java + LWJGL + Lua Scripting | **C+** | `4.7 / 10` | Hooking the Java/Lua VM (`IsoGameCharacter`), clearing zombie infection (`isInfected = false`), endurance, panic, and carry weight. |
| **110** | **Subnautica: Below Zero ⭐** | Unity Engine (x64) | **C+** | `4.7 / 10` | `OxygenManager`, `LiveMixin` health component, body temperature float, Seatruck crush depth, and Ion Cube energy. |
| **111** | **RimWorld** | Unity Engine Mono (x64) | **C+** | `4.8 / 10` | Harmony hooks on `Pawn_NeedsTracker` (colonist mood/hunger), `SkillRecord` (level 20 without XP decay), and instant construction. |
| **112** | **Satisfactory** | Unreal Engine 4 / 5 (x64 C++) | **C+** | `4.8 / 10` | Jetpack fuel, FICSIT `AWESOME Sink` coupons, inventory slots, radiation immunity, and power grid capacity. |
| **113** | **Kenshi** | Ogre3D C++ Engine (`kenshi_x64.exe`) | **C+** | `4.9 / 10` | Cats currency, character limb health struct (Head, Chest, Stomach, Left/Right Arms & Legs -> `100.0f`), hunger, and stat XP multiplier. |
| **114** | **Vampire Survivors & ULTRAKILL** | Unity Engine Mono (x64) | **C+** | `4.9 / 10` | Magnet pickup radius & wave timers in Vampire Survivors; `NewMovement` stamina dashes, `StyleHUD`, and weapon cooldowns in ULTRAKILL. |
| **115** | **Fallout: New Vegas & Fallout 4** | Gamebryo (x86) & Creation Engine (x64) | **B-** | `5.0 / 10` | `Actor` struct, S.P.E.C.I.A.L. stats, `95%` hit chance & Action Points in `V.A.T.S.`, Bottle Caps (`0xF`), and Power Armor Fusion Core charge. |
| **116** | **Mount & Blade: Warband ⭐** | TaleWorlds Custom C++ Engine | **B-** | `5.0 / 10` | Party size limit, `Morale`, `Renown`, Denars, troop XP upgrade tables, and world-map party movement speed. |
| **117** | **The Elder Scrolls IV: Oblivion** | Gamebryo Engine (x86 C++) | **B-** | `5.0 / 10` | Health, Magicka, Fatigue, unbreakable Lockpicks during tumbler minigame, enchanted weapon Soul Gem charges, and Gold. |
| **118** | **The Elder Scrolls V: Skyrim SE ⭐** | Creation Engine (x64 C++) | **B-** | `5.0 / 10` | `PlayerCharacter` singleton, `ActorValueOwner` VMT (HP/Magicka/Stamina/CarryWeight), Dragon Shout cooldown, and Papyrus VM hooks. |
| **119** | **BioShock 1 & BioShock 2 Remastered** | Modified Unreal Engine 2.5 (x64) | **B-** | `5.1 / 10` | `ADAM` for Plasmid slots, `EVE` hypo mana, vending machine Dollars, and auto-completing pipe/needle hacking minigames. |
| **120** | **Dragon Age: Origins & II ⭐** | BioWare Eclipse / Lycium Engine | **B-** | `5.1 / 10` | Party attribute arrays (`Strength`, `Willpower`, `Magic`, `Cunning`), spell cooldown timers, companion approval, and Gold Sovereigns. |
| **121** | **Mass Effect 1 / 2 / 3 (Legendary Edition)** | Unreal Engine 3 (x64 C++) | **B-** | `5.1 / 10` | `Paragon`/`Renegade` morality points, Credits, Element Zero / Platinum / Iridium / Palladium probes, and weapon heat sink cooldowns. |
| **122** | **Crysis 1 / Warhead / Crysis 2 & 3** | CryEngine 2 & CryEngine 3 (x86/x64) | **B-** | `5.2 / 10` | Nanosuit energy float (`Suit Energy` for infinite Cloak & Armor modes), Nano-Catalysts, and zero weapon recoil/spread. |
| **123** | **Dead Space (2008) & Dead Space 2** | Visceral Engine (x86 C++) | **B-** | `5.2 / 10` | Bench `Power Nodes`, `Stasis` module energy float, vacuum Oxygen timer, Credits, and Plasma Cutter ammo. |
| **124** | **Far Cry 3 & Far Cry 4** | Ubisoft Dunia Engine 2 (x86/x64) | **B-** | `5.2 / 10` | Skill Points, wallet/rucksack capacity without hunting pelts, Syringe buff timers, sniper breath, and zero recoil. |
| **125** | **S.T.A.L.K.E.R.: Call of Pripyat (OpenXRay)** | X-Ray Engine 1.6 (C++ & Lua) | **B-** | `5.3 / 10` | `CActor` class in `xrGame.dll`: radiation, bleeding, psy-health, carry weight (`MaxWalkWeight`), rubles, and weapon condition. |
| **126** | **S.T.A.L.K.E.R.: Shadow of Chernobyl & Clear Sky** | X-Ray Engine 1.0 / 1.5 (`xrGame.dll`) | **B-** | `5.3 / 10` | `CActor` stamina, radiation, bleeding, `max_walk_weight`, artifact belt slots, and weapon jam probability. |
| **127** | **Sleeping Dogs & Saints Row: The Third / IV** | United Front Engine & Volition CTG | **B-** | `5.3 / 10` | Triad/Cop/Face XP meters, `Respect` level, superpower Data Clusters in Saints Row IV, and infinite ammo. |
| **128** | **Call of Duty 4: Modern Warfare & World at War (Solo/Zombies)** | IW 3.0 Engine (x86 C++) | **B** | `5.4 / 10` | Solo Zombies `Points`, `Ray Gun` ammo, Juggernog perk flags, and `cg_t` / `centity_t` structs for bot/zombie ESP. |
| **129** | **Counter-Strike: Source & Garry's Mod ⭐** | Source Engine (x86/x64) | **B** | `5.4 / 10` | Calling `CreateInterface("VClientEntityList003")`, entity iteration, `[3][4]` bone matrix extraction, DX9 `EndScene` ImGui ESP, and GMod Lua. |
| **130** | **Half-Life 2 & Portal 2 ⭐** | Source Engine (`client.dll` & `engine.dll`) | **B** | `5.4 / 10` | Walking `ClientClass` linked list to dump **Netvars** (`DT_BasePlayer`), `CreateMove` VMT hook, AUX suit power, and portal surface placement. |
| **131** | **Portal 1 & Team Fortress 2 (Offline Bots)** | Source Engine (x86/x64 C++) | **B** | `5.4 / 10` | Velocity vectors for Accelerated Back Hopping (`ABH`), Portal Gun fire angles, and offline bot Netvars/crit bucket. |
| **132** | **Call of Duty: Black Ops I & II (Campaign & Solo Zombies)** | Treyarch IW Engine (x86 C++) | **B** | `5.5 / 10` | Solo Zombies points, `Pack-a-Punch` upgraded weapon ammo, player health, and camera FOV float. |
| **133** | **Left 4 Dead 2 (Offline Singleplayer)** | Source Engine (x86) | **B** | `5.5 / 10` | Special Infected & `Tank`/`Witch` Netvars, removing melee `Shove Cooldown` fatigue, shotgun spread, and Survivor health/temp-HP. |
| **134** | **Mirror's Edge (2008)** | Unreal Engine 3 (x86 C++) | **B** | `5.5 / 10` | Faith's horizontal `Velocity` vector, `Reaction Time` slow-motion gauge, gravity modifier for super-jumps, and speedrun timers. |
| **135** | **Borderlands 2 & The Pre-Sequel** | Unreal Engine 3 (x86 C++) | **B** | `5.6 / 10` | Scanning UE3 `GObjects` & `GNames` tables, modular weapon generator (swapping barrel/grip parts & rarity in RAM), Golden Keys, and `Badass Tokens`. |
| **136** | **Dishonored 1 & BioShock Infinite** | Unreal Engine 3 (Modified x86) | **B** | `5.6 / 10` | Piero's Spiritual Remedy mana auto-regen, `Blink` teleport range limit bypass, Corvo's Runes, Bone Charms, and `Salts`/Silver Eagles. |
| **137** | **Dishonored 2 & Prey (2017)** | Void Engine (id Tech 5) & CryEngine 4 (x64) | **B** | `5.6 / 10` | `Neuromods` & Psi Pool in Prey, Recycler Charge material yield, and Void mana / runes in Dishonored 2. |
| **138** | **Outlast 1 & Outlast 2** | Unreal Engine 3.5 (x64 C++) | **B** | `5.6 / 10` | Camcorder night-vision battery charge float (`1.0f`), spare battery count, bandages, and infinite sprint stamina. |
| **139** | **Batman: Arkham Asylum & Arkham City** | Unreal Engine 3 (Rocksteady x86) | **B** | `5.7 / 10` | Freeflow `Combo Counter` (triggering Critical Strikes / Special Takedowns after 1 hit), Glide speed vectors, and WayneTech upgrade points. |
| **140** | **Deus Ex: Human Revolution & Mankind Divided** | Crystal Engine & Dawn Engine (x64) | **B** | `5.7 / 10` | `Praxis Kits`, biocell energy bars, credits, hacking terminal countdown timer freeze, and infinite `Glass-Shield` cloak. |
| **141** | **XCOM: Enemy Unknown & XCOM 2: War of the Chosen** | Unreal Engine 3.5 (x64 C++ & Kismet) | **B** | `5.7 / 10` | Soldier `Action Points` (infinite moves per turn), `100% Aim` hit chance, `Supplies`, `Intel`, Alien Alloys, and Elerium. |
| **142** | **Assetto Corsa ⭐** | Kunos Custom C++ Physics Engine | **B+** | `5.8 / 10` | Tire `Grip` multiplier, tire temperature/wear floats, hybrid `KERS`/`ERS` battery charge, and reading `acpmf_physics` Shared Memory. |
| **143** | **Euro Truck Simulator 2 ⭐** | SCS Prism3D Engine (x64 C++) | **B+** | `5.8 / 10` | Economy (`Money`, `XP`), zero truck/trailer/cargo damage (`0.0f`), speed limiter removal, and `scs-telemetry.dll` shared memory. |
| **144** | **Grand Theft Auto IV: The Complete Edition** | RAGE Engine (x86/x64 C++) | **B+** | `5.8 / 10` | Niko's Health, Armor, Cash, Wanted Level stars, vehicle deformation immunity, and Euphoria ragdoll/gravity physics. |
| **145** | **Max Payne 3 & L.A. Noire** | RAGE Engine & Team Bondi Engine | **B+** | `5.8 / 10` | `Bullet Time` gauge, `Painkillers`, Intuition Points during interrogations in L.A. Noire, and infinite ammo. |
| **146** | **Alien: Isolation & SOMA** | Cathode Engine & Frictional HPL3 Engine | **B+** | `5.9 / 10` | Flamethrower fuel, flashlight & motion tracker battery, crafting `Scrap`, and disabling Xenomorph AI sensory detection in `Cathode`. |
| **147** | **Grand Theft Auto V Legacy (Story Mode) ⭐** | RAGE Engine (x64 C++) | **B+** | `5.9 / 10` | `CPedFactory` (`WorldPtr`), `CReplayInterface` entity list, `Native Invoker` script table, and `CHandlingData` vehicle physics. |
| **148** | **Metal Gear Solid V: The Phantom Pain** | Konami Fox Engine (x64 C++ & Lua) | **B+** | `5.9 / 10` | Mother Base `GMP` funds, processed resources, infinite weapon suppressor durability, NVG battery, and Fulton recovery balloons. |
| **149** | **Assassin's Creed II / IV Black Flag / Odyssey** | Ubisoft Anvil / AnvilNext 2.0 (x64) | **B+** | `6.0 / 10` | Florins/Drachmae, `Jackdaw` ship hull upgrade metal/wood, naval mortar ammo, ability Adrenaline segments, and stealth bush flags. |
| **150** | **Batman: Arkham Origins & Arkham Knight** | Unreal Engine 3 (Modified x64) | **B+** | `6.0 / 10` | Batmobile Afterburner & 60mm cannon energy, `WayneTech` points, Combo multiplier lock, and Riddler trial timer freeze. |
| **151** | **Dying Light 1 & 2 ⭐** | Techland Chrome Engine 6 / C-Engine | **B+** | `6.0 / 10` | Parkour & combat Stamina floats, unbreakable melee weapon durability, UV Flashlight battery, zero `Grappling Hook` cooldown, and night timer. |
| **152** | **Kingdom Come: Deliverance** | CryEngine 3.8.6 (x64 C++ & XML/Lua) | **B+** | `6.0 / 10` | Henry's Health, Stamina, Nourishment, Energy, Groschen, `Saviour Schnapps` (saving without consuming), and armor durability. |
| **153** | **Metro 2033 Redux & Metro Exodus ⭐** | 4A Engine (x64 C++) | **B+** | `6.0 / 10` | Gas mask filter countdown timer, Tikhar pneumatic air pressure float, Military-Grade Rounds currency, NVG battery, and weapon dirtiness. |
| **154** | **Middle-earth: Shadow of Mordor & Shadow of War** | LithTech Firebird Engine (x64 C++) | **B+** | `6.0 / 10` | Elven `Focus` (bow slow-mo), `Wrath` bar, Mirian currency, Skill Points, and editing Orc Captain traits/levels in the **Nemesis System**. |
| **155** | **Control & Alan Wake Remastered** | Remedy Northlight Engine (x64 DX12) | **B+** | `6.1 / 10` | Telekinetic `Launch` energy float, Ability Points, `Source` currency, Service Weapon ammo regen, and Alan Wake's flashlight batteries. |
| **156** | **Cyberpunk 2077** | REDengine 4 (x64 DirectX 12 & redscript) | **B+** | `6.1 / 10` | `StatPoolsSystem` (Health, Cyberdeck `RAM`, Stamina), Eurodollars, `Sandevistan` cooldown timer, Street Cred, and Perk/Attribute points. |
| **157** | **DOOM (2016) & DOOM Eternal** | id Tech 6 & id Tech 7 (x64 Vulkan) | **B+** | `6.1 / 10` | Chainsaw fuel pips, `Crucible` charges, `Blood Punch` gauge, unlocking restricted console variables (`CVARs`), and `vkQueuePresentKHR` hook. |
| **158** | **Forza Horizon 4 & 5 (Offline Solo Mode) & BeamNG.drive** | ForzaTech & Torque3D Soft-Body Physics | **B+** | `6.1 / 10` | Credits (`CR`), Skill Chain drift score multiplier, gravity & engine torque curves in BeamNG.drive (`Lua` + C++ node/beam physics). |
| **159** | **HITMAN 2 & HITMAN World of Assassination ⭐** | IO Interactive Glacier 2 Engine (x64) | **B+** | `6.1 / 10` | RTTI classes `ZHitman5` & `ZActor`, NPC `Enforcer` suspicion gauge timers, locking the `Silent Assassin` rating flag, and infinite Instinct. |
| **160** | **The Witcher 3: Wild Hunt (Next-Gen)** | REDengine 3 (x64 C++ & WitcherScript) | **B+** | `6.1 / 10` | RTTI class `CR4Player`, potion `Toxicity` float, Sign `Stamina`, sword/armor durability, inventory weight, and enabling the debug script console. |
| **161** | **Watch Dogs 1 & Watch Dogs 2** | Ubisoft Disrupt Engine (x64 C++) | **B+** | `6.1 / 10` | Profiler smartphone/Botnet battery charge for hacks, Cash, `Research Points`, and Felony/Police heat level suppression. |
| **162** | **Escape the Backrooms & Phasmophobia ⭐** | Unreal Engine 4 & Unity IL2CPP | **A-** | `6.2 / 10` | Locking `Sanity` drain, infinite sprint stamina, and building an `FNamePool` / Entity ESP to visualize AI monster patrol routes. |
| **163** | **Ghostrunner 1 & 2** | Unreal Engine 4 (x64 C++) | **A-** | `6.2 / 10` | Dumping UE4 SDK (`Dumper-7`), infinite mid-air slow-mo dash (`Sensory Boost`), zero ability cooldowns, and locking death counter at `0`. |
| **164** | **KovaaK's (Aim Trainer) ⭐** | Unreal Engine 4 (x64 C++) | **A-** | `6.2 / 10` | Ideal **Dumper-7** training ground: UE4 SDK dump, `UWorld -> PersistentLevel -> Actors` traversal, 3D target capsules, and `ProcessEvent` hook. |
| **165** | **Palworld (Offline Singleplayer) ⭐** | Unreal Engine 5 (x64 C++) | **A-** | `6.3 / 10` | Traversing `GWorld` actor array, Pal Sphere `100% Capture Rate` formula, base work speed, Ancient Technology Points, and carry weight. |
| **166** | **The Outer Worlds & Star Wars Jedi: Fallen Order / Survivor** | Unreal Engine 4 (x64 C++) | **A-** | `6.3 / 10` | Tactical Time Dilation (`TTD`) meter, Jedi `Force Meter`, BD-1 healing stim canisters, Skill Points, and Bits. |
| **167** | **Atomic Heart & S.T.A.L.K.E.R. 2: Heart of Chornobyl** | Unreal Engine 4 & Unreal Engine 5 (x64) | **A-** | `6.4 / 10` | Neuropolymer & glove energy in Atomic Heart; Coupons, stamina, radiation, and carry weight inside `GWorld` in S.T.A.L.K.E.R. 2. |
| **168** | **Dead Space Remake (2023) & Dragon Age: The Veilguard** | EA Frostbite Engine (x64 DX12) | **A-** | `6.4 / 10` | Navigating Frostbite's `TypeInfo` reflection & `ClientGameContext`: upgrade `Nodes`, Credits, Stasis energy, and Isaac Clarke's RIG HP. |
| **169** | **Deep Rock Galactic (Offline Solo Mode)** | Unreal Engine 4 (x64 C++) | **A-** | `6.4 / 10` | Rechargeable `Flares` count, Minigun/Drills overheat gauge, Engineer turret ammo, mined mineral multiplier (`Morkite`/`Gold`), and gravity. |
| **170** | **Lies of P & Black Myth: Wukong** | Unreal Engine 4 & Unreal Engine 5 (x64) | **A-** | `6.5 / 10` | Widening `Perfect Guard` parry window frames, Legion Arm / weapon blade `Durability`, `Fable Arts` / Mana bars, and Ergo / Will. |
| **171** | **Warhammer 40,000: Space Marine 2 (Offline Campaign)** | Saber Swarm Engine (x64 C++) | **A-** | `6.5 / 10` | Astartes Armor segments, Health, Titus's `Righteous Fury` ability meter, plasma weapon overheat float, and Bolter ammo. |
| **172** | **Aimlabs & Slime Rancher 2 ⭐** | Unity IL2CPP (x64 Native Assembly) | **A** | `6.6 / 10` | Recovering metadata via **Il2CppDumper** (`GameAssembly.dll` + `global-metadata.dat`), importing symbols into Ghidra, and hooking via **MinHook**. |
| **173** | **Hades I & Hades II** | Supergiant Custom C++ & Lua 5.2 Engine (x64) | **A** | `6.6 / 10` | Zagreus/Melinoë HP, `Darkness`, Chthonic Keys, Nectar, Titan Blood, `Death Defiance` charges, and live-editing Olympian Boon Lua scripts. |
| **174** | **Subnautica: Below Zero & Sons of the Forest** | Unity Engine Mono / IL2CPP (x64) | **A** | `6.7 / 10` | Symbol recovery with `Il2CppDumper`, body temperature, oxygen, infinite logs in hand (`LogHack`) for instant building, and 3D printer resin. |
| **175** | **Risk of Rain 2** | Unity Engine Mono / IL2CPP (x64) | **A** | `6.8 / 10` | Hooking `CharacterBody::RecalculateStats`, `Lunar Coins` counter, item stack count arrays, Gold, and teleporter charge speed. |
| **176** | **Genshin Impact / Star Rail (Local Private Sandbox Study)** | Modified Unity IL2CPP (Custom Metadata) | **A** | `6.9 / 10` | Studying `global-metadata.dat` header obfuscation & string literal encryption on local offline private sandboxes. |
| **177** | **Zenless / Honkai (Offline Local Server Architecture Lab)** | Unity IL2CPP + Custom Metadata Encryption | **A** | `6.9 / 10` | Locating `Il2CppCodeRegistration` & `Il2CppMetadataRegistration` dispatch tables in stripped binaries and dumping protobuf schemas. |
| **178** | **Don't Starve Together & Starbound ⭐** | Klei C++/Lua & Chucklefish C++/Lua 5.3 | **A+** | `7.0 / 10` | Hooking native `lua_State*` to inspect `ThePlayer.components.health`/`sanity`/`hunger`, and reversing Matter Manipulator structs in Starbound. |
| **179** | **God of War (2018) & God of War Ragnarök** | Santa Monica Proprietary Engine (x64 DX12) | **A+** | `7.0 / 10` | `Spartan Rage` meter, `Hacksilver`, Kratos & Atreus XP, Runic Attack cooldown timers, and enemy Stun bar multipliers. |
| **180** | **PAYDAY 2 (Offline Crime.Net Solo) ⭐** | Diesel Engine 2.0 (C++ & LuaJIT) | **A+** | `7.0 / 10` | Intercepting `lua_call` / `luaL_loadbuffer` (**SuperBLT** architecture), modifying `tweak_data`, bypassing the 4-pager stealth alarm limit, and Skill Points. |
| **181** | **Ghost of Tsushima Director's Cut & Death Stranding** | Sucker Punch Engine & Decima Engine (x64) | **A+** | `7.1 / 10` | Jin Sakai's `Resolve` orbs, `Supplies`, Technique Points; and Sam's cargo balance stability & exoskeleton battery in Death Stranding. |
| **182** | **Horizon Zero Dawn & Marvel's Spider-Man Remastered** | Decima Engine & Insomniac Engine (x64 DX12) | **A+** | `7.1 / 10` | Metal `Shards` & bow Concentration slow-mo in Decima; infinite web-shooters, Focus bar, and Tech Parts in Insomniac's engine. |
| **183** | **Sid Meier's Civilization VI & Hearts of Iron IV ⭐** | Firaxis LORE Engine & Clausewitz Engine | **A+** | `7.1 / 10` | Treasury Gold, Faith/Science/Culture per turn, Fog of War (`MapVisibility`) bitmasks, unit movement points, and Political Power in HoI4. |
| **184** | **NieR: Automata & Bayonetta** | PlatinumGames Engine (x64/x86 C++) | **A+** | `7.2 / 10` | `G` currency, `Plug-in Chips` memory capacity (128 limit bypass), Pod program cooldowns, and `Witch Time` duration. |
| **185** | **Resident Evil 7 Biohazard & Resident Evil Village** | Capcom RE Engine (x64 Native + Managed VM) | **A+** | `7.2 / 10` | `REFramework` reflection (`via.ManagedObject`), `Lei` currency, Duke's treasures, infinite Magnum ammo, and disabling Lady Dimitrescu's AI. |
| **186** | **Baldur's Gate 3 & Divinity: Original Sin 2** | Larian Divinity Engine 4.0 (x64 ECS) | **A+** | `7.3 / 10` | Pure **Entity-Component-System (ECS)** architecture: component pools, `Spell Slots`, Action Points, `d20` roll hooks, and the Osiris story VM. |
| **187** | **Monster Hunter: World & Monster Hunter: Rise** | MT Framework & Capcom RE Engine (x64) | **A+** | `7.3 / 10` | Purple weapon `Sharpness` lock, hunter stamina, `Wirebug` cooldown gauges, `Zenny`, Guild Points, and monster part-break thresholds. |
| **188** | **Resident Evil 2 / 3 / 4 Remake & Devil May Cry 5** | Capcom RE Engine (x64 Native + Managed VM) | **A+** | `7.3 / 10` | Internal RE Engine reflection (`via.ManagedObject`), enemy HP display, unbreakable Combat Knives, Dynamic Difficulty (`GameRankSystem`), and `Devil Trigger`. |
| **189** | **Crusader Kings III, Europa Universalis IV & Stellaris** | Paradox Clausewitz + Jomini Engine (x64) | **S-** | `7.4 / 10` | Gold, Prestige, Piety, Dynasty Renown, patching the `Ironman` memory flag to enable the developer console, and empire alloys/energy in Stellaris. |
| **190** | **Dark Souls III & Sekiro: Shadows Die Twice** | FromSoftware Dantelion Engine (x64) | **S-** | `7.5 / 10` | `WorldChrMan` singleton, dodge-roll invulnerability frame (`i-frame`) animation flags, `Posture` bar in Sekiro, and live `Param` table patching. |
| **191** | **Total War: Warhammer III & Rome II** | Creative Assembly Warscape Engine (x64) | **S-** | `7.5 / 10` | Faction treasury Gold, `Winds of Magic` battle reserve float, campaign army movement range, and unit entity health pools. |
| **192** | **Armored Core VI: Fires of Rubicon & Nioh 2** | FromSoftware Dantelion 2 & Koei Tecmo Engine | **S-** | `7.6 / 10` | AC generator energy (`EN`), `ACS Strain` stagger threshold, `COAM` credits, Repair Kits; and Amrita / `Ki` pulse recovery in Nioh 2. |
| **193** | **Elden Ring + Shadow of the Erdtree (Offline Mode)** | FromSoftware Dantelion 2 (x64 DX12) | **S-** | `7.6 / 10` | `CSChrIns` hierarchy, applying buffs via `SpEffect` IDs, `Poise`, Scadutree Blessing multipliers, and rendering 3D hitboxes over DX12. |
| **194** | **Persona 5 Royal & Yakuza 0 / Like a Dragon** | P-Studio Engine & RGG Dragon Engine (x64) | **S** | `7.7 / 10` | Yen, Persona `SP` mana, Joker's Social Stats, Persona Compendium stat/skill overrides, and Yen/Style points in Yakuza 0. |
| **195** | **Factorio & Noita** | Custom C++20 DOD & FallingEverything Engine | **S** | `7.8 / 10` | `Structure of Arrays (SoA)` slab allocators in Factorio; cellular automata pixel grid, Wand `Cast Delay`/`Recharge` structs, and PRNG seed in Noita. |
| **196** | **Zelda: Breath of the Wild & Tears of the Kingdom** | Cemu (PowerPC Big-Endian) & Ryujinx (ARM64) | **S+** | `8.1 / 10` | Cross-ISA RE: scanning `Big-Endian Float` stamina & `4 Byte Big Endian` weapon durability in Cemu, and patching `ARM64` (`AArch64`) instructions in Switch NSO. |
| **197** | **Minecraft: Java Edition (Offline Singleplayer)** | JVM Bytecode + LWJGL OpenGL (JNI/JVMTI) | **SS-** | `8.4 / 10` | Injecting a native C++ DLL, attaching to the JVM via `JNI_GetCreatedJavaVMs` & `JVMTI`, resolving obfuscated mappings, and runtime class transformation. |
| **198** | **No Man's Sky (Offline Mode)** | Hello Games Procedural Engine (x64 Vulkan) | **SS** | `8.6 / 10` | Mathematical procedural generation: galaxy seed hashes, voxel terrain noise functions, Hyperdrive fuel, and packed binary save structures. |
| **199** | **Red Dead Redemption 2 (Offline Story Mode) ⭐** | RAGE Engine (x64 Vulkan/DX12 + Arxan) | **SS+** | `8.9 / 10` | Analyzing **Arxan** background integrity verification threads (hashing `.text` for `0xE9` hooks) and implementing stealth VMT / Hardware Breakpoint (`DR0`–`DR3`) hooks. |
| **200** | **Star Citizen (Offline Arena Commander) & Diablo 1 (DevilutionX)** | StarEngine (64-bit Double Coords) & Matching Decomp | **SSS+** | `9.8 / 10` | 64-bit `double`-precision planetary coordinates, nested ship Local Physics Grids, and `100% byte-accurate` matching C++ decompilation. |
<!-- TOP100_GAMES_END -->

---

## 💻 Software, File Formats & Binary Auditing Arsenal (Programs & Utilities)

Reverse engineering is not limited to games! Mastering **desktop software, archive parsers, database engines, cryptographic vaults, media codecs, network protocols, and CTF binary suites** builds deep systems engineering intuition that directly transfers back to game engines.

| Target Program / Binary Suite | Category | Architecture & Tech Stack | Tier | Difficulty | Primary Reverse Engineering & Auditing Objective |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **In-Repo `Crackmes 01–08`** | Progressive Crackme Dojo | x64 C++20 (Source + Binaries) | **F+ to SSS-** | `0.7–9.2` | Stack strings, serial keygens, ROL/XOR ciphers, binary `.dat` structs, anti-debug, VM, MBA & Z3. |
| **HxD / Notepad++ (Plugin ABI)** | Hex & Text Editors | Win32 / x64 C++ (`Scintilla.dll`) | **E-** | `1.5 / 10` | Tracing Win32 `SendMessageW` command IDs, Scintilla text buffer pointers, and plugin DLL exports. |
| **7-Zip (`7z.exe` / `7za.dll`)** | Open-Source Archiver | Native x86/x64 C/C++ | **D-** | `2.6 / 10` | Reversing `.7z` signature headers (`37 7A BC AF 27 1C`), CRC32 streams, and LZMA2 state structs. |
| **WinRAR / Shareware Trial Dialogs** | Archive Utility (Audit Lab) | Win32 / x64 Native C++ (`rar.exe`) | **D** | `3.0 / 10` | Auditing RAR5 magic headers (`52 61 72 21`), resource dialog timers (`DialogBoxParamW`), & keyfiles. |
| **IOLI Crackme Suite (`0x00`–`0x09`)** | Classic RE Benchmark | x86 ELF / PE Binaries | **D+** | `3.3 / 10` | Classic 10-level academic crackme ladder for IDA/Ghidra control-flow and keygenning practice. |
| **CMU CS:APP `Bomb Lab` (`bomb`)** | University Systems Benchmark | x86_64 ELF / C (`6 Phases`) | **C-** | `3.9 / 10` | Defusing all 6 assembly phases (string comparison, 6-number loop, switch jump table, recursion, linked list, BST) + `secret_phase`! |
| **ILSpy / dnSpy / .NET Crackmes** | Managed CLI Applications | .NET CLR / C# IL Bytecode | **C** | `4.2 / 10` | Decompiling CIL opcodes (`ldstr`, `brfalse`), StrongName signature removal, and Harmony runtime patching. |
| **KeePass 2.x (`KDBX v4` Vault)** | Password Vault Format | .NET + Native Crypto (`ChaCha20`) | **C+** | `4.7 / 10` | Auditing the KDBX 4.0 binary header layout, Argon2d parameters, and `ProtectedBinary` memory XORing. |
| **SQLite3 (`sqlite3.dll` Engine)** | Embedded Relational DB | Pure ANSI C (x64 Amalgamation) | **B-** | `5.1 / 10` | Reversing the `SQLite format 3\0` 100-byte file header, B-Tree page layout, and SQL bytecode VDBE VM (`sqlite3VdbeExec`). |
| **PuTTY & WinSCP (SSH Key Memory)** | Network / SSH Client | Win32 / x64 C/C++ | **B** | `5.5 / 10` | Locating in-memory `SSH-2` session keys, PPKv3 keyfile parsing structs, and hooking `send`/`recv` cleartext buffers before encryption. |
| **VLC Media Player & FFmpeg (`libavcodec`)** | Multimedia Demuxer/Codec | x64 C/C++ + SIMD (`AVX2`) | **B+** | `5.9 / 10` | Auditing MP4/MKV container box parsers (`moov`, `trak` atoms) and SIMD-accelerated decode loops. |
| **Sysinternals Suite (`Procmon` / `Autoruns`)** | Windows Internals Tools | x64 Native Win32 + Kernel Driver | **A-** | `6.3 / 10` | Understanding how user-mode utilities query undocumented `ntdll.dll` (`NtQuerySystemInformation`) APIs. |
| **Wireshark (`libwireshark.dll` Dissectors)** | Network Protocol Analyzer | x64 C + Embedded Lua Dissectors | **A** | `6.7 / 10` | Reversing protocol dissector registration tables and writing custom Lua/C dissectors for game protocols. |
| **UPX & Custom PE/ELF Packers** | Executable Compression | x86/x64 Assembly Stubs (`UPX0/1`) | **A+** | `7.1 / 10` | Tracing `PUSHAD`/`POPAD` tail-jump stubs to the Original Entry Point (OEP), dumping with Scylla, and fixing the IAT. |
| **Blender / Godot Engine (Native Core)** | Open-Source 3D Engines | x64 C++ (`ClassDB` Reflection) | **S-** | `7.5 / 10` | Reversing `.blend` DNA structure blocks and Godot's `Object`/`Variant` method bind reflection tables. |
| **PyInstaller / Electron (`app.asar` & V8)** | Packaged App Runtimes | Python C-API / Chromium V8 Bytecode | **S** | `7.8 / 10` | Extracting CArchive `.pyc` marshaled code objects, fixing magic headers, and auditing V8 `.jsc` snapshots. |
| **QEMU / Bochs / Unicorn Engine** | CPU Emulators & JITs | x64 C (`TCG` Tiny Code Generator) | **S+** | `8.1 / 10` | Understanding how QEMU's Tiny Code Generator lifts guest ARM/MIPS/x86 blocks into host native code. |
| **OpenSSL (`libcrypto`) & `libsodium`** | Cryptographic Primitives | x64 C + Hand-Written Assembly | **SS-** | `8.4 / 10` | Identifying AES-NI (`aesenc`), SHA-256 constants (`0x6a09e667`), ChaCha20 quarter-rounds (`QR`), and RSA Montgomery multiplication in stripped binaries. |
| **FLARE-On CTF Challenges (Ch. 1–6)** | Mandiant Annual RE Contest | Windows PE / .NET / Shellcode / VM | **SS** | `8.7 / 10` | Solving multi-stage real-world reverse engineering challenges (custom encodings, API hashing, PE loaders). |
| **VMProtect / Themida Unpacking Labs** | Commercial Protectors | Virtualized x64 PE Binaries | **SS+** | `9.0 / 10` | Tracing `VM_Enter`, devirtualizing stack/register handlers, and recovering stolen OEP bytes. |
| **Triton / Miasm / `angr` De-Obfuscation** | DBI & Symbolic Solvers | Python + C++ SMT / LLVM | **SSS-** | `9.3 / 10` | Automated symbolic path exploration, dynamic taint analysis, and MBA expression simplification. |
| **Linux KVM / `memflow` / Windows WDK** | Hypervisor & Ring-0 Labs | Rust / C Kernel & VMI Frameworks | **SSS** | `9.6 / 10` | Out-of-VM physical memory introspection (`CR3` $\rightarrow$ `PML4` page table walking) & IOCTL drivers. |
| **Ghidra SLEIGH / LLVM `Remill` Lifters** | Decompiler & IR Tooling | Java / C++17 LLVM IR | **SSS++** | `10.0 / 10` | Authoring custom CPU architecture processors in Ghidra SLEIGH and lifting VM bytecode to LLVM IR. |

---

## 🌳 The 6-Stage Reverse Engineering Skill Tree

### Stage 1: Memory Fundamentals & Dynamic Scanning (Cheat Engine)
* Virtual Memory Architecture, Pages, and Protection Flags (`PAGE_EXECUTE_READWRITE`).
* Data representations: `Byte`, `Int16`, `Int32`, `Int64`, `Float`, `Double`, IEEE-754, and Bitmasks.
* Static Base Addresses (`module.exe + 0xOFFSET`) vs. Dynamic Heap Allocations (`malloc`/`new`).
* Multi-level Pointer Chains, Pointer Scanning, and Structure Dissecting.
* Hardware/Software Breakpoints (*"Find out what accesses/writes to this address"*).
* Auto Assembler (`.CEA`), Code Injection (`alloc`, `jmp`, `label`), and AOB (Array of Bytes) Signature Scanning.

### Stage 2: CPU Architecture & x86/x64 Assembly
* General Purpose Registers (`RAX`, `RBX`, `RCX`, `RDX`, `RSI`, `RDI`, `RBP`, `RSP`, `R8`–`R15`).
* EFLAGS/RFLAGS (`ZF`, `CF`, `SF`, `OF`) and Conditional Jumps (`JE`, `JNE`, `JG`, `JL`).
* Stack Frame Layout, `PUSH`/`POP`, Prologue/Epilogue, and $16$-byte Stack Alignment in x64.
* Calling Conventions: `__cdecl`, `__stdcall`, `__thiscall` (`ECX` = `this`), `__fastcall`, and Microsoft x64 ABI (`RCX`, `RDX`, `R8`, `R9`).
* Floating-Point & SIMD Registers (`XMM0`–`XMM15`, `MOVSS`, `ADDSS`, `MULSS`, `COMISS`).
* Static Analysis & Decompilation with **Ghidra** and **IDA Pro/Free** + Dynamic Debugging with **x64dbg**.

### Stage 3: External Tooling & Trainers (Win32 API & C++)
* Process Enumeration: `CreateToolhelp32Snapshot`, `Process32FirstW`, `Module32FirstW`.
* Handle Acquisition: `OpenProcess` with `PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION`.
* Memory Manipulation: `ReadProcessMemory` (RPM), `WriteProcessMemory` (WPM), and `VirtualProtectEx`.
* Resolving Multi-Level Pointers programmatically (implemented in [`Tools_and_Scripts/01_External_Trainer_Template`](./Tools_and_Scripts/01_External_Trainer_Template/external_memory_trainer.cpp)):
  $$\text{FinalAddress} = \left[\left[\dots\left[\left[\text{Base} + \Delta_1\right] + \Delta_2\right]\dots\right] + \Delta_{n-1}\right] + \Delta_n$$

### Stage 4: Internal Development, DLL Injection & Function Hooking
* Anatomy of a Dynamic Link Library (`DllMain`, `DLL_PROCESS_ATTACH`, worker threads — implemented in [`Tools_and_Scripts/03_Internal_DLL_Skeleton`](./Tools_and_Scripts/03_Internal_DLL_Skeleton/dllmain_internal_hook.cpp)).
* Injection Techniques: `LoadLibraryA` via `CreateRemoteThread`, Thread Hijacking, and Manual Mapping (PE Header parsing, Base Relocations, IAT resolution, TLS callbacks).
* Inline / Trampoline Hooking: Overwriting function prologues ($5$-byte relative `JMP` in x86, $14$-byte absolute `JMP` in x64) and executing original bytes via a Gateway using **MinHook** or **Microsoft Detours**.
* Virtual Method Table (VMT) Hooking: Swapping function pointers in C++ class vtables.

### Stage 5: Engine Internals, Class Reconstruction & SDK Generation
* Live Memory Class Reconstruction using **ReClass.NET** (mapping padding, pointers, vtables, arrays).
* Extracting C++ RTTI (`type_info`, Complete Object Locator) to automatically name classes in IDA/Ghidra.
* **Unity Mono:** Decompiling `Assembly-CSharp.dll` with **dnSpyEx** / **ILSpy** and injecting via Mono Embedding API or **Harmony / BepInEx**.
* **Unity IL2CPP:** Reversing `GameAssembly.dll` + `global-metadata.dat` using **Il2CppDumper**.
* **Unreal Engine (UE3/UE4/UE5):** Navigating `GWorld`, `GNames` (`FNamePool`), and `GUObjectArray`, and generating full C++ SDKs with **Dumper-7**.

### Stage 6: 3D Math, Graphics API Hooking & Internal GUIs
* Vector & Linear Algebra in 3D Space: Euclidean distance, Dot Product, Cross Product, Euler Angles (Pitch $\theta$, Yaw $\psi$, Roll $\phi$ — implemented in [`Tools_and_Scripts/02_3D_Math_and_W2S_Lib`](./Tools_and_Scripts/02_3D_Math_and_W2S_Lib/w2s_math_lab.hpp)).
* Projection Mathematics: View-Projection Matrix ($4 \times 4$) and the **WorldToScreen (W2S)** algorithm converting 3D world coordinates $(X, Y, Z)$ into 2D screen coordinates (`x_screen`, `y_screen`) via Clip Space and Normalized Device Coordinates ($\text{NDC} \in [-1, 1]$).
* Graphics Hooking: Hooking `IDXGISwapChain::Present` (DirectX 11/12), `IDirect3DDevice9::EndScene` (DX9), `wglSwapBuffers` (OpenGL), or `vkQueuePresentKHR` (Vulkan) with **Dear ImGui**.

---

## 🏆 The Complete 28-Tier RPG Campaign (`F-` $\rightarrow$ `SSS++`)

> **⚔️ How to Level Up Through the Campaign:**
> Each Tier below contains **interactive checkboxes (`- [ ]`)** across **In-Repo Dojo Labs**, **Toolcraft**, **Offline Games**, and **Software/Binary Auditing**.
> * Complete **any 3 quests (`3 TP`) inside your current Tier** — OR complete **1 Breakthrough quest (`+3 TP`) in a higher Tier** — and run `.\update_progress.bat` to rank up!

```text
╔════════════════════════════════════════════════════════════════════════════════════════╗
║                COMPLETE 28-TIER REVERSE ENGINEERING DIFFICULTY HIERARCHY               ║
╠══════════╦════════════╦════════════════════════════════════════════════════════════════╣
║   TIER   ║ DIFFICULTY ║ CORE MEMORY, ENGINE, SOFTWARE & ARCHITECTURE CHALLENGES        ║
╠══════════╬════════════╬════════════════════════════════════════════════════════════════╣
║  SSS++   ║ 10.0 / 10  ║ Silicon Glitching, Arcade Crypto Dongles & LLVM IR Lifters     ║
║  SSS+    ║  9.8 / 10  ║ Byte-Accurate Matching Decompilation & 64-bit Space Engines    ║
║  SSS     ║  9.5 / 10  ║ Hypervisor EPT Hooking, Ring-0 Drivers & QEMU/KVM VMI          ║
║  SSS-    ║  9.2 / 10  ║ O-LLVM Control-Flow Flattening, MBA & Symbolic Execution (Z3)  ║
║  SS+     ║  8.9 / 10  ║ Commercial Virtualizers (VMProtect / Themida) & Arxan Guards   ║
║  SS      ║  8.6 / 10  ║ Custom Bytecode VMs, Encrypted Packers & Legacy Ring-3 DRM     ║
║  SS-     ║  8.3 / 10  ║ JVM Native Interface (JNI/JVMTI), Obfuscated LuaJIT & OpenSSL  ║
║  S+      ║  8.0 / 10  ║ Console Emulators (PowerPC Big-Endian, PS3 Cell, Switch ARM64) ║
║  S       ║  7.7 / 10  ║ Data-Oriented Design (SoA Slabs), Custom Allocators & Voxels   ║
║  S-      ║  7.4 / 10  ║ Soulslike Proprietary Engines, Havok Physics & Param Tables    ║
║  A+      ║  7.0 / 10  ║ Hybrid C++/Lua Engines, UPX Unpacking, RE Engine & BG3 ECS     ║
║  A       ║  6.6 / 10  ║ Unity IL2CPP (Stripped C# Transpiled to Native x64 Assembly)   ║
║  A-      ║  6.2 / 10  ║ Unreal Engine 4 & 5 (GWorld, FNamePool, Dumper-7 SDKs)         ║
║  B+      ║  5.8 / 10  ║ Modern AAA x64 Proprietary Engines, Telemetry & Media Codecs   ║
║  B       ║  5.4 / 10  ║ Source Engine (Netvars/VMT/CreateMove), UE3 & Network Clients  ║
║  B-      ║  5.0 / 10  ║ Mature 32/64-bit Open-World Engines & SQLite3 B-Tree VDBE VM   ║
║  C+      ║  4.6 / 10  ║ Advanced Unity Mono, Harmony Hooking & KeePass KDBX Crypto     ║
║  C       ║  4.2 / 10  ║ Unity Mono, .NET CLR (dnSpyEx) & Binary License File Formats   ║
║  C-      ║  3.8 / 10  ║ 2D Roguelikes, ReClass VMTs, CMU Bomb Lab & GameMaker Bytecode ║
║  D+      ║  3.4 / 10  ║ Classic 32-bit Open-World, Stealth, RenderWare & IOLI Crackmes ║
║  D       ║  3.0 / 10  ║ Early 2000s 3D Arena Shooters (UE1/UE2, GoldSrc) & ROL Ciphers ║
║  D-      ║  2.6 / 10  ║ 90s Retro 2.5D/3D Engines (id Tech 1/2, Build) & 7-Zip Headers ║
║  E+      ║  2.2 / 10  ║ Casual 32-bit C++ Frameworks (PopCap Engine) & Auto Assembler  ║
║  E       ║  1.8 / 10  ║ Open-Source FPS Sandboxes, 3D Aim Trainers & Serial Keygenmes  ║
║  E-      ║  1.4 / 10  ║ Classic Win32 Desktop Games (Static 2D Grids, Minesweeper)     ║
║  E--     ║  1.0 / 10  ║ Purpose-Built Gamified RE Tutorials & Interactive Trainers     ║
║  F+      ║  0.6 / 10  ║ Unprotected Save-Files, Plaintext Configs & Stack Strings      ║
║  F       ║  0.4 / 10  ║ IEEE-754 Floats, Doubles, 16-bit Shorts & 8-bit Status Bitmasks║
║  F-      ║  0.2 / 10  ║ Self-Written C/C++ Console Loops & Exact 4-Byte Memory Scans   ║
╚══════════╩════════════╩════════════════════════════════════════════════════════════════╝
```


---

## 🌱 Act I: The Novice Grounds (`Tiers F-` to `E--`)

### 🐣 Tier `F-` : White-Box Zero (Exact Scalar Memory) — `Difficulty: 0.1–0.2 / 10` | `100 EXP/Quest`
* **🔗 Prerequisite:** None (Start here with zero experience!)
* **🆕 New Concept Unlocked:** Virtual memory addresses, 32-bit signed integers (`4 Bytes`), Exact Value Scanning, and Freezing values in Cheat Engine.

#### ⚔️ Tier `F-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier F`!)
- [ ] 🧪 **[In-Repo Lab 01 — Bronze]:** Compile and run [`lab01_static_scalars.exe`](./Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp) in **Apprentice Mode**, attach Cheat Engine, and freeze `g_HeroHP` and `g_Arrows`.
- [ ] 🧪 **[In-Repo Lab 01 — Gold]:** Restart [`lab01_static_scalars.exe`](./Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp) in **Hardcore Blind Mode** (addresses hidden), scan for `g_Gold` (`50`), set it to `999,999`, and defeat the Slime King!
- [ ] 🛠️ **[Toolcraft]:** Save your first `.CT` Cheat Table with locked entries for `HP`, `Arrows`, and `Gold`, and inspect how `.CT` files are structured as XML in a text editor.
- [ ] 🎮 **[Own Game Project]:** **Bulánci-Kitty / Bonanza-Clone (C / C++17 SDL2)** ⭐ — Attach Cheat Engine to your own compiled SDL2 game and verify where global/player variables sit in RAM.
- [ ] 💻 **[Software Audit]:** **Windows Calculator / Simple CLI Counter** — Attach Cheat Engine or System Informer (`Process Hacker`) to inspect the Virtual Memory regions (`.text`, `.rdata`, `.data`, `Heap`, `Stack`) of a running console process.

---

### 🧬 Tier `F` : Data Representations, IEEE-754 Floats & Bitmasks — `Difficulty: 0.3–0.5 / 10` | `120 EXP/Quest`
* **🔗 Prerequisite Used:** Exact 4-Byte scanning (`Tier F-`).
* **🆕 New Concept Unlocked:** Scanning for `Float` (`32-bit IEEE-754`), `Double` (`64-bit`), `2-Byte Int16`, `Unknown Initial Value` (`Increased` / `Decreased`), and packing 8 boolean flags into a single `1-Byte` Bitmask (`0x01`, `0x80`).

#### ⚔️ Tier `F` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier F+`!)
- [ ] 🧪 **[In-Repo Lab 02 — Bronze]:** Run [`lab02_datatypes_bitmasks.exe`](./Course_Solutions/Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp), scan for `g_ManaPool` (`Float`) using `Decreased Value` after casting Arcane Bolt, and set it to `999.0f`.
- [ ] 🧪 **[In-Repo Lab 02 — Gold]:** In **Hardcore Mode**, locate `g_ShieldDurability` (`2 Bytes`) and `g_StatusBitmask` (`1 Byte`), clear all debuff bits, and set bit 7 (`0x80` = `128` decimal, `DIVINE_BLESSING`) to open the Sanctuary Seal!
- [ ] 🛠️ **[Toolcraft]:** Write a 5-line Python one-liner using `struct.pack('<f', 85.5).hex()` to convert IEEE-754 floats into raw hex bytes (`00 00 AB 42`).
- [ ] 🎮 **[Game Target]:** **Self-Written OOP VTable Lab (`vtable_lab.exe`)** — Compile a C++ class with `float health` and `uint8_t flags` and inspect its raw bytes in Cheat Engine's Hex View.

---

### 📄 Tier `F+` : Unprotected State, Clickers & Plaintext/Stack Strings — `Difficulty: 0.6–0.8 / 10` | `150 EXP/Quest`
* **🔗 Prerequisite Used:** `Double`/`Float` scanning and byte inspection (`Tier F`).
* **🆕 New Concept Unlocked:** Static string analysis (`.rdata` vs runtime Stack Strings in Ghidra/x64dbg), `Double` clicker counters, Speedhack timer acceleration, and emulated retro RAM banks.

#### ⚔️ Tier `F+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier E--`!)
- [ ] 🔐 **[In-Repo Crackme 01 — Bronze]:** Open [`crackme01_strings.exe`](./Crackmes_and_CTF/01_Apprentice_Gate/crackme01_strings.cpp) in x64dbg or Ghidra, locate the Stage 1 `.rdata` string, and pass Gate 1.
- [ ] 🔐 **[In-Repo Crackme 01 — Gold]:** Recover the 13-character **Stack String** in Stage 2 of [`crackme01_strings.exe`](./Crackmes_and_CTF/01_Apprentice_Gate/crackme01_strings.cpp) without patching the binary!
- [ ] 🎮 **[Game Target]:** **Banana / Clicker Heroes / Cookie Clicker / Upload Labs** ⭐ — Scan for `Double` currency counters, test Cheat Engine's `Speedhack`, and audit unencrypted `PlayerPrefs` / JSON save states.
- [ ] 🎮 **[Game Target]:** **Zup! S & Zup! Zero / Optika / Puzzle Chambers** ⭐ — Locate level-win boolean flags (`0` $\rightarrow$ `1`) and explosion impulse floats.
- [ ] 🎮 **[Emulator Target]:** **SEGA Mega Drive & Genesis Classics (`Bonanza Bros.`, `Streets of Rage`, `Golden Axe`)** ⭐ — Locate the contiguous $64\text{ KB}$ emulated Motorola 68000 RAM block and lock player lives/health bytes.

---

### 🌱 Tier `E--` : Purpose-Built Educational RE Labs — `Difficulty: 1.0–1.2 / 10` | `180 EXP/Quest`
* **🔗 Prerequisite Used:** Value scanning, data types, and basic string lookup (`Tiers F-` to `F+`).
* **🆕 New Concept Unlocked:** Guided introduction to hardware/software breakpoints, single/multi-level pointers, and in-game live assembly patching.

#### ⚔️ Tier `E--` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier E-`!)
- [ ] 🧪 **[Official Tutorial]:** **Cheat Engine Built-in Tutorial (`Tutorial-x86_64.exe`)** — Complete Steps 1 through 9 (Exact scan, Float scan, Unknown scan, Pointers, Code Injection, Shared Code Step 9).
- [ ] 🧪 **[Graphical Tutorial]:** **Cheat Engine Graphical Tutorial (`gtutorial-x86_64.exe`)** — Complete all 3 graphical mini-games (teleportation, pointer shooting, and shared health).
- [ ] 🎮 **[Educational Game]:** **Squally** — Solve platformer RPG puzzles by editing live x86 assembly instructions (`ADD`, `SUB`, `XOR`, `JMP`) in-game.
- [ ] 🎮 **[Educational Game]:** **PwnAdventure 3: Pwnie Island (Offline Client & Local Server)** — Patch speed/jump multipliers and inspect `GameLogic.dll` in Vector 35's UE3 training game.
- [ ] 💻 **[Embedded CTF]:** **Microcorruption (MSP430 Assembly Simulator)** — Solve the first 4 hardware debugger lock-picking challenges (*Tutorial*, *New Orleans*, *Sydney*, *Hanoi*).

---

## 🗡️ Act II: The 32-Bit Frontier (`Tiers E-` to `D+`)

### 🪵 Tier `E-` : Desktop Win32 Classics (Static 2D Grids & Structs) — `Difficulty: 1.3–1.6 / 10` | `220 EXP/Quest`
* **🔗 Prerequisite Used:** Byte scanning and memory browsing (`Act I`).
* **🆕 New Concept Unlocked:** Contiguous C structures (`#pragma pack`) and static 2D byte arrays in RAM (`board[row][col]`), plus Win32 message loop (`SendMessageW`) auditing.

#### ⚔️ Tier `E-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier E`!)
- [ ] 🧪 **[In-Repo Lab 03 — Bronze]:** Run [`lab03_grid_minesweeper.exe`](./Course_Solutions/Lab03_2D_Arrays_and_Structures/lab03_grid_minesweeper.cpp), locate the 36-byte `board[6][6]` array in Cheat Engine's Hex Memory Viewer, and map out all `0x77` Relics and `0x8F` Traps.
- [ ] 🧪 **[In-Repo Lab 03 — Gold]:** Collect all 3 Relics in **Hardcore Mode** without stepping on a single `0x8F` spike trap (or zero out all traps in RAM)!
- [ ] 🎮 **[Desktop Classic]:** **Windows Minesweeper (`winmine.exe`)** — Locate the static 2D minefield array (`0x01005340`, where `0x8F` = mine), freeze the timer, and invoke the internal `Win` routine.
- [ ] 🎮 **[Desktop Classic]:** **3D Pinball: Space Cadet (`pinball.exe`) & Solitaire / SkiFree** — Lock remaining balls, edit plunger physics floats, and patch illegal card move checks (`JNZ` $\rightarrow$ `JMP`).
- [ ] 🎮 **[Game Target]:** **Codename Gordon** ⭐ — Scan 2D Half-Life sidescroller health/ammo and gravity gun charge floats.
- [ ] 💻 **[Software Audit]:** **Notepad++ / HxD (`Scintilla.dll`)** — Locate the active text buffer in memory and trace Win32 `WM_COMMAND` message IDs in x64dbg.

---

### 🔰 Tier `E` : Beginner 3D Sandboxes, Multi-Pointers & Serial Keygenning — `Difficulty: 1.7–2.0 / 10` | `260 EXP/Quest`
* **🔗 Prerequisite Used:** Contiguous C structs (`Tier E-`).
* **🆕 New Concept Unlocked:** Dynamic Heap allocations (`new`/`malloc`), **Multi-Level Pointer Chains** (`[[Base + o1] + o2]`), basic `LocalPlayer` / `EntityList` structs, and writing mathematical **Keygens**.

#### ⚔️ Tier `E` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier E+`!)
- [ ] 🧪 **[In-Repo Lab 04]:** Conquer all 5 Dungeon Floors in [`lab04_pointer_chains.exe`](./Course_Solutions/Lab04_MultiLevel_Pointers/lab04_pointer_chains.cpp) by building a 3-level pointer chain rooted at `g_WorldManager` that survives heap reallocation!
- [ ] 🔐 **[In-Repo Crackme 02]:** Reverse `ValidateSerialKey()` in [`crackme02_serial_math.exe`](./Crackmes_and_CTF/02_Mathematical_Lock/crackme02_serial_math.cpp) using Ghidra and write a Python script that generates valid `AAAA-BBBB-CCCC` keys!
- [ ] 🛠️ **[Toolcraft]:** Compile and run [`external_memory_trainer.exe`](./Tools_and_Scripts/01_External_Trainer_Template/external_memory_trainer.cpp) (`Win32 OpenProcess + ReadProcessMemory + ResolvePointerChain`) to patch `lab04_pointer_chains.exe` externally!
- [ ] 🎮 **[Game Target]:** **AssaultCube (`ac_client.exe`)** — Locate `LocalPlayer` (`0x50F4F4`), `EntityList`, Health, Ammo, Recoil, and Pitch/Yaw ViewAngles.
- [ ] 🎮 **[Game Target]:** **Aim Hero & 3D Aim Trainer** ⭐ — Locate 3D target sphere coordinates $(X, Y, Z)$, target lifetime floats, and camera FOV/Pitch/Yaw angles.
- [ ] 🎮 **[Game Target]:** **Quake III Arena (`ioquake3`) / Cube 2: Sauerbraten / SuperTuxKart** — Inspect `centity_t` structs, velocity vectors, and nitro boost floats.

---

### 🥉 Tier `E+` : Casual 32-bit C++ Frameworks & Auto Assembler Injection — `Difficulty: 2.1–2.4 / 10` | `300 EXP/Quest`
* **🔗 Prerequisite Used:** Multi-level pointer chains (`Tier E`).
* **🆕 New Concept Unlocked:** Hardware Breakpoints (*"Find out what writes"*), `NOP` (`0x90`) instruction patching, **Auto Assembler (`.CEA`)** code caves (`alloc`, `jmp`), and AOB Signatures.

#### ⚔️ Tier `E+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier D-`!)
- [ ] 🧪 **[In-Repo Lab 05]:** Clear [`lab05_code_injection.exe`](./Course_Solutions/Lab05_Code_Injection_and_NOP/lab05_code_injection.cpp) by `NOP`ing the stamina subtraction inside `ConsumeStamina()` and injecting a code cave into `GainExperience()` to grant `+50,000 EXP` per slash!
- [ ] 🛠️ **[Toolcraft]:** Run [`pe_and_aob_scanner.py`](./Tools_and_Scripts/04_Python_RE_Toolkit/pe_and_aob_scanner.py) to scan a compiled binary for wildcard AOB patterns (`48 89 5C 24 ??`) and compute section Shannon entropy.
- [ ] 🎮 **[Game Target — Completed by `deavers`]:** **Plants vs. Zombies GOTY (`PlantsVsZombies.exe`)** ⭐ — Build AOB injection scripts for Infinite Sun (`+0x5560`), Instant Seed Recharge, Immortal Plants, and Lua Speedhack (Reference: [`PvZ.CT`](./Game_Hacking/PvZ.CT)).
- [ ] 🎮 **[Game Target]:** **Castle Crashers** ⭐ — Locate character XP/Level structs, Gold, Strength/Magic/Defense/Agility stat bars, and juggle gravity floats.
- [ ] 🎮 **[Game Target]:** **Deponia: The Complete Journey / Peggle / Zuma / Insaniquarium** ⭐ — Reverse Visionaire 2D inventory arrays, Peggle guide-line length floats, and PopCap score multipliers.
- [ ] 🎮 **[Game Target]:** **Capcom Arcade Stadium (Offline ROM Wrapper)** ⭐ — Find emulated CPS-1/CPS-2 P1 health bars and invincibility timers inside wrapper memory.

---

### 🗡️ Tier `D-` : 90s Retro 2.5D/3D Engines & Binary Archive Headers — `Difficulty: 2.5–2.8 / 10` | `350 EXP/Quest`
* **🔗 Prerequisite Used:** Struct offsets and AOB code injection (`Tier E+`).
* **🆕 New Concept Unlocked:** Fixed-point arithmetic ($16.16$), classic sector/actor linked lists (`mobj_t`, `edict_t`), and binary archive magic headers.

#### ⚔️ Tier `D-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier D`!)
- [ ] 🎮 **[Game Target]:** **DOOM + DOOM II (id Tech 1 / KEX Engine / GZDoom)** ⭐ — Reverse `mobj_t` actor structures, $16.16$ fixed-point coordinates, sector lighting, ammo pointers, and god-mode bitflags.
- [ ] 🎮 **[Game Target]:** **POSTAL (Classic & Redux)** ⭐ — Locate isometric coordinate vectors, weapon ammo arrays, and execution state flags.
- [ ] 🎮 **[Game Target]:** **Duke Nukem 3D (EDuke32) / Blood: Fresh Supply / Quake I & II** — Inspect Build Engine sprite/sector static arrays, jetpack fuel, and `edict_t` structs.
- [ ] 💻 **[Software / Format Audit]:** **7-Zip (`7z.exe` / `7za.dll`)** — Trace how `7z.exe` parses the 32-byte `.7z` Signature Header (`37 7A BC AF 27 1C`), header CRC32 verification, and LZMA2 decompression streams in Ghidra/x64dbg.

---

### 🛡️ Tier `D` : Early 2000s 3D Arena Shooters, Shared Code & Bitwise Ciphers — `Difficulty: 2.9–3.2 / 10` | `400 EXP/Quest`
* **🔗 Prerequisite Used:** Auto Assembler code caves (`Tier E+`) and actor structs (`Tier D-`).
* **🆕 New Concept Unlocked:** **Shared Engine Code Disambiguation** (separating `Player` vs `Enemy` inside a shared `TakeDamage` function via `cmp [rcx+offset], id`), early OOP hierarchies (`UObject`/`APawn`), and bitwise `ROL`/`ROR` + `XOR` loops.

#### ⚔️ Tier `D` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier D+`!)
- [ ] 🧪 **[In-Repo Lab 06]:** Defeat the Shadow Dragon (`250,000 HP`) in [`lab06_shared_code.exe`](./Course_Solutions/Lab06_Shared_Code_Disambiguation/lab06_shared_code.cpp) by writing an Auto Assembler filter inside `ApplySharedDamage()` that checks `victim->factionId` (`[rcx+08]`): `1` $\rightarrow$ `0 DMG` (God Mode), `2` $\rightarrow$ `999,999 DMG` (One-Hit Kill)!
- [ ] 🔐 **[In-Repo Crackme 03]:** Reverse the `Rol8` + index-`XOR` loop in [`crackme03_xor_rol.exe`](./Crackmes_and_CTF/03_XOR_and_Rol_Cipher/crackme03_xor_rol.cpp) and write a Python script using `ROR8` to recover the 20-character rune!
- [ ] 🎮 **[Game Target — Completed by `deavers`]:** **Unreal Tournament 99 (`UnrealTournament.exe`)** ⭐ — Traverse `Engine.dll` `UObject`/`APawn` chains and craft a smart shared-code One-Hit Kill filter (Reference: [`UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT)).
- [ ] 🎮 **[Game Target]:** **Half-Life 1 / Counter-Strike 1.6 / Condition Zero (Offline Bots)** ⭐ — Reverse GoldSrc `cl_entity_s` arrays, `cl_enginefunc_t`, punch angle recoil vectors, and `FL_ONGROUND` bunnyhop flags.
- [ ] 🎮 **[Game Target]:** **POSTAL 2 & Max Payne 1/2 & Serious Sam Classic** ⭐ — Navigate UE2 `UPawn` inventory linked lists, cat-silencer counters, and MAX-FX bullet-time hourglass floats.
- [ ] 💻 **[Software Audit]:** **WinRAR (`rar.exe` / Shareware Evaluation Flow)** — Audit how RAR5 parses `52 61 72 21 1A 07 01 00` archive headers and how Win32 `DialogBoxParamW` evaluation reminders are triggered.

---

### 🏹 Tier `D+` : Classic 32-bit Open-World, Stealth & Strategy Engines — `Difficulty: 3.3–3.6 / 10` | `450 EXP/Quest`
* **🔗 Prerequisite Used:** Shared engine code filtering and OOP actor structs (`Tier D`).
* **🆕 New Concept Unlocked:** Stealth visibility/acoustic float meters, static entity pools (`CPed`, `CVehicle`), 64-bit stud counters, and academic crackme control-flow graphs.

#### ⚔️ Tier `D+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier C-`!)
- [ ] 🎮 **[Game Target]:** **Splinter Cell: Chaos Theory** ⭐ — Lock the light-visibility meter float (`0.0` = pitch black stealth), acoustic noise float, and night-vision battery charge.
- [ ] 🎮 **[Game Target]:** **Far Cry 1 (CryEngine 1) & GTA: Vice City / San Andreas (RenderWare)** ⭐ — Inspect `CryGame.dll` stamina/recoil floats, RenderWare static `CPed` (`0xB6F5F0`) pools, and call internal HUD functions.
- [ ] 🎮 **[Game Target]:** **SimCity 4 Deluxe / Evil Genius / SPORE** ⭐ — Bypass SPORE's Creature Editor complexity limit, lock SimCity treasury bonds, and Evil Genius minion loyalty bars.
- [ ] 🎮 **[Game Target]:** **LEGO Star Wars / LEGO Batman / LEGO LOTR / LEGO Worlds** ⭐ — Reverse TT Games Nu2x Engine 64-bit stud counters and Red Brick multiplier bitflags.
- [ ] 💻 **[Crackme Suite]:** **IOLI Crackme Suite (`crackme0x00` to `crackme0x09`)** — Solve all 10 classic academic x86 crackmes in Ghidra/IDA and document their control-flow graphs.

---

## 🔮 Act III: Bytecode & Managed Realms (`Tiers C-` to `C+`)

### 🔮 Tier `C-` : 2D Indie Roguelikes, ReClass VMTs & Assembly Bomb Lab — `Difficulty: 3.7–4.0 / 10` | `520 EXP/Quest`
* **🔗 Prerequisite Used:** Entity pools and shared code hooks (`Act II`).
* **🆕 New Concept Unlocked:** C++ Polymorphism (`vptr` at offset `0x00` pointing to a **Virtual Method Table**), live class reconstruction in **ReClass.NET**, room-transition stat caches, and GameMaker/Cocos2d-x internals.

#### ⚔️ Tier `C-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier C`!)
- [ ] 🧪 **[In-Repo Lab 07]:** Open [`lab07_vtable_reclass.exe`](./Course_Solutions/Lab07_ReClass_and_VMT_Hooking/lab07_vtable_reclass.cpp) in ReClass.NET / Cheat Engine, map out `AdventurerAccount`, and overwrite the `vptr` at `+0x00` with `GrandmasterAccount`'s VMT to unlock the Vault!
- [ ] 🎮 **[Game Target — Completed by `deavers`]:** **The Binding of Isaac: Repentance (`isaac-ng.exe`)** ⭐ — Dissect `Entity_Player`, heart bitmasks, active item charges, and room-transition stat locks (Reference: [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT)).
- [ ] 🎮 **[Game Target]:** **Geometry Dash (`GeometryDash.exe`)** ⭐ — Reverse Cocos2d-x `PlayLayer::destroyPlayer` (noclip patch), `PlayerObject` gravity/speed floats, and `CCNode` trees.
- [ ] 🎮 **[Game Target]:** **UBERMOSH Series / Chasm / Secrets of Grindea / Barony** ⭐ — Lock Brain-Power meters, parry window timers, procedural map reveal bitmasks, and Barony voxel `Stat` structs.
- [ ] 🎮 **[Game Target]:** **FTL: Faster Than Light / Undertale / Hotline Miami / Dead Cells** — Inspect GameMaker `data.win` dynamic variable hash maps (`UndertaleModTool`) and Dead Cells HashLink bytecode.
- [ ] 💻 **[Systems Benchmark]:** **CMU CS:APP Binary `Bomb Lab` (`bomb`)** — Defuse all 6 assembly phases (strings, loops, switch jump tables, recursive calls, pointers, and binary search trees) in GDB/Ghidra without exploding the bomb!

---

### 🥈 Tier `C` : Unity Mono, .NET CLR & Binary File Format Auditing — `Difficulty: 4.1–4.5 / 10` | `600 EXP/Quest`
* **🔗 Prerequisite Used:** ReClass structure mapping and VMTs (`Tier C-`).
* **🆕 New Concept Unlocked:** JIT-compiled managed assemblies (`Assembly-CSharp.dll`), Cheat Engine's **Mono Dissector**, C# decompilation & IL opcode editing in **dnSpyEx**, and binary file format (`#pragma pack`) struct forging.

#### ⚔️ Tier `C` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier C+`!)
- [ ] 🔐 **[In-Repo Crackme 04]:** Disassemble [`crackme04_binary_license.exe`](./Crackmes_and_CTF/04_Struct_License_File/crackme04_binary_license.cpp) in Ghidra, reconstruct the 24-byte `BinaryLicenseHeader` struct, and write a Python `struct.pack` script to forge a valid `license.dat`!
- [ ] 🎮 **[Game Target — Completed by `deavers`]:** **Streets of Rogue (`StreetsOfRogue_v98`)** ⭐ — Use Cheat Engine's Mono Dissector to locate `Agent`, `InvDatabase`, and `Stat` classes, and hook EXP/Ammo/Money in x64 JIT code (Reference: [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT)).
- [ ] 🎮 **[Game Target]:** **Punch Club 1 & 2 / Graveyard Keeper** ⭐ — Decompile `Assembly-CSharp.dll` in **dnSpyEx**, bypass daily stat decay in Punch Club, and edit Red/Green/Blue tech points & corpse quality in Graveyard Keeper.
- [ ] 🎮 **[Game Target]:** **Enter the Gungeon / Broforce / Kingdom: Two Crowns / Moonlighter** ⭐ — Inspect `PlayerController` & `HealthHaver`, dodge-roll i-frames, coin pouch capacity, and Moonlighter merchant price thresholds.
- [ ] 🎮 **[Game Target]:** **Slime Rancher 1 / Poly Bridge / Hollow Knight / Stardew Valley & Terraria** ⭐ — Override Poly Bridge hydraulic joint max stress tensors, Hollow Knight `PlayerData` Charm Notches, and JIT-scan `Terraria.Player::Update`.
- [ ] 💻 **[Software Audit]:** **.NET Crackmes & ILSpy / dnSpyEx CIL Patching** — Decompile a protected `.NET` executable in `dnSpyEx`, edit CIL instructions (`brfalse` $\rightarrow$ `brtrue` / `ldc.i4.1`), and save the patched module.

---

### ⚡ Tier `C+` : Advanced Unity Mono, Harmony Runtime Hooking & Crypto Vaults — `Difficulty: 4.6–4.9 / 10` | `680 EXP/Quest`
* **🔗 Prerequisite Used:** `dnSpyEx` decompilation and Mono Dissector (`Tier C`).
* **🆕 New Concept Unlocked:** Writing custom C# internal mod plugins with **BepInEx & Harmony** (`[HarmonyPrefix]` / `[HarmonyPostfix]`) to hook methods at runtime without touching disk files, plus auditing encrypted binary containers.

#### ⚔️ Tier `C+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier B-`!)
- [ ] 🛠️ **[Toolcraft]:** Write a C# **BepInEx + Harmony** plugin that hooks a Unity Mono game method using `[HarmonyPrefix]` and logs/modifies its parameters at runtime.
- [ ] 🎮 **[Game Target]:** **Lethal Company (Offline Solo / Local Host Sandbox)** ⭐ — Hook `PlayerControllerB` via Harmony for infinite sprint stamina, night-vision battery, and two-handed carry weight bypass.
- [ ] 🎮 **[Game Target]:** **Unturned (Offline Singleplayer) & Subnautica: Below Zero** ⭐ — Navigate `SDG.Unturned` (`PlayerLife`, `UseableGun`) for zero recoil/spread, and Subnautica `OxygenManager` / `LiveMixin` / Seatruck crush depth.
- [ ] 🎮 **[Game Target]:** **Shadowrun Returns / RimWorld / Kerbal Space Program 1 / ULTRAKILL** ⭐ — Hook turn-based Action Points (AP), RimWorld colonist mood/skill structs, and ULTRAKILL style meter / stamina regeneration.
- [ ] 💻 **[Software / Crypto Audit]:** **KeePass 2.x (`KDBX v4` Password Database Container)** — Audit how `KeePass.exe` parses the KDBX 4.0 binary header, Argon2d/AES-256 key derivation parameters, and `ProtectedBinary` in-memory XOR protection.


---

## ⚔️ Act IV: AAA Engine Architecture (`Tiers B-` to `B+`)

### ⚔️ Tier `B-` : Mature 32/64-bit Open-World Engines, 3D Math & SQLite VM — `Difficulty: 5.0–5.3 / 10` | `770 EXP/Quest`
* **🔗 Prerequisite Used:** ReClass VMTs (`Tier C-`) and external memory trainers (`Tier E`).
* **🆕 New Concept Unlocked:** **3D Vector & Projection Math** (`Vec3`, Camera Pitch/Yaw Euler angles, $4\times 4$ `ViewProjectionMatrix` **WorldToScreen**), C++ RTTI class extraction, and database B-Tree bytecode VMs.

#### ⚔️ Tier `B-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier B`!)
- [ ] 🧪 **[In-Repo Lab 08]:** Vaporize all 3 cloaked Phantom Drones in [`lab08_3d_w2s_simulator.exe`](./Course_Solutions/Lab08_3D_Math_and_WorldToScreen/lab08_3d_w2s_simulator.cpp) by computing exact 3D Camera Pitch & Yaw Euler angles using [`w2s_math_lab.hpp`](./Tools_and_Scripts/02_3D_Math_and_W2S_Lib/w2s_math_lab.hpp)!
- [ ] 🎮 **[Game Target]:** **The Elder Scrolls V: Skyrim Special Edition (`SkyrimSE.exe`)** ⭐ — Reverse the `PlayerCharacter` singleton, `ActorValueOwner` VMT, Papyrus VM hooks, shout cooldowns, and SKSE Address Library offsets.
- [ ] 🎮 **[Game Target]:** **Mount & Blade: Warband / With Fire & Sword** ⭐ — Locate party size limits, renown/morale pointers, troop XP tables, Denars, and agent combat speed floats.
- [ ] 🎮 **[Game Target]:** **Dragon Age: Origins & II / Far Cry 2 & 3 / Xenus 2: White Gold** ⭐ — Reverse BioWare Eclipse party stat blocks, Dunia Engine weapon degradation/malaria timers, and Vital Engine ZL perk bitflags.
- [ ] 🎮 **[Game Target]:** **Fallout: New Vegas & S.T.A.L.K.E.R.: Call of Pripyat (`OpenXRay`)** — Inspect Gamebryo FormIDs, S.P.E.C.I.A.L. stats, and X-Ray Engine `CActor` radiation/dispersion floats.
- [ ] 💻 **[Software Audit]:** **SQLite3 Engine (`sqlite3.dll` / `.db` File Format)** — Reverse the 100-byte `SQLite format 3\0` header, B-Tree page layout, and trace how `sqlite3VdbeExec()` executes compiled SQL bytecode opcodes.

---

### 🛡️ Tier `B` : Source Engine (Netvars/VMT), Unreal Engine 3 & Anti-Debugging — `Difficulty: 5.4–5.7 / 10` | `860 EXP/Quest`
* **🔗 Prerequisite Used:** 3D WorldToScreen math (`Tier B-`) and VMT pointers (`Tier C-`).
* **🆕 New Concept Unlocked:** Source Engine `CreateInterface` & **Netvar** dumping (`ClientClass` linked list), `CreateMove` VMT hooking, UE3 `GObjects`/`GNames` arrays, and bypassing user-mode **Anti-Debugging** (`PEB->BeingDebugged`, `0xCC` INT3 scans).

#### ⚔️ Tier `B` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier B+`!)
- [ ] 🔐 **[In-Repo Crackme 05]:** Bypass `IsDebuggerPresent()`, `CheckRemoteDebuggerPresent()`, and the `0xCC` (`INT3`) prolog scanner in [`crackme05_antidebug.exe`](./Crackmes_and_CTF/05_AntiDebug_Sentinel/crackme05_antidebug.cpp) using Hardware Breakpoints (`DR0`–`DR3`) or ScyllaHide, and reverse the FNV-1a key check!
- [ ] 🎮 **[Game Target]:** **Counter-Strike: Source & Garry's Mod & Half-Life 2 (Offline Bots)** ⭐ — Call `CreateInterface("VClientEntityList003")`, dump `DT_BasePlayer` Netvars, extract `[3][4]` bone matrices, and render a DX9 `EndScene` ImGui ESP against offline bots.
- [ ] 🎮 **[Game Target]:** **Spec Ops: The Line / A Story About My Uncle / Alien Swarm** ⭐ — Scan UE3 `GObjects` & `GNames`, override grapple beam impulse velocity vectors, and lock squad ammo.
- [ ] 🎮 **[Game Target]:** **Injustice: Gods Among Us / Borderlands 2 / Dishonored 1** ⭐ — Extract 2.5D fighting hitbox/hurtbox bounding boxes, Super Meter gauges, and Dishonored Blink teleport distance limiters.
- [ ] 💻 **[Software / Network Audit]:** **PuTTY & WinSCP (`putty.exe` SSH Client)** — Locate in-memory SSH session structures, audit PPKv3 keyfile kdf parsing, and hook cleartext terminal buffers prior to cipher encryption.

---

### 🔥 Tier `B+` : Modern AAA x64 Proprietary Engines, Internal DLLs & Telemetry — `Difficulty: 5.8–6.1 / 10` | `960 EXP/Quest`
* **🔗 Prerequisite Used:** Source/UE3 interfaces and VMT hooking (`Tier B`).
* **🆕 New Concept Unlocked:** **Internal C++ DLL Injection (`DllMain`)**, calling unexported game functions directly via RVA function pointers, inline Trampoline Hooking (**MinHook**), and shared-memory physics telemetry.

#### ⚔️ Tier `B+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier A-`!)
- [ ] 🧪 **[In-Repo Lab 09]:** Inject [`internal_hook_lab09.dll`](./Tools_and_Scripts/03_Internal_DLL_Skeleton/dllmain_internal_hook.cpp) into [`lab09_internal_hook_target.exe`](./Course_Solutions/Lab09_Internal_DLL_and_Hooks/lab09_internal_hook_target.cpp) to invoke `Engine_SpawnMythicChest(0x1337BEEF)` directly from inside the process's address space!
- [ ] 🎮 **[Game Target]:** **Euro Truck Simulator 2 & Assetto Corsa & GRID 2** ⭐ — Reverse `eurotrucks2.exe` economy/damage floats, remove the speed limiter, and read live physics telemetry from shared memory (`scs-telemetry.dll` / `acpmf_physics`).
- [ ] 🎮 **[Game Target]:** **Grand Theft Auto V Legacy (Strictly Offline Story Mode)** ⭐ — Traverse RAGE `CPedFactory` (`WorldPtr`) and `CReplayInterface` entity lists, and study the `scrNativeCallContext` Native Invoker.
- [ ] 🎮 **[Game Target]:** **Just Cause 2 & 3 / Dying Light / Metro 2033 & Exodus / South Park: FBW** ⭐ — Modify grappling hook tensile strength, Chrome Engine 6 parkour stamina, 4A Engine gas mask filter timers, and Snowdrop grid range.
- [ ] 🎮 **[Game Target]:** **HITMAN 2 (Glacier 2) / The Witcher 3 / Cyberpunk 2077 (REDengine)** ⭐ — Dissect `ZHitman5` / `ZActor` RTTI classes, AI suspicion timers, Silent Assassin flags, and DX12/Vulkan overlay hooks.
- [ ] 💻 **[Software / Codec Audit]:** **VLC Media Player & FFmpeg (`libavcodec` / `libavformat`)** — Audit how MP4/MKV container demuxers parse nested `moov`/`trak` box headers and SIMD (`AVX2`) video decode buffers.

---

## 🥇 Act V: Modern Reflection & Native Transpilation (`Tiers A-` to `A+`)

### 🥇 Tier `A-` : Unreal Engine 4 & 5 (`GWorld`, `FNamePool` & SDK Dumping) — `Difficulty: 6.2–6.5 / 10` | `1,100 EXP/Quest`
* **🔗 Prerequisite Used:** Internal DLL injection and 64-bit RTTI structs (`Tier B+`).
* **🆕 New Concept Unlocked:** Modern Unreal Engine 4/5 reflection (`UObject`, `UStruct`, `UFunction`, `UObject::ProcessEvent`), `FNamePool` chunked string tables, and automated C++ SDK generation with **Dumper-7**.

#### ⚔️ Tier `A-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier A`!)
- [ ] 🛠️ **[Toolcraft]:** Run **Dumper-7** on any Unreal Engine 4 or 5 offline game to generate a full C++ SDK (`SDK.hpp`), and locate `GWorld`, `FNamePool`, and `GUObjectArray` RVAs in Ghidra.
- [ ] 🎮 **[Game Target]:** **KovaaK's (Offline Aim Trainer Sandbox)** ⭐ — Traverse `UWorld -> PersistentLevel -> Actors` to locate bot targets, read 3D capsule coordinates, and hook `UObject::ProcessEvent`.
- [ ] 🎮 **[Game Target]:** **Escape the Backrooms & Breathedge** ⭐ — Freeze sanity decay, build an `FNamePool` entity ESP to visualize stalker AI navigation in the Backrooms, and lock oxygen in Breathedge.
- [ ] 🎮 **[Game Target]:** **Manor Lords & Palworld (Offline Singleplayer)** ⭐ — Traverse UE5 `GWorld` actor arrays, inspect Pal capture rate formulas, work speed, technology points, and Manor Lords regional wealth.
- [ ] 🎮 **[Game Target]:** **The Outlast Trials / PEAK / Lies of P / Deep Rock Galactic (Solo)** ⭐ — Reverse night-vision battery structs, climbing grip stamina in `PEAK`, and UE5 parry window frames.
- [ ] 💻 **[Software / OS Internals]:** **Sysinternals Suite (`Procmon64.exe` / `System Informer`)** — Reverse how user-mode monitoring tools invoke `ntdll.dll` (`NtQuerySystemInformation`, `NtQueryObject`) and parse ETW/kernel telemetry buffers.

---

### 🏆 Tier `A` : Unity IL2CPP (Stripped Metadata & Native x64 Assembly) & Custom VMs — `Difficulty: 6.6–6.9 / 10` | `1,250 EXP/Quest`
* **🔗 Prerequisite Used:** Unity Mono (`Tier C`) and native x64 disassembly (`Tier B+`).
* **🆕 New Concept Unlocked:** Reversing **Unity IL2CPP** (`GameAssembly.dll` + `global-metadata.dat` via **Il2CppDumper**), hooking transpiled C#-to-C++ methods with **MinHook**, and disassembling custom **Stack Virtual Machine** bytecode.

#### ⚔️ Tier `A` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier A+`!)
- [ ] 🔐 **[In-Repo Crackme 06]:** Reverse `ExecuteVirtualMachine()` and `g_BytecodeProgram[]` in [`crackme06_bytecode_vm.exe`](./Crackmes_and_CTF/06_Custom_Stack_VM/crackme06_bytecode_vm.cpp), and run/extend our Python VM Disassembler ([`crackme_solvers_and_z3_lab.py`](./Tools_and_Scripts/04_Python_RE_Toolkit/crackme_solvers_and_z3_lab.py)) to recover the 8-byte key!
- [ ] 🎮 **[Game Target]:** **Aimlabs (Offline Local Training Tasks)** ⭐ — Run **Il2CppDumper** on `GameAssembly.dll` + `global-metadata.dat`, import `script.json` into Ghidra, and reverse target spawn state machines & camera matrices.
- [ ] 🎮 **[Game Target]:** **Slime Rancher 2 & RV There Yet?** ⭐ — Reconstruct stripped IL2CPP classes and hook `PlayerState` / `Vacpack` methods via **MelonLoader** or native **MinHook**.
- [ ] 🎮 **[Game Target]:** **Risk of Rain 2 / Sons of the Forest / Dyson Sphere Program / SPT-AKI** — Hook `CharacterBody::RecalculateStats`, reverse `VailActor` AI structs, and study SPT-AKI `BifacialTransform` skeletal bone trees.
- [ ] 💻 **[Software / Protocol Audit]:** **Wireshark (`libwireshark.dll` Dissector Architecture)** — Reverse how protocol dissectors register header fields and write a custom Lua/C packet dissector for a local game protocol.

---

### 💎 Tier `A+` : Hybrid C++/Lua Engines, Code Integrity Guards & Executable Packers — `Difficulty: 7.0–7.3 / 10` | `1,400 EXP/Quest`
* **🔗 Prerequisite Used:** Native hooks (`Tier A`) and VMT redirection (`Tier C-`).
* **🆕 New Concept Unlocked:** Bridging native C++ with embedded **Lua / LuaJIT** VMs (`lua_State*`, `luaL_loadbuffer`), bypassing `.text` **CRC32 Code Integrity Guards** + XOR-encrypted RAM, and manual unpacking of **UPX** executables (`OEP` + `Scylla` IAT fix).

#### ⚔️ Tier `A+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier S-`!)
- [ ] 🧪 **[In-Repo Lab 10 — BOSS FIGHT]:** Defeat the Archon of Silicon (`1,000,000 HP`) in [`lab10_integrity_boss.exe`](./Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp) without triggering the `.text` FNV/CRC Integrity Panic—either by redirecting `g_CombatDispatcher` (VMT style) or computing `g_EncryptedHeroAttack ^ g_XorCookie`!
- [ ] 🎮 **[Game Target]:** **PAYDAY 2 (Offline Crime.Net Solo Mode)** ⭐ — Reverse how **SuperBLT** hooks `lua_call` / `luaL_loadbuffer` inside `payday2_win32_release.exe` (`Diesel Engine 2.0` + `LuaJIT`), and inspect `tweak_data` & pager counters.
- [ ] 🎮 **[Game Target]:** **Don't Starve Together (Offline World) & Starbound** ⭐ — Hook embedded `lua_State*` to inspect `ThePlayer.components.health` in Don't Starve, and reverse Starbound's C++ `WorldClient` / `Player` structs.
- [ ] 🎮 **[Game Target]:** **Civilization VI / Total War: SHOGUN 2 / Surviving Mars** ⭐ — Reverse turn-based strategy state sync, Fog of War (`MapVisibility`) bitmasks, and treasury pointers.
- [ ] 🎮 **[Game Target]:** **Sword Art Online: Hollow Realization / Dragon Age: Inquisition / Baldur's Gate 3** ⭐ — Reverse Japanese PhyreEngine SP/Burst layouts, EA Frostbite 3 `ClientGameContext` / `TypeInfo` reflection, and Capcom RE Engine / BG3 ECS pools.
- [ ] 💻 **[Software / Unpacking Lab]:** **UPX Packed Binary (`upx -9`)** — Pack any of our C++ labs with UPX, observe its `>7.5` Shannon entropy using [`pe_and_aob_scanner.py`](./Tools_and_Scripts/04_Python_RE_Toolkit/pe_and_aob_scanner.py), single-step the decompression stub in x64dbg to the tail-jump **Original Entry Point (OEP)**, and dump/rebuild the IAT with **Scylla**!


---

## 🌟 Act VI: Elite Systems, DOD & Console Emulation (`Tiers S-` to `SS+`)

### 👑 Tier `S-` : Soulslike Proprietary Engines, Havok Physics & Param Tables — `Difficulty: 7.4–7.6 / 10` | `1,600 EXP/Quest`
* **🔗 Prerequisite Used:** Internal hooks, DX12 overlays, and RTTI hierarchies (`Act V`).
* **🆕 New Concept Unlocked:** Intricate animation event state machines (Invincibility frames / `i-frames`, parry windows), Havok physics character controllers, and memory-mapped `Param` regulation tables.

#### ⚔️ Tier `S-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier S`!)
- [ ] 🎮 **[Game Target]:** **Dark Souls III & Sekiro: Shadows Die Twice (Strictly Offline)** — Traverse `WorldChrMan` singletons, inspect animation i-frame flags, lock Sekiro posture bars, and patch in-memory `Param` tables.
- [ ] 🎮 **[Game Target]:** **Elden Ring + Shadow of the Erdtree (Strictly Offline / EAC Disabled)** — Navigate Dantelion 2 `CSChrIns` hierarchies, `SpEffect` buff IDs, Poise floats, and render a DX12 command-queue ImGui hitbox viewer.
- [ ] 🎮 **[Game Target]:** **Armored Core VI & Monster Hunter: World (Offline Solo)** — Reverse EN generator recovery delays, ACS stagger gauges, and MT Framework monster part break thresholds.
- [ ] 💻 **[Software / Engine Audit]:** **Blender (`.blend` DNA Parser) & Godot Engine (`ClassDB`)** — Reverse how Blender serializes C struct definitions directly inside `.blend` `SDNA` blocks and how Godot binds native C++ methods.

---

### 🌟 Tier `S` : Data-Oriented Design (DOD), Custom Allocators, O-LLVM & MBA — `Difficulty: 7.7–7.9 / 10` | `1,800 EXP/Quest`
* **🔗 Prerequisite Used:** Custom VMs (`Tier A`) and ECS layouts (`Tier A+`).
* **🆕 New Concept Unlocked:** Cache-aligned **Structure of Arrays (SoA)** slab allocators, cellular automata pixel grids, **O-LLVM Control-Flow Flattening (CFF)** state machines, and **Mixed Boolean-Arithmetic (MBA)** simplification.

#### ⚔️ Tier `S` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier S+`!)
- [ ] 🔐 **[In-Repo Crackme 07]:** Collapse the Mixed Boolean-Arithmetic identities (`MBA_Add` & `MBA_Xor`) and trace the flattened `while(state)` switch dispatcher in [`crackme07_cff_mba.exe`](./Crackmes_and_CTF/07_Control_Flow_Maze_and_MBA/crackme07_cff_mba.cpp) to recover `K0-K1`!
- [ ] 🎮 **[Game Target]:** **Factorio & Noita** — Reverse Factorio's deterministic slab allocators & belt math, and Noita's `FallingEverything` cellular automata pixel simulation grid & wand recharge structs.
- [ ] 🎮 **[Game Target]:** **Teardown / Dwarf Fortress (`DFHack`) / Mount & Blade II: Bannerlord** — Inspect 3D voxel octree buffers in Teardown, historical entity vectors in Dwarf Fortress, and Bannerlord's native-to-managed P/Invoke bridge.
- [ ] 💻 **[Software / Runtime Audit]:** **PyInstaller / Electron (`app.asar` & V8 Bytecode Snapshots)** — Extract embedded CArchive `.pyc` code objects, repair stripped Python magic headers, and decompile bytecode.

---

### 🪐 Tier `S+` : Console Emulators, Big-Endian Memory & Cross-Arch JIT — `Difficulty: 8.0–8.2 / 10` | `2,000 EXP/Quest`
* **🔗 Prerequisite Used:** x86_64 assembly (`Stage 2`) and custom VMs (`Tier A`).
* **🆕 New Concept Unlocked:** Reversing non-x86 guest CPU architectures (**PowerPC 32-bit Big-Endian**, **Nintendo Switch ARM64**, **PS3 Cell PPU/SPU**, **PS2 MIPS R5900**) translated inside an x64 host emulator process.

#### ⚔️ Tier `S+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SS-`!)
- [ ] 🎮 **[Emulator Target]:** **Zelda: Breath of the Wild (via Cemu)** — Register `4 Byte Big Endian` & `Float Big Endian` types in Cheat Engine, resolve Cemu's `memory_base`, and patch PowerPC instructions.
- [ ] 🎮 **[Emulator Target]:** **Zelda: Tears of the Kingdom (via Ryujinx / Sudachi)** — Analyze Switch `main` NSO binaries, ARM64 (`AArch64`) instructions (`LDR`, `STR`, `B.NE`, `FMOV`), and Ultrahand physics.
- [ ] 🎮 **[Emulator Target]:** **Persona 5 / Demon's Souls (RPCS3) & Bloodborne (shadPS4) & Shadow of the Colossus (PCSX2)** — Navigate RPCS3 `0x300000000` Big-Endian mappings, shadPS4 System V AMD64 ABI `.sprx` modules, and PCSX2 MIPS assembly.
- [ ] 💻 **[Emulator Core Audit]:** **QEMU / Unicorn Engine (`TCG` Tiny Code Generator)** — Trace how QEMU translates a guest ARM64 or MIPS basic block into host `x86_64` JIT machine code in memory.

---

### 🧬 Tier `SS-` : JVM Native Interface (JNI/JVMTI), Protocol Crypto & OpenSSL — `Difficulty: 8.3–8.5 / 10` | `2,250 EXP/Quest`
* **🔗 Prerequisite Used:** Internal DLLs (`Tier B+`) and bitwise crypto (`Tier D`).
* **🆕 New Concept Unlocked:** Attaching to the **Java Virtual Machine (JNI/JVMTI)** from native C++, reversing custom binary network protocol encryption (**Blowfish / RSA / XOR stream ciphers**), and identifying standard cryptographic primitives in stripped binaries.

#### ⚔️ Tier `SS-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SS`!)
- [ ] 🎮 **[Protocol Lab]:** **Lineage 2 Chronicle 2 (`L2.exe` Client & Custom C++ Server Protocol Lab)** ⭐ — Reverse `L2.exe` packet serialization opcodes (`LoginServer` Blowfish + RSA exchange, `GameServer` XOR cipher) and match client structs in [`deavers/L2C2-Study-Server`](https://github.com/deavers/L2C2-Study-Server).
- [ ] 🎮 **[Engine & Replay Lab]:** **osu! (Offline Local Client / `osu!framework` Memory & Replay Analysis)** ⭐ — Reverse `.osr` LZMA replay binary structures, cursor trajectory smoothing math, and mixed-mode `.NET` assemblies.
- [ ] 🎮 **[JVM Target]:** **Minecraft: Java Edition (Offline Singleplayer)** — Inject a C++ DLL that attaches to the JVM via `JNI_GetCreatedJavaVMs` & `JVMTI`, resolves ProGuard/Mojang obfuscated mappings, and inspects runtime classes.
- [ ] 💻 **[Crypto Library Audit]:** **OpenSSL (`libcrypto`) & `libsodium` Binary Auditing** — Locate AES S-Boxes / AES-NI instructions (`aesenc`), SHA-256 initial state constants (`0x6a09e667`), and ChaCha20 quarter-round (`QR`) routines in a stripped binary.

---

### 🌌 Tier `SS` : Procedural Math Engines, Custom Packers & Legacy Ring-3 DRM — `Difficulty: 8.6–8.8 / 10` | `2,500 EXP/Quest`
* **🔗 Prerequisite Used:** UPX unpacking (`Tier A+`) and stream ciphers (`Tier SS-`).
* **🆕 New Concept Unlocked:** Writing and reversing custom **Reflective PE/ELF Loaders**, ChaCha20 encrypted stubs (`Shannon Entropy` $H \approx 7.99$), and rebuilding broken **Import Address Tables (IAT)** from legacy Ring-3 protectors.

#### ⚔️ Tier `SS` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SS+`!)
- [ ] 🛠️ **[Packer Lab]:** **Custom ELF64 / PE64 ChaCha20 Packer & Reflective Loader** ⭐ — Reverse an encrypted packer stub (`memfd_create` / `VirtualAlloc`) from [`deavers/lowlevel-re-and-exploitation`](https://github.com/deavers/lowlevel-re-and-exploitation) and write an automated Python unpacker.
- [ ] 🎮 **[Game Target]:** **No Man's Sky (Offline Mode)** — Reverse procedural generation seed hashes, voxel terrain noise functions, and packed binary save-state structures.
- [ ] 🎮 **[Legacy DRM Study]:** **Vintage Offline Games Protected with SecuROM / SafeDisc** — Locate the obfuscated tail jump to the Original Entry Point (OEP), dump process memory with **Scylla**, and repair import thunks.
- [ ] 💻 **[CTF Benchmark]:** **Mandiant FLARE-On CTF Challenges (Stages 1–5)** — Solve real-world multi-layered PE/shellcode/.NET reverse engineering challenges from the annual FLARE-On archive.

---

### 🔒 Tier `SS+` : Commercial Virtualizers (VMProtect / Themida) & Arxan Guards — `Difficulty: 8.9–9.1 / 10` | `2,800 EXP/Quest`
* **🔗 Prerequisite Used:** Custom Stack VMs (`Tier A`), O-LLVM/MBA (`Tier S`), and integrity guards (`Lab 10`).
* **🆕 New Concept Unlocked:** Analyzing commercial stack/register **Code Virtualizers (`VMProtect`, `Themida`)**, tracing `VM_Enter` & Virtual Instruction Pointers (`VIP`), and bypassing multi-threaded self-healing checksum mesh networks (**Arxan**).

#### ⚔️ Tier `SS+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SSS-`!)
- [ ] 🎮 **[Integrity Guard Study]:** **Red Dead Redemption 2 & Need for Speed (Offline Checksum Study)** ⭐ — Analyze Arxan integrity verification threads that hash `.text` pages, and implement stealth VMT / Hardware Breakpoint (`DR0`–`DR3`) hooks that leave `.text` untouched.
- [ ] 🔐 **[Virtualizer Lab 1]:** **CrackMe Protected with VMProtect v2/v3 (Mutation + Virtualization)** — Trace `VM_Enter`, log `VIP` handler dispatches across `.vmp0`/`.vmp1` sections, and identify virtualized Win32 API exits.
- [ ] 🔐 **[Virtualizer Lab 2]:** **CrackMe Protected with Themida / WinLicense** — Recover stolen OEP prologue bytes, unwrap obfuscated import thunks, and trace CISC VM context structures.

---

## 🌌 Act VII: The Pantheon of Silicon & Symbolic Execution (`Tiers SSS-` to `SSS++`)

### 🧩 Tier `SSS-` : Symbolic Execution (`Z3` / `angr`), Dynamic Taint & MBA Solvers — `Difficulty: 9.2–9.4 / 10` | `3,200 EXP/Quest`
* **🔗 Prerequisite Used:** O-LLVM Control-Flow Flattening & MBA (`Tier S`).
* **🆕 New Concept Unlocked:** Automated constraint solving with the **Z3 Theorem Prover (SMT)**, binary path exploration with **`angr`**, Dynamic Taint Analysis with **Triton**, and automated CFG deflattening.

#### ⚔️ Tier `SSS-` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SSS`!)
- [ ] 🔐 **[In-Repo Crackme 08 — FINAL DOJO BOSS]:** Model the 10 coupled algebraic/XOR equations of [`crackme08_z3_symbolic.exe`](./Crackmes_and_CTF/08_Symbolic_Execution_Vault/crackme08_z3_symbolic.cpp) in Python **Z3** (or run [`crackme_solvers_and_z3_lab.py`](./Tools_and_Scripts/04_Python_RE_Toolkit/crackme_solvers_and_z3_lab.py)) to synthesize the exact 8-character master flag!
- [ ] 🛠️ **[Toolcraft]:** Write a **Ghidra / Binary Ninja Python script** or **Miasm** symbolic deflattener that automatically removes O-LLVM switch dispatchers and restores the original Control Flow Graph (CFG).
- [ ] 🛠️ **[MBA Solver Lab]:** Use **Z3**, **Arybo**, or **GAMBA** to automatically simplify 50-instruction polynomial Mixed Boolean-Arithmetic (MBA) expressions back into single instructions.
- [ ] 💻 **[Automated Solver]:** **Automated CrackMe & Bomb-Lab Solver with `angr` & `AFL++`** ⭐ — Define symbolic bitvectors (`claripy.BVS`) over input buffers, prune explosion paths (`avoid=`), and auto-solve multi-stage binary constraints.

---

### ⚡ Tier `SSS` : Ring-0 Kernel Drivers, Hypervisor EPT & QEMU/KVM VMI — `Difficulty: 9.5–9.7 / 10` | `3,600 EXP/Quest`
* **🔗 Prerequisite Used:** OS Internals (`Tier A-`) and Anti-Debug (`Tier B`).
* **🆕 New Concept Unlocked:** Out-of-process and out-of-VM memory introspection: walking **x64 `CR3` Page Tables (`PML4` $\rightarrow$ `PDPT` $\rightarrow$ `PD` $\rightarrow$ `PT`)** from a Linux KVM host, Ring-0 Windows Kernel Drivers (`WDK`), and Intel VT-x / AMD-V **Extended Page Table (EPT)** shadow hooking.

#### ⚔️ Tier `SSS` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SSS+`!)
- [ ] 🖥️ **[Thesis & VMI Lab]:** **QEMU/KVM Virtual Machine Memory Introspection (Linux Host $\rightarrow$ Guest)** ⭐ — Read a guest process's virtual memory directly from the Linux host (`memflow` / `libvmi` / `/dev/shm`) by walking the x64 **CR3 Page Table Hierarchy** with zero footprint inside the guest OS!
- [ ] 🛠️ **[Ring-0 Driver Lab]:** **Custom Windows Kernel Driver (`WDK`) for Educational Memory Inspection** — Implement `IoCreateDevice`, `IRP_MJ_DEVICE_CONTROL` (`IOCTL`), `MmCopyVirtualMemory`, and `EPROCESS` walking inside a safe test-signing VM.
- [ ] 🔐 **[Anti-Debug Master Lab]:** **ScyllaHide / TitanHide Testbed** — Bypass `NtQueryInformationProcess` (`ProcessDebugPort`, `ProcessDebugObjectHandle`), TLS Callback traps, `RDTSC` timing deltas, and `NtSetInformationThread(ThreadHideFromDebugger)`.
- [ ] 🛠️ **[Hypervisor Lab]:** **Tiny VT-x / AMD-V Hypervisor EPT Shadow Page Hooking** — Split instruction TLB (`Execute-Only`) vs data TLB (`Read/Write`) views on a single physical page so checksum reads see original bytes while CPU execution runs your hook.

---

### 💀 Tier `SSS+` : Full Matching Decompilation & 64-bit Planetary Engines — `Difficulty: 9.8–9.9 / 10` | `4,200 EXP/Quest`
* **🔗 Prerequisite Used:** Deep C++ compiler codegen and engine architecture (`Acts IV–VI`).
* **🆕 New Concept Unlocked:** Reconstructing commercial binaries back into **compilable C/C++ source code that produces a $100\%$ byte-for-byte identical binary**, and authoring custom **Ghidra SLEIGH** processor specifications.

#### ⚔️ Tier `SSS+` Mastery Quests (Complete any 3 for `+3 TP` $\rightarrow$ Rank Up to `Tier SSS++`!)
- [ ] 💻 **[Matching Decomp]:** **Matching Decompilation Contribution (`decomp.me` / *DevilutionX* / *Super Mario 64* / *Zelda OoT*)** — Take a raw assembly function on `decomp.me` and tune C/C++ code + compiler flags until it reaches a **$100.0\%$ byte-accurate match**!
- [ ] 🎮 **[Engine Reimplementation]:** **OpenMW (*Morrowind*) / OpenRCT2 (*RollerCoaster Tycoon 2*) / OpenXRay** — Reverse engineer proprietary `.NIF`/`.ESM`/`.DAT` binary formats and physics state machines into clean open-source C++.
- [ ] 🎮 **[Planetary Engine Study]:** **Star Citizen (Offline Arena Commander Sandbox)** — Analyze 64-bit `double`-precision planetary world coordinates, nested Local Physics Grids, and entity component snapshots.
- [ ] 🛠️ **[Decompiler Dev]:** **Ghidra Custom SLEIGH Processor Specification** — Write a `.slaspec` processor module in Ghidra to disassemble and lift an undocumented proprietary bytecode or retro CPU.

---

### 👑🌌 Tier `SSS++` : Demigod of Silicon (LLVM Lifters, Hardware Crypto & Glitching) — `Difficulty: 10.0 / 10` | `5,000 EXP/Quest`
* **🔗 Prerequisite Used:** All previous 27 Tiers.
* **🆕 New Concept Unlocked:** Lifting virtualized/obfuscated machine code into **LLVM Intermediate Representation (`LLVM IR`)**, dynamic binary translation JITs, GPU shader bytecode (`DXIL`/`SPIR-V`) decompilation, and **Hardware Fault Injection / Silicon Glitching**.

#### ⚔️ Tier `SSS++` Mastery Quests (Complete any 3 to Achieve `100% Campaign Godhood`!)
- [ ] 🛠️ **[LLVM Binary Lifter]:** **Automated VM / Obfuscated Binary Lifter to LLVM IR (`Remill` / `McSema` / Custom Pass)** — Lift a virtualized function into LLVM IR, run `opt -O3` dead-code elimination to strip obfuscation, and recompile to clean native `x86_64`!
- [ ] 🔌 **[Hardware & BootROM Lab]:** **Silicon/Firmware Glitching & Embedded BootROM RE** ⭐ — Dump SPI/UART/JTAG firmware on ESP32-S3 / ARM Cortex-M ([`deavers/iot-hardware-arsenal`](https://github.com/deavers/iot-hardware-arsenal)), analyze bootloaders in Ghidra, and perform voltage glitching fault injection.
- [ ] 🎮 **[Arcade Crypto Security]:** **Arcade Hardware Dongle & Board Emulation (Sega Lindbergh / Taito Type X)** — Reverse USB security dongles (HASP/Sentinel), JVS I/O boards, and TPM/EEPROM cryptographic handshakes.
- [ ] 🛠️ **[GPU Shader RE]:** **Custom Graphics Wrapper (`d3d11.dll` / `dxgi.dll` Proxy) & Shader Decompiler** — Intercept compiled HLSL `DXBC`/`DXIL` or `SPIR-V` shaders at runtime, extract projection constant buffers (`cbuffer`), and inject compute shaders.

---

## 🛠️ Autonomous Community & Custom Targets (`5-Axis Rubric Verified`)

Want to add your own favorite offline games or software targets to this roadmap?  
Add them to [`data/custom_targets.json`](./data/custom_targets.json) (or run `python Tools_and_Scripts/rpg_manager.py --add-target`) and run `.\update_progress.bat`. Their difficulty score and RPG Tier are **computed automatically by our 5-Axis Technical Rubric** and synced into the table below:

<!-- CUSTOM_TARGETS_START -->
| Status | Computed Tier | Rubric Score | Category | Target Title | Engine / Arch | Quest Objective |
| :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| - [ ] | **E+** | `2.2 / 10` | Game | **Balatro (Offline Deckbuilder)** | LÖVE 2D Framework (LuaJIT + C++) | Unpack the LÖVE2D archive appended to `Balatro.exe`, inspect Lua state variables (`G.GAME.dollars`, `G.GAME.chips`), and hook chip multiplier scoring. |
| - [ ] | **C+** | `4.5 / 10` | Software | **KeePass 2.x (KDBX v4 Vault Format Audit)** | .NET CLR / Custom KDBX Binary Container | Audit how `KeePass.exe` parses the KDBX 4.0 binary header, Argon2d/AES-256-CBC key derivation parameters, and DPAPI protected in-memory strings (`ProtectedBinary`). |
<!-- CUSTOM_TARGETS_END -->

---

## 🧰 Complete Reverse Engineering Toolbox

| Category | Primary Tools | Purpose |
| :--- | :--- | :--- |
| **Memory Scanners** | **Cheat Engine 7.5+**, CrySearch, PINCE (Linux) | Dynamic memory scanning, pointer maps, Auto Assembler (`.CEA`) |
| **Dynamic Debuggers** | **x64dbg / x32dbg**, WinDbg Preview, GDB (`pwndbg`) | Step-by-step execution, hardware/memory breakpoints, tracing |
| **Static Disassemblers** | **Ghidra**, **IDA Pro / Free**, **Binary Ninja** | Decompilation to C pseudocode, CFG analysis, XREFs, RTTI |
| **Class Reconstruction** | **ReClass.NET** | Live C++ structure and VMT reconstruction in memory |
| **.NET & Unity Tools** | **dnSpyEx**, **ILSpy**, **Il2CppDumper**, **BepInEx / Harmony** | C# decompilation, IL patching, IL2CPP metadata recovery |
| **Unreal Engine Tools** | **Dumper-7**, **UESDK**, **FModel**, **UAssetGUI** | Automated SDK generation (`GObjects`, `GNames`, `GWorld`) |
| **PE/ELF & Process Analysis** | **System Informer**, **PE-bear**, **Detect It Easy (DIE)**, **Scylla** | Inspecting headers, sections, threads, handles, and IAT reconstruction |
| **Symbolic Execution & DBI** | **Z3 Theorem Prover**, **angr**, **Triton**, **Frida** | Automated constraint solving, MBA de-obfuscation, dynamic hooks |
| **Development Stack** | **Visual Studio 2022 (MSVC)**, **MinHook**, **Dear ImGui** | Writing C++20 internal DLLs, trampoline hooks, and DX11/12/OpenGL UIs |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.
