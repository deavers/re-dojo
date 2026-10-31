// ============================================================================
// [Crackme 02] The Mathematical Lock: Keygenme (Tier E | Difficulty: 1.9/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 01. Instead of comparing against a hardcoded string, real
//   software serial checks verify mathematical relationships between blocks of
//   your serial key (`AAAA-BBBB-CCCC`).
//   Reverse the arithmetic in Ghidra/IDA and write a Keygen script that can
//   generate valid serials!
// ============================================================================

#include <iostream>
#include <cstdio>
#include <cstdint>

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

NOINLINE bool ValidateSerialKey(int a, int b, int c) {
    // 1. Range check: each block must be a 4-digit number (1000..9999)
    if (a < 1000 || a > 9999 || b < 1000 || b > 9999 || c < 1000 || c > 9999) {
        return false;
    }
    // 2. Constraint 1: Sum of Block A and Block B must equal 10000
    if ((a + b) != 10000) {
        return false;
    }
    // 3. Constraint 2: Bitwise XOR of Block A and Block B must equal 9984 (0x2700)
    //    (e.g. A = 1664, B = 8336 -> 1664 + 8336 = 10000, 1664 ^ 8336 = 9984)
    if ((a ^ b) != 9984) {
        return false;
    }
    // 4. Constraint 3: Block C is derived from A and B
    int expectedC = ((a * 3) + (b ^ 0x1234)) % 9000 + 1000;
    return (c == expectedC);
}

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 02 | TIER E] THE MATHEMATICAL LOCK (Serial Keygenme)\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter Product Serial Key (Format: AAAA-BBBB-CCCC): ";

    int a = 0, b = 0, c = 0;
    if (std::scanf("%d-%d-%d", &a, &b, &c) != 3) {
        std::cout << ">> [INVALID FORMAT] Please use 4-digit blocks: 1234-5678-9012\n";
        return 1;
    }

    if (ValidateSerialKey(a, b, c)) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 02 SOLVED - TIER E CLEARED!]\n";
        std::cout << "  Valid Serial Accepted: " << a << "-" << b << "-" << c << "\n";
        std::cout << "  Next Challenge: Crackme 03 (XOR & Bit-Rotation Cipher).\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [SERIAL REJECTED] Analyze ValidateSerialKey() in Ghidra and write a Keygen!\n";
        return 1;
    }
}
