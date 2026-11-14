// ============================================================================
// [Lab 54] Own Emulator: Guest RAM - machine state, win check and flag (no I/O)
// ============================================================================
// Shared by lab54_emulator.cpp (the target) and check/lab54_selftest.cpp (CTest).
// A tiny "DojoBoy" console: 4 KiB of guest RAM live in a host heap buffer whose host address
// changes on every start. The game inside the console only knows GUEST addresses.
// Guest memory map (little-endian, from the console's manual):
//   0x0300  lives  (u8)
//   0x0302  score  (u16)
//   0x0304  level  (u8)
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <random>
#include <sstream>
#include <string>
#include <vector>

namespace lab54
{

constexpr std::uint32_t kRamSize = 0x1000;
constexpr std::uint16_t kLives = 0x0300;
constexpr std::uint16_t kScore = 0x0302;
constexpr std::uint16_t kLevel = 0x0304;

struct Machine
{
    std::uint64_t cycles;  // +0x00
    std::uint8_t* ram;     // +0x08  host pointer to guest RAM: host address = ram + guest address
    std::uint32_t ramSize; // +0x10
    std::uint16_t pc;      // +0x14  guest program counter
    std::uint8_t running;  // +0x16
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(offsetof(Machine, ram) == 0x08, "ram pointer offset");
static_assert(offsetof(Machine, ramSize) == 0x10, "ramSize offset");

inline Machine g_Machine{};
inline std::vector<void*> g_Junk;

// Guest ROM: tiny bytecode the console runs. Ops: 0x01 ADDW addr16 imm16 | 0x02 DECB addr16 | 0xFF END.
// Routine 0 (play a frame): score += 7.  Routine 1 (take a hit): lives -= 1.
inline const std::uint8_t kRom[] = {
    0x01, 0x02, 0x03, 0x07, 0x00, 0xFF, // routine 0 at ROM 0x00
    0x02, 0x00, 0x03, 0xFF,             // routine 1 at ROM 0x06
};
constexpr std::uint16_t kRoutinePlay = 0x00;
constexpr std::uint16_t kRoutineHit = 0x06;

inline std::uint16_t ReadGuest16(std::uint16_t addr)
{
    return static_cast<std::uint16_t>(g_Machine.ram[addr] | (g_Machine.ram[addr + 1] << 8));
}

inline void WriteGuest16(std::uint16_t addr, std::uint16_t v)
{
    g_Machine.ram[addr] = static_cast<std::uint8_t>(v & 0xFF);
    g_Machine.ram[addr + 1] = static_cast<std::uint8_t>(v >> 8);
}

// Runs one ROM routine. Every guest address is checked against the RAM size.
inline void RunRoutine(std::uint16_t start)
{
    g_Machine.pc = start;
    g_Machine.running = 1;
    while (g_Machine.running && g_Machine.pc < sizeof(kRom))
    {
        const std::uint8_t op = kRom[g_Machine.pc];
        g_Machine.cycles += 1;
        if (op == 0x01 && g_Machine.pc + 5u <= sizeof(kRom))
        {
            const auto addr = static_cast<std::uint16_t>(kRom[g_Machine.pc + 1] | (kRom[g_Machine.pc + 2] << 8));
            const auto imm = static_cast<std::uint16_t>(kRom[g_Machine.pc + 3] | (kRom[g_Machine.pc + 4] << 8));
            if (addr + 1u < g_Machine.ramSize)
            {
                WriteGuest16(addr, static_cast<std::uint16_t>(ReadGuest16(addr) + imm));
            }
            g_Machine.pc = static_cast<std::uint16_t>(g_Machine.pc + 5);
        }
        else if (op == 0x02 && g_Machine.pc + 3u <= sizeof(kRom))
        {
            const auto addr = static_cast<std::uint16_t>(kRom[g_Machine.pc + 1] | (kRom[g_Machine.pc + 2] << 8));
            if (addr < g_Machine.ramSize && g_Machine.ram[addr] > 0)
            {
                g_Machine.ram[addr] = static_cast<std::uint8_t>(g_Machine.ram[addr] - 1);
            }
            g_Machine.pc = static_cast<std::uint16_t>(g_Machine.pc + 3);
        }
        else
        {
            g_Machine.running = 0;
        }
    }
}

inline void PowerOn(std::uint32_t seed)
{
    std::mt19937 rng(seed);
    g_Junk.push_back(::operator new(64 + rng() % 4096)); // shifts where the guest RAM lands
    g_Machine.ram = new std::uint8_t[kRamSize]();
    g_Machine.ramSize = kRamSize;
    g_Machine.ram[kLives] = 3;
    WriteGuest16(kScore, 120);
    g_Machine.ram[kLevel] = 1;
}

// Win: lives exactly 99 and score exactly 50000 (guest values).
constexpr std::uint8_t kLivesGoal = 99;
constexpr std::uint16_t kScoreGoal = 50000;

inline bool CheckWin()
{
    return g_Machine.ram != nullptr && g_Machine.ram[kLives] == kLivesGoal && ReadGuest16(kScore) == kScoreGoal;
}

inline std::uint64_t Fnv1a64(const std::string& text)
{
    std::uint64_t h = 0xCBF29CE484222325ULL;
    for (const unsigned char c : text)
    {
        h ^= c;
        h *= 0x100000001B3ULL;
    }
    return h;
}

// The flag mixes a neutral tag with the guest values the solver wrote.
inline std::string MakeFlag()
{
    const std::string seal = "lab54|" + std::to_string(g_Machine.ram[kLives]) + "|" + std::to_string(ReadGuest16(kScore));
    std::ostringstream out;
    out << "FLAG{LAB54_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab54
