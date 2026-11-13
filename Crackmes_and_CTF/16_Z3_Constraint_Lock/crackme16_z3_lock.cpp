// ============================================================================
// [Crackme 16] The Constraint Lock (Tier A | Difficulty: 6.6/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 10 (rule-based serials). The key is four 32-bit numbers
//   tied together by five constraints: wrap-around addition, XOR, a rotation,
//   a multiplication modulo 2^32 and a masked mix. Solving them by hand is slow;
//   describe them to an SMT solver (Z3, bit-vectors of width 32) and let it find
//   the one key that satisfies all of them.
//
// Format: XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX (four 32-bit hex numbers a-b-c-d)
// Exit codes: 0 accepted (flag printed), 1 a constraint failed, 2 wrong format,
//             3 end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <cstdio>
#include <string>

namespace
{

constexpr std::uint32_t kC1 = 0xAC6C4019U;
constexpr std::uint32_t kC2 = 0x354CDFC8U;
constexpr std::uint32_t kC3 = 0xEC0F1086U;
constexpr std::uint32_t kC4 = 0xA5A6B451U;
constexpr std::uint32_t kC5 = 0x0001EBDBU;
constexpr std::uint32_t kGolden = 0x9E3779B1U;

std::uint32_t Rotl(std::uint32_t x, int n)
{
    return (x << n) | (x >> (32 - n));
}

bool HexDigit(char c)
{
    return (c >= '0' && c <= '9') || (c >= 'A' && c <= 'F') || (c >= 'a' && c <= 'f');
}

bool ParseKey(const std::string& text, std::uint32_t out[4])
{
    if (text.size() != 35)
    {
        return false;
    }
    for (int part = 0; part < 4; ++part)
    {
        std::uint32_t v = 0;
        for (int i = 0; i < 8; ++i)
        {
            const char c = text[static_cast<std::size_t>(part * 9 + i)];
            if (!HexDigit(c))
            {
                return false;
            }
            const std::uint32_t digit = (c <= '9') ? static_cast<std::uint32_t>(c - '0')
                                                   : static_cast<std::uint32_t>((c | 0x20) - 'a' + 10);
            v = (v << 4) | digit;
        }
        if (part < 3 && text[static_cast<std::size_t>(part * 9 + 8)] != '-')
        {
            return false;
        }
        out[part] = v;
    }
    return true;
}

bool CheckKey(const std::uint32_t k[4])
{
    const std::uint32_t a = k[0], b = k[1], c = k[2], d = k[3];
    return a + b == kC1                                  // 1. wrap-around addition
           && (a ^ c) == kC2                             // 2. XOR
           && Rotl(b, 7) + d == kC3                      // 3. rotation, then addition
           && ((c * kGolden) ^ d) == kC4                 // 4. multiplication modulo 2^32, then XOR
           && (a & 0xFFFFU) * 3U + (d >> 16) == kC5;     // 5. masked mix
}

} // namespace

int main()
{
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 16 | TIER A] THE CONSTRAINT LOCK\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter the key (XXXXXXXX-XXXXXXXX-XXXXXXXX-XXXXXXXX): ";

    std::string text;
    if (!(std::cin >> text))
    {
        std::cout << "\n>> The lock stays silent.\n";
        return 3;
    }
    std::uint32_t key[4] = {};
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
    char canonical[40];
    std::snprintf(canonical, sizeof(canonical), "%08X-%08X-%08X-%08X", key[0], key[1], key[2], key[3]);
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 16 SOLVED - TIER A CLEARED!]\n";
    std::cout << "  FLAG{" << canonical << "}\n";
    std::cout << "********************************************************************\n";
    return 0;
}
