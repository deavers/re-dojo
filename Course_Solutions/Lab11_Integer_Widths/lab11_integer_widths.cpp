// ============================================================================
// [Lab 11] Integer Widths & Signedness (Tier F | Difficulty: 0.3/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 01. Not every number is a 4-byte int. Learn to pick the scan
//   type (1 / 2 / 8 Bytes), and see what signed and unsigned overflow do.
//
// QUEST OBJECTIVES (the Cursed Vault opens when ALL are true):
//   1. Morale is exactly -100      (1-byte signed)
//   2. Arrows are exactly 65535    (2-byte unsigned maximum)
//   3. Gold is at least 5 billion  (8-byte value - a 4-Byte scan cannot find it)
//   Two of them can be reached inside the game if you understand overflow.
//
// Exit codes: 0 vault opened (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <string>

#include "lab11_core.hpp"

using lab11::g_Treasury;

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
    std::cout << "  [LAB 11 | TIER F] THE CURSED VAULT (Integer Widths & Signedness)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Morale  (1 byte, signed)   : " << static_cast<int>(g_Treasury.morale);
    PrintAddress(&g_Treasury.morale);
    std::cout << "\n   Potions (1 byte, unsigned) : " << static_cast<int>(g_Treasury.potions);
    PrintAddress(&g_Treasury.potions);
    std::cout << "\n   Arrows  (2 bytes, unsigned): " << g_Treasury.arrows;
    PrintAddress(&g_Treasury.arrows);
    std::cout << "\n   Gold    (8 bytes, signed)  : " << g_Treasury.gold;
    PrintAddress(&g_Treasury.gold);
    std::cout << "\n--------------------------------------------------------------------\n";
    std::cout << "  Vault needs: Morale = -100, Arrows = 65535, Gold >= 5,000,000,000\n";
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
        std::cout << "  [1] Sell a potion          (+250 Gold, -1 Potion)\n";
        std::cout << "  [2] Shoot an arrow         (-1 Arrow - nobody checks for zero!)\n";
        std::cout << "  [3] Rest at the campfire   (+10 Morale, stored in one signed byte)\n";
        std::cout << "  [4] Hear grim news         (-1 Morale)\n";
        std::cout << "  [9] Knock on the Cursed Vault\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "Goodbye, adventurer.\n";
            return 3;
        }
        switch (choice)
        {
        case 1:
            if (g_Treasury.potions > 0)
            {
                g_Treasury.potions = static_cast<std::uint8_t>(g_Treasury.potions - 1);
                g_Treasury.gold += 250;
            }
            break;
        case 2:
            // Deliberate unsigned wrap-around: 0 - 1 in 2 bytes is 65535.
            g_Treasury.arrows = static_cast<std::uint16_t>(g_Treasury.arrows - 1);
            break;
        case 3:
            // Deliberate signed wrap-around: 127 + 10 in one signed byte becomes negative.
            g_Treasury.morale = static_cast<std::int8_t>(static_cast<std::uint8_t>(g_Treasury.morale) + 10);
            break;
        case 4:
            g_Treasury.morale = static_cast<std::int8_t>(static_cast<std::uint8_t>(g_Treasury.morale) - 1);
            break;
        default:
            break;
        }
        if (lab11::CheckWin(g_Treasury))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER F CLEARED!] The Cursed Vault creaks open.\n";
            std::cout << "  " << lab11::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> The Vault stays shut. Check every requirement and its size in bytes.\n";
        }
    }
}
