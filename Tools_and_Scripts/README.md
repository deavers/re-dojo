# 🧰 Tools, Templates & Scripts (`Tools_and_Scripts/`)

This directory contains reusable **C++20 Memory Frameworks**, **3D Math Libraries**, **Internal DLL Skeletons**, and **Python Binary Analysis Utilities** built to solve the challenges in [`Course_Solutions/`](../Course_Solutions/) and [`Crackmes_and_CTF/`](../Crackmes_and_CTF/), as well as real-world offline games.

---

## 📂 Toolkit Index

| Directory / File | Language | Target Stage / Tier | Purpose |
| :--- | :---: | :---: | :--- |
| [`01_External_Trainer_Template/external_memory_trainer.cpp`](./01_External_Trainer_Template/external_memory_trainer.cpp) | C++20 (Win32) | Stage 3 (`Tier E`–`C`) | Complete external memory wrapper (`OpenProcess`, `RPM`/`WPM`, `GetModuleBaseAddress`, `ResolvePointerChain`) |
| [`02_3D_Math_and_W2S_Lib/w2s_math_lab.hpp`](./02_3D_Math_and_W2S_Lib/w2s_math_lab.hpp) | C++20 Header | Stage 6 (`Tier E`–`A`) | `Vec3` algebra, Pitch/Yaw `CalcEulerAngles`, and $4\times 4$ `WorldToScreen` (DirectX & OpenGL/Unity layouts) |
| [`03_Internal_DLL_Skeleton/dllmain_internal_hook.cpp`](./03_Internal_DLL_Skeleton/dllmain_internal_hook.cpp) | C++20 DLL | Stage 4 (`Tier B`–`A+`) | Internal `DllMain` template with debug console, direct RVA function invocation, and VMT pointer swapping |
| [`04_Python_RE_Toolkit/pe_and_aob_scanner.py`](./04_Python_RE_Toolkit/pe_and_aob_scanner.py) | Python 3 | All Tiers (`F-`–`SSS`) | Zero-dependency PE32/PE64 section analyzer, Shannon Entropy ($H$) packer detector, & Wildcard AOB Scanner |
| [`04_Python_RE_Toolkit/crackme_solvers_and_z3_lab.py`](./04_Python_RE_Toolkit/crackme_solvers_and_z3_lab.py) | Python 3 | `Tier C`–`SSS-` | Stack VM Bytecode Disassembler (`Crackme 06`), Binary Struct Forger (`Crackme 04`), & Z3 Solver (`Crackme 08`) |
| [`rpg_manager.py`](./rpg_manager.py) | Python 3 | All Tiers | Synchronizes the ASCII RPG Character Card in `README.md`, `data/player_progress.json`, and 5-Axis Rubric verification |
| [`auto_artifact_grader.py`](./auto_artifact_grader.py) | Python 3 | All Tiers | Automated 5-Axis heuristic difficulty & RPG Tier grader for `.CT` Cheat Tables, trainers, DLL hooks, and scripts |
| [`opsec_sanitizer.py`](./opsec_sanitizer.py) | Python 3 | Security / OPSEC | Audits workspace files, compiled PE/PDB binaries, and Git commit history for leaked local paths, usernames, or emails |
| [`build_web_app.py`](./build_web_app.py) | Python 3 | Web RPG | Generates the standalone, offline-ready `docs/index.html` Interactive RPG Academy & Cheat Sheet |

---

## 🚀 Quick Usage Examples

### 1. Scanning a Binary for AOB Signatures & Entropy (`pe_and_aob_scanner.py`)
```powershell
python Tools_and_Scripts/04_Python_RE_Toolkit/pe_and_aob_scanner.py build/bin/lab06_shared_code.exe "48 8B ?? 8B ?? 08"
```

### 2. Running the Stack VM Disassembler & Z3 Workbench
```powershell
python Tools_and_Scripts/04_Python_RE_Toolkit/crackme_solvers_and_z3_lab.py
```
