// ============================================================================
// [Lab 09] Internal DLL Injection & Direct Function Calling (Tier B+ | 5.8/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 08. External trainers use ReadProcessMemory/WriteProcessMemory,
//   which have syscall overhead. When you inject an INTERNAL DLL into the game's
//   own address space, you can:
//     1. Call internal engine functions directly using C++ function pointers!
//     2. Place inline Trampoline Hooks (MinHook) on verification functions!
//
// QUEST OBJECTIVE:
//   1. Inject a DLL (see `Tools_and_Scripts/03_Internal_DLL_Skeleton`) OR use
//      Cheat Engine's `CreateThread` / Auto Assembler to call the internal
//      `Engine_SpawnMythicChest(0x1337BEEF)` function directly!
//   2. Or hook `Engine_VerifySecurityToken()` so it returns `true`!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#ifdef _WIN32
#include <windows.h>
#endif

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#define EXPORT_SYM extern "C" __declspec(dllexport)
#else
#define NOINLINE __attribute__((noinline))
#define EXPORT_SYM extern "C" __attribute__((visibility("default")))
#endif

bool    g_VaultUnlocked = false;
int32_t g_MythicRelics  = 0;

// Exported / signatured internal engine functions
EXPORT_SYM NOINLINE bool Engine_VerifySecurityToken(uint32_t token) {
    // By default, no user-entered token passes unless hooked or called with 0xCAFEBABE
    return (token == 0xCAFEBABE);
}

EXPORT_SYM NOINLINE void Engine_SpawnMythicChest(uint32_t magicKey) {
    if (magicKey == 0x1337BEEF || Engine_VerifySecurityToken(magicKey)) {
        g_VaultUnlocked = true;
        g_MythicRelics += 100;
        std::cout << "\n>> [INTERNAL CALL DETECTED] Engine_SpawnMythicChest() executed inside process!\n";
    } else {
        std::cout << "\n>> [INTERNAL CALL] Invalid magicKey passed to Engine_SpawnMythicChest()!\n";
    }
}

int main() {
#ifdef _WIN32
    DWORD pid = GetCurrentProcessId();
#else
    int pid = 0;
#endif
    uintptr_t baseAddr = 0;
#ifdef _WIN32
    baseAddr = reinterpret_cast<uintptr_t>(GetModuleHandleA(nullptr));
#endif

    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Function RVAs & Pointers)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    bool blind = (mode == 2);

    while (!g_VaultUnlocked) {
        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 09 | TIER B+] THE INTERNAL CITADEL (DLL Injection & Hooks)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Process ID (PID)   : " << pid << "\n";
        std::cout << "  Mythic Relics      : " << g_MythicRelics << "\n";
        std::cout << "  Citadel Vault      : " << (g_VaultUnlocked ? "UNLOCKED" : "SEALED") << "\n";

        if (!blind) {
            uintptr_t fnSpawn  = reinterpret_cast<uintptr_t>(&Engine_SpawnMythicChest);
            uintptr_t fnVerify = reinterpret_cast<uintptr_t>(&Engine_VerifySecurityToken);
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  Module Base Address           : 0x" << std::hex << std::uppercase << baseAddr << "\n";
            std::cout << "  Engine_SpawnMythicChest Addr  : 0x" << fnSpawn
                      << " (RVA: +0x" << (fnSpawn - baseAddr) << ")\n";
            std::cout << "  Engine_VerifySecurityToken    : 0x" << fnVerify
                      << " (RVA: +0x" << (fnVerify - baseAddr) << ")\n" << std::dec;
            std::cout << "  [Tip] Inject a DLL that calls Engine_SpawnMythicChest(0x1337BEEF)!\n";
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Try Opening Citadel Door (Calls Engine_VerifySecurityToken(0))\n";
        std::cout << "  [2] Refresh Status (Check if Injected DLL called SpawnMythicChest)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            if (Engine_VerifySecurityToken(0)) {
                Engine_SpawnMythicChest(0xCAFEBABE);
            } else {
                std::cout << ">> [SEALED] Engine_VerifySecurityToken(0) returned FALSE!\n";
                std::cout << "   Hook Engine_VerifySecurityToken to return 1, or call Engine_SpawnMythicChest(0x1337BEEF)!\n";
            }
        }
    }

    if (g_VaultUnlocked) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [QUEST COMPLETE - TIER B+ CLEARED!]\n";
        std::cout << "  You executed internal engine functions from inside the process!\n";
        std::cout << "  Next Step: Proceed to Lab 10 (Final Boss: Integrity & XOR Guard).\n";
        std::cout << "********************************************************************\n";
    }
    return 0;
}
