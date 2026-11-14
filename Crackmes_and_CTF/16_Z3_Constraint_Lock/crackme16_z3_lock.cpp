// ============================================================================
// [Crackme 16] The Constraint Lock (Tier A | Difficulty: 6.6/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 10 (rule-based serials). The key is four 64-bit numbers
//   tied together by five constraints with wrap-around arithmetic. Brute force
//   over 64-bit values is hopeless; describe the constraints to an SMT solver
//   (Z3, bit-vectors) and let it find the one key that satisfies all of them.
//
// Format: four 64-bit hex numbers, 16 digits each, joined by '-'
// Exit codes: 0 accepted (flag printed), 1 a constraint failed, 2 wrong format,
//             3 end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace
{

constexpr std::uint64_t kK1 = 0x8B7E0CF748717711ULL;
constexpr std::uint64_t kK2 = 0xEB7C866297A4BF22ULL;
constexpr std::uint64_t kK3 = 0x6978DCC798EA2514ULL;
constexpr std::uint64_t kK4 = 0x98EFAED7EA37181BULL;
constexpr std::uint64_t kK5 = 0x0000000137A5519BULL;
constexpr std::uint64_t kGolden = 0x9E3779B97F4A7C15ULL;
constexpr std::size_t kDigits = 16;

std::uint64_t Rotl(std::uint64_t x, int n)
{
    return (x << n) | (x >> (64 - n));
}

bool HexDigit(char c)
{
    return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'F') || (c >= 'a' && c <= 'f');
}

bool ParseKey(const std::string& text, std::uint64_t out[4])
{
    if (text.size() != 4 * kDigits + 3)
    {
        return false;
    }
    for (std::size_t part = 0; part < 4; ++part)
    {
        std::uint64_t v = 0;
        for (std::size_t i = 0; i < kDigits; ++i)
        {
            const char c = text[part * (kDigits + 1) + i];
            if (!HexDigit(c))
            {
                return false;
            }
            const std::uint64_t digit = (c <= '9') ? static_cast<std::uint64_t>(c - '0')
                                                   : static_cast<std::uint64_t>((c | 0x20) - 'a' + 10);
            v = (v << 4) | digit;
        }
        if (part < 3 && text[part * (kDigits + 1) + kDigits] != '-')
        {
            return false;
        }
        out[part] = v;
    }
    return true;
}

bool CheckKey(const std::uint64_t k[4])
{
    const std::uint64_t a = k[0], b = k[1], c = k[2], d = k[3];
    return a + b == kK1                                       // 1. wrap-around addition
           && (a ^ c) == kK2                                  // 2. XOR
           && Rotl(b, 23) + d == kK3                          // 3. rotation, then addition
           && ((c * kGolden) ^ d) == kK4                      // 4. multiplication modulo 2^64, then XOR
           && (a & 0xFFFFFFFFULL) * 3ULL + (d >> 32) == kK5;  // 5. masked mix
}

} // namespace

int main()
{
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 16 | TIER A] THE CONSTRAINT LOCK\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter the key (4 x 16 hex digits joined by '-'): ";

    std::string text;
    if (!(std::cin >> text))
    {
        std::cout << "\n>> The lock stays silent.\n";
        return 3;
    }
    std::uint64_t key[4] = {};
    if (!ParseKey(text, key))
    {
        std::cout << ">> [FAILED] Wrong format.\n";
        return 2;
    }
    if (!CheckKey(key))
    {
        std::cout << ">> [FAILED] At least one constraint does not hold. Ask a solver.\n";
        return 1;
    }
    std::ostringstream canonical;
    canonical << std::hex << std::uppercase << std::setfill('0');
    for (int i = 0; i < 4; ++i)
    {
        canonical << (i ? "-" : "") << std::setw(16) << key[i];
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 16 SOLVED - TIER A CLEARED!]\n";
    std::cout << "  FLAG{" << canonical.str() << "}\n";
    std::cout << "********************************************************************\n";
    return 0;
}
