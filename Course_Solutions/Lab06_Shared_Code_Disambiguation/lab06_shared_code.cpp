// ============================================================================
// [Lab 06] Shared Engine Code & Entity Disambiguation (Tier D | Diff: 3.0/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 05. In real engines (Unreal Tournament 99, Half-Life, Unity),
//   there is ONLY ONE `ApplyDamage(Actor* victim, int dmg)` function shared by
//   both the Player and all Enemies!
//   If you simply NOP the `victim->hp -= dmg` instruction like in Lab 05, the
//   Boss becomes invincible too!
//
// QUEST OBJECTIVE:
//   Write an Auto Assembler script in `ApplySharedDamage` that inspects
//   `victim->factionId` (Offset +0x08):
//     - If factionId == 1 (Player) -> Set damage to 0 (God Mode)
//     - If factionId == 2 (Dragon) -> Set damage to 999,999 (One-Hit Kill!)
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

struct CombatActor {
    const char* name;       // +0x00 (8 bytes on x64)
    int32_t     factionId;  // +0x08 (1 = Player, 2 = Enemy Boss)
    int32_t     level;      // +0x0C
    int32_t     hp;         // +0x10 <-- Shared HP Offset!
    int32_t     maxHp;      // +0x14
    int32_t     attack;     // +0x18
};

CombatActor g_Hero   = { "Sir Deavers",    1, 15,    200,    200,  35 };
CombatActor g_Dragon = { "Shadow Dragon",  2, 99, 250000, 250000, 180 };
bool        g_Blind  = false;

// BOTH the Hero and the Dragon take damage through this exact same function!
NOINLINE void ApplySharedDamage(CombatActor* victim, int32_t dmg) {
    // ------------------------------------------------------------------------
    // SHARED INSTRUCTION:
    //   On x64 MSVC: RCX = victim, EDX = dmg
    //   victim->factionId is at [RCX + 0x08]
    //   victim->hp        is at [RCX + 0x10]
    // ------------------------------------------------------------------------
    victim->hp -= dmg;
    if (victim->hp < 0) victim->hp = 0;
}

int main() {
    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Struct Offsets & Shared Function)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_Blind = (mode == 2);

    while (g_Hero.hp > 0 && g_Dragon.hp > 0) {
        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 06 | TIER D] LAIR OF SHARED CODE (Player vs Boss Filter)\n";
        std::cout << "====================================================================\n";
        std::cout << "  [PLAYER] " << g_Hero.name   << " (Faction " << g_Hero.factionId   << ") | HP: " << g_Hero.hp   << " / " << g_Hero.maxHp << "\n";
        std::cout << "  [BOSS]   " << g_Dragon.name << " (Faction " << g_Dragon.factionId << ") | HP: " << g_Dragon.hp << " / " << g_Dragon.maxHp << "\n";

        if (!g_Blind) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  Hero Struct   : 0x" << std::hex << (uintptr_t)&g_Hero   << " (HP at +0x10, FactionId at +0x08)\n";
            std::cout << "  Dragon Struct : 0x" << (uintptr_t)&g_Dragon << " (HP at +0x10, FactionId at +0x08)\n";
            std::cout << "  Shared Fn     : 0x" << (uintptr_t)&ApplySharedDamage << std::dec << "\n";
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Exchange Blows (Calls ApplySharedDamage on Dragon, then on Hero)\n";
        std::cout << "  [2] Heal Hero (+50 HP)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            std::cout << "\n>> Hero strikes Shadow Dragon...\n";
            ApplySharedDamage(&g_Dragon, g_Hero.attack);

            if (g_Dragon.hp > 0) {
                std::cout << ">> Shadow Dragon breathes fire on Hero...\n";
                ApplySharedDamage(&g_Hero, g_Dragon.attack);
            }
        } else if (choice == 2) {
            g_Hero.hp = (g_Hero.hp + 50 > g_Hero.maxHp) ? g_Hero.maxHp : g_Hero.hp + 50;
            std::cout << ">> Restored 50 HP.\n";
        }
    }

    if (g_Dragon.hp <= 0 && g_Hero.hp > 0) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [QUEST COMPLETE - TIER D CLEARED!]\n";
        std::cout << "  You separated Player vs Enemy inside a shared engine routine!\n";
        std::cout << "  (This exact technique powers UT99 & Isaac One-Hit-Kill scripts!)\n";
        std::cout << "  Next Step: Proceed to Lab 07 (ReClass.NET & VMT Polymorphism).\n";
        std::cout << "********************************************************************\n";
    } else {
        std::cout << "\n[YOU DIED] Don't just NOP ApplySharedDamage—compare [rcx+08] == 1!\n";
    }
    return 0;
}
