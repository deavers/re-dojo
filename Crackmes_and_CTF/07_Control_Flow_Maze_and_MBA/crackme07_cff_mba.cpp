// ============================================================================
// [Crackme 07] O-LLVM Control-Flow Flattening & MBA (Tier S | Diff: 7.8/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 06. Modern obfuscators (Obfuscator-LLVM, Arxan, Denuvo)
//   use two mathematical weapons to break Ghidra/IDA decompilers:
//     1. Control-Flow Flattening (CFF): Breaking basic blocks into a giant
//        state-machine switch loop (`while (state != EXIT)`).
//     2. Mixed Boolean-Arithmetic (MBA): Replacing simple `x + y` or `x ^ y`
//        with complex bitwise identities like `(x ^ y) + 2 * (x & y)`!
//
// MBA IDENTITIES USED IN THIS CHALLENGE:
//   - Identity 1: (x ^ y) + 2 * (x & y)         === x + y
//   - Identity 2: (x | y) - (x & y)             === x ^ y
//   - Identity 3: (x + y) - ((x ^ y) >> 1) * 2  === x & y
// ============================================================================

#include <iostream>
#include <cstdio>
#include <cstdint>

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

// Obfuscated MBA equivalent of (x + y)
NOINLINE uint32_t MBA_Add(uint32_t x, uint32_t y) {
    return (x ^ y) + 2U * (x & y);
}

// Obfuscated MBA equivalent of (x ^ y)
NOINLINE uint32_t MBA_Xor(uint32_t x, uint32_t y) {
    return (x | y) - (x & y);
}

// Control-Flow Flattened verification machine
NOINLINE bool VerifyFlattenedDispatcher(uint32_t k0, uint32_t k1) {
    uint32_t state  = 0x91A2B3C4U;
    bool     result = false;

    while (state != 0x00000000U) {
        switch (state) {
            case 0x91A2B3C4U: {
                // Step 1: Check if MBA_Add(k0, k1) == 5000 (i.e. k0 + k1 == 5000)
                uint32_t sum = MBA_Add(k0, k1);
                state = (sum == 5000U) ? 0x33445566U : 0xDEAD0001U;
                break;
            }
            case 0x33445566U: {
                // Step 2: Check if MBA_Xor(k0, k1) == 4280 (i.e. k0 ^ k1 == 4280)
                // Note: 1337 + 3663 = 5000, and 1337 ^ 3663 = 4280!
                uint32_t xval = MBA_Xor(k0, k1);
                state = (xval == 4280U) ? 0x778899AAU : 0xDEAD0001U;
                break;
            }
            case 0x778899AAU: {
                // Step 3: Ensure k0 < k1 (so k0 = 1337, k1 = 3663)
                state = (k0 < k1) ? 0xCAFE0000U : 0xDEAD0001U;
                break;
            }
            case 0xCAFE0000U: {
                result = true;
                state  = 0x00000000U;
                break;
            }
            case 0xDEAD0001U:
            default: {
                result = false;
                state  = 0x00000000U;
                break;
            }
        }
    }
    return result;
}

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 07 | TIER S] LABYRINTH OF O-LLVM (CFF & MBA Obfuscation)\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter Dual Numerical Keys (Format: K0-K1, e.g. 1111-2222): ";

    uint32_t k0 = 0, k1 = 0;
    if (std::scanf("%u-%u", &k0, &k1) != 2) {
        std::cout << ">> [ERROR] Invalid format.\n";
        return 1;
    }

    if (VerifyFlattenedDispatcher(k0, k1)) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 07 SOLVED - TIER S CLEARED!]\n";
        std::cout << "  You simplified Mixed Boolean-Arithmetic & deflattened the CFG!\n";
        std::cout << "  Flag: FLAG{MBA_SIMPLIFIED_" << k0 << "_" << k1 << "}\n";
        std::cout << "  Next Challenge: Crackme 08 (Z3 / angr Symbolic Execution Vault).\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [ACCESS DENIED] Simplify MBA_Add and MBA_Xor to solve for K0 and K1!\n";
        return 1;
    }
}
