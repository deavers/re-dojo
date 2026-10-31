// ============================================================================
// [Lab 07] C++ Polymorphism, ReClass.NET & VMT Hooking (Tier C- | Diff: 3.8/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 06. How does C++ implement `virtual` functions under the hood?
//   At offset 0x00 of any polymorphic object lies an 8-byte pointer (`vptr`)
//   pointing to a Virtual Method Table (VMT) — an array of function pointers!
//
// QUEST OBJECTIVES:
//   1. Inspect `g_PlayerInstance` in ReClass.NET or Cheat Engine Structure Dissect.
//   2. Locate the hidden `GrandmasterAccount` vtable (or overwrite the `vptr` /
//      VMT entry `IsGrandmasterAuthorized()`) to unlock the Forbidden Vault!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

class IAccount {
public:
    virtual const char* GetRankTitle()           = 0; // VMT Index [0] (+0x00)
    virtual int32_t     GetDailyGoldAllowance()  = 0; // VMT Index [1] (+0x08)
    virtual bool        IsGrandmasterAuthorized()= 0; // VMT Index [2] (+0x10)
};

class AdventurerAccount : public IAccount {
public:
    // Offset +0x00: Implicit vptr (8 bytes on x64)
    int32_t accountId    = 10042;  // Offset +0x08
    int32_t goldBalance  = 250;    // Offset +0x0C
    float   reputation   = 14.5f;  // Offset +0x10
    int32_t secretPin    = 7777;   // Offset +0x14

    const char* GetRankTitle() override { return "Tier C Adventurer (Standard)"; }
    int32_t     GetDailyGoldAllowance() override { return 10; }
    bool        IsGrandmasterAuthorized() override { return false; }
};

// A privileged class compiled into the binary whose VMT grants full access!
class GrandmasterAccount : public IAccount {
public:
    int32_t accountId    = 1;
    int32_t goldBalance  = 999999;
    float   reputation   = 999.9f;
    int32_t secretPin    = 1337;

    const char* GetRankTitle() override { return "Tier SSS++ Grandmaster Architect"; }
    int32_t     GetDailyGoldAllowance() override { return 50000; }
    bool        IsGrandmasterAuthorized() override { return true; }
};

IAccount*           g_PlayerInstance    = nullptr;
GrandmasterAccount* g_ReferenceGMObject = nullptr;
bool                g_Blind             = false;

int main() {
    g_PlayerInstance    = new AdventurerAccount();
    g_ReferenceGMObject = new GrandmasterAccount();

    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Object & VTable Pointers)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_Blind = (mode == 2);

    while (true) {
        uintptr_t vptr = *reinterpret_cast<uintptr_t*>(g_PlayerInstance);
        uintptr_t gmVptr = *reinterpret_cast<uintptr_t*>(g_ReferenceGMObject);

        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 07 | TIER C-] SANCTUM OF VIRTUAL TABLES (ReClass & VMT Lab)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Current Rank Title : " << g_PlayerInstance->GetRankTitle() << "\n";
        std::cout << "  Daily Allowance    : " << g_PlayerInstance->GetDailyGoldAllowance() << " Gold\n";
        std::cout << "  Vault Authorized?  : " << (g_PlayerInstance->IsGrandmasterAuthorized() ? "YES [UNLOCKED]" : "NO [ACCESS DENIED]") << "\n";

        if (!g_Blind) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  g_PlayerInstance (Heap Object) : 0x" << std::hex << std::uppercase << (uintptr_t)g_PlayerInstance << "\n";
            std::cout << "   -> [Offset +0x00] Current vptr: 0x" << vptr << " (AdventurerAccount VMT)\n";
            std::cout << "  Grandmaster VMT Address        : 0x" << gmVptr << " <-- Swap vptr to this!\n" << std::dec;
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Claim Daily Gold Allowance (Calls VMT[1])\n";
        std::cout << "  [2] Attempt to Open Grandmaster Vault (Calls VMT[2])\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            AdventurerAccount* adv = reinterpret_cast<AdventurerAccount*>(g_PlayerInstance);
            int32_t bonus = g_PlayerInstance->GetDailyGoldAllowance();
            adv->goldBalance += bonus;
            std::cout << ">> Claimed " << bonus << " Gold! New Balance: " << adv->goldBalance << "\n";
        } else if (choice == 2) {
            if (g_PlayerInstance->IsGrandmasterAuthorized()) {
                std::cout << "\n********************************************************************\n";
                std::cout << "  [QUEST COMPLETE - TIER C- CLEARED!]\n";
                std::cout << "  You hijacked a C++ Virtual Method Table (vptr) in live memory!\n";
                std::cout << "  Next Step: Proceed to Lab 08 (3D Math & WorldToScreen Simulator).\n";
                std::cout << "********************************************************************\n";
                break;
            } else {
                std::cout << ">> [ACCESS DENIED] VMT[2] returned false! Swap the vptr at [g_PlayerInstance+0x00]!\n";
            }
        }
    }
    return 0;
}
