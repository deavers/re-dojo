// ============================================================================
// [Crackme 10] The Checksum Serial (Tier D- | Difficulty: 2.6/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 02. A serial is accepted by RULES, not by comparing it to
//   one stored value: a check digit (the Luhn algorithm), a digit-sum rule and
//   a block derived from another block. Many serials are valid - reverse the
//   three rules and write a key generator that produces any valid one.
//
// Format: NNNN-NNNN-NNNN-NNNN (16 digits in 4 blocks)
// Exit codes: 0 accepted (flag printed), 1 a rule failed, 2 wrong format,
//             3 end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

static bool ParseSerial(const std::string& text, int digits[16])
{
    if (text.size() != 19)
    {
        return false;
    }
    int n = 0;
    for (std::size_t i = 0; i < text.size(); ++i)
    {
        const bool dashSlot = (i == 4 || i == 9 || i == 14);
        if (dashSlot)
        {
            if (text[i] != '-')
            {
                return false;
            }
        }
        else
        {
            if (text[i] < '0' || text[i] > '9')
            {
                return false;
            }
            digits[n++] = text[i] - '0';
        }
    }
    return n == 16;
}

static int Block(const int digits[16], int index)
{
    int v = 0;
    for (int i = 0; i < 4; ++i)
    {
        v = v * 10 + digits[index * 4 + i];
    }
    return v;
}

// Rule 1: the Luhn check digit over all 16 digits.
static bool LuhnOk(const int digits[16])
{
    int sum = 0;
    for (int i = 0; i < 16; ++i)
    {
        int d = digits[15 - i];
        if (i % 2 == 1)
        {
            d *= 2;
            if (d > 9)
            {
                d -= 9;
            }
        }
        sum += d;
    }
    return sum % 10 == 0;
}

// Rule 2: the digits of block 1 add up to 20.
static bool DigitSumOk(const int digits[16])
{
    return digits[0] + digits[1] + digits[2] + digits[3] == 20;
}

// Rule 3: block 3 is derived from block 1.
static bool DerivedBlockOk(const int digits[16])
{
    return Block(digits, 2) == (Block(digits, 0) * 7 + 1234) % 10000;
}

static std::string MakeFlag()
{
    const std::string seal = "cm10|luhn|sum20|b3=7*b1+1234";
    std::uint64_t h = 0xCBF29CE484222325ULL;
    for (const unsigned char c : seal)
    {
        h ^= c;
        h *= 0x100000001B3ULL;
    }
    std::ostringstream out;
    out << "FLAG{CM10_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << h << "}";
    return out.str();
}

int main()
{
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 10 | TIER D-] THE CHECKSUM SERIAL\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter serial (NNNN-NNNN-NNNN-NNNN): ";

    std::string text;
    if (!(std::cin >> text))
    {
        std::cout << "\n>> No serial entered.\n";
        return 3;
    }
    int digits[16] = {};
    if (!ParseSerial(text, digits))
    {
        std::cout << ">> [FAILED] Wrong format. Expected NNNN-NNNN-NNNN-NNNN.\n";
        return 2;
    }
    if (!LuhnOk(digits) || !DigitSumOk(digits) || !DerivedBlockOk(digits))
    {
        std::cout << ">> [FAILED] Serial rejected. More than one rule guards this door.\n";
        return 1;
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 10 SOLVED - TIER D- CLEARED!]\n";
    std::cout << "  " << MakeFlag() << "\n";
    std::cout << "  Next: write a key generator that prints a NEW valid serial every run.\n";
    std::cout << "********************************************************************\n";
    return 0;
}
