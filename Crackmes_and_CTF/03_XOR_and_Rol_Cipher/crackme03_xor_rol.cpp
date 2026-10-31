// ============================================================================
// [Crackme 03] XOR & Bitwise Rotation Cipher (Tier D | Difficulty: 3.1/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 02. Teaches how to recognize bitwise rotation idioms
//   (`ROL` / `ROR`: `(x << n) | (x >> (8 - n))`) and position-dependent XOR
//   keys in disassembled loops, and how to invert the transformation in Python.
// ============================================================================

#include <iostream>
#include <string>
#include <cstdint>

static inline uint8_t Rol8(uint8_t val, int shift) {
    shift &= 7;
    return static_cast<uint8_t>((val << shift) | (val >> (8 - shift)));
}

// Target encrypted bytes corresponding to the 20-character ASCII flag:
// "BITWISE_ALCHEMIST_99"
// Formula per index i: target[i] = Rol8(input[i] ^ ((0x5A + i * 7) & 0xFF), 3)
static const uint8_t kEncryptedTarget[20] = {
    0xC0, 0x41, 0xE1, 0xC1, 0xF9, 0x71, 0x0E, 0xA6, 0x9E, 0xAE,
    0x1F, 0x7F, 0x5F, 0xC7, 0xAF, 0x84, 0xF4, 0x74, 0x0F, 0x37
};

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 03 | TIER D] THE ALCHEMIST'S CIPHER (XOR + ROL8 Loop)\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter the 20-character Decryption Rune: ";

    std::string input;
    std::cin >> input;

    if (input.size() != 20) {
        std::cout << ">> [FAILED] Input must be exactly 20 characters long!\n";
        return 1;
    }

    for (size_t i = 0; i < 20; ++i) {
        uint8_t keyByte = static_cast<uint8_t>(0x5A + i * 7);
        uint8_t xored   = static_cast<uint8_t>(input[i]) ^ keyByte;
        uint8_t rotated = Rol8(xored, 3);
        if (rotated != kEncryptedTarget[i]) {
            std::cout << ">> [FAILED] Mismatch at byte index " << i
                      << "! Reverse the Rol8 + XOR loop in Ghidra!\n";
            return 1;
        }
    }

    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 03 SOLVED - TIER D CLEARED!]\n";
    std::cout << "  Decrypted Rune Verified: FLAG{" << input << "}\n";
    std::cout << "  Next Challenge: Crackme 04 (Binary License File Format RE).\n";
    std::cout << "********************************************************************\n";
    return 0;
}
