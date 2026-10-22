# 🛡️ Reverse Engineering & Offline Game Hacking Journey

![Focus](https://img.shields.io/badge/Focus-Offline%20Reverse%20Engineering-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20x86%20%2F%20x64%20%7C%20Linux-informational?style=for-the-badge)
![Status](https://img.shields.io/badge/Current%20Rank-Tier%20C%20(Adventurer)-success?style=for-the-badge)
![Targets](https://img.shields.io/badge/Roadmap-28%20Tiers%20(F--%20to%20SSS%2B%2B)%20%7C%20190%2B%20Targets-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **⚠️ Educational Disclaimer:** This repository documents my personal learning journey in **Low-Level Systems Architecture, x86/x64 Assembly, Binary Auditing, and Dynamic Memory Analysis**. All research, Cheat Engine tables (`.CT`), and tools in this repository target **strictly local, single-player, offline games, emulators, and crackmes**. There is zero involvement with multiplayer cheats, online competitive services, or server-side exploitation.

---

## 📂 Repository Structure & Current Progress

```text
Reverse-Engineering-Journey/
├── 📁 Course_Solutions/       # Notes, exercises, and binary analysis labs from RE courses
├── 📁 Crackmes_and_CTF/       # Keygenmes, reverse engineering CTF writeups, and binary patches
├── 📁 Game_Hacking/           # Cheat Engine tables (.CT), Auto Assembler scripts, & trainers
│   ├── 📄 PvZ.CT                      # [Tier E+] Plants vs. Zombies (GOTY)
│   ├── 📄 UnrealTournament_UT99.CT    # [Tier D]  Unreal Tournament 99 (UE1)
│   ├── 📄 isaac-ng.CT                 # [Tier C-] The Binding of Isaac: Repentance
│   ├── 📄 StreetsOfRogue_v98.CT       # [Tier C]  Streets of Rogue (v98 Unity)
│   └── 📄 README.md                   # Detailed breakdown of offsets, pointers & scripts
├── 📁 Tools_and_Scripts/      # Custom C++/Python memory utilities, pointer scanners, & SDK dumpers
├── 📄 .gitignore              # Clean filtering for IDA/Ghidra/VS/CE temporary artifacts
├── 📄 LICENSE                 # MIT License
└── 📄 README.md               # Main documentation & F- to SSS++ Game RE Roadmap
```

### 🎯 Completed Milestones in `Game_Hacking/`

| Target Binary | Game Title | Engine / Arch | Tier | Difficulty | Status | Artifact |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| `PlantsVsZombies.exe` | **Plants vs. Zombies GOTY** | PopCap Framework (x86) | **E+** | `2.2 / 10` | ✅ Done | [`PvZ.CT`](./Game_Hacking/PvZ.CT) |
| `UnrealTournament.exe` | **Unreal Tournament 99** | Unreal Engine 1 (x86) | **D** | `3.0 / 10` | ✅ Done | [`UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT) |
| `isaac-ng.exe` | **The Binding of Isaac: Repentance** | Custom C++20 Engine (x86) | **C-** | `4.2 / 10` | ✅ Done | [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT) |
| `StreetsOfRogue.exe` | **Streets of Rogue (v98)** | Unity Engine Mono (x64) | **C** | `4.6 / 10` | ✅ Done | [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT) |

---

## 🎮 Personal Target Arsenal (Tailored to My Steam Library & Interests)

To keep motivation at $100\%$, this roadmap integrates games directly from my personal Steam library (recent purchases and most-played single-player/offline titles over the last 5 years) across my favorite genres:

1. **🎯 3D Aim Trainers & Classic Arena Shooters (`AimHero`, `Aimlabs`, `KovaaK's`, `Half-Life 1/2`, `DOOM + DOOM II`, `UT99`, `POSTAL 2`, `Quake`):**
   * *Why it fits:* Perfect legal, single-player sandboxes for mastering **3D Linear Algebra**, $4 \times 4$ **View-Projection Matrices**, **WorldToScreen (W2S)** overlays, Pitch/Yaw Euler angle math, and entity target arrays.
2. **🗡️ 2D Action Roguelikes, Bullet-Hells & Precision Arcade (`Binding of Isaac`, `Enter the Gungeon`, `Broforce`, `Castle Crashers`, `Moonlighter`, `Barony`, `Chasm`, `Secrets of Grindea`, `UBERMOSH`, `Geometry Dash`, `osu!` offline):**
   * *Why it fits:* Ideal for dissecting dynamic entity linked lists, i-frame/dodge timers, weapon cooldown state machines, procedural room grids, and PRNG seed predictors.
3. **🏰 Management RPGs, Colony Sims & Grand Strategy (`Punch Club 1 & 2`, `Graveyard Keeper`, `Kingdom: Classic & Two Crowns`, `Terraria`, `Stardew Valley`, `Starbound`, `Don't Starve Together`, `Civilization VI`, `Manor Lords`, `Total War: SHOGUN 2`, `Crusader Kings II`, `SPORE`, `Slime Rancher 1 & 2`, `Poly Bridge`, `Scribblenauts`):**
   * *Why it fits:* Rich `.NET`/Mono assemblies, embedded Lua VMs, and complex resource/stat data structures that reward **dnSpyEx**, **Harmony**, and **ReClass.NET** structure mapping.
4. **🕵️ Stealth, Immersive Action & Open-World Sandboxes (`Splinter Cell: Chaos Theory`, `HITMAN 2`, `PAYDAY 2` Offline Solo, `GTA V` Story Mode, `Just Cause 2 & 3`, `Dying Light`, `Assassin's Creed II`, `Mount & Blade: Warband`, `Skyrim SE`, `Dragon Age: Origins / II / Inquisition`, `Far Cry 1 & 2`, `Metro 2033`, `Spec Ops: The Line`, `Subnautica: Below Zero`):**
   * *Why it fits:* Deep C++ inheritance trees, RTTI class reconstruction, AI stealth detection cones, ballistics physics, and internal DX11/DX12 hooking.
5. **🏎️ Driving/Physics Simulators, Anime Action RPGs, Indie Horror & Retro/LEGO (`Euro Truck Simulator 2`, `Assetto Corsa`, `GRID 2`, `Sword Art Online: Hollow Fragment / Lost Song / Hollow Realization`, `Lethal Company`, `Escape the Backrooms`, `The Outlast Trials`, `PEAK`, `A Story About My Uncle`, `South Park: The Fractured But Whole`, `Injustice: Gods Among Us`, `LEGO Star Wars / Batman / LOTR`, `SEGA Genesis / Bonanza Bros.`, `Lineage 2 C2` offline server/client):**
   * *Why it fits:* Covers everything from real-time vehicle telemetry (`Prism3D` / `Assetto Corsa` shared memory & physics structs) and retro 16-bit Motorola 68000 emulation to custom network packet protocol analysis.

*(Games marked with ⭐ below are directly in my personal Steam library / active backlog).*

---

## 🗺️ The 6-Stage Game Reverse Engineering Roadmap

### Stage 1: Memory Fundamentals & Dynamic Scanning (Cheat Engine)
* Virtual Memory Architecture, Pages, and Protection Flags (`PAGE_EXECUTE_READWRITE`).
* Data representations: `Byte`, `Int16`, `Int32`, `Int64`, `Float`, `Double`, IEEE-754, and Bitmasks.
* Static Base Addresses (`module.exe + 0xOFFSET`) vs. Dynamic Heap Allocations.
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
* Resolving Multi-Level Pointers programmatically:
  $$\text{FinalAddress} = \left[\left[\dots\left[\left[\text{Base} + \Delta_1\right] + \Delta_2\right]\dots\right] + \Delta_{n-1}\right] + \Delta_n$$

### Stage 4: Internal Development, DLL Injection & Function Hooking
* Anatomy of a Dynamic Link Library (`DllMain`, `DLL_PROCESS_ATTACH`, worker threads).
* Injection Techniques: `LoadLibraryA` via `CreateRemoteThread`, Thread Hijacking, and Manual Mapping (PE Header parsing, Base Relocations, IAT resolution, TLS callbacks).
* Inline / Trampoline Hooking: Overwriting function prologues ($5$-byte relative `JMP` in x86, $14$-byte absolute `JMP` in x64) and executing original bytes via a Gateway using **MinHook** or **Microsoft Detours**.
* Virtual Method Table (VMT) Hooking: Swapping function pointers in C++ class vtables.

### Stage 5: Engine Internals, Class Reconstruction & SDK Generation
* Live Memory Class Reconstruction using **ReClass.NET** (mapping padding, pointers, vtables, arrays).
* Extracting C++ RTTI (`type_info`, Complete Object Locator) to automatically name classes in IDA/Ghidra.
* **Unity Mono:** Decompiling `Assembly-CSharp.dll` with **dnSpyEx** / **ILSpy** and injecting via Mono Embedding API (`mono_domain_get`, `mono_runtime_invoke`) or **Harmony / BepInEx**.
* **Unity IL2CPP:** Reversing `GameAssembly.dll` + `global-metadata.dat` using **Il2CppDumper** and **Il2CppInspector**.
* **Unreal Engine (UE3/UE4/UE5):** Navigating `GWorld`, `GNames` (`FNamePool`), and `GUObjectArray`, and generating full C++ SDKs with **Dumper-7**.

### Stage 6: 3D Math, Graphics API Hooking & Internal GUIs
* Vector & Linear Algebra in 3D Space: Euclidean distance, Dot Product, Cross Product, Euler Angles (Pitch $\theta$, Yaw $\psi$, Roll $\phi$).
* Projection Mathematics: View-Projection Matrix ($4 \times 4$) and the **WorldToScreen (W2S)** algorithm converting 3D world coordinates $(X, Y, Z)$ into 2D screen coordinates (`x_screen`, `y_screen`) via Clip Space and Normalized Device Coordinates ($\text{NDC} \in [-1, 1]$).
* Graphics Hooking: Hooking `IDXGISwapChain::Present` / `ResizeBuffers` (DirectX 11/12), `IDirect3DDevice9::EndScene` (DX9), `wglSwapBuffers` (OpenGL), or `vkQueuePresentKHR` (Vulkan).
* Rendering custom **Dear ImGui** interactive menus and 2D/3D ESP overlays inside the game's render pipeline.

---

## 🏆 The Complete RPG Tier List of Offline Games for Reverse Engineering (`F-` $\rightarrow$ `SSS++`)

This full progression ladder spans **28 distinct RPG difficulty tiers** (filling in all sub-tiers including `F-`, `F`, `F+`, `SS-`, `SS+`, and `SSS-`) and **190+ offline targets**, with explicit difficulty ratings (`0.1 / 10` to `10.0 / 10`) based on memory indirection, architecture, engine reflection, and binary protection.

```text
╔════════════════════════════════════════════════════════════════════════════════════════╗
║                COMPLETE 28-TIER REVERSE ENGINEERING DIFFICULTY HIERARCHY               ║
╠══════════╦════════════╦════════════════════════════════════════════════════════════════╣
║   TIER   ║ DIFFICULTY ║ CORE MEMORY, ENGINE & ARCHITECTURE CHALLENGES                  ║
╠══════════╬════════════╬════════════════════════════════════════════════════════════════╣
║  SSS++   ║ 10.0 / 10  ║ Silicon Glitching, Arcade Crypto Dongles & LLVM IR Lifters     ║
║  SSS+    ║  9.8 / 10  ║ Byte-Accurate Matching Decompilation & 64-bit Space Engines    ║
║  SSS     ║  9.5 / 10  ║ Hypervisor EPT Hooking, Ring-0 Drivers & QEMU/KVM VMI          ║
║  SSS-    ║  9.2 / 10  ║ O-LLVM Control-Flow Flattening, MBA & Symbolic Execution (Z3)  ║
║  SS+     ║  8.9 / 10  ║ Commercial Virtualizers (VMProtect / Themida) & Arxan Guards   ║
║  SS      ║  8.6 / 10  ║ Custom Bytecode VMs, Encrypted Packers & Legacy Ring-3 DRM     ║
║  SS-     ║  8.3 / 10  ║ JVM Native Interface (JNI/JVMTI), Obfuscated LuaJIT & ProGuard ║
║  S+      ║  8.0 / 10  ║ Console Emulators (PowerPC Big-Endian, PS3 Cell, Switch ARM64) ║
║  S       ║  7.7 / 10  ║ Data-Oriented Design (SoA Slabs), Custom Allocators & Voxels   ║
║  S-      ║  7.4 / 10  ║ Soulslike Proprietary Engines, Havok Physics & Param Tables    ║
║  A+      ║  7.0 / 10  ║ Hybrid C++/Lua Engines, Capcom RE Engine & Divinity 4.0 ECS    ║
║  A       ║  6.6 / 10  ║ Unity IL2CPP (Stripped C# Transpiled to Native x64 Assembly)   ║
║  A-      ║  6.2 / 10  ║ Unreal Engine 4 & 5 (GWorld, FNamePool, Dumper-7 SDKs)         ║
║  B+      ║  5.8 / 10  ║ Modern AAA x64 Proprietary Engines (REDengine, RAGE, Glacier)  ║
║  B       ║  5.4 / 10  ║ Source Engine (Netvars/VMT/CreateMove) & Unreal Engine 3       ║
║  B-      ║  5.0 / 10  ║ Mature 32/64-bit Open-World Engines (Creation, Gamebryo, X-Ray)║
║  C+      ║  4.6 / 10  ║ Advanced Unity Mono, Harmony Runtime Hooking & Complex Sims    ║
║  C       ║  4.2 / 10  ║ Unity Mono & .NET CLR (dnSpyEx Decompilation & IL Patching)    ║
║  C-      ║  3.8 / 10  ║ 2D Roguelikes, Custom C++ State Machines & GameMaker Bytecode  ║
║  D+      ║  3.4 / 10  ║ Classic 32-bit Open-World, Stealth & Simulators (RenderWare)   ║
║  D       ║  3.0 / 10  ║ Early 2000s 3D Arena Shooters (UE1/UE2, GoldSrc, MAX-FX)       ║
║  D-      ║  2.6 / 10  ║ 90s Retro 2.5D/3D Engines (id Tech 1/2, Build Engine, KEX)     ║
║  E+      ║  2.2 / 10  ║ Casual 32-bit C++ Frameworks (PopCap Engine & 2D Beat-'Em-Ups) ║
║  E       ║  1.8 / 10  ║ Open-Source FPS Sandboxes & Offline 3D Aim Trainers            ║
║  E-      ║  1.4 / 10  ║ Classic Win32 Desktop Games (Static Grids, Pinball, Solitaire) ║
║  E--     ║  1.0 / 10  ║ Purpose-Built Gamified RE Tutorials & Interactive Trainers     ║
║  F+      ║  0.6 / 10  ║ Unprotected Save-Files, Plaintext Configs & Memory Snapshots   ║
║  F / F-  ║  0.2 / 10  ║ Self-Written C/C++ Console Loops & 1-Variable Memory Targets   ║
╚══════════╩════════════╩════════════════════════════════════════════════════════════════╝
```

---

### 🐣 Tier `F-` & `F` : White-Box Zero (Self-Written C/C++ Targets) — `Difficulty: 0.1–0.3 / 10`
*You have your own source code, symbols (`.pdb`), and compiler output right in front of you.*

1. **Self-Written 20-Line C++ CLI Loop (`health_ammo_target.exe`)**
   * *Difficulty:* `0.1 / 10` | *Arch:* x86 / x64 Console C++ (Debug & Release builds).
   * *Skills:* Compiling a `while` loop that prints `Health`, `Ammo`, and memory addresses (`&health`), then finding and modifying them in Cheat Engine.
2. **Self-Written C++ OOP Class & Virtual Function Target (`vtable_lab.exe`)**
   * *Difficulty:* `0.2 / 10` | *Arch:* x64 C++ with `virtual void takeDamage(int)`.
   * *Skills:* Observing how the compiler lays out the `vptr` at offset `0x00` in ReClass.NET and comparing Debug vs. `-O2` assembly in Ghidra.
3. **Bulánci-Kitty / Bonanza-Clone (My Own C / C++17 SDL2 Projects)** ⭐
   * *Difficulty:* `0.3 / 10` | *Engine:* Custom C & C++17 + SDL2 (`bonanza-clone`, `Bulanci-Kitty`).
   * *Skills:* Attaching Cheat Engine and x64dbg to your own 2D SDL2 games to see how your C structs (`Player`, `Bullet`, `TileMap`) look in compiled assembly.

---

### 📄 Tier `F+` : Unprotected State, Save-File & Clicker Memory — `Difficulty: 0.5–0.8 / 10`
*Single static integers/doubles, zero pointer indirection, or human-readable serialized state.*

4. **Banana / Clicker Heroes / Upload Labs** ⭐
   * *Difficulty:* `0.5 / 10` | *Engine:* Unity / Simple 2D Counter Frameworks.
   * *Skills:* 4-byte and `Double` exact value scans, timer acceleration via Cheat Engine Speedhack, and inspecting unencrypted PlayerPrefs/JSON state.
5. **Zup! S & Zup! Zero / Optika / Puzzle Chambers** ⭐
   * *Difficulty:* `0.6 / 10` | *Engine:* Simple 2D Physics Puzzle Frameworks.
   * *Skills:* Locating level completion boolean flags (`0` $\rightarrow$ `1`), explosion impulse floats, and puzzle timer freezes.
6. **SEGA Mega Drive & Genesis Classics (`Bonanza Bros.`, `Streets of Rage`, `Golden Axe`)** ⭐
   * *Difficulty:* `0.8 / 10` | *Engine:* Genesis/Mega Drive Emulator Wrapper (68000 RAM bank).
   * *Skills:* Finding the contiguous $64\text{ KB}$ emulated Motorola 68000 work RAM block inside the host process and locking lives, health, and timer bytes.

---

### 🌱 Tier `E--` : Purpose-Built Educational RE Labs — `Difficulty: 1.0–1.2 / 10`
*Designed specifically to teach memory scanning, pointers, and assembly patching in a guided environment.*

7. **Cheat Engine Built-in Tutorial (`Tutorial-i386.exe` & `Tutorial-x86_64.exe`)**
   * *Difficulty:* `1.0 / 10` | *Arch:* x86 & x64 Pascal/Lazarus GUI.
   * *Skills:* Steps 1–9: Exact/Unknown scans, floating-point values, code finding, single/multi-level pointers, Auto Assembler injection, and shared code separation (`cmp`).
8. **Cheat Engine Graphical Tutorial (`gtutorial-x86_64.exe`)**
   * *Difficulty:* `1.1 / 10` | *Arch:* x64 2D/3D OpenGL Canvas.
   * *Skills:* Applying pointer chains, player coordinate teleportation, and enemy health separation in an actual game loop.
9. **Squally**
   * *Difficulty:* `1.1 / 10` | *Engine:* Unity / Custom x86 Educational RPG.
   * *Skills:* Solving platformer RPG puzzles by editing live x86 assembly instructions (`ADD`, `SUB`, `XOR`, `JMP`) and memory flags in-game.
10. **PwnAdventure 3: Pwnie Island (Offline Local Server & Client)**
    * *Difficulty:* `1.2 / 10` | *Engine:* Unreal Engine 3 (Created by Vector 35 / Binary Ninja team).
    * *Skills:* Built specifically for reverse engineering practice—patching client logic, speed/jump multipliers, teleportation, and reversing `GameLogic.dll`.
11. **Microcorruption (Embedded Assembly CTF Simulator)**
    * *Difficulty:* `1.2 / 10` | *Arch:* TI MSP430 Assembly.
    * *Skills:* Pure register, stack frame, and memory flag manipulation through interactive hardware debugger challenges.

---

### 🪵 Tier `E-` : Desktop Win32 Classics (Static Memory & 2D Arrays) — `Difficulty: 1.3–1.6 / 10`
*Tiny executables, zero obfuscation, deterministic Win32 API loops, and easily readable global variables.*

12. **Windows Minesweeper (`winmine.exe` — WinXP / Win7)**
    * *Difficulty:* `1.3 / 10` | *Engine:* Native Win32 C.
    * *Skills:* Locating the static 2D byte array (`0x01005340`) representing the minefield grid (`0x8F` = mine), freezing the timer, and calling the internal `Win` function.
13. **3D Pinball: Space Cadet (`pinball.exe`)**
    * *Difficulty:* `1.4 / 10` | *Engine:* Native 32-bit Win32 C.
    * *Skills:* Score manipulation, infinite balls, plunger physics floats, and tilting counter patches.
14. **Microsoft Solitaire / Spider Solitaire (WinXP / Win7)**
    * *Difficulty:* `1.4 / 10` | *Engine:* Win32 C++.
    * *Skills:* Reversing card deck structures, score multipliers, and forcing legal card moves via conditional jump patches (`JNZ` $\rightarrow$ `JMP`).
15. **Purble Place (Win7)**
    * *Difficulty:* `1.5 / 10` | *Engine:* Win32 C++ / DirectX.
    * *Skills:* Timer freezes and memory structures of pattern-matching mini-games.
16. **SkiFree (`skifree.exe` 32-bit build)**
    * *Difficulty:* `1.5 / 10` | *Engine:* Win32 C.
    * *Skills:* Speed floats, distance counters, and disabling the Abominable Snowman spawn check.
17. **Codename Gordon** ⭐
    * *Difficulty:* `1.6 / 10` | *Engine:* 2D Flash / Win32 Wrapper (`Codename Gordon.exe`).
    * *Skills:* 2D Half-Life sidescroller health/ammo scanning, gravity gun charge floats, and score counters.

---

### 🔰 Tier `E` : Beginner FPS Sandboxes & Offline Aim Trainers — `Difficulty: 1.7–2.0 / 10`
*Open-source FPS engines and single-player 3D aim trainers—ideal for learning `LocalPlayer`, `EntityList`, and `ViewMatrix` math.*

18. **AssaultCube (`ac_client.exe`)**
    * *Difficulty:* `1.7 / 10` | *Engine:* Cube Engine (x86 C++ Open-Source).
    * *Skills:* **The #1 Beginner Benchmark.** `LocalPlayer` pointer (`0x50F4F4`), `EntityList` array, Health/Ammo/Recoil, ViewMatrix $4 \times 4$, WorldToScreen ESP, and Pitch/Yaw ViewAngle math.
19. **Aim Hero** ⭐
    * *Difficulty:* `1.8 / 10` | *Engine:* Unity (x86/x64 Single-Player Aim Trainer — **357h played**).
    * *Skills:* **Perfect Legal 3D Math Testbed.** Locating spawned target sphere coordinates $(X, Y, Z)$, target lifetime floats, camera Pitch/Yaw angles, and writing an external C++ WorldToScreen overlay for practice targets.
20. **Cube 2: Sauerbraten**
    * *Difficulty:* `1.9 / 10` | *Engine:* Cube 2 Engine (x86/x64 C++ & OpenGL).
    * *Skills:* Octree world geometry, player velocity vectors, and OpenGL `wglSwapBuffers` hooking.
21. **Quake III Arena / OpenArena (`ioquake3`)**
    * *Difficulty:* `1.9 / 10` | *Engine:* id Tech 3 (C).
    * *Skills:* Pure C structs (`centity_t`, `clientInfo_t`), `vmMain` bytecode/native DLL calls, and Strafe/BunnyHop velocity math.
22. **Teeworlds (Offline Local Practice)**
    * *Difficulty:* `2.0 / 10` | *Engine:* Custom 2D C++ Engine.
    * *Skills:* 2D coordinate vectors, hook physics, and projectile trajectory math.
23. **SuperTuxKart**
    * *Difficulty:* `2.0 / 10` | *Engine:* Antarctica Engine (Open-Source C++).
    * *Skills:* Nitro boost floats, kart physics structures, and lap counter manipulation.

---

### 🥉 Tier `E+` : Casual 32-bit C++ Frameworks & 2D Arcade — `Difficulty: 2.1–2.4 / 10`
*Clean 32-bit C++ class hierarchies with simple 1-to-3 level pointer chains and readable AOB signatures.*

24. **Plants vs. Zombies (GOTY Edition)** — *(✅ Completed in [`Game_Hacking/PvZ.CT`](./Game_Hacking/PvZ.CT))*
    * *Difficulty:* `2.1 / 10` | *Engine:* PopCap Framework (x86 C++).
    * *Skills:* Sun counter (`+0x5560`), plant slot recharge timers, projectile ID swapping, instant recharge, immortal plants, and Lua speed controller.
25. **Castle Crashers** ⭐
    * *Difficulty:* `2.2 / 10` | *Engine:* The Behemoth Custom 2D C++ Engine (x86).
    * *Skills:* Character XP/Level structs, Gold, Strength/Magic/Defense/Agility stat bars, potion quantities, and juggle gravity floats.
26. **Peggle Deluxe / Peggle Nights**
    * *Difficulty:* `2.2 / 10` | *Engine:* PopCap Framework (x86).
    * *Skills:* Free ball counters, trajectory guide line length extension, and fever meter manipulation.
27. **Zuma Deluxe**
    * *Difficulty:* `2.3 / 10` | *Engine:* PopCap Framework (x86).
    * *Skills:* Linked list of rolling spheres, frog rotation float, and score multipliers.
28. **Insaniquarium Deluxe & Bejeweled 3**
    * *Difficulty:* `2.3 / 10` | *Engine:* PopCap Framework (x86).
    * *Skills:* Shell currency, fish hunger timers, 2D board matrix scanning, and score multiplier hooks.
29. **Capcom Arcade Stadium (Offline Local Arcade ROMs)** ⭐
    * *Difficulty:* `2.4 / 10` | *Engine:* Capcom RE/Arcade Emulator Wrapper (x64).
    * *Skills:* Locating emulated CP-System (CPS-1/CPS-2) credit counters, P1 health bars, and invincibility timers inside wrapper memory.

---

### 🗡️ Tier `D-` : 90s Retro 2.5D & 3D Engines (Fixed-Point & Sector Math) — `Difficulty: 2.5–2.8 / 10`
*Classic C/C++ engines that teach low-level memory arrays, bitflags, and fixed-point arithmetic.*

30. **DOOM + DOOM II (KEX Engine / Crispy Doom / GZDoom)** ⭐
    * *Difficulty:* `2.5 / 10` | *Engine:* id Tech 1 / KEX Engine (C/C++).
    * *Skills:* `mobj_t` actor structures, fixed-point numbers ($16.16$), sector lighting, ammo/armor pointers, and god-mode bitflags.
31. **POSTAL (Classic & Redux)** ⭐
    * *Difficulty:* `2.6 / 10` | *Engine:* Custom Isometric C++ / Unreal Engine 4 (Redux).
    * *Skills:* Isometric coordinate vectors, weapon ammo arrays, health, and execute state flags.
32. **Duke Nukem 3D (EDuke32)**
    * *Difficulty:* `2.6 / 10` | *Engine:* Build Engine.
    * *Skills:* Sprite/wall/sector static arrays, jetpack fuel, steroid timers, and weapon ammo tables.
33. **Blood: Fresh Supply / Shadow Warrior Classic**
    * *Difficulty:* `2.7 / 10` | *Engine:* Build Engine / KEX Engine.
    * *Skills:* Actor state machines, flare damage multipliers, and inventory structs.
34. **Quake I & Quake II**
    * *Difficulty:* `2.7 / 10` | *Engine:* id Tech 2.
    * *Skills:* Edict structures (`edict_t`), QuakeC virtual machine stack, and `glBegin`/`glEnd` wallhack fundamentals.
35. **Wolfenstein 3D / Spear of Destiny (ECWolf)**
    * *Difficulty:* `2.8 / 10` | *Engine:* Wolf3D Raycaster.
    * *Skills:* $64 \times 64$ tilemap memory grids, secret pushwall flags, and guard state machines.

---

### 🛡️ Tier `D` : Early 2000s 3D Arena & Action Classics — `Difficulty: 2.9–3.2 / 10`
*Introduction to early object-oriented C++ game engines, virtual tables, and console CVARs.*

36. **Unreal Tournament 99 (`UT99`)** — *(✅ Completed in [`Game_Hacking/UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT))*
    * *Difficulty:* `2.9 / 10` | *Engine:* Unreal Engine 1 (x86 C++ & UnrealScript).
    * *Skills:* First look at Unreal's `UObject` / `AActor` / `APawn` hierarchy, `Engine.dll` base chains, weapon ammo offsets, health, and smart one-hit-kill filters.
37. **Half-Life 1 (1998 Original)** ⭐
    * *Difficulty:* `3.0 / 10` | *Engine:* GoldSrc (`hw.dll` & `client.dll`).
    * *Skills:* `cl_entity_s` array, engine function table pointers (`cl_enginefunc_t`), HEV suit power, and bunnyhop ground flags (`FL_ONGROUND`).
38. **Counter-Strike 1.6 & Counter-Strike: Condition Zero (Offline with Bots)** ⭐
    * *Difficulty:* `3.0 / 10` | *Engine:* GoldSrc (x86 — **1,856h + 316h in library**).
    * *Skills:* Bone matrix positions, punch angle (recoil) vectors, money offsets, FOV overrides, and OpenGL `glBegin` studio renderer hooks against local bots.
39. **POSTAL 2 (Complete / Paradise Lost)** ⭐
    * *Difficulty:* `3.1 / 10` | *Engine:* Unreal Engine 1.5 / 2 (`Postal2.exe`, x86).
    * *Skills:* Extending your UT99 knowledge to UE2—`UPawn` inventory linked lists, cat-silencer ammo counters, health pipes, and NPC AI aggression state flags.
40. **Max Payne 1 & Max Payne 2**
    * *Difficulty:* `3.1 / 10` | *Engine:* MAX-FX Engine (x86).
    * *Skills:* Bullet-time hourglass float, painkiller inventory counters, and projectile speed hooks.
41. **Serious Sam: Classic First & Second Encounter**
    * *Difficulty:* `3.2 / 10` | *Engine:* Serious Engine 1 (Open-Source C++).
    * *Skills:* Massive entity spawners, armor/health/ammo pointers, and gravity modifiers.

---

### 🏹 Tier `D+` : Classic 32-bit Open-World, Stealth & Strategy — `Difficulty: 3.3–3.6 / 10`
*Large static memory pools, vehicle/stealth physics structs, and classic RTS/RPG engines.*

42. **Tom Clancy's Splinter Cell: Chaos Theory** ⭐
    * *Difficulty:* `3.3 / 10` | *Engine:* Lead Engine (Heavily Modified Unreal Engine 2.5, x86).
    * *Skills:* Light meter visibility float (`0.0` = pitch black stealth), acoustic noise generation float, night-vision battery charge, SC-20K ammo, and AI alertness states.
43. **Far Cry 1 (2004 Original)** ⭐
    * *Difficulty:* `3.3 / 10` | *Engine:* CryEngine 1 (`CryGame.dll`, x86 C++ & Lua).
    * *Skills:* Stamina/breath bars, binocular tag ranges, weapon recoil floats, and CryEngine 1 entity table inspection.
44. **Grand Theft Auto: Vice City & San Andreas (Original x86)**
    * *Difficulty:* `3.4 / 10` | *Engine:* RenderWare (x86 C++).
    * *Skills:* Direct static pools for `CPed` (`0xB6F5F0`) and `CVehicle`, weapon slots, wanted level stars, and calling internal engine functions (`CHud::SetHelpMessage`).
45. **SimCity 4 Deluxe Edition & Evil Genius** ⭐
    * *Difficulty:* `3.4 / 10` | *Engine:* Custom 32-bit C++ Strategy/Management Engines.
    * *Skills:* Treasury gold/simoleon pointers, minion loyalty/attention bars, power grid capacity, and instant room construction hooks.
46. **SPORE** ⭐
    * *Difficulty:* `3.5 / 10` | *Engine:* Maxis Custom C++ Engine (x86).
    * *Skills:* DNA points (`Creature` / `Tribal` / `Civilization` stages), complexity meter limit bypass in the Creature Editor, and spaceship energy/spice cargo holds.
47. **LEGO Star Wars: The Complete Saga / LEGO Batman 1 / LEGO LOTR / LEGO The Hobbit** ⭐
    * *Difficulty:* `3.5 / 10` | *Engine:* Traveller's Tales **Nu2x Engine** (x86/x64 C++).
    * *Skills:* True Jedi stud meter thresholds, 64-bit stud counters, Red Brick multiplier bitflags, and character jump/hover height floats.
48. **FlatOut 2 & Need for Speed: Most Wanted (2005)**
    * *Difficulty:* `3.6 / 10` | *Engine:* Custom x86 C++ / EAGL Engine.
    * *Skills:* Vehicle mass/torque floats, N2O/Speedbreaker regeneration, ragdoll launch velocity vectors, and heat/bounty points.
49. **Gothic I & II / Star Wars: KOTOR I & II**
    * *Difficulty:* `3.6 / 10` | *Engine:* ZenGin & Odyssey Engine (x86).
    * *Skills:* `oCNpc` class reconstruction, D20 combat roll hooks, Force/mana points, and Daedalus script VM inspection.

---

### 🔮 Tier `C-` : 2D Indie Roguelikes, State Machines & Bytecode Engines — `Difficulty: 3.7–4.0 / 10`
*Dynamic heap allocations, procedural rooms, entity component lists, and custom 2D C++/GameMaker/Cocos2d engines.*

50. **The Binding of Isaac: Rebirth / Repentance (`isaac-ng.exe`)** ⭐ — *(✅ Completed in [`Game_Hacking/isaac-ng.CT`](./Game_Hacking/isaac-ng.CT))*
    * *Difficulty:* `3.8 / 10` | *Engine:* Custom x86 C++20 Engine + Lua 5.3.
    * *Skills:* `Entity_Player` pointer chains, Red/Soul/Black heart bitmasks, tear delay/fire rate formulas, room-transition stat locks, and pedestal item ID swapping.
51. **Geometry Dash (`GeometryDash.exe`)** ⭐
    * *Difficulty:* `3.8 / 10` | *Engine:* **Cocos2d-x** C++ (`libcocos2d.dll`, x86/x64).
    * *Skills:* **Iconic C++ Modding Target.** Reversing `PlayLayer` (`PlayLayer::destroyPlayer` noclip patch), `PlayerObject` gravity/speed floats, practice music sync bypass, and inspecting Cocos2d `CCNode` trees.
52. **UBERMOSH / UBERMOSH:BLACK / UBERMOSH:WRAITH / Vol.3 / Vol.5** ⭐
    * *Difficulty:* `3.7 / 10` | *Engine:* GameMaker Studio (x86).
    * *Skills:* Bullet-cutting reflection window frames, Brain-Power meter lock, countdown timer freeze, and high-score double variables.
53. **Chasm & Secrets of Grindea** ⭐
    * *Difficulty:* `3.8 / 10` | *Engine:* Custom XNA/FNA & C++ 2D Action RPG Engines.
    * *Skills:* Procedural metroidvania map reveal arrays, perfect-block parry window timers, skill point counters, and rare loot drop table weights.
54. **Barony** ⭐
    * *Difficulty:* `3.9 / 10` | *Engine:* Custom 3D Voxel-Dungeon C++ Engine (Open-Source friendly).
    * *Skills:* First-person roguelike `Stat` structs (`HP`, `MP`, `CON`, `DEX`), cursed item identification flags (`beatitude`), hunger timers, and spellcasting cost hooks.
55. **FTL: Faster Than Light & Spelunky HD**
    * *Difficulty:* `3.9 / 10` | *Engine:* Custom C++ Engines (x86/x64).
    * *Skills:* Hull integrity, reactor power bars, scrap currency, procedural level tile grids, and ghost spawn timer freezes.
56. **Hotline Miami 1 & 2 / Undertale & Deltarune**
    * *Difficulty:* `4.0 / 10` | *Engine:* GameMaker Studio (`data.win` VM Bytecode).
    * *Skills:* Using **UndertaleModTool** alongside Cheat Engine to understand how GameMaker stores dynamic `double` variables in hash maps.

---

### 🥈 Tier `C` : Unity Mono & .NET CLR (Decompilation & Bytecode Editing) — `Difficulty: 4.1–4.5 / 10`
*JIT-compiled C# assemblies (`Assembly-CSharp.dll`) where full class, method, and field names are preserved.*

57. **Streets of Rogue (`StreetsOfRogue_v98`)** — *(✅ Completed in [`Game_Hacking/StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT))*
    * *Difficulty:* `4.1 / 10` | *Engine:* Unity Engine (Mono / x64).
    * *Skills:* Enabling Cheat Engine's `.NET / Mono Dissector`, locating `Agent`, `InvDatabase`, `Stat` classes, infinite durability/ammo, EXP hooks, and trait points.
58. **Punch Club & Punch Club 2: Fast Forward** ⭐
    * *Difficulty:* `4.1 / 10` | *Engine:* Unity (Mono — Lazy Bear Games).
    * *Skills:* Decompiling `Assembly-CSharp.dll` in **dnSpyEx**, bypassing daily stat decay in Punch Club 1, locking Energy/Hunger/Mood bars, and editing GPP/skill points.
59. **Graveyard Keeper** ⭐
    * *Difficulty:* `4.2 / 10` | *Engine:* Unity (Mono — Lazy Bear Games).
    * *Skills:* Reversing `WorldGameObject` and `PlayerComponent`, infinite Energy, Red/Green/Blue tech points, faith multipliers, and corpse quality (`White Skulls`) overrides.
60. **Enter the Gungeon** ⭐
    * *Difficulty:* `4.2 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Inspecting `PlayerController` and `HealthHaver`, infinite Blanks, Hegemony Credits, Key/Casing counters, zero gun spread, and dodge-roll invulnerability duration.
61. **Broforce** ⭐
    * *Difficulty:* `4.2 / 10` | *Engine:* Unity (Mono).
    * *Skills:* `TestVanDammeAnim` player controller, infinite special grenades/airstrikes, extra lives, and destructible terrain tile damage multipliers.
62. **Kingdom: Classic & Kingdom Two Crowns** ⭐
    * *Difficulty:* `4.3 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Coin pouch capacity (`Wallet`), steed stamina float, gem counters, builder/archer walk speed, and Greed blood-moon wave timer manipulation.
63. **Moonlighter & Moon Hunters** ⭐
    * *Difficulty:* `4.3 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Shop item price satisfaction thresholds (customers always pay max gold), dungeon pendant portal costs, and weapon enchantment flags.
64. **Slime Rancher 1 & Fallout Shelter** ⭐
    * *Difficulty:* `4.3 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Vacpack slot capacity, jetpack energy, Newbucks currency, Nuka-Cola Quantum counters, and dweller SPECIAL training timers.
65. **Poly Bridge & Scribblenauts Unlimited / Unmasked** ⭐
    * *Difficulty:* `4.4 / 10` | *Engine:* Unity (Mono) & Custom 2D Object-Dictionary Engine.
    * *Skills:* Bridge budget limit overrides, hydraulic joint max stress thresholds (`unbreakable joints`), and Scribblenauts adjective bitmask injection.
66. **Hollow Knight & Cuphead**
    * *Difficulty:* `4.4 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Inspecting `HeroController` and `PlayerData` in **dnSpy**, infinite Soul/Geo, Charm Notches, and Cuphead `LevelPlayerWeaponManager` Ex-Move cards.
67. **Stardew Valley & Terraria** ⭐
    * *Difficulty:* `4.5 / 10` | *Engine:* .NET / MonoGame & C# XNA/FNA (**1,314h + 72h in library**).
    * *Skills:* JIT signature scanning for `Terraria.Player::Update` (infinite mana/wing flight time, tile reach) and `StardewValley.Game1.player` stamina/luck manipulation.

---

### ⚡ Tier `C+` : Advanced Unity Mono, Harmony Hooking & Complex Sims — `Difficulty: 4.6–4.9 / 10`
*Large managed codebases with thousands of interacting classes, runtime C# mod loaders (BepInEx/Harmony), and physics systems.*

68. **Lethal Company (Offline Solo / Local Host Sandbox)** ⭐
    * *Difficulty:* `4.6 / 10` | *Engine:* Unity (Mono + Unity Netcode).
    * *Skills:* Writing a custom **BepInEx + Harmony** C# internal plugin (`PlayerControllerB`), infinite sprint stamina, night-vision battery light, two-handed carry weight bypass, and quota deadline manipulation.
69. **Unturned (Offline Singleplayer Sandbox)** ⭐
    * *Difficulty:* `4.6 / 10` | *Engine:* Unity (Mono — **1,310h in library**).
    * *Skills:* Navigating `SDG.Unturned` namespaces (`PlayerLife`, `PlayerInventory`, `UseableGun`), recoil/spread zeroing, radiation immunity, and vehicle fuel/health.
70. **Subnautica & Subnautica: Below Zero** ⭐
    * *Difficulty:* `4.7 / 10` | *Engine:* Unity.
    * *Skills:* `OxygenManager`, `LiveMixin` (universal health component), body temperature float in Below Zero, Seatruck depth crush immunity, and blueprint unlocking.
71. **Shadowrun Returns & We Were Here (Local Test)** ⭐
    * *Difficulty:* `4.7 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Turn-based Action Points (AP), Karma points, cyberware essence limits, and dialogue skill-check overrides.
72. **RimWorld & Kerbal Space Program 1**
    * *Difficulty:* `4.8 / 10` | *Engine:* Unity (Mono).
    * *Skills:* C# runtime prefix/postfix hooks with **Harmony**, colonist mood/skill structs, orbital mechanics vectors, and fuel tank resource structures.
73. **Vampire Survivors & ULTRAKILL**
    * *Difficulty:* `4.9 / 10` | *Engine:* Unity (Mono).
    * *Skills:* Enemy wave spawner intervals, magnet pickup radius, ULTRAKILL style meter points, stamina regeneration, and hitstop frame timers.

---

### ⚔️ Tier `B-` : Mature 32/64-bit Open-World & RPG Engines — `Difficulty: 5.0–5.3 / 10`
*Massive C++ inheritance trees, RTTI analysis, RefIDs/FormIDs, and custom scripting engines.*

74. **The Elder Scrolls V: Skyrim Special Edition (`SkyrimSE.exe`)** ⭐
    * *Difficulty:* `5.0 / 10` | *Engine:* Creation Engine (x64 C++ — **Recently added Oct 2026**).
    * *Skills:* Reversing `PlayerCharacter` singleton, `ActorValueOwner` VMT, Papyrus VM hooks, shout cooldowns, Magicka/Stamina/CarryWeight, and SKSE address library offsets.
75. **Mount & Blade / Warband / With Fire & Sword** ⭐
    * *Difficulty:* `5.0 / 10` | *Engine:* TaleWorlds Custom x86 C++ Engine (**30h+ across all 3 titles**).
    * *Skills:* Party size limits, renown/morale pointers, troop XP tables, Denars, agent horse/combat speed, and module system opcode reversing.
76. **Dragon Age: Origins & Dragon Age II (Ultimate Editions)** ⭐
    * *Difficulty:* `5.1 / 10` | *Engine:* BioWare **Eclipse / Lycium Engine** (x86 C++).
    * *Skills:* Party member stat blocks (`Strength`, `Willpower`, `Cunning`), spell mana/stamina cooldown timers, approval rating offsets, and inventory sovereign/gold pointers.
77. **Far Cry 2 & Far Cry 3** ⭐
    * *Difficulty:* `5.1 / 10` | *Engine:* Dunia Engine (x86 C++).
    * *Skills:* Weapon degradation/jamming counters, malaria pill timers, diamond currency, syringe buffs, and world entity lists.
78. **Xenus 2: White Gold** ⭐
    * *Difficulty:* `5.2 / 10` | *Engine:* Deep Shadows **Vital Engine ZL** (x86 C++).
    * *Skills:* RPG perk tree bitflags, faction reputation floats, addiction/fatigue counters, and vehicle fuel/ammo structures.
79. **Fallout: New Vegas & S.T.A.L.K.E.R.: Call of Pripyat (`OpenXRay`)**
    * *Difficulty:* `5.3 / 10` | *Engine:* Gamebryo (x86) & X-Ray Engine (x64 C++ + Lua).
    * *Skills:* FormIDs, S.P.E.C.I.A.L. stats, V.A.T.S. accuracy hooks, `CActor` class layout, radiation floats, and weapon dispersion.

---

### 🛡️ Tier `B` : Source Engine (Netvars/VMT) & Unreal Engine 3 — `Difficulty: 5.4–5.7 / 10`
*Industry-standard FPS/Action architectures with formal interface systems (`CreateInterface`) and virtual method tables.*

80. **Half-Life 2 & Portal 2 (x64 Update)** ⭐
    * *Difficulty:* `5.4 / 10` | *Engine:* Source Engine (`client.dll` & `engine.dll`).
    * *Skills:* Walking the `ClientClass` linked list to dump **Netvars** (`DT_BasePlayer`), `CreateMove` VMT hooking, AUX power, and portal placement checks.
81. **Counter-Strike: Source & Garry's Mod (Offline Local Sandbox / Bots)** ⭐
    * *Difficulty:* `5.4 / 10` | *Engine:* Source Engine (x86/x64 — **1,668h in library**).
    * *Skills:* **Classic Source SDK Lab.** Calling `CreateInterface("VClientEntityList003")`, iterating `IClientEntityList`, bone matrix `[3][4]` extraction, DirectX 9 `EndScene` ImGui ESP against offline bots, and GMod Lua C-API state inspection.
82. **Alien Swarm: Reactive Drop & No More Room in Hell (Offline Solo)** ⭐
    * *Difficulty:* `5.5 / 10` | *Engine:* Source Engine.
    * *Skills:* Top-down / survival Source netvars, marine ammo/welder charge, infection timer floats, and stamina depletion hooks.
83. **Spec Ops: The Line & A Story About My Uncle** ⭐
    * *Difficulty:* `5.5 / 10` | *Engine:* Unreal Engine 3 (x86).
    * *Skills:* UE3 `GObjects` & `GNames` scanning, grapple beam impulse velocity vectors, max grapple count (`A Story About My Uncle`), and squad health/ammo in `Spec Ops`.
84. **Injustice: Gods Among Us Ultimate Edition** ⭐
    * *Difficulty:* `5.6 / 10` | *Engine:* Modified Unreal Engine 3 (NetherRealm x86).
    * *Skills:* Fighting game hitbox/hurtbox bounding boxes, Super Meter bar lock, frame data timers, and S.T.A.R. Labs mission stars.
85. **Left 4 Dead 2 / Borderlands 2 / Dishonored 1 / BioShock Infinite**
    * *Difficulty:* `5.7 / 10` | *Engine:* Source Engine & Unreal Engine 3 (x86).
    * *Skills:* Generating full UE3 SDKs, modular weapon part structures, Dishonored Blink teleport distance limiters, and AI vision cones.

---

### 🔥 Tier `B+` : Modern AAA x64 Proprietary C++ & Simulation Engines — `Difficulty: 5.8–6.1 / 10`
*Complex 64-bit engines with ASLR, SIMD (`XMM`/`YMM`) math everywhere, physics telemetry, and multi-threaded job systems.*

86. **Euro Truck Simulator 2 & Scania Truck Driving Simulator** ⭐
    * *Difficulty:* `5.8 / 10` | *Engine:* SCS **Prism3D Engine** (x64 C++ — **481.4h played!**).
    * *Skills:* Reversing `eurotrucks2.exe` economy pointers (Money, XP, Skill points), chassis/cargo damage floats (`0.0` wear), fuel consumption, speed limiter removal, and building a custom C++ telemetry dashboard via the **SCS Telemetry SDK** shared memory (`scs-telemetry.dll`).
87. **Assetto Corsa & GRID 2** ⭐
    * *Difficulty:* `5.8 / 10` | *Engine:* Kunos Simulazioni Custom C++ Physics Engine & Codemasters EGO 3.0 (**176.9h played!**).
    * *Skills:* Tire temperature/wear/grip multipliers, DRS/KERS hybrid battery charge, fuel load floats, and reading live physics shared memory (`acpmf_physics`, `acpmf_graphics`).
88. **Grand Theft Auto V Legacy (Strictly Offline Story Mode)** ⭐
    * *Difficulty:* `5.9 / 10` | *Engine:* RAGE Engine (x64 C++ — **240.9h played**).
    * *Skills:* `CPedFactory` (`WorldPtr`), `CReplayInterface` entity iteration, Native Invoker (`scrNativeCallContext`), weapon damage modifiers, and vehicle handling flags.
89. **Just Cause 2 & Just Cause 3** ⭐
    * *Difficulty:* `5.9 / 10` | *Engine:* Avalanche Engine 2.0 & 3.0 (x86/x64 C++).
    * *Skills:* Grappling hook tether tensile strength, infinite C4/Bavarium wingsuit boost, Chaos score multipliers, and rebel drop beacon counters.
90. **Dying Light & Assassin's Creed II** ⭐
    * *Difficulty:* `6.0 / 10` | *Engine:* Techland **Chrome Engine 6** (x64) & Ubisoft **Anvil Engine**.
    * *Skills:* Parkour/combat stamina floats, weapon durability/repairs, UV flashlight battery, Grappling Hook cooldowns, and Ezio's Florins/Medicine counters.
91. **Metro 2033 & Metro Exodus** ⭐
    * *Difficulty:* `6.0 / 10` | *Engine:* 4A Engine (x64).
    * *Skills:* Gas mask filter timers, military-grade rounds (currency), pneumatic weapon pressure floats, battery charge, and stealth light indicators.
92. **South Park: The Fractured But Whole** ⭐
    * *Difficulty:* `6.0 / 10` | *Engine:* Ubisoft **Snowdrop Engine** (x64 C++).
    * *Skills:* Tactical combat grid movement range, Artifacts/Might rating structs, Ultimate gauge charge, and crafting component counters.
93. **HITMAN 2 (Offline Campaign Sandbox)** ⭐
    * *Difficulty:* `6.1 / 10` | *Engine:* IO Interactive **Glacier 2 Engine** (x64 C++ — **54.8h, 132/146 achievements**).
    * *Skills:* Dissecting `ZHitman5` / `ZActor` RTTI classes, AI suspicion/enforcer perception timers, Silent Assassin rating flags, instinct vision, and item inventory capacity.
94. **The Witcher 3: Wild Hunt & Cyberpunk 2077 & Doom Eternal**
    * *Difficulty:* `6.1 / 10` | *Engine:* REDengine 3/4 (x64 DX12) & id Tech 7 (x64 Vulkan).
    * *Skills:* Deep RTTI class hierarchies (`CR4Player`), Cyberware RAM regeneration, and Vulkan `vkQueuePresentKHR` overlay hooking.

---

### 🥇 Tier `A-` : Unreal Engine 4 & 5 (`GWorld`, `FNamePool` & SDK Dumping) — `Difficulty: 6.2–6.5 / 10`
*Mastering modern Unreal Engine memory reflection (`UObject`, `UStruct`, `UFunction`, `ProcessEvent`) using Dumper-7.*

95. **KovaaK's (Offline Aim Trainer Sandbox)** ⭐
    * *Difficulty:* `6.2 / 10` | *Engine:* Unreal Engine 4 (x64).
    * *Skills:* **Ultimate UE4 Learning Lab.** Dumping the UE4 SDK with **Dumper-7**, traversing `UWorld -> PersistentLevel -> Actors` to locate bot targets in memory, reading 3D bone/capsule coordinates, and testing UE4 `UObject::ProcessEvent` hooks in a single-player aim trainer.
96. **Escape the Backrooms & Breathedge** ⭐
    * *Difficulty:* `6.2 / 10` | *Engine:* Unreal Engine 4 (x64 — **12h played, 31/34 achievements**).
    * *Skills:* Sanity meter decay freeze, sprint stamina, entity ESP via `AActor` class names (`FNamePool`) to visualize how stalker AI navigates Backrooms levels, and oxygen/suit durability in `Breathedge`.
97. **Manor Lords** ⭐
    * *Difficulty:* `6.3 / 10` | *Engine:* Unreal Engine 4 (x64).
    * *Skills:* Regional wealth, King's Treasury, Influence points, public order approval floats, retinue unit health/fatigue, and seasonal resource yields.
98. **Palworld (Offline Singleplayer)** ⭐
    * *Difficulty:* `6.3 / 10` | *Engine:* Unreal Engine 5 (x64 — **97.7h played!**).
    * *Skills:* `GWorld` $\rightarrow$ `PersistentLevel` $\rightarrow$ `Actors` array traversal, Pal capture rate formulas, work speed, weight capacity, technology points, and stamina.
99. **The Outlast Trials (Offline / Solo Introspection Study) & Shift At Midnight / PEAK** ⭐
    * *Difficulty:* `6.4 / 10` | *Engine:* Unreal Engine 4 / 5 (x64).
    * *Skills:* Studying UE4/UE5 night-vision battery structs, psychosis/health bars, stamina recovery rates, and climbing grip stamina in `PEAK`.
100. **Lies of P / Deep Rock Galactic (Solo) / S.T.A.L.K.E.R. 2 / Black Myth: Wukong**
     * *Difficulty:* `6.5 / 10` | *Engine:* Unreal Engine 4 & 5.1 (x64).
     * *Skills:* UE5 `FNamePool` decryption/indexing, `UWorldPartition` streaming cells, parry window frames, and mineral multipliers.

---

### 🏆 Tier `A` : Unity IL2CPP (Stripped Metadata & Native x64 Assembly) — `Difficulty: 6.6–6.9 / 10`
*C# code transpiled to C++ and compiled into native x64 machine code (`GameAssembly.dll`). No CIL bytecode left.*

101. **Aimlabs (Offline Local Training Tasks)** ⭐
     * *Difficulty:* `6.6 / 10` | *Engine:* Unity IL2CPP (x64 — **104.7h played!**).
     * *Skills:* Running **Il2CppDumper** on `GameAssembly.dll` + `global-metadata.dat`, importing generated `script.json` symbols into Ghidra/IDA, and analyzing target spawn state machines and camera matrix functions in native x64 assembly.
102. **Slime Rancher 2 & RV There Yet?** ⭐
     * *Difficulty:* `6.7 / 10` | *Engine:* Unity IL2CPP (x64).
     * *Skills:* Reconstructing stripped C# classes from IL2CPP metadata, hooking `PlayerState` / `Vacpack` methods via **MelonLoader** or native **MinHook**, and modifying currency/energy floats.
103. **Risk of Rain 2 & Cult of the Lamb**
     * *Difficulty:* `6.8 / 10` | *Engine:* Unity IL2CPP (x64).
     * *Skills:* Hooking `CharacterBody::RecalculateStats`, Lunar coin counters, item stack arrays, and follower faith/hunger structs.
104. **Sons of the Forest & Dyson Sphere Program**
     * *Difficulty:* `6.8 / 10` | *Engine:* Unity IL2CPP (x64).
     * *Skills:* Reversing `VailActor` AI structs, log building instant-complete hooks, mecha energy core floats, and planetary logistics arrays.
105. **SPT-AKI (Single Player Tarkov Offline Sandbox Mod)**
     * *Difficulty:* `6.9 / 10` | *Engine:* Unity (Mono / IL2CPP hybrid architecture).
     * *Skills:* Complex skeletal bone hierarchy (`BifacialTransform`), ballistics penetration math, procedural weapon recoil, and optic Picture-in-Picture (PiP) WorldToScreen.

---

### 💎 Tier `A+` : Hybrid C++/Lua Engines, Custom VMs & Proprietary AAA — `Difficulty: 7.0–7.3 / 10`
*Custom C++ cores tightly coupled with embedded Lua/Python scripting VMs, Frostbite/Lycium internals, or pure ECS.*

106. **PAYDAY 2 (Offline Crime.Net Solo Mode)** ⭐
     * *Difficulty:* `7.0 / 10` | *Engine:* Grin/Overkill **Diesel Engine 2.0** (C++ + **LuaJIT** — **243.8h, 1,130 achievements!**).
     * *Skills:* **Classic C++ / LuaJIT Bridge Lab.** Understanding how **SuperBLT** hooks `lua_call` / `luaL_loadbuffer` inside `payday2_win32_release.exe`, inspecting `tweak_data`, pager counters, skill point limits, and armor/dodge regeneration timers.
107. **Don't Starve Together (Offline Local World) & Starbound** ⭐
     * *Difficulty:* `7.0 / 10` | *Engine:* Klei Custom C++ + Lua Engine & Chucklefish C++ + Lua 5.3 (**72.5h + 230.7h, 100% achievements!**).
     * *Skills:* Hooking the embedded `lua_State*` to inspect `ThePlayer.components.health` / `sanity` / `hunger` in Don't Starve, and reversing Starbound's C++ `WorldClient` / `Player` pixel/matter-manipulator structs.
108. **Sid Meier's Civilization VI & Total War: SHOGUN 2 & Crusader Kings II** ⭐
     * *Difficulty:* `7.1 / 10` | *Engine:* Firaxis **LORE Engine** (x64 C++ + Lua), Warscape Engine, & Clausewitz Engine.
     * *Skills:* Reversing turn-based strategy state synchronization—Treasury Gold, Faith/Science/Culture per turn, Fog of War visibility bitmasks (`MapVisibility`), and movement points.
109. **Sword Art Online Re: Hollow Fragment / Lost Song / Hollow Realization** ⭐
     * *Difficulty:* `7.1 / 10` | *Engine:* Aquria / Artdink Custom C++ & PhyreEngine (x64 — **30h+ played, 100% achievements!**).
     * *Skills:* Reversing Japanese custom C++ action-RPG memory layouts (`eugeoas` special!): SP (Soul Points) bar locks, Burst Gauge, sword skill cooldown timers, weapon proficiency floats, and Col currency.
110. **Dragon Age: Inquisition (GOTY) & LEGO Star Wars: The Skywalker Saga** ⭐
     * *Difficulty:* `7.2 / 10` | *Engine:* EA **Frostbite 3 Engine** (x64) & TT **NTT Engine** (x64).
     * *Skills:* Navigating Frostbite's `ClientGameContext`, `PlayerManager`, and `TypeInfo` reflection lists (`Inquisition` Power/Gold/Cooldowns), and reversing TT's modern NTT Engine ECS layouts.
111. **Hades I & II / Resident Evil 2/3/4 Remake / Devil May Cry 5 / Baldur's Gate 3**
     * *Difficulty:* `7.3 / 10` | *Engine:* Supergiant C++/Lua, Capcom **RE Engine** (`via.ManagedObject`), & Divinity 4.0 **ECS**.
     * *Skills:* Injecting Lua boons at runtime, reversing RE Engine's managed C#-style reflection inside native C++, and navigating Baldur's Gate 3's pure Entity-Component-System pools.

---

### 👑 Tier `S-` : Soulslike Proprietary Engines, Havok Physics & Param Tables — `Difficulty: 7.4–7.6 / 10`
*Intricate animation state machines, encrypted regulation files, and frame-perfect combat flags.*

112. **Dark Souls III (Strictly Offline Mode)**
     * *Difficulty:* `7.4 / 10` | *Engine:* FromSoftware Dantelion Engine (x64).
     * *Skills:* `WorldChrMan` singleton traversal, animation event flags (Invincibility frames / i-frames), stamina consumption, and `Param` table memory patching.
113. **Sekiro: Shadows Die Twice**
     * *Difficulty:* `7.5 / 10` | *Engine:* Dantelion Engine (x64).
     * *Skills:* Posture bar regeneration/damage floats, Spirit Emblem counters, and deflect window frame extensions.
114. **Elden Ring + Shadow of the Erdtree (Strictly Offline / EAC Disabled via Launch Flag)**
     * *Difficulty:* `7.5 / 10` | *Engine:* Dantelion 2 Engine (x64 DirectX 12).
     * *Skills:* `CSChrIns` hierarchy, SpEffect IDs (buffs/debuffs), Poise floats, Scadutree blessing multipliers, and DX12 command queue ImGui rendering.
115. **Armored Core VI: Fires of Rubicon & Monster Hunter: World (Offline Solo)**
     * *Difficulty:* `7.6 / 10` | *Engine:* Dantelion Engine & Capcom MT Framework (x64).
     * *Skills:* EN generator recovery delay, ACS stagger gauge, weapon sharpness gauges, and monster part break HP thresholds.

---

### 🌟 Tier `S` : Data-Oriented Design (DOD), Custom Allocators & Voxel Engines — `Difficulty: 7.7–7.9 / 10`
*No traditional OOP classes: memory is packed into cache-aligned SoA (Structure of Arrays) slabs or custom cellular automata.*

116. **Factorio**
     * *Difficulty:* `7.7 / 10` | *Engine:* Custom Ultra-Optimized C++20 Engine.
     * *Skills:* Deterministic tick architecture, custom slab memory allocators, belt item spacing math, and Lua API bridge internals.
117. **Noita**
     * *Difficulty:* `7.8 / 10` | *Engine:* FallingEverything Engine (Custom C++ + LuaJIT).
     * *Skills:* Cellular automata memory grid (every single pixel's material, velocity, and temperature simulated in memory), wand recharge/cast delay structs, and deterministic seed PRNG reversing.
118. **Teardown**
     * *Difficulty:* `7.8 / 10` | *Engine:* Custom C++ Voxel Raytracing Engine.
     * *Skills:* 3D voxel octree buffers in RAM/VRAM, structural integrity stress checks, and tool ammo counters.
119. **Dwarf Fortress (Steam Edition) & Mount & Blade II: Bannerlord**
     * *Difficulty:* `7.9 / 10` | *Engine:* Custom C++ Simulation Engines.
     * *Skills:* Studying **DFHack** (reversing massive historical entity vectors and fluid grids) and Bannerlord's native-to-managed P/Invoke bridge handling 2,000+ simultaneous AI agents.

---

### 🪐 Tier `S+` : Console Emulators, Big-Endian Memory & Cross-Arch JIT — `Difficulty: 8.0–8.2 / 10`
*Reversing a guest console CPU architecture (PowerPC, Cell SPU, ARM64, MIPS) translated inside an x64 host emulator process.*

120. **The Legend of Zelda: Breath of the Wild (via Cemu Emulator)**
     * *Difficulty:* `8.0 / 10` | *Arch:* Wii U Espresso PowerPC (32-bit **Big-Endian**) $\rightarrow$ x64 Host.
     * *Skills:* Registering custom Big-Endian value types (`4 Byte Big Endian`, `Float Big Endian`) in Cheat Engine, resolving emulated base memory (`memory_base`), and patching PowerPC assembly instructions.
121. **The Legend of Zelda: Tears of the Kingdom (via Ryujinx / Sudachi)**
     * *Difficulty:* `8.1 / 10` | *Arch:* Nintendo Switch ARM64 (`AArch64`) $\rightarrow$ x64 JIT.
     * *Skills:* Understanding `main` NSO binary layouts, ARM64 assembly (`LDR`, `STR`, `B.NE`, `FMOV`), and Ultrahand physics constraints.
122. **Persona 5 / Demon's Souls / God of War III (via RPCS3 Emulator)**
     * *Difficulty:* `8.1 / 10` | *Arch:* PlayStation 3 Cell Broadband Engine (64-bit PPU + 128-bit SPU RISC).
     * *Skills:* Navigating RPCS3's `0x300000000` virtual memory mapping, endianness swaps, and SPU thread local store inspection.
123. **Bloodborne (via shadPS4 Emulator) & Shadow of the Colossus (via PCSX2)**
     * *Difficulty:* `8.2 / 10` | *Arch:* PS4 Orbis OS (FreeBSD x86_64 System V ABI) & PS2 Emotion Engine (MIPS R5900).
     * *Skills:* Reversing System V AMD64 ABI (`RDI`, `RSI`, `RDX`, `RCX`) `.sprx` modules in shadPS4 and MIPS assembly (`LUI`, `ORI`, `LW`, `SW`) in PCSX2.

---

### 🧬 Tier `SS-` : JVM Native Interface (JNI/JVMTI), Custom Protocol Emulation & Obfuscated Scripting — `Difficulty: 8.3–8.5 / 10`
*Bridging native C++ with managed virtual machines (JVM), obfuscated bytecode tables, and custom binary network protocols.*

124. **Lineage 2 Chronicle 2 (`L2.exe` Client & Custom C++ Server Protocol Lab)** ⭐
     * *Difficulty:* `8.3 / 10` | *Engine:* Modified Unreal Engine 2 (`Core.dll`, `Engine.dll`, `NWindow.dll`) + RSA/Blowfish Packet Crypto (**Connected to [`deavers/L2C2-Study-Server`](https://github.com/deavers/L2C2-Study-Server)**).
     * *Skills:* Reversing `L2.exe` packet serialization opcodes (`LoginServer` Blowfish + RSA key exchange, `GameServer` XOR stream cipher), reconstructing packet structures (`0x00 ProtocolVersion`, `0x0E AuthLogin`, `CharInfo`), and matching client-side expectations in a custom C++ study server.
125. **osu! (Offline Local Client / `osu!framework` Memory & Replay Analysis)** ⭐
     * *Difficulty:* `8.4 / 10` | *Engine:* Custom .NET / C# Framework + Mixed-Mode Native Assemblies (**Connected to `AimCoach` sensitivity & cursor analysis**).
     * *Skills:* Studying `.osr` LZMA replay binary structures, cursor trajectory smoothing/interpolation math, audio offset synchronization timers, and how mixed-mode `.NET` assemblies protect beatmap parser routines.
126. **Minecraft: Java Edition (Offline Singleplayer)**
     * *Difficulty:* `8.4 / 10` | *Engine:* JVM (Java Virtual Machine Bytecode + LWJGL OpenGL).
     * *Skills:* Attaching to the JVM via **JNI (Java Native Interface)** and **JVMTI** from an injected C++ DLL, translating obfuscated ProGuard mappings (Mojang/Yarn mappings), and runtime class bytecode redefinition.
127. **Custom LuaJIT 2.1 / PyInstaller Encrypted Indie Games**
     * *Difficulty:* `8.5 / 10` | *Engine:* Modified LuaJIT / Python Bytecode.
     * *Skills:* Reversing randomized LuaJIT opcode dispatch tables (`BC_ADD`, `BC_CALL`) and dumping decrypted `.pyc` / `.lua` chunks from memory at load time.

---

### 🌌 Tier `SS` : Procedural Math Engines, Custom Bytecode VMs & Legacy Ring-3 Packers — `Difficulty: 8.6–8.8 / 10`
*Targets where variables are computed mathematically on the fly, executed inside custom stack/register VMs, or wrapped in classic protectors.*

128. **No Man's Sky (Offline Mode)**
     * *Difficulty:* `8.6 / 10` | *Engine:* Custom Procedural Engine (x64 Vulkan).
     * *Skills:* Reversing procedural generation seed hashes, voxel terrain noise functions, and packed binary save-state structures.
129. **Custom ELF64 / PE64 ChaCha20 Packer & Reflective Loader (Self-Built Target)** ⭐
     * *Difficulty:* `8.7 / 10` | *Engine:* Custom C++20 / Assembly Stub (**Connected to [`deavers/lowlevel-re-and-exploitation`](https://github.com/deavers/lowlevel-re-and-exploitation)**).
     * *Skills:* Reversing your own encrypted packer stub (`Payload Entropy` $H \approx 7.99$), tracing `memfd_create` / `VirtualAlloc` unpacking in GDB/x64dbg, and automating unpackers.
130. **Legacy Offline Games Protected with SecuROM / SafeDisc / StarForce**
     * *Difficulty:* `8.8 / 10` | *Protection:* Ring-3 Packed PE Executables.
     * *Skills:* Finding the **Original Entry Point (OEP)** after decompression stubs, dumping the process with **Scylla**, and rebuilding a broken **Import Address Table (IAT)**.

---

### 🔒 Tier `SS+` : Commercial Virtualizers (VMProtect / Themida) & Self-Healing Checksums — `Difficulty: 8.9–9.1 / 10`
*Heavy commercial software protectors featuring code mutation, opaque predicates, and custom virtual machine bytecode.*

131. **Red Dead Redemption 2 & Need for Speed (2016) (Offline Checksum & Integrity Study)** ⭐
     * *Difficulty:* `8.9 / 10` | *Engine:* RAGE Engine & Frostbite 3 (x64 + **Arxan / Integrity Guards**).
     * *Skills:* Analyzing self-healing code checksums (Arxan integrity verification threads that hash `.text` pages and crash if a `0xE9` jump hook is detected), and using hardware breakpoints / VMT / page-guard hooks instead of `.text` patching.
132. **Offline CrackMes Protected with VMProtect v2 / v3 (Mutation & Virtualization)**
     * *Difficulty:* `9.0 / 10` | *Protection:* Stack-based RISC Virtual Machine.
     * *Skills:* Tracing `VM_Enter` pushes, logging virtual instruction pointer (`VIP`) dispatches across `VMP0`/`VMP1` sections, and identifying virtualized Win32 API calls.
133. **Offline CrackMes Protected with Themida / WinLicense (CISC VM & IAT Wrapping)**
     * *Difficulty:* `9.1 / 10` | *Protection:* Multi-threaded CISC Virtual Machine + Stolen Bytes.
     * *Skills:* Recovering stolen prologue bytes, unwrapping obfuscated import thunks, and tracing VM context structures.

---

### 🧩 Tier `SSS-` : Obfuscator-LLVM (O-LLVM), Mixed Boolean-Arithmetic (MBA) & Symbolic Execution — `Difficulty: 9.2–9.4 / 10`
*Mathematical de-obfuscation using SMT solvers (`Z3`), Dynamic Taint Analysis (`Triton`), and Symbolic Execution (`angr`).*

134. **Obfuscator-LLVM (O-LLVM) Control-Flow Flattening (CFF) & Bogus Control Flow (BCF) Binaries**
     * *Difficulty:* `9.2 / 10` | *Protection:* LLVM Pass Obfuscation.
     * *Skills:* Writing a **Ghidra / Binary Ninja Python script** or **Miasm** symbolic deflattener to eliminate state-machine switch dispatchers and recover the original Control Flow Graph (CFG).
135. **Mixed Boolean-Arithmetic (MBA) Expression Simplification Labs**
     * *Difficulty:* `9.3 / 10` | *Protection:* Linear & Polynomial MBA Obfuscation.
     * *Skills:* Collapsing 50-instruction bitwise/arithmetic tangles like $(x \oplus y) + 2 \cdot (x \land y)$ back into $x + y$ using **Z3 Theorem Prover**, **Arybo**, and **GAMBA**.
136. **Automated CrackMe & Bomb-Lab Solver with `angr` & `AFL++`** ⭐
     * *Difficulty:* `9.4 / 10` | *Tools:* `angr`, `Z3`, `AFL++` QEMU mode.
     * *Skills:* Defining symbolic bitvectors (`claripy.BVS`) over input buffers, pruning dead paths (`avoid=`), and automatically solving multi-stage binary constraints.

---

### ⚡ Tier `SSS` : Anti-Debug Labs, Ring-0 Kernel Drivers & Hypervisor VMI — `Difficulty: 9.5–9.7 / 10`
*Out-of-process and out-of-VM memory introspection: walking page tables from Linux KVM host or Ring-0 kernel space.*

137. **Advanced Anti-Debug & Anti-Tamper CrackMes (ScyllaHide / TitanHide Testbeds)**
     * *Difficulty:* `9.5 / 10` | *Skills:* Bypassing `IsDebuggerPresent`, `PEB->BeingDebugged`, `NtGlobalFlag`, `NtQueryInformationProcess` (`ProcessDebugPort`, `ProcessDebugObjectHandle`), TLS Callback traps, `RDTSC` timing checks, `NtSetInformationThread(ThreadHideFromDebugger)`, and Hardware Breakpoint (`DR0`–`DR7`) clearing.
138. **QEMU/KVM Virtual Machine Memory Introspection (Linux Host $\rightarrow$ Windows/Linux Guest)** ⭐
     * *Difficulty:* `9.6 / 10` | *Arch:* Linux Host (`EndeavourOS` / `Ubuntu`) inspecting isolated QEMU/KVM Guest (**Directly aligned with BSc Thesis Sandbox Architecture!**).
     * *Skills:* Reading a guest process's virtual memory directly from the Linux host (`memflow` / `libvmi` / `/dev/shm` looking-glass) by walking the x64 **CR3 Page Table Hierarchy** (`PML4` $\rightarrow$ `PDPT` $\rightarrow$ `PD` $\rightarrow$ `PT` $\rightarrow$ Physical Address) with **zero footprint** inside the guest OS.
139. **Writing a Custom Windows Kernel Driver (`Ring-0`) for Educational Memory Inspection**
     * *Difficulty:* `9.6 / 10` | *Skills:* Windows Driver Kit (WDK), `IoCreateDevice`, `IRP_MJ_DEVICE_CONTROL` (IOCTL), `MmCopyVirtualMemory`, `KeStackAttachProcess`, `EPROCESS` ActiveProcessLinks walking, and testing safely inside a VMware/QEMU test-signing VM.
140. **Custom Tiny Hypervisor (Intel VT-x / AMD-V EPT Shadow Page Hooking Lab)**
     * *Difficulty:* `9.7 / 10` | *Skills:* Extended Page Tables (EPT) shadow page splitting—marking a code page as Execute-Only (`R=0, W=0, X=1`) so memory reads/checksums return original bytes while instruction execution runs your hook cleanly.

---

### 💀 Tier `SSS+` : Full Matching Decompilation & 64-bit Planetary Engines — `Difficulty: 9.8–9.9 / 10`
*Reconstructing an entire commercial game engine back into compilable C/C++ source code that produces a byte-for-byte identical binary.*

141. **Matching Decompilation Projects (`decomp.me`, *Zelda: Ocarina of Time*, *Super Mario 64*, *Diablo 1 DevilutionX*)**
     * *Difficulty:* `9.8 / 10` | *Skills:* Taking raw assembly functions, writing clean C/C++ code, and tuning compiler flags until the compiled output matches $100\%$ of the original binary's bytes and register allocations.
142. **OpenMW (*Morrowind*) / OpenRCT2 (*RollerCoaster Tycoon 2*) / OpenXRay Engine Reimplementation**
     * *Difficulty:* `9.8 / 10` | *Skills:* Complete reverse engineering of proprietary file formats (`.NIF`, `.ESM`, `.DAT`), physics engines, audio pipelines, and AI state machines from scratch.
143. **Star Citizen (Offline Arena Commander / Singleplayer Sandbox Client)**
     * *Difficulty:* `9.9 / 10` | *Engine:* StarEngine (Heavily Modified CryEngine x64).
     * *Skills:* **64-bit Double-Precision (`double`) World Coordinates** spanning millions of kilometers, nested Local Physics Grids, and serialized entity component snapshots.
144. **Ghidra / Binary Ninja Custom Architecture & SLEIGH Processor Module Development**
     * *Difficulty:* `9.9 / 10` | *Skills:* Writing a custom processor specification in Ghidra's **SLEIGH** language to disassemble an undocumented proprietary game script bytecode or retro CPU.

---

### 👑🌌 Tier `SSS++` : God of Reverse Engineering (Silicon, Crypto & LLVM Binary Lifters) — `Difficulty: 10.0 / 10`
*The absolute apex of reverse engineering: hardware-software co-design, custom dynamic binary translators, and automated LLVM IR lifters.*

145. **Building an Automated Binary Lifter (x86_64 / VM Bytecode $\rightarrow$ LLVM IR)**
     * *Difficulty:* `10.0 / 10` | *Skills:* Using **Remill**, **McSema**, or custom **LLVM** passes to lift heavily obfuscated or virtualized game functions into LLVM Intermediate Representation (IR), running compiler optimization passes (`opt -O3`) to strip dead/junk instructions, and recompiling back into a clean native `.dll`.
146. **Arcade Hardware Security & Dongle Emulation (Sega Lindbergh, Taito Type X, Namco System 357)**
     * *Difficulty:* `10.0 / 10` | *Skills:* Reversing hardware USB security dongles (HASP/Sentinel), custom I/O JVS boards, and TPM/EEPROM cryptographic handshakes.
147. **Writing a Dynamic Binary Translator / Console Emulator JIT from Scratch**
     * *Difficulty:* `10.0 / 10` | *Skills:* Translating guest CPU instructions (e.g., ARM64 or MIPS) into optimized host `x86_64` machine code blocks at runtime with register caching and fast memory page tables.
148. **GPU Shader Reverse Engineering & Custom Graphics Wrapper (`d3d11.dll` / `dxgi.dll` Proxy)**
     * *Difficulty:* `10.0 / 10` | *Skills:* Intercepting compiled HLSL DXBC/DXIL or SPIR-V shader bytecode at runtime, decompiling shaders to extract depth/projection constant buffers (`cbuffer`), and injecting custom post-processing compute shaders.
149. **Silicon/Firmware Glitching & Embedded BootROM Reverse Engineering (Offline Hardware Lab)** ⭐
     * *Difficulty:* `10.0 / 10` | *Arch:* ESP32-S3 / ARM Cortex-M / SPI Flash (**Connected to [`deavers/iot-hardware-arsenal`](https://github.com/deavers/iot-hardware-arsenal)**).
     * *Skills:* Dumping firmware via SPI/UART/JTAG, analyzing encrypted bootloaders in Ghidra, fault injection / voltage glitching labs, and understanding hardware Chain of Trust.

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
