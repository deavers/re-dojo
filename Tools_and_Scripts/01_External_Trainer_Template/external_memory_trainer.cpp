// ============================================================================
// [Tool 01] Win32 External Memory Trainer Template (C++20)
// ============================================================================
// PURPOSE:
//   A clean, reusable C++ class for Stage 3 External Tooling:
//     - Process ID lookup via `CreateToolhelp32Snapshot`
//     - Module Base Address resolution (`module.exe + offset`)
//     - Type-safe `Read<T>()` and `Write<T>()` wrappers
//     - Multi-level pointer chain resolution (`[[Base + o1] + o2] + o3`)
//
// TEST TARGET:
//   Run `lab04_pointer_chains.exe` first, then run this trainer!
// ============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <cstdint>
#include <iomanip>

#ifdef _WIN32
#include <windows.h>
#include <tlhelp32.h>

class ExternalProcess {
public:
    DWORD     pid        = 0;
    HANDLE    hProcess   = nullptr;
    uintptr_t moduleBase = 0;

    ~ExternalProcess() {
        if (hProcess) CloseHandle(hProcess);
    }

    bool Attach(const std::wstring& processName) {
        HANDLE snap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if (snap == INVALID_HANDLE_VALUE) return false;

        PROCESSENTRY32W pe{};
        pe.dwSize = sizeof(pe);
        if (Process32FirstW(snap, &pe)) {
            do {
                if (processName == pe.szExeFile) {
                    pid = pe.th32ProcessID;
                    break;
                }
            } while (Process32NextW(snap, &pe));
        }
        CloseHandle(snap);
        if (!pid) return false;

        hProcess = OpenProcess(PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION | PROCESS_QUERY_INFORMATION, FALSE, pid);
        if (!hProcess) return false;

        moduleBase = GetModuleBase(processName);
        return (moduleBase != 0);
    }

    uintptr_t GetModuleBase(const std::wstring& moduleName) {
        HANDLE snap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid);
        if (snap == INVALID_HANDLE_VALUE) return 0;

        MODULEENTRY32W me{};
        me.dwSize = sizeof(me);
        uintptr_t base = 0;
        if (Module32FirstW(snap, &me)) {
            do {
                if (moduleName == me.szModule) {
                    base = reinterpret_cast<uintptr_t>(me.modBaseAddr);
                    break;
                }
            } while (Module32NextW(snap, &me));
        }
        CloseHandle(snap);
        return base;
    }

    template <typename T>
    T Read(uintptr_t address) const {
        T buffer{};
        ReadProcessMemory(hProcess, reinterpret_cast<LPCVOID>(address), &buffer, sizeof(T), nullptr);
        return buffer;
    }

    template <typename T>
    bool Write(uintptr_t address, const T& value) const {
        SIZE_T written = 0;
        return WriteProcessMemory(hProcess, reinterpret_cast<LPVOID>(address), &value, sizeof(T), &written) && (written == sizeof(T));
    }

    // Resolves: [[...[baseAddr] + offsets[0]] + offsets[1]...] + offsets[n-1]
    uintptr_t ResolvePointerChain(uintptr_t basePointerAddr, const std::vector<uintptr_t>& offsets) const {
        uintptr_t addr = Read<uintptr_t>(basePointerAddr);
        for (size_t i = 0; i < offsets.size(); ++i) {
            if (!addr) return 0;
            if (i == offsets.size() - 1) {
                addr += offsets[i];
            } else {
                addr = Read<uintptr_t>(addr + offsets[i]);
            }
        }
        return addr;
    }
};
#endif

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [TOOL 01] WIN32 EXTERNAL MEMORY TRAINER TEMPLATE\n";
    std::cout << "====================================================================\n";
#ifdef _WIN32
    ExternalProcess proc;
    std::wstring targetName = L"lab04_pointer_chains.exe";
    std::wcout << L"[*] Searching for target process: " << targetName << L"...\n";

    if (!proc.Attach(targetName)) {
        std::cout << "[!] Process not running. Launch `lab04_pointer_chains.exe` first!\n";
        std::cout << "    (Or enter a custom &g_WorldManager hex address once attached.)\n";
        return 0;
    }

    std::cout << "[+] Attached! PID: " << proc.pid
              << " | Module Base: 0x" << std::hex << std::uppercase << proc.moduleBase << std::dec << "\n";
    std::cout << "Enter hex address of &g_WorldManager (shown in Lab 04 Apprentice Mode): 0x";
    uintptr_t worldMgrAddr = 0;
    std::cin >> std::hex >> worldMgrAddr >> std::dec;

    // Lab 04 Pointer Chain: [g_WorldManager] -> +0x10 (Floor*) -> +0x18 (Hero*) -> +0x0C (HP)
    uintptr_t hpAddr  = proc.ResolvePointerChain(worldMgrAddr, { 0x10, 0x18, 0x0C });
    uintptr_t atkAddr = proc.ResolvePointerChain(worldMgrAddr, { 0x10, 0x18, 0x10 });

    if (hpAddr && atkAddr) {
        std::cout << "[+] Resolved Hero HP Address     : 0x" << std::hex << hpAddr << std::dec
                  << " (Current Value: " << proc.Read<int32_t>(hpAddr) << ")\n";
        std::cout << "[+] Resolved Hero Attack Address : 0x" << std::hex << atkAddr << std::dec
                  << " (Current Value: " << proc.Read<int32_t>(atkAddr) << ")\n";

        proc.Write<int32_t>(hpAddr, 99999);
        proc.Write<int32_t>(atkAddr, 99999);
        std::cout << "[+] Patched Hero HP and Attack to 99,999 via External Pointer Chain!\n";
    }
#else
    std::cout << "[!] Win32 External Trainer requires Windows.\n";
#endif
    return 0;
}
