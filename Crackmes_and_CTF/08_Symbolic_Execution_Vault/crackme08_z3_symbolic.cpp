// ============================================================================
// [Crackme 08] The Symbolic Execution Vault: Z3 & angr (Tier SSS- | 9.2/10)
// ============================================================================
// SKILLS LEARNED:
//   The Grand Finale of `Crackmes_and_CTF/`!
//   When a binary checks 8+ coupled algebraic/bitwise equations across all
//   characters of an input key simultaneously, solving by hand takes hours and
//   brute-forcing $256^8$ takes centuries.
//   By translating these 8 constraints into the **Z3 Theorem Prover** (SMT
//   solver) or running **angr**, the exact ASCII key is found in 0.02 seconds!
// ============================================================================

#include <iostream>
#include <string>
#include <cstdint>

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

// Target 8-byte ASCII key solved by Z3: "Z3_MAGE!"
// ASCII codes:
//   s[0] = 'Z' (90)
//   s[1] = '3' (51)
//   s[2] = '_' (95)
//   s[3] = 'M' (77)
//   s[4] = 'A' (65)
//   s[5] = 'G' (71)
//   s[6] = 'E' (69)
//   s[7] = '!' (33)
NOINLINE bool VerifySymbolicConstraints(const std::string& s) {
    if (s.size() != 8) return false;

    uint32_t b0 = static_cast<uint8_t>(s[0]);
    uint32_t b1 = static_cast<uint8_t>(s[1]);
    uint32_t b2 = static_cast<uint8_t>(s[2]);
    uint32_t b3 = static_cast<uint8_t>(s[3]);
    uint32_t b4 = static_cast<uint8_t>(s[4]);
    uint32_t b5 = static_cast<uint8_t>(s[5]);
    uint32_t b6 = static_cast<uint8_t>(s[6]);
    uint32_t b7 = static_cast<uint8_t>(s[7]);

    // Coupled System of 8 SMT Constraints:
    bool c0 = (b0 + b1 == 141);               // 90 + 51 = 141
    bool c1 = ((b0 ^ b1) == 105);             // 90 ^ 51 = 105
    bool c2 = (b2 - b1 == 44);                // 95 - 51 = 44
    bool c3 = (b2 + b3 == 172);               // 95 + 77 = 172
    bool c4 = ((b3 ^ b4) == 12);              // 77 ^ 65 = 12
    bool c5 = (b4 * 2 - b5 == 59);            // 130 - 71 = 59
    bool c6 = (b5 + b6 == 140);               // 71 + 69 = 140
    bool c7 = ((b5 ^ b6) == 2);               // 71 ^ 69 = 2
    bool c8 = (b6 - b7 == 36);                // 69 - 33 = 36
    bool c9 = (b0 + b4 + b7 == 188);          // 90 + 65 + 33 = 188

    return c0 && c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
}

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 08 | TIER SSS-] THE SYMBOLIC VAULT (Z3 SMT Solver Lab)\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter the 8-character Symbolic Master Key: ";

    std::string key;
    std::cin >> key;

    if (VerifySymbolicConstraints(key)) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 08 SOLVED - TIER SSS- CLEARED!]\n";
        std::cout << "  You conquered the Symbolic Execution Vault with SMT Solving!\n";
        std::cout << "  Master Flag: FLAG{SMT_SOLVER_" << key << "}\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [VAULT LOCKED] Constraint system unsatisfied!\n";
        std::cout << "   Model `VerifySymbolicConstraints` in Python Z3 (`BitVec('b0', 32)`) to solve!\n";
        return 1;
    }
}
