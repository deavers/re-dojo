// ============================================================================
// [Lab 11] Integer Widths & Signedness - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab11_integer_widths.cpp (the target) and check/lab11_selftest.cpp (CTest).
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab11
{

struct Treasury
{
    std::int8_t morale;   // +0x00  1 byte, signed   (-128 .. 127)
    std::uint8_t potions; // +0x01  1 byte, unsigned (0 .. 255)
    std::uint16_t arrows; // +0x02  2 bytes, unsigned (0 .. 65535)
    std::int64_t gold;    // +0x08  8 bytes; bytes +0x04 .. +0x07 are alignment padding
};

static_assert(offsetof(Treasury, morale) == 0x00, "morale offset");
static_assert(offsetof(Treasury, potions) == 0x01, "potions offset");
static_assert(offsetof(Treasury, arrows) == 0x02, "arrows offset");
static_assert(offsetof(Treasury, gold) == 0x08, "gold offset");
static_assert(sizeof(Treasury) == 0x10, "Treasury size");

// Cursed Vault requirements.
// Gold goal 5000000000 does not fit in 4 bytes: a 4-Byte scan will never find the right value.
constexpr std::int64_t kGoldGoal = 5'000'000'000LL;
constexpr std::uint16_t kArrowsGoal = 65535;
constexpr std::int8_t kMoraleGoal = -100;

inline Treasury g_Treasury = {12, 3, 40, 1500};

inline bool CheckWin(const Treasury& t)
{
    return t.gold >= kGoldGoal && t.arrows == kArrowsGoal && t.morale == kMoraleGoal;
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

// The flag is derived from the requirements, so it is not stored anywhere as plain text.
inline std::string MakeFlag()
{
    const std::string seal = "lab11|" + std::to_string(kGoldGoal) + "|" + std::to_string(kArrowsGoal) + "|" +
                             std::to_string(static_cast<int>(kMoraleGoal));
    std::ostringstream out;
    out << "FLAG{LAB11_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab11
