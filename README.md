# 🛡️ Reverse Engineering & Offline Game Hacking Journey

![Focus](https://img.shields.io/badge/Focus-Offline%20Reverse%20Engineering-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20x86%20%2F%20x64%20%7C%20Linux-informational?style=for-the-badge)
![Status](https://img.shields.io/badge/Current%20Rank-Tier%20C%20(Adventurer)-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **⚠️ Educational Disclaimer:** This repository documents my personal learning journey in **Low-Level Systems Architecture, x86/x64 Assembly, Binary Auditing, and Memory Analysis**. All research, Cheat Engine tables (`.CT`), and tools in this repository target **strictly local, single-player, offline games and crackmes**. There is zero involvement with multiplayer cheats, online services, or server-side exploitation.

---

## 📂 Repository Structure & Current Progress

```text
Reverse-Engineering-Journey/
├── 📁 Course_Solutions/       # Notes, exercises, and binary analysis labs from RE courses
├── 📁 Crackmes_and_CTF/       # Keygenmes, reverse engineering CTF writeups, and patches
├── 📁 Game_Hacking/           # Cheat Engine tables (.CT), Auto Assembler scripts, & trainers
│   ├── 📄 PvZ.CT                      # [Tier E+] Plants vs. Zombies (GOTY)
│   ├── 📄 UnrealTournament_UT99.CT    # [Tier D]  Unreal Tournament 99 (UE1)
│   ├── 📄 isaac-ng.CT                 # [Tier C-] The Binding of Isaac: Repentance
│   ├── 📄 StreetsOfRogue_v98.CT       # [Tier C]  Streets of Rogue (v98 Unity)
│   └── 📄 README.md                   # Detailed breakdown of offsets, pointers & scripts
├── 📁 Tools_and_Scripts/      # Custom C++/Python memory utilities, dumpers, and MCP scripts
├── 📄 .gitignore              # Clean filtering for IDA/Ghidra/VS/CE temporary artifacts
├── 📄 LICENSE                 # MIT License
└── 📄 README.md               # Main documentation & E-- to SSS++ Game RE Roadmap
```

### 🎯 Completed Milestones in `Game_Hacking/`

| Target Binary | Game Title | Engine / Arch | Tier | Status | Artifact |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `PlantsVsZombies.exe` | **Plants vs. Zombies** | PopCap Framework (x86) | **E+** | ✅ Done | [`PvZ.CT`](./Game_Hacking/PvZ.CT) |
| `UnrealTournament.exe` | **Unreal Tournament 99** | Unreal Engine 1 (x86) | **D** | ✅ Done | [`UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT) |
| `isaac-ng.exe` | **The Binding of Isaac: Repentance** | Custom C++20 Engine (x86) | **C-** | ✅ Done | [`isaac-ng.CT`](./Game_Hacking/isaac-ng.CT) |
| `StreetsOfRogue.exe` | **Streets of Rogue (v98)** | Unity Engine (x64) | **C** | ✅ Done | [`StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT) |

---

## 🤖 Deep Dive: What is REA (Reverse Engineer Anything)?

In late 2026, the open-source project **REA (Reverse Engineer Anything / `rea-agents`)** gained massive traction in the reverse engineering community. It is an AI-orchestration toolkit built around the **Model Context Protocol (MCP)**.

### How REA Works
* **Bridge Between LLMs and Binary Disassemblers:** REA is not a standalone disassembler. Instead, it acts as an MCP server and skill suite that connects AI coding agents (Claude Code, Cursor, Codex, etc.) directly to static and dynamic reverse engineering tools such as **Ghidra**, **Hopper**, **radare2/rizin**, **PE-bear**, **.NET decompilers (ILSpy/dnSpy CLI)**, and **Electron/ASAR unpackers**.
* **Automated Static Triage:** Instead of manually copying and pasting assembly listings into an LLM prompt, the agent queries the binary autonomously—extracting Cross-References (XREFs), String Literals, Import/Export Tables (IAT/EAT), and decompiled C pseudocode with exact virtual addresses.

### Pros & Cons for Game Reverse Engineering
* **✅ Strengths:**
  * **Instant Binary Triage:** Quickly identifies compilers (MSVC, Clang, MinGW), packer signatures, runtime libraries, and RTTI (Run-Time Type Information) class hierarchies.
  * **Scripting & Managed Code:** Excels at dissecting Unity Mono assemblies, Electron games, Python/Ren'Py bytecode, and Lua scripts.
  * **Math De-obfuscation:** Great at explaining complex SIMD (`SSE`/`AVX`) matrix transformations and physics formulas in decompiled code.
* **❌ Limitations:**
  * **Static $\neq$ Dynamic:** Game hacking is $70\%$ runtime dynamic memory analysis (Heap allocations, multi-level pointer chains, live VMT inspection, and thread-local storage). Static analysis alone cannot see runtime heap layouts without a live debugger attached.
  * **Hallucinated Offsets in Virtualized Code:** When confronted with heavy obfuscation or custom virtual machines, LLMs often guess control flow inaccurately.
* **💡 Verdict:** Use REA as a **Force Multiplier / Co-Pilot** alongside Ghidra and x64dbg, **never as a replacement** for mastering assembly and manual memory debugging.

---

## 🗺️ The 6-Stage Game Reverse Engineering Roadmap

### Stage 1: Memory Fundamentals & Dynamic Scanning (Cheat Engine)
* Virtual Memory Architecture, Pages, and Protection Flags (`PAGE_EXECUTE_READWRITE`).
* Data representations: `Byte`, `Int16`, `Int32`, `Int64`, `Float`, `Double`, IEEE-754, and Bitmasks.
* Static Base Addresses (`module.exe + 0xOFFSET`) vs. Dynamic Heap Allocations.
* Multi-level Pointer Chains, Pointer Scanning, and Structure Dissecting.
* Hardware/Software Breakpoints ("Find out what accesses/writes to this address").
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
  $$Address_{final} = \left[\left[\dots\left[\left[Base + \Delta_1\right] + \Delta_2\right]\dots\right] + \Delta_{n-1}\right] + \Delta_n$$

### Stage 4: Internal Development, DLL Injection & Function Hooking
* Anatomy of a Dynamic Link Library (`DllMain`, `DLL_PROCESS_ATTACH`, worker threads).
* Injection Techniques: `LoadLibraryA` via `CreateRemoteThread`, Thread Hijacking, and Manual Mapping (PE Header parsing, Base Relocations, IAT resolution, TLS callbacks).
* Inline / Trampoline Hooking: Overwriting function prologues ($5$-byte relative `JMP` in x86, $14$-byte absolute `JMP` in x64) and executing original bytes via a Gateway using **MinHook** or **Microsoft Detours**.
* Virtual Method Table (VMT) Hooking: Swapping function pointers in C++ class vtables.

### Stage 5: Engine Internals, Class Reconstruction & SDK Generation
* Live Memory Class Reconstruction using **ReClass.NET** (mapping padding, pointers, vtables, arrays).
* Extracting C++ RTTI (`type_info`, Complete Object Locator) to automatically name classes in IDA/Ghidra.
* **Unity Mono:** Decompiling `Assembly-CSharp.dll` with **dnSpyEx** / **ILSpy** and injecting via Mono Embedding API (`mono_domain_get`, `mono_runtime_invoke`).
* **Unity IL2CPP:** Reversing `GameAssembly.dll` + `global-metadata.dat` using **Il2CppDumper** and **Il2CppInspector**.
* **Unreal Engine (UE3/UE4/UE5):** Navigating `GWorld`, `GNames` (`FNamePool`), and `GUObjectArray`, and generating full C++ SDKs with **Dumper-7**.

### Stage 6: 3D Math, Graphics API Hooking & Internal GUIs
* Vector & Linear Algebra in 3D Space: Euclidean distance, Dot Product, Cross Product, Euler Angles (Pitch $\theta$, Yaw $\psi$, Roll $\phi$).
* Projection Mathematics: View-Projection Matrix ($4 \times 4$) and the **WorldToScreen (W2S)** algorithm converting 3D world coordinates $(X, Y, Z)$ into 2D screen coordinates $(x_{screen}, y_{screen})$ via Clip Space and Normalized Device Coordinates ($NDC_x, NDC_y \in [-1, 1]$).
* Graphics Hooking: Hooking `IDXGISwapChain::Present` / `ResizeBuffers` (DirectX 11/12), `IDirect3DDevice9::EndScene` (DX9), `wglSwapBuffers` (OpenGL), or `vkQueuePresentKHR` (Vulkan).
* Rendering custom **Dear ImGui** interactive menus and 2D/3D ESP overlays inside the game's render pipeline.

---

## 🏆 The Ultimate RPG Tier List of Offline Games for Reverse Engineering (`E--` $\rightarrow$ `SSS++`)

This comprehensive progression ladder features **23 distinct RPG ranks** and **115 carefully selected offline games and targets**, ordered by memory complexity, architecture, engine internals, and binary protection.

```text
╔════════════════════════════════════════════════════════════════════════════╗
║                  REVERSE ENGINEERING DIFFICULTY HIERARCHY                  ║
╠══════════╦═════════════════════════════════════════════════════════════════╣
║  SSS++   ║ Silicon, Firmware, Arcade Crypto & Custom JIT Binary Lifters    ║
║  SSS+    ║ Full Matching Binary Decompilation & 64-bit Space Engines       ║
║  SSS     ║ Hypervisor Introspection, LLVM MBA De-obfuscation & Anti-Debug  ║
║  SS      ║ Custom Bytecode VMs, Packers (VMP/Themida), Procedural Math     ║
║  S+      ║ Console Emulators (PowerPC Big-Endian, PS3 Cell, ARM64 Switch)  ║
║  S       ║ Data-Oriented Design (DOD), Custom Allocators & Voxel Engines   ║
║  S-      ║ Soulslike Proprietary Engines, Havok Physics & Param Tables     ║
║  A+      ║ Hybrid C++/Lua Engines, RE Engine & Divinity 4.0 Internals      ║
║  A       ║ Unity IL2CPP (Stripped C# to Native x64 C++ Assembly)           ║
║  A-      ║ Unreal Engine 4 & 5 (GWorld, FNamePool, Dumper-7 SDKs)          ║
║  B+      ║ Modern AAA x64 Proprietary Engines (REDengine, RAGE, id Tech 7) ║
║  B       ║ Source Engine (Netvars/VMT) & Unreal Engine 3                   ║
║  B-      ║ Mature 32/64-bit Open-World Engines (Creation, Gamebryo, X-Ray) ║
║  C+      ║ Advanced Unity Mono, Harmony Patching & Complex Simulations     ║
║  C       ║ Unity Mono & .NET CLR (dnSpy Decompilation & IL Editing)        ║
║  C-      ║ 2D Roguelikes, Custom C++ State Machines & GameMaker Bytecode   ║
║  D+      ║ Classic 32-bit Open-World & Racing (RenderWare, ZenGin)         ║
║  D       ║ Early 2000s 3D Arena Shooters (UE1, GoldSrc, MAX-FX)            ║
║  D-      ║ 90s Retro 2.5D/3D Engines (id Tech 1/2, Build Engine)           ║
║  E+      ║ Casual 32-bit Frameworks (PopCap Engine)                        ║
║  E       ║ Open-Source FPS Sandboxes (AssaultCube, Sauerbraten, Quake III) ║
║  E-      ║ Classic Win32 Desktop Games (Minesweeper, Pinball, Solitaire)   ║
║  E--     ║ Purpose-Built Educational Tutorials & Gamified RE Labs          ║
╚══════════╩═════════════════════════════════════════════════════════════════╝
```

---

### 🌱 Tier `E--` : Absolute Zero (Purpose-Built Educational Labs)
*Designed specifically to teach memory scanning, pointers, and assembly patching in a controlled environment.*

1. **Cheat Engine Built-in Tutorial (`Tutorial-i386.exe` & `Tutorial-x86_64.exe`)**
   * *Skills:* Steps 1–9. Exact/Unknown scans, floating-point values, code finding, single/multi-level pointers, Auto Assembler injection, and shared code separation.
2. **Squally**
   * *Engine:* Unity / Custom x86 التعليمية RPG.
   * *Skills:* A 2D platformer RPG where you literally solve puzzles by editing x86 assembly and memory flags in-game.
3. **PwnAdventure 3: Pwnie Island (Offline Local Server & Client)**
   * *Engine:* Unreal Engine 3 (Created by Vector 35 / Binary Ninja team).
   * *Skills:* Built specifically for reverse engineering practice—patching client logic, teleportation, and reversing DLL game logic (`GameLogic.dll`).
4. **Custom Local CLI CrackMes & Memory Target Apps**
   * *Engine:* Native C/C++ Console Apps.
   * *Skills:* Writing a 20-line C++ loop with `health` and `ammo` variables, compiling it yourself, and reversing your own binary in Cheat Engine and Ghidra.
5. **Microcorruption (Embedded Assembly Simulator)**
   * *Arch:* MSP430 Assembly.
   * *Skills:* Pure register, stack, and memory flag manipulation through interactive debugger challenges.

---

### 🪵 Tier `E-` : Desktop Win32 Classics (Static Memory & 2D Arrays)
*Tiny executables, zero obfuscation, deterministic Win32 API loops, and easily readable global variables.*

6. **Windows Minesweeper (`winmine.exe` — WinXP / Win7)**
   * *Engine:* Native Win32 C.
   * *Skills:* Locating the static 2D byte array representing the minefield grid, freezing the timer, and calling the internal `Win` function.
7. **3D Pinball: Space Cadet (`pinball.exe`)**
   * *Engine:* Native 32-bit Win32 C.
   * *Skills:* Score manipulation, infinite balls, plunger physics floats, and tilting counter patches.
8. **Microsoft Solitaire / Spider Solitaire (WinXP / Win7)**
   * *Engine:* Win32 C++.
   * *Skills:* Reversing card deck structures, score multipliers, and forcing legal card moves via conditional jump patches (`JNZ` $\rightarrow$ `JMP`).
9. **Purble Place (Win7)**
   * *Engine:* Win32 C++ / DirectX.
   * *Skills:* Timer freezes, memory structure of pattern matching mini-games.
10. **SkiFree (`skifree.exe` 32-bit build)**
    * *Engine:* Win32 C.
    * *Skills:* Speed floats, distance counters, and disabling the Abominable Snowman spawn check.

---

### 🔰 Tier `E` : Beginner Sandboxes (Open-Source FPS Classics)
*You have access to the original C++ source code to verify your reverse-engineered structures in ReClass.NET.*

11. **AssaultCube (`ac_client.exe`)**
    * *Engine:* Cube Engine (x86 C++ Open-Source).
    * *Skills:* **The #1 Beginner Benchmark.** LocalPlayer pointer (`0x50F4F4`), EntityList array, Health/Ammo/Recoil, ViewMatrix $4 \times 4$, WorldToScreen ESP, and ViewAngle math.
12. **Cube 2: Sauerbraten**
    * *Engine:* Cube 2 Engine (x86/x64 C++ & OpenGL).
    * *Skills:* Octree world geometry, player velocity vectors, and OpenGL `wglSwapBuffers` hooking.
13. **Quake III Arena / OpenArena (`ioquake3`)**
    * *Engine:* id Tech 3 (C).
    * *Skills:* Pure C structs (`centity_t`, `clientInfo_t`), `vmMain` bytecode/native DLL calls, and Strafe/BunnyHop velocity math.
14. **Teeworlds (Offline Local Practice)**
    * *Engine:* Custom 2D C++ Engine.
    * *Skills:* 2D coordinate vectors, hook physics, and projectile trajectory math.
15. **SuperTuxKart**
    * *Engine:* Antarctica Engine (Open-Source C++).
    * *Skills:* Nitro boost floats, kart physics structures, and lap counter manipulation.

---

### 🥉 Tier `E+` : Casual 32-bit Frameworks (PopCap & Arcade)
*Clean 32-bit C++ class hierarchies with simple 1-to-3 level pointer chains.*

16. **Plants vs. Zombies (GOTY Edition)** — *(✅ Completed in [`Game_Hacking/PvZ.CT`](./Game_Hacking/PvZ.CT))*
    * *Engine:* PopCap Framework (x86 C++).
    * *Skills:* Sun counter (`+0x5560`), plant slot recharge timers, projectile ID swapping (shooting cob cannons from peashooters), and coin bypasses.
17. **Peggle Deluxe / Peggle Nights**
    * *Engine:* PopCap Framework (x86).
    * *Skills:* Free ball counters, trajectory guide line length extension, and fever meter manipulation.
18. **Zuma Deluxe**
    * *Engine:* PopCap Framework (x86).
    * *Skills:* Linked list of rolling spheres, frog rotation float, and score multipliers.
19. **Insaniquarium Deluxe**
    * *Engine:* PopCap Framework (x86).
    * *Skills:* Shell currency, fish hunger timers, and alien spawn timers.
20. **Bejeweled 3**
    * *Engine:* PopCap Framework (x86).
    * *Skills:* 2D board matrix scanning, timer freezes, and score multiplier hooks.

---

### 🗡️ Tier `D-` : 90s Retro 2.5D & 3D Engines (Fixed-Point & Sector Math)
*Classic C/C++ engines that teach low-level memory arrays, bitflags, and fixed-point arithmetic.*

21. **Doom I & Doom II (Crispy Doom / Chocolate Doom / GZDoom)**
    * *Engine:* id Tech 1 (C/C++).
    * *Skills:* `mobj_t` actor structures, fixed-point numbers ($16.16$), sector lighting, and god-mode bitflags.
22. **Duke Nukem 3D (EDuke32)**
    * *Engine:* Build Engine.
    * *Skills:* Sprite/wall/sector static arrays, jetpack fuel, steroid timers, and weapon ammo tables.
23. **Blood: Fresh Supply / Shadow Warrior Classic**
    * *Engine:* Build Engine / KEX Engine.
    * *Skills:* Actor state machines, flare damage multipliers, and inventory structs.
24. **Quake I & Quake II**
    * *Engine:* id Tech 2.
    * *Skills:* Edict structures (`edict_t`), QuakeC virtual machine stack, and `glBegin`/`glEnd` wallhack fundamentals.
25. **Wolfenstein 3D / Spear of Destiny (ECWolf)**
    * *Engine:* Wolf3D Raycaster.
    * *Skills:* 64$\times$64 tilemap memory grids, secret pushwall flags, and guard state machines.

---

### 🛡️ Tier `D` : Early 2000s 3D Arena & Action Classics
*Introduction to early object-oriented C++ game engines, virtual tables, and console CVARs.*

26. **Unreal Tournament 99 (`UT99`)** — *(✅ Completed in [`Game_Hacking/UnrealTournament_UT99.CT`](./Game_Hacking/UnrealTournament_UT99.CT))*
    * *Engine:* Unreal Engine 1 (x86 C++ & UnrealScript).
    * *Skills:* First look at Unreal's `UObject` / `AActor` / `APawn` hierarchy, weapon ammo offsets, health, and dodge physics.
27. **Half-Life 1 (1998 Original)**
    * *Engine:* GoldSrc (`hw.dll` & `client.dll`).
    * *Skills:* `cl_entity_s` array, engine function table pointers (`cl_enginefunc_t`), and bunnyhop ground flags.
28. **Counter-Strike 1.6 (Offline with Bots)**
    * *Engine:* GoldSrc (x86).
    * *Skills:* Bone matrix positions, punch angle (recoil) vectors, money offsets, and OpenGL studio renderer hooks.
29. **Max Payne 1 & Max Payne 2**
    * *Engine:* MAX-FX Engine (x86).
    * *Skills:* Bullet-time hourglass float, painkiller inventory counters, and projectile speed hooks.
30. **Serious Sam: Classic First & Second Encounter**
    * *Engine:* Serious Engine 1 (Open-Source C++).
    * *Skills:* Massive entity spawners, armor/health/ammo pointers, and gravity modifiers.

---

### 🏹 Tier `D+` : Classic 32-bit Open-World & Racing
*Large static memory pools, vehicle physics structs, and script thread engines.*

31. **Grand Theft Auto: Vice City & San Andreas (Original x86)**
    * *Engine:* RenderWare (x86 C++).
    * *Skills:* Direct static pools for `CPed` (`0xB6F5F0`) and `CVehicle`, weapon slots, wanted level stars, and calling internal engine functions (`CHud::SetHelpMessage`).
32. **FlatOut 2**
    * *Engine:* Custom x86 C++ Engine.
    * *Skills:* Vehicle mass/torque floats, nitro regeneration, ragdoll launch velocity vectors, and cash rewards.
33. **Need for Speed: Underground 2 & Most Wanted (2005)**
    * *Engine:* EAGL (EA Graphics Library x86).
    * *Skills:* Speedbreaker meter, N2O float, heat level, bounty points, and car handling physics structs.
34. **Gothic I & Gothic II: Night of the Raven**
    * *Engine:* ZenGin (x86 C++).
    * *Skills:* `oCNpc` class reconstruction, mana/health/LP attributes, and Daedalus script VM inspection.
35. **Star Wars: Knights of the Old Republic (KOTOR I & II)**
    * *Engine:* Odyssey Engine (x86).
    * *Skills:* D20 combat roll hooks, Force points, alignment shifts, and inventory item duplication.

---

### 🔮 Tier `C-` : 2D Indie Roguelikes, State Machines & Bytecode Engines
*Dynamic heap allocations, procedural rooms, entity component lists, and custom 2D engines.*

36. **The Binding of Isaac: Rebirth / Repentance (`isaac-ng.exe`)** — *(✅ Completed in [`Game_Hacking/isaac-ng.CT`](./Game_Hacking/isaac-ng.CT))*
    * *Engine:* Custom x86 C++ Engine + Lua 5.3.
    * *Skills:* `Entity_Player` pointer chains, Red/Soul/Black heart bitmasks, tear delay/fire rate formulas, Bombs/Keys/Coins, and pedestal item ID swapping.
37. **FTL: Faster Than Light**
    * *Engine:* Custom C++ Engine (x86/x64).
    * *Skills:* Hull integrity, reactor power bars, weapon charge floats, scrap currency, and crew health structs.
38. **Spelunky HD**
    * *Engine:* Custom C++ DirectX 9 Engine.
    * *Skills:* Procedural level tile grid in memory, bomb/rope counters, whip damage, and ghost spawn timer freeze.
39. **Hotline Miami 1 & 2**
    * *Engine:* GameMaker / PhyreEngine.
    * *Skills:* Combo multiplier timers, weapon ammo counts, and AI line-of-sight checks.
40. **Undertale / Deltarune**
    * *Engine:* GameMaker Studio (`data.win` VM Bytecode).
    * *Skills:* Using **UndertaleModTool** alongside Cheat Engine to understand how GameMaker stores dynamic `double` variables in hash maps.

---

### 🥈 Tier `C` : Unity Mono & .NET CLR (Decompilation & Bytecode Editing)
*JIT-compiled C# assemblies (`Assembly-CSharp.dll`) where full class, method, and field names are preserved.*

41. **Streets of Rogue (`StreetsOfRogue_v98`)** — *(✅ Completed in [`Game_Hacking/StreetsOfRogue_v98.CT`](./Game_Hacking/StreetsOfRogue_v98.CT))*
    * *Engine:* Unity Engine (Mono / x64).
    * *Skills:* Enabling Cheat Engine's `.NET / Mono Dissector`, locating `Agent`, `InvDatabase`, `Stat` classes, infinite durability/ammo, and trait points.
42. **Hollow Knight**
    * *Engine:* Unity (Mono).
    * *Skills:* Inspecting `HeroController` and `PlayerData` in **dnSpy**, infinite Soul, Geo, Charm Notches, and invincible shadow dash.
43. **Cuphead**
    * *Engine:* Unity (Mono).
    * *Skills:* Reversing `LevelPlayerWeaponManager`, locking Ex-Move super meter cards, and boss HP tracking.
44. **Stardew Valley**
    * *Engine:* .NET / MonoGame (`Stardew Valley.dll`).
    * *Skills:* Reversing `Game1.player`, stamina float, time-of-day freeze, and luck level manipulation.
45. **Terraria**
    * *Engine:* C# XNA / FNA (.NET JIT).
    * *Skills:* JIT signature scanning for `Terraria.Player::Update`, infinite mana/wing flight time, and tile reach range.

---

### ⚡ Tier `C+` : Advanced Unity Mono, Harmony Patching & Complex Sims
*Large managed codebases with thousands of interacting classes, mod loaders (BepInEx/Harmony), and physics systems.*

46. **RimWorld**
    * *Engine:* Unity (Mono) + XML Defs.
    * *Skills:* Writing C# runtime prefix/postfix hooks with **Harmony**, colonist mood/skill structs, and instant construction patches.
47. **Subnautica (Legacy Mono / Current Builds)**
    * *Engine:* Unity.
    * *Skills:* `OxygenManager`, `LiveMixin` (universal health component), depth crush immunity, and blueprint unlocking.
48. **Kerbal Space Program 1**
    * *Engine:* Unity (Mono).
    * *Skills:* Orbital mechanics vectors, fuel tank resource structures, and heat shield temperature floats.
49. **Vampire Survivors**
    * *Engine:* Unity (Mono).
    * *Skills:* Enemy wave spawner intervals, magnet pickup radius, gold multiplier, and weapon cooldown arrays.
50. **ULTRAKILL**
    * *Engine:* Unity (Mono).
    * *Skills:* Style meter points, stamina regeneration, weapon cooldowns, and hitstop frame timers.

---

### ⚔️ Tier `B-` : Mature 32/64-bit Open-World Engines (Creation, Gamebryo, X-Ray)
*Massive C++ inheritance trees, RTTI analysis, RefIDs/FormIDs, and custom scripting engines.*

51. **Fallout: New Vegas & Fallout 3**
    * *Engine:* Gamebryo (x86 C++).
    * *Skills:* `ActorValueOwner` VMT, FormIDs, S.P.E.C.I.A.L. stats, carry weight, and V.A.T.S. accuracy calculation hooks.
52. **The Elder Scrolls V: Skyrim Special Edition (`SkyrimSE.exe`)**
    * *Engine:* Creation Engine (x64 C++).
    * *Skills:* Reversing `PlayerCharacter` singleton, Papyrus VM hooks,shout cooldowns, and SKSE address library offsets.
53. **S.T.A.L.K.E.R.: Call of Pripyat / Anomaly (`OpenXRay`)**
    * *Engine:* X-Ray Engine (x64 C++ + Lua).
    * *Skills:* `CActor` class layout, radiation/psy-health floats, weapon dispersion/recoil, and inventory weight.
54. **Mount & Blade: Warband**
    * *Engine:* Custom x86 C++ Engine.
    * *Skills:* Party size limits, renown/morale pointers, troop XP tables, and agent combat speed.
55. **Far Cry 2 & Far Cry 3**
    * *Engine:* Dunia Engine (x86 C++).
    * *Skills:* Weapon degradation counters, malaria pill timers, syringe buffs, and world entity lists.

---

### 🛡️ Tier `B` : Source Engine (Netvars/VMT) & Unreal Engine 3
*Industry-standard FPS/Action architectures with formal interface systems and virtual method tables.*

56. **Portal 2 & Half-Life 2 (x64 Update)**
    * *Engine:* Source Engine (`client.dll` & `engine.dll`).
    * *Skills:* Walking the `ClientClass` linked list to dump **Netvars** (`DT_BasePlayer`), `CreateMove` VMT hooking, and portal placement checks.
57. **Left 4 Dead 2 (Offline Singleplayer)**
    * *Engine:* Source Engine.
    * *Skills:* Entity list iteration (`IClientEntityList`), infected bone matrices, shove cooldowns, and melee reach.
58. **Borderlands 2**
    * *Engine:* Unreal Engine 3 (x86).
    * *Skills:* Generating an UE3 SDK, understanding modular weapon part structures, Badass Rank tokens, and shield capacity.
59. **Dishonored 1**
    * *Engine:* Unreal Engine 3 (x86).
    * *Skills:* Mana potion regeneration checks, Blink teleportation distance limiters, and AI vision cone floats.
60. **BioShock Infinite**
    * *Engine:* Unreal Engine 3.
    * *Skills:* Salts/Shield/Health structures, Silver Eagle currency, and weapon upgrade bitflags.

---

### 🔥 Tier `B+` : Modern AAA x64 Proprietary C++ Engines
*Complex 64-bit engines with ASLR, SIMD (`XMM`/`YMM`) math everywhere, and multi-threaded job systems.*

61. **The Witcher 3: Wild Hunt (Next-Gen v4.04 x64)**
    * *Engine:* REDengine 3 (x64 C++).
    * *Skills:* Deep RTTI class hierarchies (`CR4Player`), Stamina/Toxicity/Adrenaline floats, Witcher script VM, and inventory weight.
62. **Cyberpunk 2077**
    * *Engine:* REDengine 4 (x64 C++ / DirectX 12).
    * *Skills:* Cyberware RAM regeneration, optical camo timers, street cred/perk points, and RED4ext structure layouts.
63. **Grand Theft Auto V (Strictly Offline Story Mode)**
    * *Engine:* RAGE Engine (x64 C++).
    * *Skills:* `CPedFactory` (`WorldPtr`), `CReplayInterface` entity iteration, Native Invoker (`scrNativeCallContext`), and vehicle handling flags.
64. **Doom (2016) & Doom Eternal**
    * *Engine:* id Tech 6 & id Tech 7 (x64 Vulkan).
    * *Skills:* Vulkan `vkQueuePresentKHR` overlay hooking, idDecl weapon definitions, blood punch charges, and dash cooldowns.
65. **Metro Exodus**
    * *Engine:* 4A Engine (x64).
    * *Skills:* Gas mask filter timers, pneumatic weapon pressure floats, battery charge, and crafting resources.

---

### 🥇 Tier `A-` : Unreal Engine 4 & 5 (`GWorld`, `FNamePool` & SDK Dumping)
*Mastering modern Unreal Engine memory reflection (`UObject`, `UStruct`, `UFunction`, `ProcessEvent`).*

66. **Lies of P**
    * *Engine:* Unreal Engine 4 (x64).
    * *Skills:* Dumping SDK with **Dumper-7**, hooking `UObject::ProcessEvent`, Legion Arm energy, weapon durability, and parry window frames.
67. **Palworld (Offline Singleplayer)**
    * *Engine:* Unreal Engine 5 (x64).
    * *Skills:* `GWorld` $\rightarrow$ `PersistentLevel` $\rightarrow$ `Actors` array traversal, Pal capture rate formulas, work speed, and stamina.
68. **Clair Obscur: Expedition 33 / Black Myth: Wukong**
    * *Engine:* Unreal Engine 5 (x64).
    * *Skills:* UE5 `FNamePool` decryption/indexing, action timing windows, cooldowns, and camera FOV overrides.
69. **Deep Rock Galactic (Offline Solo Mode)**
    * *Engine:* Unreal Engine 4 (x64).
    * *Skills:* Flare recharge timers, nitra/gold mineral multipliers, overheating gauges, and Bosco drone behavior.
70. **S.T.A.L.K.E.R. 2: Heart of Chornobyl**
    * *Engine:* Unreal Engine 5.1 (x64).
    * *Skills:* Complex UE5 world partitioning (`UWorldPartition`), anomaly damage mitigation, and artifact stat modifiers.

---

### 🏆 Tier `A` : Unity IL2CPP (Stripped Metadata & Native x64 Assembly)
*C# code transpiled to C++ and compiled into native x64 machine code (`GameAssembly.dll`). No CIL bytecode left.*

71. **Risk of Rain 2 (IL2CPP Build)**
    * *Engine:* Unity IL2CPP (x64).
    * *Skills:* Running **Il2CppDumper** on `GameAssembly.dll` + `global-metadata.dat`, importing generated headers into Ghidra/IDA, and hooking `CharacterBody::RecalculateStats`.
72. **Sons of the Forest**
    * *Engine:* Unity IL2CPP (x64).
    * *Skills:* Reversing `VailActor` AI structs, inventory item limits, log building instant-complete hooks, and survival stats.
73. **Cult of the Lamb**
    * *Engine:* Unity IL2CPP (x64).
    * *Skills:* Follower faith/hunger structures, fervor regeneration, and tarot card modifier arrays.
74. **Dyson Sphere Program**
    * *Engine:* Unity IL2CPP (x64).
    * *Skills:* Mecha energy core floats, research hash rate multipliers, and planetary logistics array structures.
75. **SPT-AKI (Single Player Tarkov Offline Sandbox Mod)**
    * *Engine:* Unity (Mono / IL2CPP hybrid architecture).
    * *Skills:* Complex skeletal bone hierarchy (`BifacialTransform`), ballistics penetration math, procedural weapon recoil, and optic Picture-in-Picture (PiP) WorldToScreen.

---

### 💎 Tier `A+` : Complex Proprietary Engines & Hybrid Scripting Bridges
*Custom AAA C++ cores tightly coupled with embedded scripting VMs or custom Entity-Component-Systems (ECS).*

76. **Hades I & Hades II**
    * *Engine:* Supergiant Custom C++ Engine + Lua 5.2/5.4.
    * *Skills:* Locating the global `lua_State*` pointer in native x64 code, hooking `luaL_loadbuffer`, and injecting custom Lua boons directly into the runtime state.
77. **Resident Evil 2 / 3 / 4 Remake & RE Village**
    * *Engine:* Capcom **RE Engine** (x64 C++).
    * *Skills:* Managed C#-style internal reflection inside a native C++ engine (`via.ManagedObject`), dynamic enemy HP scaling (Adaptive Difficulty rank), and skeletal joint matrices.
78. **Devil May Cry 5**
    * *Engine:* Capcom RE Engine (x64).
    * *Skills:* Devil Trigger gauges, Sin DT timers, Royal Guard release frames, and Style rank decay freezes.
79. **Baldur's Gate 3**
    * *Engine:* Divinity Engine 4.0 (x64 ECS + Osiris Scripting).
    * *Skills:* Navigating a pure **Entity-Component-System (ECS)** architecture where data is split across hundreds of component pools rather than a single `Player` class.
80. **Control / Alan Wake 2**
    * *Engine:* Remedy Northlight Engine (x64).
    * *Skills:* Telekinesis energy pools, Havok physics object throwing velocity, and custom shader pipeline hooks.

---

### 👑 Tier `S-` : Soulslike Proprietary Engines, Havok Physics & Param Tables
*Intricate animation state machines, encrypted regulation files, and frame-perfect combat flags.*

81. **Dark Souls III (Strictly Offline Mode)**
    * *Engine:* FromSoftware Dantelion Engine (x64).
    * *Skills:* `WorldChrMan` singleton traversal, animation event flags (Invincibility frames / i-frames), stamina consumption, and `Param` table memory patching.
82. **Sekiro: Shadows Die Twice**
    * *Engine:* Dantelion Engine (x64).
    * *Skills:* Posture bar regeneration/damage floats, Spirit Emblem counters, and deflect window frame extensions.
83. **Elden Ring + Shadow of the Erdtree (Strictly Offline / EAC Disabled via Launch Flag)**
    * *Engine:* Dantelion 2 Engine (x64 DirectX 12).
    * *Skills:* `CSChrIns` hierarchy, SpEffect IDs (buffs/debuffs), Poise floats, Scadutree blessing multipliers, and DX12 command queue ImGui rendering.
84. **Armored Core VI: Fires of Rubicon (Offline Mode)**
    * *Engine:* Dantelion Engine (x64).
    * *Skills:* EN (Energy) generator output/recovery delay, ACS stagger gauge, and lock-on tracking speed.
85. **Monster Hunter: World (Offline Solo)**
    * *Engine:* Capcom MT Framework (x64).
    * *Skills:* Weapon sharpness gauges, monster part break HP thresholds, and Mantle cooldown timers.

---

### 🌟 Tier `S` : Data-Oriented Design (DOD), Custom Allocators & Voxel Engines
*No traditional OOP classes: memory is packed into cache-aligned SoA (Structure of Arrays) slabs or custom cellular automata.*

86. **Factorio**
    * *Engine:* Custom Ultra-Optimized C++20 Engine.
    * *Skills:* Deterministic tick architecture, custom slab memory allocators, belt item spacing math, and Lua API bridge internals.
87. **Noita**
    * *Engine:* FallingEverything Engine (Custom C++ + LuaJIT).
    * *Skills:* Cellular automata memory grid (every single pixel's material, velocity, and temperature simulated in memory), wand recharge/cast delay structs, and deterministic seed PRNG reversing.
88. **Teardown**
    * *Engine:* Custom C++ Voxel Raytracing Engine.
    * *Skills:* 3D voxel octree buffers in RAM/VRAM, structural integrity stress checks, and tool ammo counters.
89. **Dwarf Fortress (Steam Edition)**
    * *Engine:* Custom C++ Simulation Engine.
    * *Skills:* Contributing to or studying **DFHack**—reversing massive historical entity vectors, dwarf personality structs, and fluid grids.
90. **Mount & Blade II: Bannerlord**
    * *Engine:* Custom C++ Engine + Custom .NET Host.
    * *Skills:* Reversing the native-to-managed P/Invoke bridge handling 2,000+ simultaneous AI combat agents in real time.

---

### 🪐 Tier `S+` : Console Emulators, Big-Endian Memory & Cross-Arch JIT
*Reversing a guest console CPU architecture (PowerPC, Cell SPU, ARM64) translated inside an x64 host emulator process.*

91. **The Legend of Zelda: Breath of the Wild (via Cemu Emulator)**
    * *Arch:* Wii U Espresso PowerPC (32-bit **Big-Endian**) $\rightarrow$ x64 Host.
    * *Skills:* Registering custom Big-Endian value types (`4 Byte Big Endian`, `Float Big Endian`) in Cheat Engine, resolving emulated base memory (`memory_base`), and patching PowerPC assembly instructions.
92. **The Legend of Zelda: Tears of the Kingdom (via Ryujinx / Sudachi)**
    * *Arch:* Nintendo Switch ARM64 (`AArch64`) $\rightarrow$ x64 JIT.
    * *Skills:* Understanding `main` NSO binary layouts, ARM64 assembly (`LDR`, `STR`, `B.NE`, `FMOV`), and Ultrahand physics constraints.
93. **Persona 5 / Demon's Souls / God of War III (via RPCS3 Emulator)**
    * *Arch:* PlayStation 3 Cell Broadband Engine (64-bit PPU + 128-bit SPU RISC).
    * *Skills:* Navigating RPCS3's `0x300000000` virtual memory mapping, endianness swaps, and SPU thread local store inspection.
94. **Bloodborne (via shadPS4 Emulator)**
    * *Arch:* PlayStation 4 Orbis OS (FreeBSD x86_64 ELF/SELF) $\rightarrow$ Windows x64.
    * *Skills:* Reversing System V AMD64 ABI (`RDI`, `RSI`, `RDX`, `RCX`) binaries running inside a Windows wrapper, resolving `.sprx` modules, and frame-pacing patches.
95. **Shadow of the Colossus / God of War II (via PCSX2 Emulator)**
    * *Arch:* PlayStation 2 Emotion Engine (MIPS R5900 + VU0/VU1 Vector Units).
    * *Skills:* MIPS assembly reversing (`LUI`, `ORI`, `LW`, `SW`), EE memory mirror ranges (`0x20000000`), and grip stamina floats.

---

### 🌌 Tier `SS` : Procedural Math, Custom Bytecode VMs & Binary Packers
*Targets where variables are computed mathematically on the fly, executed inside custom bytecode interpreters, or wrapped in commercial protectors.*

96. **No Man's Sky (Offline Mode)**
    * *Engine:* Custom Procedural Engine (x64 Vulkan).
    * *Skills:* Reversing procedural generation seed hashes, voxel terrain noise functions, and packed binary save-state structures.
97. **Minecraft: Java Edition (Offline Singleplayer)**
    * *Engine:* JVM (Java Virtual Machine Bytecode + LWJGL OpenGL).
    * *Skills:* Attaching to the JVM via **JNI (Java Native Interface)** and **JVMTI** from an injected C++ DLL, translating obfuscated ProGuard mappings (Mojang/Yarn mappings), and class bytecode redefinition.
98. **Custom LuaJIT / Python Bytecode Obfuscated Indie Games**
    * *Engine:* Modified LuaJIT 2.1 / PyInstaller Encrypted Archives.
    * *Skills:* Reversing randomized LuaJIT opcode dispatch tables (`BC_ADD`, `BC_CALL`) and dumping decrypted bytecode chunks from memory at load time.
99. **Legacy Offline Games Protected with SecuROM / SafeDisc / StarForce**
    * *Protection:* Ring-3 Packed PE Executables.
    * *Skills:* Finding the **Original Entry Point (OEP)** after decompression stubs, dumping the process with **Scylla**, and rebuilding a broken **Import Address Table (IAT)**.
100. **Offline CrackMes & Mod Targets with VMProtect v2 / Themida**
     * *Protection:* Code Mutation & Custom RISC/Stack Virtual Machines.
     * *Skills:* Tracing VM entry (`VM_Enter`), analyzing handlers in `VMP0`/`VMP1` sections, and devirtualizing simple routines.

---

### ⚡ Tier `SSS` : Anti-Debug Labs, LLVM Obfuscation & Hypervisor Introspection
*Advanced defensive/offensive binary research: defeating anti-debugging checks, simplifying Mixed Boolean-Arithmetic (MBA), and out-of-VM memory inspection.*

101. **Advanced Anti-Debug & Anti-Tamper CrackMes (ScyllaHide / TitanHide Testbeds)**
     * *Skills:* Bypassing `IsDebuggerPresent`, `PEB->BeingDebugged`, `NtGlobalFlag`, `NtQueryInformationProcess` (`ProcessDebugPort`), TLS Callback traps, `RDTSC` timing checks, and Hardware Breakpoint (`DR0`–`DR7`) clearing via `GetThreadContext`.
102. **Obfuscator-LLVM (O-LLVM) & Mixed Boolean-Arithmetic (MBA) Binaries**
     * *Skills:* Defeating Control Flow Flattening (CFF), Bogus Control Flow (BCF), and simplifying opaque predicates like $(x \oplus y) + 2 \cdot (x \land y) \equiv x + y$ using **Z3 Theorem Prover** and **Triton / Miasm** symbolic execution.
103. **QEMU/KVM Virtual Machine Memory Introspection (Linux Host $\rightarrow$ Windows Guest)**
     * *Skills:* Reading and analyzing a Windows game's physical/virtual memory pages directly from the Linux host OS (`memflow` / `Win32-VMI`) by walking the x64 **CR3 Page Table Hierarchy** (`PML4` $\rightarrow$ `PDPT` $\rightarrow$ `PD` $\rightarrow$ `PT` $\rightarrow$ Physical Address) with zero footprint inside the guest OS.
104. **Writing a Custom Windows Kernel Driver (`Ring-0`) for Educational Memory Inspection**
     * *Skills:* Windows Driver Kit (WDK), `IoCreateDevice`, `IRP_MJ_DEVICE_CONTROL` (IOCTL), `MmCopyVirtualMemory`, `KeStackAttachProcess`, and testing in a VMware/QEMU test-signing environment.
105. **Custom Tiny Hypervisor (Intel VT-x / AMD-V EPT Hooking Lab)**
     * *Skills:* Extended Page Tables (EPT) shadow page splitting—marking a code page as Execute-Only so reads return original bytes while execution runs your hook (Stealth Inline Hooking).

---

### 💀 Tier `SSS+` : Full Matching Decompilation & 64-bit Space Engines
*Reconstructing an entire commercial game engine back into compilable C/C++ source code that produces a byte-for-byte identical binary.*

106. **Matching Decompilation Projects (e.g., `decomp.me`, Zelda: Ocarina of Time, Super Mario 64, Diablo 1 `DevilutionX`)**
     * *Skills:* Taking raw assembly functions, writing clean C/C++ code, and tuning compiler flags until the compiled output matches $100\%$ of the original binary's bytes and register allocations.
107. **OpenMW (Morrowind) / OpenRCT2 (RollerCoaster Tycoon 2) Engine Reimplementation**
     * *Skills:* Complete reverse engineering of proprietary file formats (`.NIF`, `.ESM`, `.DAT`), physics engines, audio pipelines, and AI state machines from scratch.
108. **Star Citizen (Offline Arena Commander / Singleplayer Sandbox Client)**
     * *Engine:* StarEngine (Heavily Modified CryEngine x64).
     * *Skills:* **64-bit Double-Precision (`double`) World Coordinates** spanning millions of kilometers, nested Local Physics Grids (a player walking inside a ship moving inside a rotating planet's orbit), and serialized entity component snapshots.
109. **Red Dead Redemption 2 (Strictly Offline Story Mode)**
     * *Engine:* RAGE Engine (x64 DirectX 12 / Vulkan + Heavy Arxan Checksum Guards).
     * *Skills:* Navigating self-healing code checksums (Arxan integrity checks), massive thread-local fiber pools, and inverse kinematics (IK) animation trees.
110. **Ghidra / Binary Ninja Custom Architecture & Sleigh Processor Module Development**
     * *Skills:* Writing a custom processor specification in Ghidra's **SLEIGH** language to disassemble an undocumented proprietary game script bytecode or retro CPU.

---

### 👑🌌 Tier `SSS++` : God of Reverse Engineering (Silicon, Crypto & Binary Lifters)
*The absolute apex of reverse engineering: hardware-software co-design, custom dynamic binary translators, and automated LLVM IR lifters.*

111. **Arcade Hardware Security & Dongle Emulation (Sega Lindbergh, Taito Type X, Namco System 357)**
     * *Skills:* Reversing hardware USB security dongles (HASP/Sentinel), custom I/O JVS boards, and TPM/EEPROM cryptographic handshakes.
112. **Building an Automated Binary Lifter (x86_64 / VM Bytecode $\rightarrow$ LLVM IR)**
     * *Skills:* Using **Remill** or **LLVM** to lift heavily obfuscated or virtualized game functions into LLVM Intermediate Representation (IR), running compiler optimization passes (`opt -O3`) to strip dead code, and recompiling back to a clean native `.dll`.
113. **Writing a Dynamic Binary Translator / Console Emulator JIT from Scratch**
     * *Skills:* Translating guest CPU instructions (e.g., ARM64 or MIPS) into optimized host `x86_64` machine code blocks at runtime with register caching and fast memory page tables.
114. **GPU Shader Reverse Engineering & Custom Graphics Wrapper (`d3d11.dll` / `dxgi.dll` Proxy)**
     * *Skills:* Intercepting compiled HLSL DXBC/DXIL or SPIR-V shader bytecode at runtime, decompiling shaders to extract depth/projection constant buffers (`cbuffer`), and injecting custom post-processing compute shaders.
115. **Silicon/Firmware Glitching & Console BootROM Reverse Engineering (Offline Hardware Lab)**
     * *Skills:* Dumping firmware via SPI/UART/JTAG, analyzing encrypted bootloaders in Ghidra, and understanding hardware Chain of Trust.

---

## 🧰 Complete Reverse Engineering Toolbox

| Category | Primary Tools | Purpose |
| :--- | :--- | :--- |
| **Memory Scanners** | **Cheat Engine 7.5+**, CrySearch, PINCE (Linux) | Dynamic memory scanning, pointer maps, Auto Assembler |
| **Dynamic Debuggers** | **x64dbg / x32dbg**, WinDbg Preview, GDB | Step-by-step execution, hardware/memory breakpoints, tracing |
| **Static Disassemblers** | **Ghidra**, **IDA Pro / Free**, **Binary Ninja** | Decompilation to C pseudocode, CFG analysis, XREFs, RTTI |
| **Class Reconstruction** | **ReClass.NET** | Live C++ structure and VMT reconstruction in memory |
| **.NET & Unity Tools** | **dnSpyEx**, **ILSpy**, **Il2CppDumper**, **BepInEx** | C# decompilation, IL patching, IL2CPP metadata recovery |
| **Unreal Engine Tools** | **Dumper-7**, **UESDK**, **FModel** | Automated SDK generation (`GObjects`, `GNames`, `GWorld`) |
| **PE & Process Analysis** | **System Informer**, **PE-bear**, **Detect It Easy (DIE)** | Inspecting PE headers, sections, threads, handles, and packers |
| **AI & Automation** | **REA (`rea-agents` MCP)**, **Z3 Prover**, **Frida** | LLM-assisted binary triage, symbolic execution, dynamic hooks |
| **Development Stack** | **Visual Studio 2022 (MSVC)**, **MinHook**, **Dear ImGui** | Writing C++20 internal DLLs, trampoline hooks, and DX11/12 UIs |

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.
