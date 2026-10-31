// ============================================================================
// [Lab 05] Assembly NOP Patching & Code Injection (Tier E+ | Diff: 2.3/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 04. What happens when a game checks if you modified a value
//   or drains your stamina inside the instruction itself?
//   Instead of scanning & freezing data, you attach a debugger ("Find out what
//   writes to this address"), NOP the instruction that subtracts ammo/stamina,
//   and write an Auto Assembler code cave (`alloc` / `jmp`) to multiply XP!
//
// QUEST OBJECTIVES:
//   1. Prevent `ConsumeStamina()` from subtracting 30 Stamina when attacking.
//   2. Inject code into `GainExperience()` or patch it so you reach 100,000 XP!
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

#if defined(_MSC_VER)
#define NOINLINE __declspec(noinline)
#else
#define NOINLINE __attribute__((noinline))
#endif

struct Duelist {
    int32_t stamina;    // +0x00
    int32_t maxStamina; // +0x04
    int32_t experience; // +0x08
    int32_t rankGoal;   // +0x0C
};

Duelist g_Duelist = { 100, 100, 0, 100000 };
bool    g_Blind   = false;

// Separate noinline functions so they appear as crystal-clear assembly routines
NOINLINE void ConsumeStamina(Duelist* d) {
    // TARGET INSTRUCTION 1: NOP this subtraction in Cheat Engine / x64dbg!
    d->stamina -= 30;
}

NOINLINE void GainExperience(Duelist* d) {
    // TARGET INSTRUCTION 2: Code-inject here to add 50,000 XP instead of 5!
    d->experience += 5;
}

int main() {
    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Function & Struct Addresses)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_Blind = (mode == 2);

    while (g_Duelist.experience < g_Duelist.rankGoal) {
        // Anti-Freeze Sanity Check: if someone freezes stamina > 100, clamp it!
        if (g_Duelist.stamina > g_Duelist.maxStamina) {
            std::cout << ">> [SANITY CHECK] Stamina exceeded maxStamina (100)! Clamping back to 100.\n";
            g_Duelist.stamina = g_Duelist.maxStamina;
        }

        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 05 | TIER E+] ARENA OF CODE CAVES (NOP & Auto Assembler)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Stamina    : " << g_Duelist.stamina << " / " << g_Duelist.maxStamina << "\n";
        std::cout << "  Experience : " << g_Duelist.experience << " / " << g_Duelist.rankGoal << " XP\n";
        if (!g_Blind) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  &g_Duelist.stamina    : 0x" << std::hex << (uintptr_t)&g_Duelist.stamina << "\n";
            std::cout << "  &g_Duelist.experience : 0x" << (uintptr_t)&g_Duelist.experience << "\n";
            std::cout << "  fn ConsumeStamina()   : 0x" << (uintptr_t)&ConsumeStamina << "\n";
            std::cout << "  fn GainExperience()   : 0x" << (uintptr_t)&GainExperience << std::dec << "\n";
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Perform Heavy Slash (-30 Stamina, +5 EXP)\n";
        std::cout << "  [2] Rest at Campfire    (+10 Stamina)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            if (g_Duelist.stamina >= 30) {
                ConsumeStamina(&g_Duelist);
                GainExperience(&g_Duelist);
                std::cout << ">> Performed Heavy Slash! Stamina is now " << g_Duelist.stamina
                          << ", EXP is now " << g_Duelist.experience << "\n";
            } else {
                std::cout << ">> [EXHAUSTED!] Not enough Stamina! NOP ConsumeStamina() in Disassembler!\n";
            }
        } else if (choice == 2) {
            g_Duelist.stamina += 10;
            if (g_Duelist.stamina > g_Duelist.maxStamina) g_Duelist.stamina = g_Duelist.maxStamina;
            std::cout << ">> Rested (+10 Stamina).\n";
        }
    }

    if (g_Duelist.experience >= g_Duelist.rankGoal) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [QUEST COMPLETE - TIER E+ CLEARED!]\n";
        std::cout << "  You mastered Hardware Breakpoints, NOPs, and Code Injection!\n";
        std::cout << "  Next Step: Proceed to Lab 06 (Shared Engine Code & Boss Fight).\n";
        std::cout << "********************************************************************\n";
    }
    return 0;
}
