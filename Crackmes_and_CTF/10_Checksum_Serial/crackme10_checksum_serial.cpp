// ============================================================================
// [Crackme 10] The Checksum Serial (Tier D- | Difficulty: 2.6/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 02. A serial is accepted by RULES, not by comparing it to
//   one stored value. Every run asks for a serial that contains a fresh random
//   block, so a single found serial is useless: reverse the rules and write a
//   key generator.
//
// Format: DOJO-AAAA-BBBB-CCCC-D (BBBB = the block printed by this run)
// Exit codes: 0 accepted (flag printed), 1 a rule failed, 2 wrong format,
//             3 end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#include <random>
#include <sstream>
#include <string>

static bool ParseSerial(const std::string& text, int digits[13])
{
    if (text.size() != 21 || text.compare(0, 5, "DOJO-") != 0)
    {
        return false;
    }
    int n = 0;
    for (std::size_t i = 5; i < text.size(); ++i)
    {
        const bool dashSlot = (i == 9 || i == 14 || i == 19);
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
    return n == 13;
}

static int Block(const int digits[13], int index)
{
    int v = 0;
    for (int i = 0; i < 4; ++i)
    {
        v = v * 10 + digits[index * 4 + i];
    }
    return v;
}

static bool LuhnOk(const int digits[13])
{
    int sum = 0;
    for (int i = 0; i < 13; ++i)
    {
        int d = digits[12 - i];
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

static bool RulesOk(const int digits[13], int challenge)
{
    const int a = Block(digits, 0);
    const int b = Block(digits, 1);
    const int c = Block(digits, 2);
    const bool blockB = (b == challenge);
    const bool digitSum = digits[0] + digits[1] + digits[2] + digits[3] == 20;
    const bool derived = (c == (a * 7 + b * 3 + 1234) % 10000);
    return blockB && digitSum && derived && LuhnOk(digits);
}

// The flag mixes a neutral tag with the accepted serial.
static std::string MakeFlag(const std::string& serial)
{
    std::uint64_t h = 0xCBF29CE484222325ULL;
    for (const unsigned char ch : "cm10|" + serial)
    {
        h ^= ch;
        h *= 0x100000001B3ULL;
    }
    std::ostringstream out;
    out << "FLAG{CM10_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << h << "}";
    return out.str();
}

int main()
{
    std::random_device rd;
    const int challenge = static_cast<int>(rd() % 10000);
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 10 | TIER D-] THE CHECKSUM SERIAL\n";
    std::cout << "====================================================================\n";
    std::cout << "CHALLENGE: " << std::setw(4) << std::setfill('0') << challenge << std::setfill(' ') << std::endl;
    std::cout << "Enter a serial DOJO-AAAA-BBBB-CCCC-D whose second block is the challenge: " << std::flush;

    std::string text;
    if (!(std::cin >> text))
    {
        std::cout << "\n>> No serial entered.\n";
        return 3;
    }
    int digits[13] = {};
    if (!ParseSerial(text, digits))
    {
        std::cout << ">> [FAILED] Wrong format. Expected DOJO-AAAA-BBBB-CCCC-D.\n";
        return 2;
    }
    if (!RulesOk(digits, challenge))
    {
        std::cout << ">> [FAILED] Serial rejected. More than one rule guards this door.\n";
        return 1;
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 10 SOLVED - TIER D- CLEARED!]\n";
    std::cout << "  " << MakeFlag(text) << "\n";
    std::cout << "********************************************************************\n";
    return 0;
}
