// ============================================================================
// [Lab 17] Nested Structs & Padding (Tier E | Difficulty: 1.6/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 16. Real game objects nest structs inside structs, and the
//   compiler inserts padding so every field is aligned to its size. A packed
//   struct (#pragma pack(1)) has no padding at all. Map the hero in Cheat
//   Engine's Structure Dissect / ReClass.NET and find each field's real offset.
//
// QUEST OBJECTIVES (you become a Legend when ALL are true):
//   1. Crit chance = 1.0
//   2. Armor durability = 9999
//   3. Loot gold value = 1000000
//
// Exit codes: 0 legend (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <iomanip>
#include <cstdint>

#include "lab17_core.hpp"

using lab17::g_Hero;

static bool g_BlindMode = false;

static void PrintState()
{
    const std::uint32_t lootGold = g_Hero.loot.goldValue;
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 17 | TIER E] THE LEGEND'S LEDGER (Nested Structs & Padding)\n";
    std::cout << "====================================================================\n";
    if (!g_BlindMode)
    {
        std::cout << "   Hero object at 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(&g_Hero)
                  << std::dec << "  (open it in Structure Dissect)\n";
    }
    std::cout << "   Level " << static_cast<int>(g_Hero.stats.level) << "   STR " << g_Hero.stats.strength << "   AGI "
              << g_Hero.stats.agility << "\n";
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "   Crit chance      : " << g_Hero.stats.crit << "\n";
    std::cout << std::defaultfloat << std::setprecision(6);
    std::cout << "   Armor tier " << static_cast<int>(g_Hero.armor.tier) << ", durability " << g_Hero.armor.durability
              << "\n";
    std::cout << "   Loot rarity " << static_cast<int>(g_Hero.loot.rarity) << ", gold value " << lootGold << "\n";
    std::cout << "--------------------------------------------------------------------\n";
    std::cout << "  Legend needs: Crit = 1.00, Durability = 9999, Loot gold = 1000000\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows the hero object address)\n";
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
        std::cout << "  [1] Train precision (+0.01 crit, stops at 0.50)\n";
        std::cout << "  [2] Repair armor    (+100 durability, stops at 2000)\n";
        std::cout << "  [3] Level up        (+1 level, +1 STR, +1 AGI)\n";
        std::cout << "  [9] Ask the bards for a legend\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The ledger closes.\n";
            return 3;
        }
        switch (choice)
        {
        case 1:
            g_Hero.stats.crit = (g_Hero.stats.crit + 0.01 > lab17::kCritCap) ? lab17::kCritCap : g_Hero.stats.crit + 0.01;
            break;
        case 2:
            g_Hero.armor.durability = static_cast<std::uint16_t>(
                (g_Hero.armor.durability + 100 > lab17::kDurabilityCap) ? lab17::kDurabilityCap
                                                                         : g_Hero.armor.durability + 100);
            break;
        case 3:
            g_Hero.stats.level = static_cast<std::uint8_t>(g_Hero.stats.level + 1);
            g_Hero.stats.strength += 1;
            g_Hero.stats.agility = static_cast<std::uint16_t>(g_Hero.stats.agility + 1);
            break;
        default:
            break;
        }
        if (lab17::CheckWin(g_Hero))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E CLEARED!] The bards sing of a new Legend.\n";
            std::cout << "  " << lab17::MakeFlag(g_Hero) << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> No legend yet. Padding hides between fields - and sometimes it does not.\n";
        }
    }
}
