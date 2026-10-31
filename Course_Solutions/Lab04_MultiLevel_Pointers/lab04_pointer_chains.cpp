// ============================================================================
// [Lab 04] Dynamic Heap & Multi-Level Pointer Chains (Tier E | Diff: 1.8/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 03. Why do Cheat Engine beginners lose their addresses every
//   time a new level loads? Because modern engines allocate objects on the HEAP
//   using `new` / `malloc`!
//   To survive level transitions, you must trace the Multi-Level Pointer Chain
//   back to a static module base address (`g_WorldManager`).
//
// POINTER CHAIN ARCHITECTURE:
//   [g_WorldManager] -> +0x10 (ActiveFloor*) -> +0x18 (HeroActor*) -> +0x0C (HP)
//                                                                 -> +0x10 (Attack)
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>
#include <cstdlib>

struct HeroActor {
    uint64_t actorId;       // +0x00
    int32_t  stamina;       // +0x08
    int32_t  health;        // +0x0C  <-- Target Offset +0x0C
    int32_t  attackDamage;  // +0x10  <-- Target Offset +0x10
    int32_t  keys;          // +0x14
};

struct ActiveFloor {
    int32_t    floorNumber; // +0x00
    int32_t    guardianHP;  // +0x04
    uint64_t   reserved[2]; // +0x08 .. +0x17 padding
    HeroActor* pHero;       // +0x18  <-- 2nd Pointer Indirection (+0x18)
};

struct WorldManager {
    uint64_t     engineVersion; // +0x00
    uint64_t     tickCount;     // +0x08
    ActiveFloor* pCurrentFloor; // +0x10  <-- 1st Pointer Indirection (+0x10)
};

// Static root pointer stored in the binary's .data section
WorldManager* g_WorldManager = nullptr;
bool          g_BlindMode    = false;

void ReallocateFloor(int newFloorNum, int carryHP, int carryAtk) {
    if (g_WorldManager->pCurrentFloor) {
        delete g_WorldManager->pCurrentFloor->pHero;
        delete g_WorldManager->pCurrentFloor;
    }
    // Allocate fresh padding blocks to ensure heap address changes every floor!
    volatile void* heapShuffle = std::malloc(64 + (newFloorNum * 32));
    (void)heapShuffle;

    ActiveFloor* floor = new ActiveFloor();
    floor->floorNumber = newFloorNum;
    floor->guardianHP  = newFloorNum * 400;
    floor->pHero       = new HeroActor{ 0xBEEF0000ULL + newFloorNum, 100, carryHP, carryAtk, 1 };
    g_WorldManager->pCurrentFloor = floor;
}

int main() {
    g_WorldManager = new WorldManager{ 0x20261031ULL, 0, nullptr };
    ReallocateFloor(1, 100, 25);

    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Pointer Offsets)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    g_BlindMode = (mode == 2);

    while (true) {
        ActiveFloor* fl = g_WorldManager->pCurrentFloor;
        HeroActor*   hr = fl->pHero;

        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 04 | TIER E] TOWER OF SHIFTING HEAPS (Multi-Level Pointers)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Current Dungeon Floor : " << fl->floorNumber << " / 5\n";
        std::cout << "  Floor Guardian HP     : " << fl->guardianHP << "\n";
        std::cout << "  Hero Health           : " << hr->health << "   (Heap Addr: 0x"
                  << std::hex << std::uppercase << (uintptr_t)&hr->health << std::dec << ")\n";
        std::cout << "  Hero Attack Damage    : " << hr->attackDamage << "   (Heap Addr: 0x"
                  << std::hex << std::uppercase << (uintptr_t)&hr->attackDamage << std::dec << ")\n";

        if (!g_BlindMode) {
            std::cout << "--------------------------------------------------------------------\n";
            std::cout << "  [POINTER CHAIN BLUEPRINT]\n";
            std::cout << "  Static &g_WorldManager : 0x" << std::hex << (uintptr_t)&g_WorldManager << "\n";
            std::cout << "   -> [+0x10] pCurrentFloor : 0x" << (uintptr_t)fl << "\n";
            std::cout << "   -> [+0x18] pHero         : 0x" << (uintptr_t)hr << "\n";
            std::cout << "   -> [+0x0C] Hero->health  : 0x" << (uintptr_t)&hr->health << std::dec << "\n";
        }
        std::cout << "====================================================================\n";
        std::cout << "Actions:\n";
        std::cout << "  [1] Strike Floor Guardian (Deals " << hr->attackDamage << " DMG, Guardian hits back for 45)\n";
        std::cout << "  [2] Ascend to Next Floor  (REALLOCATES Hero on Heap! Raw addresses break!)\n";
        std::cout << "  [0] Exit Lab\n> ";

        int choice = 0;
        if (!(std::cin >> choice) || choice == 0) break;

        if (choice == 1) {
            fl->guardianHP -= hr->attackDamage;
            std::cout << ">> You struck the Guardian for " << hr->attackDamage << " damage!\n";
            if (fl->guardianHP > 0) {
                hr->health -= 45;
                std::cout << ">> Guardian counter-attacks for 45 damage!\n";
                if (hr->health <= 0) {
                    std::cout << "\n[YOU DIED] Build a Pointer Chain in Cheat Engine so your HP stays frozen across floors!\n";
                    break;
                }
            } else {
                std::cout << ">> [GUARDIAN DEFEATED!] Press [2] to ascend to the next floor!\n";
            }
        } else if (choice == 2) {
            if (fl->guardianHP > 0) {
                std::cout << ">> [!] Defeat the current Floor Guardian before ascending!\n";
            } else if (fl->floorNumber >= 5) {
                std::cout << "\n********************************************************************\n";
                std::cout << "  [QUEST COMPLETE - TIER E CLEARED!]\n";
                std::cout << "  You conquered all 5 Floors and mastered Multi-Level Pointers!\n";
                std::cout << "  Next Step: Proceed to Lab 05 (Code Injection & NOP Patching).\n";
                std::cout << "********************************************************************\n";
                break;
            } else {
                int nextFl = fl->floorNumber + 1;
                ReallocateFloor(nextFl, hr->health, hr->attackDamage);
                std::cout << "\n>> [HEAP REALLOCATED] Entered Floor " << nextFl
                          << "! Old heap addresses are now invalid!\n";
            }
        }
    }
    return 0;
}
