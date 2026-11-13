// ============================================================================
// [Lab 15] Fixed-Point 16.16 - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab15_fixed_point.cpp (the target) and check/lab15_selftest.cpp (CTest).
// A 16.16 fixed-point number is a 4-byte int: real value = raw / 65536.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab15
{

constexpr std::int32_t kOne = 65536; // 1.0 in 16.16

struct Starship
{
    std::int32_t fuel;   // +0x00  16.16 fixed point (raw / 65536)
    std::int32_t thrust; // +0x04  16.16 fixed point (raw / 65536)
    std::uint32_t jumps; // +0x08  plain counter
};

static_assert(offsetof(Starship, fuel) == 0x00, "fuel offset");
static_assert(offsetof(Starship, thrust) == 0x04, "thrust offset");
static_assert(offsetof(Starship, jumps) == 0x08, "jumps offset");
static_assert(sizeof(Starship) == 0x0C, "Starship size");

// Hyperjump requirements: fuel exactly 1000.0 and thrust exactly 3.25.
// In game: refuelling stops at 50.0 fuel, the thrust lever stops at 2.0.
constexpr std::int32_t kFuelGoal = 1000 * kOne;
constexpr std::int32_t kThrustGoal = 3 * kOne + kOne / 4;
constexpr std::int32_t kFuelCap = 50 * kOne;
constexpr std::int32_t kThrustCap = 2 * kOne;

inline Starship g_Ship = {12 * kOne + kOne / 2, kOne + 3 * kOne / 4, 0};

inline double ToReal(std::int32_t raw)
{
    return static_cast<double>(raw) / kOne;
}

inline bool CheckWin(const Starship& s)
{
    return s.fuel == kFuelGoal && s.thrust == kThrustGoal;
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
    const std::string seal = "lab15|fuel=1000.0|thrust=3.25";
    std::ostringstream out;
    out << "FLAG{LAB15_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab15
