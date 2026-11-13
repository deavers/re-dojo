// ============================================================================
// [Lab 12] Double & Fuzzy Scans - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab12_double_fuzzy.cpp (the target) and check/lab12_selftest.cpp (CTest).
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab12
{

struct Alchemy
{
    double essence;       // +0x00  8-byte IEEE-754 double, shown rounded to 1 decimal
    float catalystPurity; // +0x08  4-byte IEEE-754 float, shown as a rounded percent
    std::int32_t brews;   // +0x0C  4-byte int
};

static_assert(offsetof(Alchemy, essence) == 0x00, "essence offset");
static_assert(offsetof(Alchemy, catalystPurity) == 0x08, "catalystPurity offset");
static_assert(offsetof(Alchemy, brews) == 0x0C, "brews offset");
static_assert(sizeof(Alchemy) == 0x10, "Alchemy size");

// Philosopher's Stone requirements: essence >= 1 million, purity >= 0.999 (99.9 %).
// In-game filtering stops at 95 % purity, so purity needs a memory edit.
constexpr double kEssenceGoal = 1000000.0;
constexpr float kPurityGoal = 0.999f;
constexpr float kPurityCap = 0.95f;

inline Alchemy g_Alchemy = {12.7531, 0.4137f, 0};

inline bool CheckWin(const Alchemy& a)
{
    return a.essence >= kEssenceGoal && a.catalystPurity >= kPurityGoal;
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
    const std::string seal = "lab12|essence>=1000000|purity>=0.999";
    std::ostringstream out;
    out << "FLAG{LAB12_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab12
