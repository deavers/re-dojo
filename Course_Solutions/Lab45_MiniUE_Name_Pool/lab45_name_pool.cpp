// ============================================================================
// [Lab 45] Mini-"UE": Name Pool (Tier B+ | Difficulty: 5.6/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 33 (RTTI) and Lab 35 (names through hashes). Engines like
//   Unreal do not store object names as strings inside objects: an object holds
//   an FName INDEX into a global name pool. To read any name you must understand
//   the pool: where the global lives, how chunks are stored, how an entry is laid
//   out, and how an index splits into chunk and offset. That is step one of
//   every SDK dumper.
//
// QUEST OBJECTIVE:
//   Three sealed objects show only their FName indices. Name all three.
//   Then write a full dumper for the pool (the lab45 checker validates it; format in the map hints).
//
// Exit codes: 0 seals broken (flag printed), 1 wrong names, 2 wrong format, 3 end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#include <random>
#include <string>

#include "lab45_core.hpp"

int main()
{
    std::random_device rd;
    const std::uint32_t seed = rd();
    lab45::BuildPool(seed);

    std::cout << "====================================================================\n";
    std::cout << "  [LAB 45 | TIER B+] THE NAMELESS VAULT (Mini-UE: Name Pool)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Name pool global at 0x" << std::hex << std::uppercase
              << reinterpret_cast<std::uintptr_t>(&lab45::g_NamePool) << std::dec << "  (" << lab45::kNameCount
              << " names, " << (lab45::g_NamePool.currentChunk + 1) << " chunks)\n";
    std::cout << "   Pool seed: " << seed << "  (give it to the checker together with your dump)\n";
    std::cout << "   Sealed objects reference these FName indices:\n";
    for (const std::size_t i : lab45::kSealed)
    {
        std::cout << "      0x" << std::hex << std::uppercase << std::setw(8) << std::setfill('0') << lab45::g_Index[i]
                  << std::dec << std::setfill(' ') << "\n";
    }
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "Type the three names, separated by spaces, in the order shown: ";

    std::string names[3];
    if (!(std::cin >> names[0]))
    {
        std::cout << "\n>> The vault stays sealed.\n";
        return 3;
    }
    if (!(std::cin >> names[1] >> names[2]))
    {
        std::cout << ">> [FAILED] Three names are needed.\n";
        return 2;
    }
    for (int k = 0; k < 3; ++k)
    {
        if (names[k] != lab45::Resolve(lab45::g_Index[lab45::kSealed[k]]))
        {
            std::cout << ">> [FAILED] Seal " << (k + 1) << " does not answer to that name.\n";
            return 1;
        }
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [QUEST COMPLETE - TIER B+ CLEARED!] All three seals break.\n";
    std::cout << "  " << lab45::MakeFlag(seed) << "\n";
    std::cout << "  Next: dump the WHOLE pool and run the checker (format: hints on the map).\n";
    std::cout << "********************************************************************\n";
    return 0;
}
