// ============================================================================
// [Lab 54] Own Emulator: Guest RAM (Tier A | Difficulty: 6.5/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 18. In an emulated console the game's variables live inside
//   the GUEST's RAM, which is just a buffer in the emulator's (host) heap. The
//   console manual gives guest addresses; Cheat Engine sees host addresses.
//   Find the host base of guest RAM (host address - guest address), find the
//   emulator's pointer to it, and translate guest addresses to host addresses.
//
// QUEST OBJECTIVE:
//   Inside the console: lives exactly 99 and score at least 50000.
//   Manual: lives at guest 0x0300 (u8), score at guest 0x0302 (u16, little-endian).
//
// Exit codes: 0 high score accepted (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <random>

#include "lab54_core.hpp"

using lab54::g_Machine;

static bool g_BlindMode = false;

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 54 | TIER A] THE DOJOBOY CONSOLE (Own Emulator: Guest RAM)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Guest lives : " << static_cast<int>(g_Machine.ram[lab54::kLives]) << "   (guest 0x0300)\n";
    std::cout << "   Guest score : " << lab54::ReadGuest16(lab54::kScore) << "   (guest 0x0302)\n";
    std::cout << "   Guest level : " << static_cast<int>(g_Machine.ram[lab54::kLevel]) << "\n";
    std::cout << "   Cycles      : " << g_Machine.cycles << "\n";
    if (!g_BlindMode)
    {
        std::cout << "   Host address of the score: 0x" << std::hex << std::uppercase
                  << reinterpret_cast<std::uintptr_t>(&g_Machine.ram[lab54::kScore]) << std::dec
                  << "  (changes on every start)\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  High score table needs: lives = 99 and score >= 50000.\n";
}

int main()
{
    std::random_device rd;
    lab54::PowerOn(rd());

    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the host address of the score)\n";
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
        std::cout << "  [1] Play a frame  (guest ROM: score += 7)\n";
        std::cout << "  [2] Take a hit    (guest ROM: lives -= 1)\n";
        std::cout << "  [9] Submit to the high score table\n";
        std::cout << "  [0] Power off\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The console powers off.\n";
            return 3;
        }
        if (choice == 1)
        {
            lab54::RunRoutine(lab54::kRoutinePlay);
        }
        else if (choice == 2)
        {
            lab54::RunRoutine(lab54::kRoutineHit);
        }
        if (lab54::CheckWin())
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER A CLEARED!] New high score on the DojoBoy.\n";
            std::cout << "  " << lab54::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> Rejected. Guest addresses are not host addresses - find the RAM base.\n";
        }
    }
}
