# 🛡️ Security, Legal Safe-Harbor & Reverse Engineer's OPSEC Policy

## 1. Educational Scope & Strict Non-Interference Policy

This repository (**RE:DOJO — Reverse Engineering, Binary Auditing & Offline Game Hacking RPG**) is an open-source computer science curriculum dedicated to **x86/x64 Assembly, Operating Systems Internals, Binary Auditing, Compiler Design, and Dynamic Memory Analysis**.

To protect both the repository maintainers and the broader community, the following boundaries are **strictly enforced**:

* **100% Offline, Single-Player & Self-Written Targets Only:** All research notes, Cheat Engine tables (`.CT`), scripts, and writeups apply exclusively to **self-written C++20 practice binaries (`Course_Solutions/`, `Crackmes_and_CTF/`)** or **strictly local, offline, single-player software and games**.
* **Zero Multiplayer or Live-Service Involvement:** This repository contains **zero** code, offsets, or documentation targeting online multiplayer games, competitive matchmaking, server-authoritative logic, or live-service economies.
* **Zero Anti-Cheat Circumvention:** We do **not** research, host, or accept pull requests involving commercial anti-cheat bypasses (EasyAntiCheat, BattlEye, Vanguard, Ricochet, VAC, etc.) or unauthorized kernel driver exploitation (`BYOVD`).
* **Zero Piracy or DRM Circumvention:** No copyrighted game executables (`.exe`), proprietary shared libraries (`.dll`, `steam_api64.dll`), game archives (`.pak`, `.assets`), license keys, or DRM/SteamStub cracks are hosted or permitted in this repository.

---

## 2. Legal Safe-Harbor & Interoperability Notice

All original C++20 source code, Python scripts, and documentation in this repository are licensed under the [MIT License](./LICENSE).

Any symbolic memory offsets, structure definitions, or Auto Assembler injection scripts (`.CT`) referencing third-party offline software are published strictly for **educational computer science research, debugging, and interoperability analysis** under applicable statutory exemptions:
* **17 U.S.C. § 1201(f) (DMCA Reverse Engineering & Interoperability Exemption)** and **17 U.S.C. § 107 (Fair Use for Scholarship & Technical Education)**.
* **Directive 2009/24/EC of the European Parliament (Articles 5(3) & 6)** permitting observation, study, and decompilation of software behavior for interoperability and educational analysis.

No proprietary or copyrighted binary code is reproduced or distributed. If you are a rights holder and have a concern regarding any specific entry, please open an issue so it can be reviewed and addressed promptly.

---

## 3. Reverse Engineer's Personal OPSEC & Account Safety Guide

When practicing reverse engineering locally and publishing your progress to GitHub, follow these **5 Golden OPSEC Rules** to protect your personal identity and gaming accounts:

### Rule 1: Anonymize Git Commit Metadata (`noreply` Email)
Git embeds your local `user.name` and `user.email` inside every commit object permanently. Never commit with your personal email (`@gmail.com`, etc.) or real legal name.
```powershell
git config --local user.name "deavers"
git config --local user.email "106682353+deavers@users.noreply.github.com"
```
Also enable **"Keep my email addresses private"** and **"Block command line pushes that expose my email"** in your GitHub Settings (`Settings -> Emails`).

### Rule 2: Strip Local OS Paths (`C:\Users\<username>`) from Compiled Binaries
By default, Microsoft Visual C++ (`cl.exe` / `link.exe`) embeds the full absolute path to your `.pdb` file (`C:\Users\YourRealName\...\binary.pdb`) inside the PE executable's `IMAGE_DEBUG_DIRECTORY` (`RSDS` CodeView record) and embeds the exact compilation timestamp in the PE header.
* Both [`CMakeLists.txt`](./CMakeLists.txt) and [`build_all.bat`](./build_all.bat) in this repository are hardened with:
  * `/Brepro` — zeroes out real timestamps in PE headers for deterministic builds.
  * `/PDBALTPATH:%_PDB%` — strips `C:\Users\<username>\...` and writes only the bare filename (`target.pdb`).
  * `/INCREMENTAL:NO` — disables `.ilk` files that leak local environment paths.
  * `-ffile-prefix-map` / `-fdebug-prefix-map` — strips local paths on GCC/Clang/MinGW.

### Rule 3: Never Commit Process Dumps (`.dmp`) or Disassembler Databases (`.i64` / `.idb`)
* **Process Memory Dumps (`*.dmp`, `*.mdmp`)** capture the target process's entire environment block (`PEB -> ProcessParameters -> Environment`), which contains `USERNAME=...`, `USERPROFILE=C:\Users\...`, `COMPUTERNAME=...`, and—if dumped from a Steam game—your **active Steam session ticket and SteamID64**!
* **IDA / Ghidra / x64dbg Databases (`*.i64`, `*.idb`, `*.dd64`)** store the full local file path of the analyzed binary in their header metadata.
* All of these extensions are blocked automatically by [`.gitignore`](./.gitignore) and scanned by [`Tools_and_Scripts/opsec_sanitizer.py`](./Tools_and_Scripts/opsec_sanitizer.py).

### Rule 4: Protect Your Steam / Gaming Accounts from Accidental Anti-Cheat Flags
Even when you only reverse engineer **offline single-player games**, modern anti-cheats (VAC, EAC, BattlEye, Vanguard) used by *other* games on your PC scan for active debugger processes, open handles, and loaded kernel drivers:
1. **Launch Offline Games with Anti-Cheat Disabled:** For Valve Source / GoldSrc games (*Half-Life*, *Portal*, *Left 4 Dead 2*, *CS 1.6* offline bots), always add `-insecure -novid +sv_lan 1` to the launch options before attaching Cheat Engine or x64dbg.
2. **Avoid Loading Kernel Drivers (`dbk64.sys`) Unnecessarily:** Standard user-mode Win32 APIs (`OpenProcess` / `ReadProcessMemory` / `VirtualAllocEx`) are sufficient for 99% of offline games. Do not load Cheat Engine's DBVM / `dbk64.sys` kernel driver on the same Windows boot session where you play online games.
3. **Close All RE Tools & Reboot Before Playing Online Multiplayer:** Never leave Cheat Engine, x64dbg, Process Hacker / System Informer, ReClass.NET, or API Monitor running in the background (or minimized to tray) when launching any online multiplayer game.
4. **Use a Dedicated VM or Windows Sandbox for Unfamiliar Crackmes:** Always analyze third-party CTF crackmes inside an isolated VM (VMware / VirtualBox / QEMU) or Windows Sandbox with network access disabled.

### Rule 5: Run the Automated OPSEC Sanitizer Before Pushing
Before pushing any new commits, run the repository's built-in OPSEC auditor:
```powershell
python Tools_and_Scripts/opsec_sanitizer.py
```
It verifies that zero personal file paths, emails, usernames, or binary metadata leaks exist in the workspace or Git commit history.
