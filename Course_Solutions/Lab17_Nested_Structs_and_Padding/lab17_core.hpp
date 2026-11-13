// ============================================================================
// [Lab 17] Nested Structs & Padding - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab17_nested_padding.cpp (the target) and check/lab17_selftest.cpp (CTest).
// Offsets below are relative to the start of g_Hero.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab17
{

struct Stats
{
    std::uint8_t level;    // Stats +0x00
    std::int32_t strength; // Stats +0x04  (3 padding bytes before it)
    std::uint16_t agility; // Stats +0x08
    double crit;           // Stats +0x10  (6 padding bytes before it: a double is 8-aligned)
};

struct Armor
{
    std::uint8_t tier;        // Armor +0x00
    std::uint16_t durability; // Armor +0x02  (1 padding byte before it)
    std::uint32_t enchant;    // Armor +0x04
};

#pragma pack(push, 1)
struct PackedLoot
{
    std::uint8_t rarity;     // Loot +0x00
    std::uint32_t goldValue; // Loot +0x01  (packed: NO padding, the int is unaligned)
    std::uint16_t quantity;  // Loot +0x05
};
#pragma pack(pop)

struct Hero
{
    std::uint32_t id; // Hero +0x00
    Stats stats;      // Hero +0x08  (8-aligned because of the double inside)
    Armor armor;      // Hero +0x20
    PackedLoot loot;  // Hero +0x28
};

static_assert(offsetof(Stats, crit) == 0x10, "Stats.crit offset");
static_assert(sizeof(Stats) == 0x18, "Stats size");
static_assert(offsetof(Armor, durability) == 0x02, "Armor.durability offset");
static_assert(sizeof(Armor) == 0x08, "Armor size");
static_assert(offsetof(PackedLoot, goldValue) == 0x01, "PackedLoot.goldValue offset");
static_assert(sizeof(PackedLoot) == 0x07, "PackedLoot size");
static_assert(offsetof(Hero, stats) == 0x08, "Hero.stats offset");
static_assert(offsetof(Hero, armor) == 0x20, "Hero.armor offset");
static_assert(offsetof(Hero, loot) == 0x28, "Hero.loot offset");
static_assert(sizeof(Hero) == 0x30, "Hero size");
// Absolute offsets inside g_Hero: crit +0x18, durability +0x22, loot gold +0x29.

// Legend requirements: crit >= 1.0 (training stops at 0.5), armor durability exactly 9999 (repairs stop
// at 2000), loot gold value exactly 1000000 (the appraiser never changes it).
constexpr double kCritGoal = 1.0;
constexpr std::uint16_t kDurabilityGoal = 9999;
constexpr std::uint32_t kLootGoal = 1000000;
constexpr double kCritCap = 0.5;
constexpr std::uint16_t kDurabilityCap = 2000;

inline Hero g_Hero = {7, {3, 14, 9, 0.05}, {2, 640, 0}, {1, 120, 2}};

inline bool CheckWin(const Hero& h)
{
    const std::uint32_t lootGold = h.loot.goldValue; // read through the packed member, never by pointer
    return h.stats.crit >= kCritGoal && h.armor.durability == kDurabilityGoal && lootGold == kLootGoal;
}

inline std::uint64_t Fnv1a64(const std::string& text)
{
    std::uint64_t h = 0xCBF29CE484222325ULL;
    for (const unsigned char c : text)
    {
        h ^= c;
        h *= 0x100000001B3ULL;
    }
    return h;
}

inline std::string MakeFlag()
{
    const std::string seal = "lab17|crit>=1.0|durability=9999|loot=1000000";
    std::ostringstream out;
    out << "FLAG{LAB17_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab17
