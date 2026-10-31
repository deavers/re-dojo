// ============================================================================
// [Crackme 05] Anti-Debug Sentinel & FNV-1a Key Check (Tier B | Diff: 5.5/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 04. Commercial binaries and crackmes actively fight back
//   against debuggers! This target implements 3 classic anti-debug checks:
//     1. Win32 `IsDebuggerPresent()` API check (reads `PEB->BeingDebugged`).
//     2. `CheckRemoteDebuggerPresent()` API check.
//     3. Software Breakpoint (`0xCC` / `INT3`) prolog scanner on `VerifyKey()`.
//
//   Learn how to bypass these using ScyllaHide, patching `PEB->BeingDebugged`,
//   or using Hardware Breakpoints (`DR0`-`DR3`) instead of `0xCC`!
// ============================================================================

#include <iostream>
#include <string>
#include <cstdint>
#ifdef _WIN32
#include <windows.h>
#endif

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

NOINLINE bool VerifyKeyFNV1a(const std::string& key) {
    // Computes 32-bit FNV-1a hash of the input string
    // Target phrase: "SHADOW_DEBUGGER_SLAYER" -> FNV-1a = 0x7A4B0C29
    uint32_t hash = 2166136261U;
    for (unsigned char c : key) {
        hash ^= c;
        hash *= 16777619U;
    }
    return (hash == 0x7A4B0C29U) && (key.size() == 22) && (key[0] == 'S') && (key[6] == '_');
}

NOINLINE bool DetectDebuggerTrap() {
#ifdef _WIN32
    if (IsDebuggerPresent()) {
        std::cout << ">> [ANTI-DEBUG #1] IsDebuggerPresent() detected a debugger (PEB->BeingDebugged == 1)!\n";
        return true;
    }
    BOOL remoteDbg = FALSE;
    CheckRemoteDebuggerPresent(GetCurrentProcess(), &remoteDbg);
    if (remoteDbg) {
        std::cout << ">> [ANTI-DEBUG #2] CheckRemoteDebuggerPresent() triggered!\n";
        return true;
    }
#endif
    // Anti-Debug #3: Scan the first 24 bytes of VerifyKeyFNV1a for 0xCC (INT3 software breakpoint)
    const uint8_t* fnBytes = reinterpret_cast<const uint8_t*>(&VerifyKeyFNV1a);
    for (int i = 0; i < 24; ++i) {
        if (fnBytes[i] == 0xCC) {
            std::cout << ">> [ANTI-DEBUG #3] Software Breakpoint (0xCC / INT3) detected inside VerifyKeyFNV1a()!\n";
            std::cout << "   Tip: Use Hardware Breakpoints (DR0-DR3) instead of F2 Software Breakpoints!\n";
            return true;
        }
    }
    return false;
}

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 05 | TIER B] THE ANTI-DEBUG SENTINEL (PEB & INT3 Scan)\n";
    std::cout << "====================================================================\n";

    if (DetectDebuggerTrap()) {
        std::cout << ">> [TERMINATED] Bypass the Anti-Debug checks in x64dbg (or enable ScyllaHide)!\n";
        return 1;
    }

    std::cout << ">> [INTEGRITY OK] No active debugger traps tripped.\n";
    std::cout << "Enter Sentinel Master Key: ";
    std::string key;
    std::cin >> key;

    if (DetectDebuggerTrap()) {
        return 1;
    }

    if (VerifyKeyFNV1a(key)) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 05 SOLVED - TIER B CLEARED!]\n";
        std::cout << "  You bypassed the Anti-Debug Sentinel! Key: " << key << "\n";
        std::cout << "  Next Challenge: Crackme 06 (Custom Bytecode Stack VM).\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [INVALID KEY] Sentinel rejected your input.\n";
        return 1;
    }
}
