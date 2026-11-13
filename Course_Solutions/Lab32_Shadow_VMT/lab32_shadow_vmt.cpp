// ============================================================================
// [Lab 32] Shadow VMT (Tier C | Difficulty: 3.9/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 07. Every object of a class shares ONE virtual method table.
//   Patching that table changes the behaviour of ALL objects of the class - and
//   in a real binary the table sits in read-only memory anyway. The precise way
//   is a "shadow VMT": copy the table into your own memory, change one slot in
//   the copy, and point only the chosen object's vptr at the copy.
//
// QUEST OBJECTIVE:
//   Bribe the Captain (third guard) so that IsBribable() returns true for HIM
//   ONLY. If any other guard becomes bribable too, the Marshal notices.
//   Hint: the Merchant's table already has an IsBribable() that returns true.
//
// Exit codes: 0 bribe accepted (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <cstring>

#include "lab32_core.hpp"

using lab32::g_Roster;

static bool g_BlindMode = false;

static std::uintptr_t VptrOf(const void* object)
{
    std::uintptr_t v = 0;
    std::memcpy(&v, object, sizeof(v));
    return v;
}

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 32 | TIER C] THE CAPTAIN'S PRICE (Shadow VMT)\n";
    std::cout << "====================================================================\n";
    for (int i = 0; i < 3; ++i)
    {
        lab32::IPerson* p = g_Roster[i];
        std::cout << "   [" << i << "] " << p->Name() << "  greet " << p->Greet() << "  strength " << p->Strength();
        if (!g_BlindMode)
        {
            std::cout << "   [obj 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(p)
                      << ", vptr 0x" << VptrOf(p) << std::dec << "]";
        }
        std::cout << "\n";
    }
    if (!g_BlindMode)
    {
        std::cout << "   Merchant: obj 0x" << std::hex << std::uppercase
                  << reinterpret_cast<std::uintptr_t>(&lab32::g_Merchant) << ", vptr 0x" << VptrOf(&lab32::g_Merchant)
                  << std::dec << "\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  Only the Captain may take the bribe. The Marshal watches the other guards.\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows objects and vptr values)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses - find them yourself)\n> ";
    int mode = 1;
    if (!(std::cin >> mode))
    {
        return 3;
    }
    g_BlindMode = (mode == 2);

    while (true)
    {
        PrintState();
        std::cout << "Actions:\n";
        std::cout << "  [1] Ask every guard if he can be bribed\n";
        std::cout << "  [9] Offer the bribe to the Captain\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "You leave the gatehouse.\n";
            return 3;
        }
        if (choice == 1)
        {
            for (int i = 0; i < 3; ++i)
            {
                std::cout << "   [" << i << "] " << (g_Roster[i]->IsBribable() ? "nods slowly" : "refuses") << "\n";
            }
        }
        if (lab32::CheckWin())
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER C CLEARED!] The Captain pockets the gold.\n";
            std::cout << "  " << lab32::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            if (g_Roster[0]->IsBribable() || g_Roster[1]->IsBribable())
            {
                std::cout << ">> The Marshal notices that EVERY guard takes bribes. You patched the shared table.\n";
            }
            else
            {
                std::cout << ">> The Captain refuses. His IsBribable() still answers false.\n";
            }
        }
    }
}
