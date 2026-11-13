// ============================================================================
// [Lab 32] Shadow VMT - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab32_shadow_vmt.cpp (the target) and check/lab32_selftest.cpp (CTest).
// Single inheritance and NO virtual destructor: the table layout is the same on MSVC and GCC
// (vptr at +0x00 of the object, slots in declaration order, 8 bytes each on x64).
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab32
{

class IPerson
{
  public:
    virtual const char* Name() const = 0; // slot 0  (table +0x00)
    virtual int Greet() const = 0;        // slot 1  (table +0x08)
    virtual bool IsBribable() const = 0;  // slot 2  (table +0x10)
    virtual int Strength() const = 0;     // slot 3  (table +0x18)
};

constexpr std::size_t kSlots = 4;

class Guard : public IPerson
{
  public:
    Guard(std::int32_t rank, std::int32_t gold) : rank_(rank), gold_(gold)
    {
    }
    const char* Name() const override
    {
        return rank_ >= 3 ? "Captain" : "Guard";
    }
    int Greet() const override
    {
        return 10 + rank_;
    }
    bool IsBribable() const override
    {
        return false; // no guard can be bribed
    }
    int Strength() const override
    {
        return 50 + 10 * rank_;
    }

  private:
    std::int32_t rank_; // object +0x08 (after the 8-byte vptr)
    std::int32_t gold_; // object +0x0C
};

class Merchant : public IPerson
{
  public:
    const char* Name() const override
    {
        return "Merchant";
    }
    int Greet() const override
    {
        return 99;
    }
    bool IsBribable() const override
    {
        return true; // touches no member: safe to call with any object as "this"
    }
    int Strength() const override
    {
        return 5;
    }
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(sizeof(Guard) == 0x10, "Guard size: vptr + two ints");

// g_Guards[0] and [1] are guards, g_Guards[2] (object +0x20 in the array) is the Captain.
// All three share ONE table. The donor g_Merchant has a table where slot 2 returns true.
constexpr std::size_t kCaptain = 2;
inline Guard g_Guards[3] = {Guard(1, 10), Guard(1, 12), Guard(3, 40)};
inline Merchant g_Merchant;

// Calls go through a volatile pointer so the compiler cannot devirtualise them:
// the program must really read each object's vptr, exactly like a game would.
inline IPerson* volatile g_Roster[3] = {&g_Guards[0], &g_Guards[1], &g_Guards[2]};

// Win: ONLY the Captain takes the bribe. If any other guard does too, the Marshal notices.
inline bool CheckWin()
{
    return g_Roster[kCaptain]->IsBribable() && !g_Roster[0]->IsBribable() && !g_Roster[1]->IsBribable();
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
    const std::string seal = "lab32|captain-only|shadow-vmt";
    std::ostringstream out;
    out << "FLAG{LAB32_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab32
