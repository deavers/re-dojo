// ============================================================================
// [Lab 18] Lazy Singleton (Tier E+ | Difficulty: 2.0/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 04. Many engines keep their managers behind a static pointer
//   that stays NULL until first use. A pointer scan taken too early finds
//   nothing; the base only becomes useful once the object graph exists.
//   Find the static pointer, wait for the lazy init, then walk the chain.
//
// QUEST OBJECTIVE:
//   Open the Treasure Room with exactly 99999 gems.
//   Each dungeon visit gives one gem.
//
// Exit codes: 0 treasure opened (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>

#include "lab18_core.hpp"

using lab18::g_pGameManager;

static bool g_BlindMode = false;

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 18 | TIER E+] THE SLEEPING MANAGER (Lazy Singleton)\n";
    std::cout << "====================================================================\n";
    if (!g_BlindMode)
    {
        std::cout << "   Static pointer g_pGameManager lives at 0x" << std::hex << std::uppercase
                  << reinterpret_cast<std::uintptr_t>(&g_pGameManager) << std::dec << "\n";
    }
    if (g_pGameManager == nullptr)
    {
        std::cout << "   The Game Manager is still asleep (pointer is NULL).\n";
    }
    else
    {
        const lab18::Player* p = g_pGameManager->player;
        std::cout << "   Floor " << g_pGameManager->floor << ", visits " << g_pGameManager->ticks << "\n";
        std::cout << "   HP " << p->hp << ", level " << p->level << ", gems " << p->inventory->gems << "\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  The Treasure Room needs exactly 99999 gems.\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the static pointer address)\n";
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
        std::cout << "  [1] Enter the dungeon (wakes the manager on the first visit, +1 gem)\n";
        std::cout << "  [9] Open the Treasure Room\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "You leave the dungeon.\n";
            return 3;
        }
        if (choice == 1)
        {
            lab18::GameManager* gm = lab18::EnterDungeon();
            gm->player->inventory->gems += 1;
        }
        if (lab18::CheckWin())
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E+ CLEARED!] The Treasure Room opens.\n";
            std::cout << "  " << lab18::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> Locked. Follow the static pointer - once it is no longer NULL.\n";
        }
    }
}
