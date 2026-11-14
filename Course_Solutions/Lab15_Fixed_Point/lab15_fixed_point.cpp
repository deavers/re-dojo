// ============================================================================
// [Lab 15] Fixed-Point 16.16 (Tier E- | Difficulty: 1.1/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 12. Fractional values are not always floats. Older engines,
//   physics code and emulated consoles often store them as fixed point: a plain
//   4-byte int where the low 16 bits are the fraction (value = raw / 65536).
//   A Float scan finds nothing; you must scan the raw integer.
//
// QUEST OBJECTIVES (the hyperjump engages when BOTH are exact):
//   1. Fuel   = 1000.0   (refuelling stops at 50.0)
//   2. Thrust = 3.25     (the lever stops at 2.0)
//
// Exit codes: 0 hyperjump (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <iomanip>
#include <cstdint>

#include "lab15_core.hpp"

using lab15::g_Ship;

static bool g_BlindMode = false;

static void PrintAddress(const void* p)
{
    if (!g_BlindMode)
    {
        std::cout << "   [Addr: 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(p) << std::dec
                  << "]";
    }
}

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 15 | TIER E-] THE FIXED-POINT STARSHIP (16.16 Fixed Point)\n";
    std::cout << "====================================================================\n";
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "   Fuel   : " << lab15::ToReal(g_Ship.fuel);
    PrintAddress(&g_Ship.fuel);
    std::cout << "\n   Thrust : " << lab15::ToReal(g_Ship.thrust);
    PrintAddress(&g_Ship.thrust);
    std::cout << "\n   Jumps  : " << g_Ship.jumps;
    PrintAddress(&g_Ship.jumps);
    std::cout << std::defaultfloat << std::setprecision(6);
    std::cout << "\n--------------------------------------------------------------------\n";
    std::cout << "  Hyperjump needs: Fuel = 1000.00 exactly, Thrust = 3.25 exactly\n";
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows memory addresses on screen)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses - pure Cheat Engine scan)\n> ";
    int mode = 1;
    if (!(std::cin >> mode))
    {
        return 3;
    }
    g_BlindMode = (mode == 2);

    while (true)
    {
        PrintState();
        std::cout << "Actions:\n";
        std::cout << "  [1] Refuel           (+0.25 fuel, stops at 50.00)\n";
        std::cout << "  [2] Short jump       (-1.50 fuel, +1 jump)\n";
        std::cout << "  [3] Push thrust lever (+0.50, stops at 2.00)\n";
        std::cout << "  [4] Pull thrust lever (-0.50)\n";
        std::cout << "  [9] Engage hyperjump\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "The engines power down.\n";
            return 3;
        }
        switch (choice)
        {
        case 1:
            g_Ship.fuel += lab15::kOne / 4;
            if (g_Ship.fuel > lab15::kFuelCap)
            {
                g_Ship.fuel = lab15::kFuelCap;
            }
            break;
        case 2:
            if (g_Ship.fuel >= lab15::kOne + lab15::kOne / 2)
            {
                g_Ship.fuel -= lab15::kOne + lab15::kOne / 2;
                g_Ship.jumps += 1;
            }
            break;
        case 3:
            g_Ship.thrust += lab15::kOne / 2;
            if (g_Ship.thrust > lab15::kThrustCap)
            {
                g_Ship.thrust = lab15::kThrustCap;
            }
            break;
        case 4:
            if (g_Ship.thrust >= lab15::kOne / 2)
            {
                g_Ship.thrust -= lab15::kOne / 2;
            }
            break;
        default:
            break;
        }
        if (lab15::CheckWin(g_Ship))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E- CLEARED!] Hyperjump engaged.\n";
            std::cout << "  " << lab15::MakeFlag(g_Ship) << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> The drive refuses. A Float scan will not help you here.\n";
        }
    }
}
