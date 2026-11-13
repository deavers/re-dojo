// ============================================================================
// [Lab 16] Array of Structs & Stride - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab16_array_of_structs.cpp (the target) and check/lab16_selftest.cpp (CTest).
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab16
{

constexpr std::uint32_t kAlive = 0x1; // flags bit 0

struct Unit
{
    std::uint32_t id;    // +0x00
    std::int32_t hp;     // +0x04
    std::int32_t maxHp;  // +0x08
    float x;             // +0x0C
    float y;             // +0x10
    std::uint32_t flags; // +0x14  bit 0 = alive
};

constexpr std::size_t kSquadSize = 8;

struct Squad
{
    Unit units[kSquadSize]; // element i starts at +0x18 * i (the stride)
};

static_assert(offsetof(Unit, hp) == 0x04, "hp offset");
static_assert(offsetof(Unit, maxHp) == 0x08, "maxHp offset");
static_assert(offsetof(Unit, flags) == 0x14, "flags offset");
static_assert(sizeof(Unit) == 0x18, "Unit stride");
static_assert(sizeof(Squad) == 0xC0, "Squad size");

// March requirements: every one of the 8 units has hp >= 500 and is alive.
// In game, healing stops at maxHp (at most 120) and a fallen unit cannot be revived.
constexpr std::int32_t kHpGoal = 500;

inline Squad g_Squad = {{
    {101, 80, 100, 1.0f, 2.0f, kAlive},
    {102, 95, 110, 2.0f, 2.0f, kAlive},
    {103, 60, 90, 3.0f, 2.0f, kAlive},
    {104, 120, 120, 4.0f, 2.0f, kAlive},
    {105, 45, 100, 1.0f, 3.0f, kAlive},
    {106, 0, 105, 2.0f, 3.0f, 0}, // fallen
    {107, 70, 95, 3.0f, 3.0f, kAlive},
    {108, 88, 100, 4.0f, 3.0f, kAlive},
}};

inline bool CheckWin(const Squad& s)
{
    for (const Unit& u : s.units)
    {
        if (u.hp < kHpGoal || (u.flags & kAlive) == 0)
        {
            return false;
        }
    }
    return true;
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
    const std::string seal = "lab16|squad=8|hp>=500|alive";
    std::ostringstream out;
    out << "FLAG{LAB16_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab16
