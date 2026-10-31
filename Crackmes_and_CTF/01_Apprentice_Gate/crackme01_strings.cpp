// ============================================================================
// [Crackme 01] The Apprentice Gate: Strings & Stack Strings (Tier F+ | 0.7/10)
// ============================================================================
// SKILLS LEARNED:
//   1. Finding plaintext strings in the `.rdata` section using `strings`,
//      Ghidra, or x64dbg ("Search for -> All Referenced Text Strings").
//   2. Understanding why "Stack Strings" (characters pushed onto the stack one
//      by one at runtime) hide from basic `strings` scans, and how to read them
//      in a decompiler or inspect the memory buffer at a breakpoint!
// ============================================================================

#include <iostream>
#include <string>
#include <cstring>

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 01 | TIER F+] THE APPRENTICE GATE (Strings & Stack)\n";
    std::cout << "====================================================================\n";

    // Stage 1: Classic .rdata string comparison
    std::cout << "[Stage 1/2] Enter Apprentice Passcode: ";
    std::string input1;
    std::cin >> input1;

    if (input1 != "OPEN_SESAME_x86") {
        std::cout << ">> [ACCESS DENIED] Wrong Stage 1 passcode! (Tip: Check Referenced Strings in x64dbg/Ghidra)\n";
        return 1;
    }
    std::cout << ">> [STAGE 1 CLEARED] Good! Now let's see if you can find a Stack String...\n\n";

    // Stage 2: Stack-constructed string (Does NOT appear as a contiguous string in .rdata!)
    volatile char stackSecret[14];
    stackSecret[0]  = 'S';
    stackSecret[1]  = 'T';
    stackSecret[2]  = 'A';
    stackSecret[3]  = 'C';
    stackSecret[4]  = 'K';
    stackSecret[5]  = '_';
    stackSecret[6]  = 'A';
    stackSecret[7]  = 'L';
    stackSecret[8]  = 'C';
    stackSecret[9]  = 'H';
    stackSecret[10] = 'E';
    stackSecret[11] = 'M';
    stackSecret[12] = 'Y';
    stackSecret[13] = '\0';

    std::cout << "[Stage 2/2] Enter Stack Alchemist Key: ";
    std::string input2;
    std::cin >> input2;

    bool match = (input2.size() == 13);
    for (size_t i = 0; i < 13 && match; ++i) {
        if (input2[i] != stackSecret[i]) match = false;
    }

    if (match) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 01 SOLVED - TIER F+ CLEARED!]\n";
        std::cout << "  Flag: FLAG{STACK_STRINGS_CANNOT_HIDE_FROM_GHIDRA}\n";
        std::cout << "  Next Challenge: Crackme 02 (Mathematical Serial Keygenme).\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [ACCESS DENIED] Wrong Stage 2 key! Inspect the stack frame in Ghidra/x64dbg!\n";
        return 1;
    }
}
