// ============================================================================
// [Lab 18] Lazy Singleton - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab18_lazy_singleton.cpp (the target) and check/lab18_selftest.cpp (CTest).
// The static pointer g_pGameManager is NULL until the player enters the dungeon for the first time.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <sstream>
#include <string>

namespace lab18
{

struct Inventory
{
    std::uint32_t slots;  // +0x00
    std::uint32_t keys;   // +0x04
    std::uint64_t weight; // +0x08
    std::int32_t gems;    // +0x10
};

struct Player
{
    std::int32_t hp;       // +0x00
    std::int32_t level;    // +0x04
    Inventory* inventory;  // +0x08  pointer (8 bytes on x64)
};

struct GameManager
{
    std::uint32_t ticks;   // +0x00
    std::uint32_t floor;   // +0x04
    Player* player;        // +0x08  pointer (8 bytes on x64)
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(offsetof(Inventory, gems) == 0x10, "gems offset");
static_assert(offsetof(Player, inventory) == 0x08, "inventory pointer offset");
static_assert(offsetof(GameManager, player) == 0x08, "player pointer offset");

// Chain: [g_pGameManager] +0x08 -> Player, Player +0x08 -> Inventory, Inventory +0x10 = gems.
inline GameManager* g_pGameManager = nullptr;

// Treasure requirement: at least 99999 gems (one gem per dungeon visit in game).
constexpr std::int32_t kGemGoal = 99999;

// Lazy initialisation: the whole object graph is created on the first visit only.
inline GameManager* EnterDungeon()
{
    if (g_pGameManager == nullptr)
    {
        Inventory* inv = new Inventory{12, 1, 340, 3};
        Player* player = new Player{100, 4, inv};
        g_pGameManager = new GameManager{0, 1, player};
    }
    g_pGameManager->ticks += 1;
    return g_pGameManager;
}

inline bool CheckWin()
{
    const GameManager* gm = g_pGameManager;
    return gm != nullptr && gm->player != nullptr && gm->player->inventory != nullptr &&
           gm->player->inventory->gems >= kGemGoal;
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

inline std::string MakeFlag()
{
    const std::string seal = "lab18|gems>=99999";
    std::ostringstream out;
    out << "FLAG{LAB18_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab18
