// ============================================================================
// [Lab 02] Data Types, IEEE-754 Floats & Bitmasks (Tier F | Difficulty: 0.5/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 01. Real games don't just use 32-bit ints!
//   They use IEEE-754 Floats (stamina/mana bars), Doubles (clicker currencies),
//   16-bit Shorts (item durability), and 8-bit Bitmasks (status flags packed
//   into a single byte).
//
// QUEST OBJECTIVES:
//   To open the Sanctuary Seal, all 3 conditions must hold simultaneously:
//   1. g_ManaPool (float)        >= 500.0f
//   2. g_ShieldDurability (int16)>= 1000
//   3. g_StatusBitmask (uint8_t) : Must have NO debuffs (Poison/Curse/Silence = 0)
//                                  AND must have DIVINE_BLESSING bit (0x80) set!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

// Status bitmask flags packed into 1 byte (uint8_t)
constexpr uint8_t FLAG_POISONED        = 0x01; // 0000 0001
constexpr uint8_t FLAG_CURSED          = 0x02; // 0000 0010
constexpr uint8_t FLAG_SILENCED        = 0x04; // 0000 0100
constexpr uint8_t FLAG_BURNING         = 0x08; // 0000 1000
constexpr uint8_t FLAG_DIVINE_BLESSING = 0x80; // 1000 0000 (Decimal 128)

float    g_ManaPool         = 85.5f;
double   g_SoulEssence      = 12.75;
int16_t  g_ShieldDurability = 45;
uint8_t  g_StatusBitmask    = FLAG_POISONED | FLAG_CURSED | FLAG_SILENCED; // 0x07 (Decimal 7)
bool     g_BlindMode        = false;

void PrintStatusBits(uint8_t mask) {
    std::cout << "0x" << std::hex << std::uppercase << std::setw(2) << std::setfill('0') << (int)mask << std::dec << " [ ";
    if (mask & FLAG_POISONED)        std::cout << "POISONED ";
    if (mask & FLAG_CURSED)          std::cout << "CURSED ";
    if (mask & FLAG_SILENCED)        std::cout << "SILENCED ";
    if (mask & FLAG_BURNING)         std::cout << "BURNING ";
    if (mask & FLAG_DIVINE_BLESSING) std::cout << "✨DIVINE_BLESSING✨ ";
    if (mask == 0)                   std::cout << "CLEAN ";
    std::cout << "]";
}

int main() {
    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Guided)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_BlindMode = (mode == 2);

    while (true) {
        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 02 | TIER F] THE SANCTUARY SEAL (Data Types & Bitmasks)\n";
        std::cout << "====================================================================\n";
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "  1. Mana Pool (Float)         : " << g_ManaPool << " / 500.00 req";
        if (!g_BlindMode) std::cout << "\t[0x" << std::hex << (uintptr_t)&g_ManaPool << std::dec << "]";
        std::cout << "\n  2. Soul Essence (Double)     : " << g_SoulEssence;
        if (!g_BlindMode) std::cout << "\t\t[0x" << std::hex << (uintptr_t)&g_SoulEssence << std::dec << "]";
        std::cout << "\n  3. Shield Durability (2-Byte): " << g_ShieldDurability << " / 1000 req";
        if (!g_BlindMode) std::cout << "\t\t[0x" << std::hex << (uintptr_t)&g_ShieldDurability << std::dec << "]";
        std::cout << "\n  4. Status Bitmask (1-Byte)   : ";
        PrintStatusBits(g_StatusBitmask);
        if (!g_BlindMode) std::cout << " [0x" << std::hex << (uintptr_t)&g_StatusBitmask << std::dec << "]";
        std::cout << "\n====================================================================\n";

        std::cout << "Actions:\n";
        std::cout << "  [1] Channel Arcane Bolt (-6.25 Float Mana, +1.50 Double Essence)\n";
        std::cout << "  [2] Block Enemy Strike  (-5 Short Shield Durability)\n";
        std::cout << "  [3] Toggle Burning Debuff Bit (XOR 0x08 on Status Bitmask)\n";
        std::cout << "  [4] Inspect Sanctuary Seal (Check Victory Conditions)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            g_ManaPool -= 6.25f;
            g_SoulEssence += 1.50;
            std::cout << ">> Cast Arcane Bolt! (Scan for Decreased Float in Cheat Engine)\n";
        } else if (choice == 2) {
            g_ShieldDurability -= 5;
            std::cout << ">> Blocked strike! (Scan for 2-Byte Short in Cheat Engine)\n";
        } else if (choice == 3) {
            g_StatusBitmask ^= FLAG_BURNING;
            std::cout << ">> Toggled Burning bit! Status byte is now " << (int)g_StatusBitmask << "\n";
        } else if (choice == 4) {
            bool manaOk   = (g_ManaPool >= 500.0f);
            bool shieldOk = (g_ShieldDurability >= 1000);
            bool maskOk   = (g_StatusBitmask == FLAG_DIVINE_BLESSING); // 0x80 (128)

            if (manaOk && shieldOk && maskOk) {
                std::cout << "\n********************************************************************\n";
                std::cout << "  [QUEST COMPLETE - TIER F CLEARED!]\n";
                std::cout << "  You mastered IEEE-754 Floats, 16-bit Shorts, and Bitmask Bytes!\n";
                std::cout << "  Next Step: Proceed to Lab 03 (2D Arrays & Contiguous Structs).\n";
                std::cout << "********************************************************************\n";
                break;
            } else {
                std::cout << "\n>> [SEAL LOCKED] Remaining requirements:\n";
                if (!manaOk)   std::cout << "   - Float Mana Pool must be >= 500.0 (Current: " << g_ManaPool << ")\n";
                if (!shieldOk) std::cout << "   - 2-Byte Shield Durability must be >= 1000 (Current: " << g_ShieldDurability << ")\n";
                if (!maskOk)   std::cout << "   - 1-Byte Status Bitmask must equal 0x80 (128 decimal) [DIVINE_BLESSING only]\n";
            }
        }
    }
    return 0;
}
