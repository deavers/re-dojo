// ============================================================================
// [Lab 12] Double & Fuzzy Scans (Tier F+ | Difficulty: 0.6/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 02. The screen shows ROUNDED numbers, so an exact scan for the
//   value you see fails. Learn "Unknown initial value" + Increased / Decreased
//   scans, and the difference between an 8-byte double and a 4-byte float.
//
// QUEST OBJECTIVES (the Philosopher's Stone forms when BOTH are true):
//   1. Essence is at least 1,000,000   (double)
//   2. Catalyst purity is at least 99.9 %  (float; filtering stops at 95 %)
//
// Exit codes: 0 stone formed (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdint>

#include "lab12_core.hpp"

using lab12::g_Alchemy;

static bool g_BlindMode = false;

static void PrintAddress(const void* p)
{
    if (!g_BlindMode)
    {
        std::cout << "   [Addr: 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(p) << std::dec
                  << "]";
    }
}

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 12 | TIER F+] THE ALCHEMIST'S ROUNDING (Double & Fuzzy Scans)\n";
    std::cout << "====================================================================\n";
    std::cout << std::fixed << std::setprecision(1);
    std::cout << "   Essence          : ~" << g_Alchemy.essence;
    PrintAddress(&g_Alchemy.essence);
    std::cout << "\n   Catalyst purity  : ~" << std::setprecision(0) << g_Alchemy.catalystPurity * 100.0f << " %";
    PrintAddress(&g_Alchemy.catalystPurity);
    std::cout << "\n   Brews            : " << g_Alchemy.brews;
    PrintAddress(&g_Alchemy.brews);
    std::cout << std::defaultfloat << std::setprecision(6);
    std::cout << "\n--------------------------------------------------------------------\n";
    std::cout << "  Stone needs: Essence >= 1,000,000 and Purity >= 99.9 % (values on screen are rounded)\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows memory addresses on screen)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses - pure Cheat Engine scan)\n> ";
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
        std::cout << "  [1] Brew           (Essence grows by an uneven amount)\n";
        std::cout << "  [2] Spill a flask  (Essence shrinks by 10 %)\n";
        std::cout << "  [3] Filter catalyst (+3.71 % purity, stops at 95 %)\n";
        std::cout << "  [4] Stir carelessly (-2.3 % purity)\n";
        std::cout << "  [9] Try to form the Philosopher's Stone\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The furnace cools down.\n";
            return 3;
        }
        switch (choice)
        {
        case 1:
            g_Alchemy.essence += 3.14159 * (1.0 + g_Alchemy.catalystPurity) + 0.0173 * g_Alchemy.brews;
            g_Alchemy.brews += 1;
            break;
        case 2:
            g_Alchemy.essence *= 0.9;
            break;
        case 3:
            g_Alchemy.catalystPurity = std::fmin(lab12::kPurityCap, g_Alchemy.catalystPurity + 0.0371f);
            break;
        case 4:
            g_Alchemy.catalystPurity = std::fmax(0.0f, g_Alchemy.catalystPurity - 0.023f);
            break;
        default:
            break;
        }
        if (lab12::CheckWin(g_Alchemy))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER F+ CLEARED!] The Philosopher's Stone glows.\n";
            std::cout << "  " << lab12::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> Nothing happens. Remember: what you see on screen is rounded.\n";
        }
    }
}
