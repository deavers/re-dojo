// ============================================================================
// [Lab 10] Final Boss: Code Integrity Guard & XOR Encryption (Tier A+ | 7.2/10)
// ============================================================================
// PURPOSE:
//   The culmination of Course Solutions Labs 01-09!
//   Modern AAA engines and anti-tamper systems (like Arxan in RDR2/GTAV) protect
//   their functions with:
//     1. Code Section Integrity Hashing: Hashing the machine code bytes of
//        critical functions to detect `0x90` (NOP), `0xE9` (JMP hook), or
//        `0xCC` (Software Breakpoint INT3)!
//     2. XOR-Obfuscated Memory: Storing sensitive stats (`HP`, `Gold`) XORed
//        with a dynamic runtime key so plain Cheat Engine scans find nothing!
//     3. Debugger Detection: Checking `IsDebuggerPresent()`.
//
// HOW TO DEFEAT THE ARCHON OF SILICON (3 Valid Master Solutions):
//   - Solution A (VMT / Function Pointer Hook): Notice `g_CombatDispatcher`
//     calls `ProtectedCombatTick` through a writable pointer in `.data`!
//     Redirecting the pointer does NOT modify the `.text` bytes of the function!
//   - Solution B (XOR Memory Math): Read `g_XorCookie` and write
//     `(1000000 ^ g_XorCookie)` directly into `g_EncryptedHeroAttack`!
//   - Solution C (Neutralize the Guard): Patch or bypass `VerifyCodeIntegrity`!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#ifdef _WIN32
#include <windows.h>
#endif

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

uint32_t g_XorCookie           = 0x5A3C9E71U;
uint32_t g_EncryptedHeroHP     = 250U ^ 0x5A3C9E71U;
uint32_t g_EncryptedHeroAttack = 40U  ^ 0x5A3C9E71U;
int32_t  g_ArchonBossHP        = 1000000;
uint32_t g_BaselineChecksum    = 0;

int32_t GetHeroHP()     { return static_cast<int32_t>(g_EncryptedHeroHP ^ g_XorCookie); }
void    SetHeroHP(int32_t v) { g_EncryptedHeroHP = static_cast<uint32_t>(v) ^ g_XorCookie; }
int32_t GetHeroAttack() { return static_cast<int32_t>(g_EncryptedHeroAttack ^ g_XorCookie); }

// This function's machine code bytes are monitored by the CRC/FNV Integrity Guard!
NOINLINE void ProtectedCombatRound() {
    int32_t atk = GetHeroAttack();
    g_ArchonBossHP -= atk;
    if (g_ArchonBossHP > 0) {
        SetHeroHP(GetHeroHP() - 60);
    }
}

// Writable function pointer table (simulating a VMT / Callback in .data)
using fnCombatRound = void(*)();
fnCombatRound g_CombatDispatcher = &ProtectedCombatRound;

// Alternative function already inside the binary for VMT/Pointer redirection!
NOINLINE void DivineOverloadCombatRound() {
    g_ArchonBossHP = 0;
    std::cout << ">> [VMT REDIRECTION] DivineOverloadCombatRound() executed cleanly without touching .text!\n";
}

// Hashes the first 32 bytes of ProtectedCombatRound() to detect 0xCC, 0x90, 0xE9!
NOINLINE uint32_t ComputeFunctionHash() {
    const uint8_t* pBytes = reinterpret_cast<const uint8_t*>(&ProtectedCombatRound);
    uint32_t hash = 2166136261U;
    for (int i = 0; i < 32; ++i) {
        hash ^= pBytes[i];
        hash *= 16777619U;
    }
    return hash;
}

int main() {
    g_BaselineChecksum = ComputeFunctionHash();

    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows XOR Keys & Dispatcher Pointers)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    bool blind = (mode == 2);

    while (GetHeroHP() > 0 && g_ArchonBossHP > 0) {
        // 1. Check code integrity of ProtectedCombatRound
        uint32_t currentHash = ComputeFunctionHash();
        if (currentHash != g_BaselineChecksum) {
            std::cout << "\n[!!! INTEGRITY PANIC !!!] ProtectedCombatRound() machine code was modified!\n";
            std::cout << "Expected Hash: 0x" << std::hex << g_BaselineChecksum
                      << " | Actual: 0x" << currentHash << std::dec << "\n";
            std::cout << "Hint: Do NOT place software breakpoints (0xCC) or NOPs (0x90) inside ProtectedCombatRound!\n";
            std::cout << "      Use VMT/Pointer hooking (g_CombatDispatcher) or edit the XOR-encrypted variables!\n";
            return 1;
        }

        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 10 | TIER A+ BOSS] ARCHON OF SILICON (Integrity & XOR Guard)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Hero HP (XOR Encrypted)     : " << GetHeroHP() << "\n";
        std::cout << "  Hero Attack (XOR Encrypted) : " << GetHeroAttack() << "\n";
        std::cout << "  Archon Boss HP              : " << g_ArchonBossHP << " / 1,000,000\n";
        std::cout << "  .text Integrity Status      : VERIFIED (0x" << std::hex << currentHash << std::dec << ")\n";

        if (!blind) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  &g_XorCookie           : 0x" << std::hex << (uintptr_t)&g_XorCookie << " (Val: 0x" << g_XorCookie << ")\n";
            std::cout << "  &g_EncryptedHeroAttack : 0x" << (uintptr_t)&g_EncryptedHeroAttack << "\n";
            std::cout << "  &g_CombatDispatcher    : 0x" << (uintptr_t)&g_CombatDispatcher << " -> Points to 0x" << (uintptr_t)g_CombatDispatcher << "\n";
            std::cout << "  fn DivineOverloadRound : 0x" << (uintptr_t)&DivineOverloadCombatRound << " <-- Safe Hook Target!\n" << std::dec;
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Execute Combat Round (Calls g_CombatDispatcher())\n";
        std::cout << "  [2] Meditate (+25 HP)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            g_CombatDispatcher();
            std::cout << ">> Combat round completed!\n";
        } else if (choice == 2) {
            SetHeroHP(GetHeroHP() + 25);
        }
    }

    if (g_ArchonBossHP <= 0) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [GRAND COMPLETE - ALL 10 COURSE LABS CLEARED!]\n";
        std::cout << "  You defeated the Archon of Silicon without tripping .text CRC!\n";
        std::cout << "  You are ready for AAA Engines, Crackmes_and_CTF, and Tier A-SSS!\n";
        std::cout << "********************************************************************\n";
    } else {
        std::cout << "\n[DEFEATED] The Archon overwhelmed your defenses.\n";
    }
    return 0;
}
