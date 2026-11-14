// ============================================================================
// [Lab 19] Pointer Scan Across Restarts - world, path verification and flag (no I/O)
// ============================================================================
// Used by lab19_pointer_scan.cpp. Every build of the world uses a random heap layout (allocation
// order, sizes and junk allocations in between), so the hero's address changes every time. Only the
// path from the static object g_World survives a rebuild. Two decoys look right on screen: a mob
// whose gold mirrors the hero's every turn, and a snapshot copy of the hero refreshed every turn.
// ============================================================================
#pragma once

#include <array>
#include <cstddef>
#include <cstdint>
#include <cstring>
#include <iomanip>
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
    Entity* lastSpawned;  // +0x10  decoy: a mob whose gold mirrors the hero's every turn
    Registry* registry;   // +0x18  the stable path
    Entity* heroSnapshot; // +0x20  decoy: a copy of the hero, refreshed every turn
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
constexpr std::size_t kMaxOffsets = 8;
constexpr int kRebuilds = 3;

inline World g_World{};
inline std::vector<void*> g_Junk; // junk allocations that shift the heap layout (never freed)

// Small own PRNG (xorshift32): no dependence on a standard library's distributions.
struct Rng
{
    std::uint32_t s;
    std::uint32_t Next()
    {
        s ^= s << 13;
        s ^= s >> 17;
        s ^= s << 5;
        return s;
    }
};

inline Entity* Hero()
{
    return g_World.registry->list[kHeroIndex];
}

// Builds a fresh world (the previous one is simply abandoned - a "restart").
inline void BuildWorld(std::uint32_t seed)
{
    Rng rng{seed | 1u};
    const auto junk = [&rng]()
    {
        g_Junk.push_back(::operator new(16 + rng.Next() % 1024));
    };
    junk();
    Registry* reg = new Registry{kEntityCount, kEntityCount + rng.Next() % 8, nullptr};
    junk();
    reg->list = new Entity*[reg->capacity]();
    std::array<std::uint32_t, kEntityCount> order = {0, 1, 2, 3, 4, 5, 6, 7};
    for (std::uint32_t i = kEntityCount - 1; i > 0; --i)
    {
        const std::uint32_t j = rng.Next() % (i + 1);
        const std::uint32_t t = order[i];
        order[i] = order[j];
        order[j] = t;
    }
    for (const std::uint32_t i : order)
    {
        junk();
        const std::uint32_t kind = (i == kHeroIndex) ? kKindHero : kKindMob;
        reg->list[i] = new Entity{900 + i, kind, {1.0f * i, 0.0f, 2.0f}, 100, 5, {}, 1, 100};
    }
    const char heroName[] = "Wanderer";
    std::memcpy(reg->list[kHeroIndex]->name, heroName, sizeof(heroName));
    std::uint32_t mob = rng.Next() % (kEntityCount - 1);
    if (mob >= kHeroIndex)
    {
        mob += 1; // never the hero
    }
    g_World.frame = 0;
    g_World.seed = seed;
    g_World.registry = reg;
    g_World.lastSpawned = reg->list[mob];
    g_World.heroSnapshot = new Entity(*reg->list[kHeroIndex]);
}

// One game turn: both decoys follow the hero, so on screen they look exactly like it.
inline void Turn()
{
    *g_World.heroSnapshot = *Hero();
    g_World.lastSpawned->gold = Hero()->gold;
    g_World.frame += 1;
}

struct Region
{
    const unsigned char* begin;
    std::size_t size;
};

inline std::vector<Region> WorldRegions()
{
    std::vector<Region> r;
    const Registry* reg = g_World.registry;
    r.push_back({reinterpret_cast<const unsigned char*>(&g_World), sizeof(g_World)});
    r.push_back({reinterpret_cast<const unsigned char*>(reg), sizeof(*reg)});
    r.push_back({reinterpret_cast<const unsigned char*>(reg->list), sizeof(Entity*) * reg->capacity});
    for (std::uint32_t i = 0; i < reg->count; ++i)
    {
        r.push_back({reinterpret_cast<const unsigned char*>(reg->list[i]), sizeof(Entity)});
    }
    r.push_back({reinterpret_cast<const unsigned char*>(g_World.heroSnapshot), sizeof(Entity)});
    return r;
}

inline bool Inside(const std::vector<Region>& regions, std::uintptr_t addr, std::size_t len)
{
    for (const Region& rg : regions)
    {
        const auto lo = reinterpret_cast<std::uintptr_t>(rg.begin);
        if (addr >= lo && len <= rg.size && addr - lo <= rg.size - len)
        {
            return true;
        }
    }
    return false;
}

// Follows the path from g_World in the CURRENT world; every read is bounds-checked.
inline bool ResolvesToHeroGold(const std::vector<std::size_t>& offsets)
{
    if (offsets.empty() || offsets.size() > kMaxOffsets)
    {
        return false;
    }
    const std::vector<Region> regions = WorldRegions();
    std::uintptr_t cur = reinterpret_cast<std::uintptr_t>(&g_World);
    for (std::size_t i = 0; i + 1 < offsets.size(); ++i)
    {
        const std::uintptr_t slot = cur + offsets[i];
        if (!Inside(regions, slot, sizeof(void*)))
        {
            return false;
        }
        std::uintptr_t next = 0;
        std::memcpy(&next, reinterpret_cast<const void*>(slot), sizeof(next));
        if (next == 0)
        {
            return false;
        }
        cur = next;
    }
    return cur + offsets.back() == reinterpret_cast<std::uintptr_t>(&Hero()->gold);
}

// The path must reach the hero's gold in kRebuilds freshly built worlds.
inline bool VerifyAcrossRebuilds(const std::vector<std::size_t>& offsets, std::uint32_t seedBase)
{
    for (int k = 0; k < kRebuilds; ++k)
    {
        BuildWorld(seedBase + 0x9E3779B9u * static_cast<std::uint32_t>(k + 1));
        if (!ResolvesToHeroGold(offsets))
        {
            return false;
        }
    }
    return true;
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

// The flag mixes a neutral tag with the submitted path (lower-case hex, comma separated).
inline std::string MakeFlag(const std::vector<std::size_t>& offsets)
{
    std::ostringstream path;
    for (std::size_t i = 0; i < offsets.size(); ++i)
    {
        path << (i ? "," : "") << std::hex << offsets[i];
    }
    std::ostringstream out;
    out << "FLAG{LAB19_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0')
        << Fnv1a64("lab19|" + path.str()) << "}";
    return out.str();
}

} // namespace lab19
