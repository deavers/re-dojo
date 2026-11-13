// ============================================================================
// [Lab 16] Array of Structs & Stride (Tier E- | Difficulty: 1.4/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 03. Games keep entities in arrays of structs: the same field
//   of the next unit sits exactly one struct size (the "stride") further on.
//   Find one unit's HP, work out the stride, and edit the whole squad.
//
// QUEST OBJECTIVE:
//   The squad marches when ALL 8 units have at least 500 HP and are alive.
//   Healing stops at each unit's max HP, and the fallen unit cannot be revived
//   from the menu.
//
// Exit codes: 0 squad marches (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <iomanip>
#include <cstdint>

#include "lab16_core.hpp"

using lab16::g_Squad;

static bool g_BlindMode = false;

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 16 | TIER E-] THE IRON SQUAD (Array of Structs & Stride)\n";
    std::cout << "====================================================================\n";
    if (!g_BlindMode)
    {
        std::cout << "   Squad array at 0x" << std::hex << std::uppercase
                  << reinterpret_cast<std::uintptr_t>(&g_Squad) << std::dec << "\n";
    }
    std::cout << "   #  ID    HP / MAX   POS        STATUS\n";
    for (std::size_t i = 0; i < lab16::kSquadSize; ++i)
    {
        const lab16::Unit& u = g_Squad.units[i];
        std::cout << "   " << i << "  " << u.id << "   " << std::setw(4) << u.hp << " / " << std::setw(3) << u.maxHp
                  << "   (" << u.x << ", " << u.y << ")   " << ((u.flags & lab16::kAlive) ? "alive" : "FALLEN")
                  << "\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  The squad marches when every unit has >= 500 HP and is alive.\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the array address on screen)\n";
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
        std::cout << "  [1] Heal a unit   (+5 HP, up to its max)\n";
        std::cout << "  [2] Skirmish      (unit 0 takes 3 damage)\n";
        std::cout << "  [9] Order the march\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The squad stands down.\n";
            return 3;
        }
        if (choice == 1)
        {
            std::cout << "Unit number (0-7): ";
            std::size_t n = 0;
            if (!(std::cin >> n))
            {
                return 3;
            }
            if (n < lab16::kSquadSize && (g_Squad.units[n].flags & lab16::kAlive) != 0)
            {
                lab16::Unit& u = g_Squad.units[n];
                u.hp = (u.hp + 5 > u.maxHp) ? u.maxHp : u.hp + 5;
            }
            else
            {
                std::cout << ">> Nobody to heal there.\n";
            }
        }
        else if (choice == 2 && g_Squad.units[0].hp > 3)
        {
            g_Squad.units[0].hp -= 3;
        }
        if (lab16::CheckWin(g_Squad))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E- CLEARED!] The Iron Squad marches out.\n";
            std::cout << "  " << lab16::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> The squad is not ready. Every unit counts - including the fallen one.\n";
        }
    }
}
