# 🎮 Game Hacking — Cheat Engine Tables & Memory Research

Personal collection of `.CT` Cheat Engine tables, Auto Assembler (`.CEA`) code injections, pointer chains, and Lua memory scripts for **strictly offline, single-player games**.  
All scripts use AOB signature injection or Lua automation — tested with **Cheat Engine 7.5+**.

---

## 📋 Completed Milestones & Table Index

| Tier | Difficulty | Game Title | Target Binary | Architecture / Engine | Cheat Table |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **F- to D** | `1.0–3.2` | **In-Repo C++20 Dojo Labs (01, 04, 05, 06)** | `lab01`–`lab06.exe` | x64 — Custom C++20 Dojo | [`Dojo_Labs_Reference.CT`](./Dojo_Labs_Reference.CT) |
| **E+** | `2.1 / 10` | [Plants vs. Zombies GOTY](#1-plants-vs-zombies-goty-tier-e--21--10) | `PlantsVsZombies.exe` | x86 — PopCap Framework | [`PvZ.CT`](./PvZ.CT) |
| **D** | `2.9 / 10` | [Unreal Tournament GOTY (1999)](#2-unreal-tournament-goty-1999-tier-d--29--10) | `UnrealTournament.exe` | x86 — Unreal Engine 1 | [`UnrealTournament_UT99.CT`](./UnrealTournament_UT99.CT) |
| **C-** | `3.8 / 10` | [The Binding of Isaac: Repentance](#3-the-binding-of-isaac-repentance-tier-c---38--10) | `isaac-ng.exe` | x86 — Custom C++20 + Lua | [`isaac-ng.CT`](./isaac-ng.CT) |
| **C** | `4.1 / 10` | [Streets of Rogue (v98)](#4-streets-of-rogue-v98-tier-c--41--10) | `StreetsOfRogue.exe` | x64 — Unity Engine (Mono) | [`StreetsOfRogue_v98.CT`](./StreetsOfRogue_v98.CT) |

---

## 1. Plants vs. Zombies GOTY (`Tier E+` | `2.1 / 10`)

| Feature | Technique | Technical Notes |
| :--- | :--- | :--- |
| **Infinite Sun** | AOB Injection | Hooks sun update instruction and forces sun counter (`+0x5560`) to `999` |
| **Instant Recharge** | AOB Injection | Bypasses seed packet cooldown timer comparison |
| **Immortal Plants** | AOB Injection | Nullifies zombie bite decrement on plant HP struct |
| **One-Hit Kill** | AOB Injection | Instakills Normal and Conehead/Buckethead armor states |
| **Infinite Coins** | AOB Injection | Sets Crazy Dave's shop coin balance to `999,990` |
| **Speed Controller** | Lua Script | Custom UI dropdown controller for `speedhack_setSpeed()` |

* **File:** [`PvZ.CT`](./PvZ.CT)  
* **Engine:** 32-bit (`x86`), PopCap Framework (`popcapgame1.exe` / `PlantsVsZombies.exe`)
* **Skills Applied:** Multi-level pointer chains (`LawnApp -> Board -> Sun`), AOB code injection, Lua GUI scripting.

---

## 2. Unreal Tournament GOTY 1999 (`Tier D` | `2.9 / 10`)

| Feature | Technique | Technical Notes |
| :--- | :--- | :--- |
| **Infinite HP (God Mode)** | AOB Injection | Nullifies incoming damage on player `APawn` |
| **Infinite Ammo** | Lua Freeze | Dynamically freezes all child weapon ammo entries to `999` |
| **Smart One-Shot Kill** | AOB Injection | Shared-code filter — skips timers/coordinates and instakills non-player pawns |
| **Player Base Chain** | Pointer Chain | Rooted at `Engine.dll+002EAC38` (`UObject` / `APawn` hierarchy) |

* **File:** [`UnrealTournament_UT99.CT`](./UnrealTournament_UT99.CT)  
* **Engine:** 32-bit (`x86`), Unreal Engine 1 (`Engine.dll` / `Core.dll` / `Render.dll`)
* **Skills Applied:** Shared instruction filtering (`Player` vs `Bot` disambiguation), UE1 `APawn` offsets.

---

## 3. The Binding of Isaac: Repentance (`Tier C-` | `3.8 / 10`)

| Feature | Technique | Technical Notes |
| :--- | :--- | :--- |
| **Infinite Resources** | AOB Injection | Locks Coins, Bombs, and Keys at `99` |
| **Infinite Health** | AOB Injection | Locks Red Hearts and Soul/Black Armor Hearts to maximum |
| **Infinite Active Charge** | AOB Injection | Active item bypasses room-charge depletion cycle |
| **Stats AOB Lock** | AOB Injection | Overrides room-transition cache resets for `Damage`, `Speed`, and `Tears` |
| **Player Structure** | Structure Dissect | Mapped `Entity_Player` float and bitmask offsets |

* **File:** [`isaac-ng.CT`](./isaac-ng.CT)  
* **Engine:** 32-bit (`x86`), Custom C++20 Engine (`isaac-ng.exe`)
* **Skills Applied:** Bitmask heart containers, stat recalculation hook bypass, structure dissection.

---

## 4. Streets of Rogue v98 (`Tier C` | `4.1 / 10`)

| Feature | Technique | Technical Notes |
| :--- | :--- | :--- |
| **Infinite HP** | Lua Freeze | Freezes all child HP entries to `999` |
| **Infinite Money** | AOB Injection | Hooks currency update inside `UnityPlayer.dll` / JIT code |
| **Infinite Ammo** | AOB Injection | Prevents weapon durability/ammo decrement |
| **999,999 EXP** | AOB Injection | Triggers massive XP reward on any EXP gain event |
| **99 Item Stack Override** | AOB Injection | Overrides inventory item stack count |

* **File:** [`StreetsOfRogue_v98.CT`](./StreetsOfRogue_v98.CT)  
* **Engine:** 64-bit (`x64`), Unity Engine Mono (`StreetsOfRogue.exe` / `UnityPlayer.dll`)
* **Skills Applied:** Cheat Engine Mono Dissector (`Agent`, `InvDatabase`, `Stat` classes), x64 JIT AOB hooks.

---

## ⚙️ Requirements, Usage & Automated Tier Grading

1. Install [Cheat Engine 7.5+](https://www.cheatengine.org/).
2. Launch the target offline game (or compile our in-repo C++ Dojo Labs with `..\build_all.bat`), then open the corresponding `.CT` file in Cheat Engine.
3. Attach Cheat Engine to the target process and toggle the desired scripts (`[X]`).
4. **Automated `.CT` Difficulty & Tier Grader:** You can automatically evaluate the RPG Tier (`F-` to `SSS++`) and 5-Axis Difficulty score (`0.5`–`10.0`) of any `.CT` file by running:
   ```powershell
   python ../Tools_and_Scripts/auto_artifact_grader.py Game_Hacking
   ```
   Or upload your `.CT` file directly in the **🔬 Auto-Grade Script / .CT / Trainer** tab inside [`docs/index.html`](../docs/index.html)!
