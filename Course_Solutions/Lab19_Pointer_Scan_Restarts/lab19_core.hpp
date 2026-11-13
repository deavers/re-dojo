// ============================================================================
// [Lab 19] Pointer Scan Across Restarts - game state, win check and flag (no I/O)
// ============================================================================
// Shared by lab19_pointer_scan.cpp (the target) and check/lab19_selftest.cpp (CTest).
// Every start builds the world with a random heap layout (allocation order, sizes and
// junk allocations in between), so the hero's address changes on every run. Only the
// path from the static object g_World survives a restart. Two decoy pointers look
// tempting but never lead to the real hero.
// ============================================================================
#pragma once

#include <algorithm>
#include <array>
#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <random>
#include <sstream>
#include <string>
#include <vector>

namespace lab19
{

constexpr std::uint32_t kKindHero = 1;
constexpr std::uint32_t kKindMob = 2;

struct Entity
{
    std::uint32_t id;    // +0x00
    std::uint32_t kind;  // +0x04
    float pos[3];        // +0x08
    std::int32_t hp;     // +0x14
    std::int32_t armor;  // +0x18
    char name[12];       // +0x1C
    std::uint32_t flags; // +0x28
    std::int32_t gold;   // +0x2C
};

struct Registry
{
    std::uint32_t count;    // +0x00
    std::uint32_t capacity; // +0x04
    Entity** list;          // +0x08  array of Entity* (8 bytes each); the hero is always list[3]
};

struct World
{
    std::uint64_t frame;  // +0x00
    std::uint64_t seed;   // +0x08
    Entity* lastSpawned;  // +0x10  decoy: always some mob, never the hero
    Registry* registry;   // +0x18  the stable path
    Entity* heroSnapshot; // +0x20  decoy: a COPY of the hero taken at start-up
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(offsetof(Entity, gold) == 0x2C, "gold offset");
static_assert(sizeof(Entity) == 0x30, "Entity size");
static_assert(offsetof(Registry, list) == 0x08, "list offset");
static_assert(offsetof(World, registry) == 0x18, "registry offset");
static_assert(offsetof(World, heroSnapshot) == 0x20, "snapshot offset");

// Stable path: g_World +0x18 -> Registry, +0x08 -> list, +0x18 (= 3 * 8) -> hero, +0x2C = gold.
constexpr std::size_t kHeroIndex = 3;
constexpr std::uint32_t kEntityCount = 8;
constexpr std::int32_t kCrownPrice = 777777;

inline World g_World{};
inline std::vector<void*> g_Junk; // junk allocations that shift the heap layout

inline Entity* Hero()
{
    return g_World.registry->list[kHeroIndex];
}

inline void BuildWorld(std::uint32_t seed)
{
    std::mt19937 rng(seed);
    const auto junk = [&rng]()
    {
        g_Junk.push_back(::operator new(16 + rng() % 1024));
    };
    junk();
    Registry* reg = new Registry{kEntityCount, static_cast<std::uint32_t>(kEntityCount + rng() % 8), nullptr};
    junk();
    reg->list = new Entity*[reg->capacity]();
    std::array<std::uint32_t, kEntityCount> order = {0, 1, 2, 3, 4, 5, 6, 7};
    std::shuffle(order.begin(), order.end(), rng);
    for (const std::uint32_t i : order)
    {
        junk();
        const std::uint32_t kind = (i == kHeroIndex) ? kKindHero : kKindMob;
        reg->list[i] = new Entity{900 + i, kind, {1.0f * i, 0.0f, 2.0f}, 100, 5, {}, 1, (i == kHeroIndex) ? 100 : 3};
    }
    const char heroName[] = "Wanderer";
    std::copy(heroName, heroName + sizeof(heroName), reg->list[kHeroIndex]->name);
    std::uint32_t mob = rng() % (kEntityCount - 1);
    if (mob >= kHeroIndex)
    {
        mob += 1; // never the hero
    }
    g_World.seed = seed;
    g_World.registry = reg;
    g_World.lastSpawned = reg->list[mob];
    g_World.heroSnapshot = new Entity(*reg->list[kHeroIndex]);
}

inline bool CheckWin()
{
    return g_World.registry != nullptr && Hero()->gold >= kCrownPrice;
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
    const std::string seal = "lab19|crown|gold>=777777";
    std::ostringstream out;
    out << "FLAG{LAB19_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab19
