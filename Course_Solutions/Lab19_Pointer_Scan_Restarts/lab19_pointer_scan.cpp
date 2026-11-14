// ============================================================================
// [Lab 19] Pointer Scan Across Restarts (Tier E+ | Difficulty: 2.1/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 18. Every start of this program lays the heap out differently,
//   so the hero's gold has a new address every time. Find a pointer path to it
//   that survives restarts, then submit that path: the program rebuilds the
//   world three times with fresh heap layouts and checks the path in each one.
//
// QUEST OBJECTIVE:
//   Submit a chain of offsets, starting at the static world object, that leads
//   to the hero's gold in every rebuilt world.
//
// Exit codes: 0 path accepted (flag printed), 1 path rejected, 2 malformed path,
//             3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <random>
#include <sstream>
#include <string>
#include <vector>

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
                  << ", world object at 0x" << reinterpret_cast<std::uintptr_t>(&g_World) << std::dec << "\n";
    }
    std::cout << "   Hero " << hero->name << ": HP " << hero->hp << ", gold " << hero->gold << "\n";
    std::cout << "   World frame " << g_World.frame << "\n";
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  Submit a path from the world object to the hero's gold that survives restarts.\n";
}

// Parses "0x18 0x08 ..." (hex or decimal). Returns false for an empty or malformed line.
static bool ParsePath(const std::string& line, std::vector<std::size_t>& offsets)
{
    std::istringstream in(line);
    std::string tok;
    while (in >> tok)
    {
        try
        {
            if (tok[0] == '-')
            {
                return false;
            }
            offsets.push_back(static_cast<std::size_t>(std::stoull(tok, nullptr, 0)));
        }
        catch (const std::exception&)
        {
            return false;
        }
    }
    return !offsets.empty() && offsets.size() <= lab19::kMaxOffsets;
}

int main()
{
    std::random_device rd;
    lab19::BuildWorld(rd());

    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the hero gold and world object addresses)\n";
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
        std::cout << "  [2] Wait a turn\n";
        std::cout << "  [5] Submit a pointer path (offsets from the world object)\n";
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
        if (choice == 1 || choice == 2)
        {
            lab19::Turn();
        }
        if (choice == 5)
        {
            std::cout << "Offsets, e.g. 0x10 0x2C: ";
            std::string line;
            std::cin >> std::ws;
            if (!std::getline(std::cin, line))
            {
                return 3;
            }
            std::vector<std::size_t> offsets;
            if (!ParsePath(line, offsets))
            {
                std::cout << ">> [FAILED] Malformed path.\n";
                return 2;
            }
            if (!lab19::VerifyAcrossRebuilds(offsets, rd()))
            {
                std::cout << ">> [FAILED] The path breaks after a restart (or never reached the hero's gold).\n";
                return 1;
            }
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E+ CLEARED!] The path held in three rebuilt worlds.\n";
            std::cout << "  " << lab19::MakeFlag(offsets) << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
    }
}
