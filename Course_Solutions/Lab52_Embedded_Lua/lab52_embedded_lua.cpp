// ============================================================================
// [Lab 52] Embedded Lua 5.4: lua_State (Tier A- | Difficulty: 6.3/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 09 (internal DLL) and Lab 17 (struct layout). Many games run
//   their logic in an embedded Lua VM. Instead of hunting numbers, find the
//   game's lua_State and run your own Lua code inside it: from an injected DLL,
//   take luaL_loadstring / lua_pcallk from lua54.dll (GetProcAddress), read the
//   state pointer from the engine object, and execute a chunk.
//
// QUEST OBJECTIVE:
//   The Archmage Guild admits a hero with exactly 1,000,000 gold and the title
//   "Archmage". The script only ever adds 1 gold per turn and never changes the
//   title - change them through the game's own Lua state.
//
// Exit codes: 0 admitted (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <string>

#include "lab52_core.hpp"

using lab52::g_Engine;

static bool g_BlindMode = false;

static void PrintState()
{
    double gold = 0.0;
    std::string title;
    lab52::ReadHero(gold, title);
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 52 | TIER A-] THE ARCHMAGE GUILD (Embedded Lua 5.4)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Script " << g_Engine.scriptName << ", turn " << g_Engine.turn << "\n";
    std::cout << "   hero.gold  = " << static_cast<std::int64_t>(gold) << "\n";
    std::cout << "   hero.title = " << title << "\n";
    if (!g_BlindMode)
    {
        std::cout << "   Engine object at 0x" << std::hex << std::uppercase
                  << reinterpret_cast<std::uintptr_t>(&g_Engine) << ", lua_State* 0x"
                  << reinterpret_cast<std::uintptr_t>(g_Engine.L) << std::dec << "\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  The Guild needs hero.gold == 1000000 and hero.title == \"Archmage\".\n";
}

int main()
{
    if (!lab52::Boot())
    {
        std::cout << "The realm script failed to load.\n";
        return 2;
    }
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the engine object and the lua_State pointer)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses)\n> ";
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
        std::cout << "  [1] End the turn (Lua tick(): +1 gold)\n";
        std::cout << "  [9] Ask the Guild to admit you\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The realm sleeps.\n";
            return 3;
        }
        if (choice == 1)
        {
            lab52::Tick();
        }
        if (lab52::CheckWin())
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER A- CLEARED!] The Archmage Guild opens its doors.\n";
            std::cout << "  " << lab52::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> Refused. The numbers live in Lua - speak to the game's lua_State.\n";
        }
    }
}
