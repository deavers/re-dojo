// ============================================================================
// [Tool 03] Internal DLL Skeleton & Function Pointer Invoker (C++20)
// ============================================================================
// PURPOSE:
//   A clean Stage 4 Internal DLL template (`DllMain` + worker thread) that can
//   be injected into `lab09_internal_hook_target.exe` (or any offline game).
//   Demonstrates:
//     1. Safe worker thread creation on `DLL_PROCESS_ATTACH`
//     2. Resolving an internal engine function via `GetProcAddress` or RVA offset
//     3. Calling `Engine_SpawnMythicChest(0x1337BEEF)` directly from inside the
//        target process's memory space!
//     4. Cleanly unloading the DLL when pressing `[END]`.
// ============================================================================

#ifdef _WIN32
#include <windows.h>
#include <iostream>
#include <cstdint>

using fnSpawnMythicChest = void(*)(uint32_t magicKey);

DWORD WINAPI InternalWorkerThread(LPVOID hModule) {
    std::cout << "\n[+] [INTERNAL DLL] Injected successfully into PID " << GetCurrentProcessId() << "!\n";

    HMODULE hMainExe = GetModuleHandleA(nullptr);
    std::cout << "[+] [INTERNAL DLL] Main Module Base Address: 0x"
              << std::hex << reinterpret_cast<uintptr_t>(hMainExe) << std::dec << "\n";

    // Look up Lab 09's exported internal function (or replace with Base + RVA offset!)
    auto pSpawnChest = reinterpret_cast<fnSpawnMythicChest>(
        GetProcAddress(hMainExe, "Engine_SpawnMythicChest")
    );

    if (pSpawnChest) {
        std::cout << "[+] [INTERNAL DLL] Located Engine_SpawnMythicChest at 0x"
                  << std::hex << reinterpret_cast<uintptr_t>(pSpawnChest) << std::dec << "\n";
        std::cout << "[*] [INTERNAL DLL] Invoking Engine_SpawnMythicChest(0x1337BEEF)...\n";
        pSpawnChest(0x1337BEEF);
    } else {
        std::cout << "[!] [INTERNAL DLL] Export not found. In stripped games, use:\n";
        std::cout << "    auto fn = reinterpret_cast<fnType>(moduleBase + 0xRVA);\n";
    }

    FreeLibraryAndExitThread(static_cast<HMODULE>(hModule), 0);
    return 0;
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    (void)lpReserved;
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hModule);
        HANDLE hThread = CreateThread(nullptr, 0, InternalWorkerThread, hModule, 0, nullptr);
        if (hThread) CloseHandle(hThread);
    }
    return TRUE;
}
#endif
