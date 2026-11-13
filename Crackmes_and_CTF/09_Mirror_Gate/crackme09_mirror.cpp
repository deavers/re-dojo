// ============================================================================
// [Crackme 09] The Mirror Gate (Tier E-- | Difficulty: 0.9/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 01. The password is no longer a plain string: it is stored
//   after a simple, reversible transformation (the text is mirrored, then every
//   byte is shifted). Find the comparison loop in Ghidra / x64dbg, recognise the
//   transformation and invert it - by hand or with a few lines of Python.
//
// Exit codes: 0 gate opened (flag printed), 1 wrong password, 2 wrong length,
//             3 end of input.
// ============================================================================

#include <iostream>
#include <cstddef>
#include <cstdint>
#include <string>

// The password, mirrored and shifted. It is never stored as readable text.
static const std::uint8_t kEncoded[13] = {
    0x56, 0x56, 0x44, 0x4F, 0x4A, 0x62, 0x49, 0x52, 0x62, 0x52, 0x4B, 0x46, 0x48,
};
static const std::uint8_t kShift = 3;

static bool CheckPassword(const std::string& input)
{
    const std::size_t n = sizeof(kEncoded);
    for (std::size_t i = 0; i < n; ++i)
    {
        // Character i of the mirrored input, shifted, must match the stored byte.
        const std::uint8_t mirrored = static_cast<std::uint8_t>(input[n - 1 - i]);
        if (static_cast<std::uint8_t>(mirrored + kShift) != kEncoded[i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 09 | TIER E--] THE MIRROR GATE\n";
    std::cout << "====================================================================\n";
    std::cout << "The gate shows your reflection. Speak the password: ";

    std::string input;
    if (!(std::cin >> input))
    {
        std::cout << "\n>> Silence. The gate stays shut.\n";
        return 3;
    }
    if (input.size() != sizeof(kEncoded))
    {
        std::cout << ">> [FAILED] The reflection does not match in length.\n";
        return 2;
    }
    if (!CheckPassword(input))
    {
        std::cout << ">> [FAILED] The mirror cracks. Look at how the stored bytes are compared.\n";
        return 1;
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 09 SOLVED - TIER E-- CLEARED!]\n";
    std::cout << "  FLAG{" << input << "}\n";
    std::cout << "********************************************************************\n";
    return 0;
}
