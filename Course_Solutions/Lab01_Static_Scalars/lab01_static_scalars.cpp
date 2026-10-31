// ============================================================================
// [Lab 01] Static Scalars & Exact Value Scanning (Tier F- | Difficulty: 0.1/10)
// ============================================================================
// PURPOSE:
//   Your very first step in Reverse Engineering & Game Hacking.
//   Learn how integer variables live in virtual memory, how to scan for
//   exact values (4-Byte Int) in Cheat Engine, and how to modify/freeze them.
//
// QUEST OBJECTIVES:
//   1. Attach Cheat Engine to this process.
//   2. Find the memory addresses of g_HeroHP, g_Arrows, and g_Gold.
//   3. Give yourself 99,999 Gold to buy the Dragon Slayer Sword, OR set your
//      Attack Power to 9999 to one-shot the Slime King (5,000 HP)!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

// Global static variables (stored in the .data section of the PE binary)
int32_t g_HeroHP      = 100;
int32_t g_HeroMaxHP   = 100;
int32_t g_AttackPower = 12;
int32_t g_Arrows      = 10;
int32_t g_Gold        = 50;
int32_t g_SlimeKingHP = 5000;
bool    g_BlindMode   = false;

void PrintBanner() {
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 01 | TIER F-] THE SLIME KING'S GATE (Static Scalars Lab)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Hero HP      : " << g_HeroHP << " / " << g_HeroMaxHP;
    if (!g_BlindMode) std::cout << "   \t[Addr: 0x" << std::hex << std::uppercase << (uintptr_t)&g_HeroHP << std::dec << "]";
    std::cout << "\n   Attack Power : " << g_AttackPower;
    if (!g_BlindMode) std::cout << "          \t[Addr: 0x" << std::hex << std::uppercase << (uintptr_t)&g_AttackPower << std::dec << "]";
    std::cout << "\n   Arrows       : " << g_Arrows;
    if (!g_BlindMode) std::cout << "          \t[Addr: 0x" << std::hex << std::uppercase << (uintptr_t)&g_Arrows << std::dec << "]";
    std::cout << "\n   Gold Coins   : " << g_Gold;
    if (!g_BlindMode) std::cout << "          \t[Addr: 0x" << std::hex << std::uppercase << (uintptr_t)&g_Gold << std::dec << "]";
    std::cout << "\n--------------------------------------------------------------------\n";
    std::cout << "  [BOSS] Slime King HP : " << g_SlimeKingHP << " / 5000";
    if (!g_BlindMode) std::cout << "\t[Addr: 0x" << std::hex << std::uppercase << (uintptr_t)&g_SlimeKingHP << std::dec << "]";
    std::cout << "\n====================================================================\n";
}

int main() {
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows memory addresses on screen)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses - pure Cheat Engine scan)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_BlindMode = (mode == 2);

    while (g_HeroHP > 0 && g_SlimeKingHP > 0) {
        PrintBanner();
        std::cout << "Actions:\n";
        std::cout << "  [1] Shoot Arrow at Slime King (-1 Arrow, deals " << g_AttackPower << " DMG)\n";
        std::cout << "  [2] Drink Healing Potion      (-15 Gold, +40 HP)\n";
        std::cout << "  [3] Scavenge Dungeon Floor    (+7 Gold, Slime attacks you!)\n";
        std::cout << "  [4] Buy Dragon Slayer Sword   (Costs 99,999 Gold -> +5,000 Attack!)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice)) break;
        if (choice == 0) return 0;

        switch (choice) {
            case 1:
                if (g_Arrows > 0) {
                    g_Arrows--;
                    g_SlimeKingHP -= g_AttackPower;
                    std::cout << "\n>> You fired an arrow for " << g_AttackPower << " damage!\n";
                } else {
                    std::cout << "\n>> [!] Out of Arrows! Scan & freeze g_Arrows in Cheat Engine!\n";
                }
                break;
            case 2:
                if (g_Gold >= 15) {
                    g_Gold -= 15;
                    g_HeroHP += 40;
                    if (g_HeroHP > g_HeroMaxHP) g_HeroHP = g_HeroMaxHP;
                    std::cout << "\n>> Restored health!\n";
                } else {
                    std::cout << "\n>> [!] Not enough Gold!\n";
                }
                break;
            case 3:
                g_Gold += 7;
                std::cout << "\n>> Found 7 Gold coins on the floor!\n";
                break;
            case 4:
                if (g_Gold >= 99999) {
                    g_Gold -= 99999;
                    g_AttackPower += 5000;
                    std::cout << "\n>> [LEGENDARY] Equipped the Dragon Slayer Sword! Attack Power +5000!\n";
                } else {
                    std::cout << "\n>> [!] You need 99,999 Gold! (Hint: Scan for Gold in Cheat Engine)\n";
                }
                break;
            default:
                break;
        }

        if (g_SlimeKingHP > 0) {
            int bossDmg = 35;
            g_HeroHP -= bossDmg;
            std::cout << ">> Slime King slams you for " << bossDmg << " damage!\n";
        }
    }

    if (g_SlimeKingHP <= 0) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [QUEST COMPLETE - TIER F- CLEARED!]\n";
        std::cout << "  You defeated the Slime King through Memory Manipulation!\n";
        std::cout << "  Next Step: Proceed to Lab 02 (Data Types, Floats & Bitmasks).\n";
        std::cout << "********************************************************************\n";
    } else {
        std::cout << "\n[YOU DIED] Tip: Freeze your HP or edit Gold/AttackPower in Cheat Engine!\n";
    }
    std::cout << "Press Enter to exit...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}
