// ============================================================================
// [Lab 13] Strings in Memory - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab13_strings.cpp (the target) and check/lab13_selftest.cpp (CTest).
// char16_t (always 2 bytes) is used on purpose: wchar_t is 2 bytes on Windows but 4 on Linux.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab13
{

struct NameCard
{
    char16_t heroName[16];  // +0x00  UTF-16LE, zero-terminated, 32 bytes
    std::uint8_t tagLength; // +0x20  length prefix: the game reads exactly this many tag letters
    char guildTag[7];       // +0x21  ASCII letters
};

static_assert(sizeof(char16_t) == 2, "char16_t must be 2 bytes");
static_assert(offsetof(NameCard, heroName) == 0x00, "heroName offset");
static_assert(offsetof(NameCard, tagLength) == 0x20, "tagLength offset");
static_assert(offsetof(NameCard, guildTag) == 0x21, "guildTag offset");
static_assert(sizeof(NameCard) == 0x28, "NameCard size");

// Hall of Legends requirements: hero name DRAGONSLAYER (12 letters; the game only allows 8),
// guild tag DOJO (4 letters; the game only allows 3).
constexpr char16_t kNameGoal[] = u"DRAGONSLAYER";
constexpr char kTagGoal[] = "DOJO";
constexpr std::size_t kMaxNameInGame = 8;
constexpr std::size_t kMaxTagInGame = 3;

inline NameCard g_Card = {u"Apprentice", 3, "NEW"};

inline bool NameIs(const NameCard& c, const char16_t* goal)
{
    for (std::size_t i = 0; i < 16; ++i)
    {
        if (c.heroName[i] != goal[i])
        {
            return false;
        }
        if (goal[i] == 0)
        {
            return true;
        }
    }
    return false;
}

inline bool CheckWin(const NameCard& c)
{
    const std::size_t tagLen = sizeof(kTagGoal) - 1;
    return NameIs(c, kNameGoal) && c.tagLength == tagLen && std::memcmp(c.guildTag, kTagGoal, tagLen) == 0;
}

inline std::string NameAscii(const NameCard& c)
{
    std::string out;
    for (std::size_t i = 0; i < 16 && c.heroName[i] != 0; ++i)
    {
        out += c.heroName[i] < 0x80 ? static_cast<char>(c.heroName[i]) : '?';
    }
    return out;
}

inline std::string TagAscii(const NameCard& c)
{
    const std::size_t n = c.tagLength < sizeof(c.guildTag) ? c.tagLength : sizeof(c.guildTag);
    return std::string(c.guildTag, n);
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

// The flag mixes a neutral tag with the texts the solver wrote.
inline std::string MakeFlag(const NameCard& c)
{
    const std::string seal = "lab13|" + NameAscii(c) + "|" + TagAscii(c);
    std::ostringstream out;
    out << "FLAG{LAB13_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab13
