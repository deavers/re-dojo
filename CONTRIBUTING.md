# 🤝 Contributing & Community RPG Guide

Welcome to the **Reverse Engineering, Binary Auditing & Offline Game Hacking RPG**!  
This repository is built as an open-source, self-paced learning academy for everyone. Whether you want to track your own progression from **Tier `F-` (Novice)** to **Tier `SSS++` (Demigod of Silicon)**, add new offline games/software targets, or submit your own `.CT` tables and crackme writeups to the **Verified Hall of Fame**, here is everything you need to know.

---

## 🎮 1. How to Play & Track Your Own Progress

You have two ways to track your personal RPG progression:

### Option A: In Your Browser (`docs/index.html` / GitHub Pages)
1. Open [`docs/index.html`](./docs/index.html) in any browser (or visit the GitHub Pages deployment).
2. Enter your **Adventurer Handle** at the top and check off quests or games from the **Top 200 Popular Games (`#001`–`#200`)** tab.
3. **100% Private Local Save:** Your progress is stored automatically in your browser's `localStorage` (`re_rpg_journey_state_v2`). Nobody else's progress overrides yours.
4. **Sync to `README.md`:** Click **`💾 Export player_progress.json`** in the **Save & Sync** tab, save it to `data/player_progress.json`, and run:
   ```powershell
   python Tools_and_Scripts/rpg_manager.py --from-json
   ```

### Option B: Directly in `README.md` (Fork / Local Clone)
1. Fork or clone this repository.
2. As you solve quests in `README.md`, change `- [ ]` to `- [x]`.
3. Run the one-click progress updater:
   ```powershell
   .\update_progress.bat --name "YourHandle"
   ```
   This recalculates your **Total EXP**, checks the **Breakthrough Level-Up Rule** (`3 TP` per Tier: `1` same-tier quest = `+1 TP`; `1` higher-tier quest = `+3 TP`), updates the ASCII Character Card at the top of `README.md`, and saves a snapshot to `data/player_progress.json`.

---

## 🔬 2. How to Automatically Grade Your `.CT` Tables, Trainers & Scripts

Wondering what **RPG Tier (`F-` to `SSS++`)** and **Difficulty (`0.5` – `10.0`)** your Cheat Engine table (`.CT`), C++/C# trainer/DLL, or Python solver qualifies for?

Run the **Automated Artifact Tier Grader** on your file:
```powershell
# Grade a single file:
python Tools_and_Scripts/auto_artifact_grader.py path/to/your_table.CT

# Or via rpg_manager.py:
python Tools_and_Scripts/rpg_manager.py --analyze path/to/your_script.py
```
Or upload your file directly inside the **🔬 Auto-Grade Script / .CT / Trainer** tab in [`docs/index.html`](./docs/index.html).

The analyzer inspects 5 objective technical axes:
1. **Axis 1 — Architecture & Runtime Target (`0.2 – 2.0`):** x86 vs x64, multi-module C++, Unity Mono/IL2CPP, Unreal `GWorld`/`GNames`, cross-ISA emulators (`PowerPC`/`ARM64`), LLVM IR.
2. **Axis 2 — Memory Indirection & Struct Depth (`0.1 – 2.0`):** Pointer chain depth (`<Offsets>`), C++ class member displacements, VMTs, 4x4 matrices, or `CR3` page tables.
3. **Axis 3 — Code, Hook & Math Complexity (`0.1 – 2.0`):** Number of `aobscanmodule` / `alloc(newmem)` hooks, shared-code entity filters (`cmp` + conditional branches separating Player vs Enemy), 64-bit RIP-relative near allocations, `{$lua}` automation, `MinHook`/VMT detours, or `Z3`/`angr` symbolic execution.
4. **Axis 4 — Protection & Obfuscation (`0.0 – 2.5`):** Bitwise `ROL`/`ROR`/`XOR`, raw JIT heap scanning, anti-debugging (`PEB`/`RDTSC`), packers (`UPX`/`ChaCha20`), custom bytecode VMs, MBA, or `VMProtect`/`Arxan`.
5. **Axis 5 — Privilege & Execution Boundary (`0.0 – 1.5`):** External Ring-3 vs In-Process Injected DLL (`DllMain`) vs Ring-0 Kernel Driver / KVM VMI.

---

## 🏅 3. Submitting a Pull Request to the Verified Hall of Fame

To join the **Global Verified Hall of Fame** in `README.md` and [`data/leaderboard.json`](./data/leaderboard.json):
1. **Strictly Offline & Educational:** Ensure your target is a local, single-player, offline game, emulator, open-source application, or crackme. **Zero multiplayer cheats, online services, or piracy/DRM cracks are permitted.**
2. **Include a Verifiable Proof Artifact:** Add your `.CT` table to `Game_Hacking/`, your tool/script to `Tools_and_Scripts/`, or your crackme writeup to `Crackmes_and_CTF/`.
3. **Run the Auto-Grader:** Verify your artifact's tier using `python Tools_and_Scripts/auto_artifact_grader.py <your_file>`.
4. **Add Your Entry:** Add your handle, verified tier, and artifact path to [`data/leaderboard.json`](./data/leaderboard.json) and open a Pull Request!
