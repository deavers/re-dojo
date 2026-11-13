// ============================================================================
// [Lab 19] Pointer Scan Across Restarts (Tier E+ | Difficulty: 2.1/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 18. Every start of this program lays the heap out differently,
//   so the hero's gold has a new address on every run. Use Cheat Engine's
//   pointer scanner, restart the program, and rescan until only paths that
//   survive restarts remain. Two pointers look right on the first run but are
//   traps: one points to some other entity, one to a stale copy of the hero.
//
// QUEST OBJECTIVE:
//   Buy the Crown: the hero needs at least 777777 gold. A path that is valid
//   after three restarts is the real answer.
//
// Exit codes: 0 crown bought (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <random>

#include "lab19_core.hpp"

using lab19::g_World;

static bool g_BlindMode = false;

static void PrintState()
{
    const lab19::Entity* hero = lab19::Hero();
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 19 | TIER E+] THE SHIFTING HALLS (Pointer Scan Across Restarts)\n";
    std::cout << "====================================================================\n";
    if (!g_BlindMode)
    {
        std::cout << "   Hero gold at 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(&hero->gold)
                  << std::dec << "  (a different address on every start)\n";
    }
    std::cout << "   Hero " << hero->name << ": HP " << hero->hp << ", gold " << hero->gold << "\n";
    std::cout << "   World frame " << g_World.frame << "\n";
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  The Crown costs 777777 gold.\n";
}

int main()
{
    std::random_device rd;
    lab19::BuildWorld(rd());

    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the hero gold address)\n";
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
        std::cout << "  [1] Pick up a coin   (+1 gold)\n";
        std::cout << "  [2] Wait a turn      (world frame +1)\n";
        std::cout << "  [9] Buy the Crown\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The halls shift behind you.\n";
            return 3;
        }
        if (choice == 1)
        {
            lab19::Hero()->gold += 1;
        }
        g_World.frame += 1;
        if (lab19::CheckWin())
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E+ CLEARED!] The Crown is yours.\n";
            std::cout << "  " << lab19::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> Not enough gold. Does your pointer still work after a restart?\n";
        }
    }
}
