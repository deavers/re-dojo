// ============================================================================
// [Lab 45] Mini-"UE": Name Pool - engine state, checks and flag (no I/O)
// ============================================================================
// Shared by lab45_name_pool.cpp (the target) and check/lab45_selftest.cpp (the dump checker).
// A name pool in the style of Unreal's FNamePool, but our own and much smaller:
//   * names live in chunks of kChunkSize bytes allocated on the heap (addresses differ per start);
//   * an entry is a 2-byte little-endian header (length << 6) followed by the ASCII characters,
//     padded so the next entry starts on an even offset;
//   * an FName index is (chunk << 16) | (byte offset / 2).
// The names are stored XOR-encoded in the binary and only decoded into the pool at start-up.
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

namespace lab45
{

constexpr std::uint32_t kChunkSize = 0xC0;
constexpr std::uint32_t kMaxChunks = 16;
constexpr std::uint32_t kStride = 2;
constexpr std::uint8_t kNameKey = 0x5C;

struct NamePool
{
    std::uint32_t currentChunk;       // +0x00
    std::uint32_t currentOffset;      // +0x04  byte offset inside the current chunk
    std::uint8_t* chunks[kMaxChunks]; // +0x08  chunk pointers, 8 bytes each
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(offsetof(NamePool, chunks) == 0x08, "chunks offset");

struct EncodedName
{
    std::uint8_t len;
    std::uint8_t bytes[16]; // character j of name i = bytes[j] ^ ((kNameKey + i * 7 + j * 3) & 0xFF)
};

const EncodedName kEncodedNames[] = {
    {4, {0x12, 0x30, 0x0C, 0x00}},
    {6, {0x2C, 0x04, 0x03, 0x09, 0x0C, 0x06}},
    {5, {0x29, 0x01, 0x11, 0x00, 0x05}},
    {7, {0x21, 0x15, 0x14, 0x11, 0x1C, 0xE7, 0xE6}},
    {5, {0x39, 0x18, 0x0A, 0xEE, 0xF6}},
    {4, {0x2F, 0xE3, 0xF2, 0xE6}},
    {9, {0xC5, 0xE1, 0xED, 0xFD, 0xF3, 0xF6, 0xEC, 0xFE, 0xEC}},
    {16, {0xDD, 0xFC, 0xF2, 0xEF, 0xFC, 0xEE, 0xDC, 0xCD, 0xCB, 0xDC, 0xD9, 0xC1, 0xDD, 0xD8, 0xD2, 0xC8}},
    {8, {0xD3, 0xF6, 0xF7, 0xF8, 0xED, 0xCC, 0xC2, 0xCC}},
    {5, {0xCC, 0xF1, 0xD3, 0xC8, 0xC3}},
    {5, {0xEE, 0xC0, 0xDE, 0xCE, 0xC2}},
    {14, {0xFA, 0xCF, 0xCA, 0xDC, 0xD0, 0xFB, 0xD4, 0xD3, 0xB1, 0xAB, 0xA9, 0xAF, 0xA3, 0xA4}},
    {15, {0xF8, 0xD6, 0xD7, 0xD5, 0xC8, 0xD7, 0x81, 0xAA, 0xA5, 0xBB, 0xA1, 0xBF, 0xB1, 0xB9, 0xAE}},
    {6, {0xFF, 0xDF, 0xDC, 0xAC, 0xB7, 0xAE}},
    {9, {0xF3, 0xA0, 0xBC, 0x8F, 0xAF, 0xAC, 0xBC, 0xA7, 0xBE}},
    {6, {0x96, 0xA0, 0xA2, 0xAB, 0xBD, 0xB0}},
    {4, {0x8D, 0xA2, 0xBF, 0xBA}},
    {7, {0x9E, 0xB7, 0xA1, 0x9D, 0xB2, 0x8F, 0x8A}},
    {9, {0x93, 0xB3, 0x96, 0x86, 0x88, 0x9D, 0x83, 0x9D, 0x8B}},
    {6, {0xB6, 0x81, 0x86, 0x9A, 0x82, 0x9E}},
    {6, {0xAC, 0x8A, 0x83, 0x90, 0x93, 0x92}},
    {8, {0xA9, 0x9B, 0x87, 0x9D, 0xA9, 0x9F, 0x75, 0x61}},
    {8, {0xBA, 0x96, 0x9F, 0x9E, 0x76, 0x6C, 0x67, 0x65}},
    {8, {0xAF, 0x6F, 0x77, 0x67, 0x7D, 0x65, 0x60, 0x7C}},
    {8, {0x52, 0x62, 0x66, 0x62, 0x73, 0x7A, 0x62, 0x60}},
    {8, {0x4C, 0x7B, 0x70, 0x66, 0x73, 0x73, 0x7C, 0x4E}},
    {4, {0x46, 0x70, 0x79, 0x76}},
    {5, {0x4A, 0x7F, 0x70, 0x50, 0x40}},
    {5, {0x6B, 0x4A, 0x4A, 0x45, 0x5F}},
    {6, {0x63, 0x4F, 0x4C, 0x44, 0x5B, 0x45}},
    {4, {0x63, 0x54, 0x47, 0x5F}},
    {8, {0x78, 0x59, 0x4F, 0x5B, 0x33, 0x2D, 0x26, 0x26}},
    {7, {0x68, 0x5A, 0x3A, 0x31, 0x3D, 0x39, 0x2B}},
    {5, {0x10, 0x29, 0x3C, 0x22, 0x2B}},
    {8, {0x1A, 0x2C, 0x22, 0x27, 0x3F, 0x3A, 0x30, 0x3A}},
    {5, {0x02, 0x3D, 0x30, 0x33, 0x31}},
    {5, {0x0C, 0x32, 0x33, 0x04, 0x16}},
    {7, {0x0C, 0x12, 0x04, 0x1F, 0x05, 0x0B, 0x03}},
    {4, {0x22, 0x06, 0x03, 0x1D}},
    {3, {0x26, 0x15, 0x0A}},
    {5, {0x37, 0x1F, 0x1F, 0x0E, 0xF4}},
    {4, {0x3C, 0x11, 0xED, 0xE0}},
    {10, {0xC7, 0xFD, 0xF8, 0xEE, 0xFC, 0xF8, 0xF1, 0xF9, 0xF9, 0xF8}},
    {8, {0xC5, 0xE9, 0xF9, 0xF7, 0xF9, 0xC7, 0xCE, 0xEE}},
    {5, {0xC3, 0xF8, 0xFF, 0xF5, 0xF0}},
    {7, {0xD6, 0xF8, 0xF4, 0xCC, 0xCA, 0xD2, 0xD0}},
    {8, {0xDD, 0xCE, 0xCB, 0xCB, 0xCE, 0xC2, 0xC7, 0xDD}},
    {8, {0xE6, 0xC7, 0xDD, 0xCB, 0xDF, 0xD5, 0xD9, 0xCE}},
    {4, {0xEE, 0xC0, 0xC1, 0xC6}},
    {5, {0xF2, 0xC4, 0xDC, 0xD2, 0xDE}},
};
constexpr std::size_t kNameCount = sizeof(kEncodedNames) / sizeof(kEncodedNames[0]);

inline NamePool g_NamePool{};
inline std::vector<std::uint32_t> g_Index; // FName index of name i, in insertion order
inline std::vector<void*> g_Junk;

inline std::uint32_t AddName(const char* text, std::uint32_t len, std::mt19937& rng)
{
    const std::uint32_t size = (2 + len + 1) & ~1u;
    if (g_NamePool.chunks[g_NamePool.currentChunk] != nullptr && g_NamePool.currentOffset + size > kChunkSize)
    {
        g_NamePool.currentChunk += 1;
        g_NamePool.currentOffset = 0;
    }
    std::uint8_t*& chunk = g_NamePool.chunks[g_NamePool.currentChunk];
    if (chunk == nullptr)
    {
        g_Junk.push_back(::operator new(32 + rng() % 2048)); // chunks land at different addresses
        chunk = new std::uint8_t[kChunkSize]();
    }
    std::uint8_t* entry = chunk + g_NamePool.currentOffset;
    const std::uint16_t header = static_cast<std::uint16_t>(len << 6);
    entry[0] = static_cast<std::uint8_t>(header & 0xFF);
    entry[1] = static_cast<std::uint8_t>(header >> 8);
    std::memcpy(entry + 2, text, len);
    const std::uint32_t index = (g_NamePool.currentChunk << 16) | (g_NamePool.currentOffset / kStride);
    g_NamePool.currentOffset += size;
    return index;
}

inline void BuildPool(std::uint32_t seed)
{
    std::mt19937 rng(seed);
    for (std::size_t i = 0; i < kNameCount; ++i)
    {
        char text[16] = {};
        const EncodedName& e = kEncodedNames[i];
        for (std::size_t j = 0; j < e.len; ++j)
        {
            text[j] = static_cast<char>(e.bytes[j] ^ ((kNameKey + i * 7 + j * 3) & 0xFF));
        }
        g_Index.push_back(AddName(text, e.len, rng));
    }
}

// Resolves an FName index by walking the pool exactly like a dumper would. Empty string if invalid.
inline std::string Resolve(std::uint32_t index)
{
    const std::uint32_t chunk = index >> 16;
    const std::uint32_t offset = (index & 0xFFFF) * kStride;
    if (chunk > g_NamePool.currentChunk || g_NamePool.chunks[chunk] == nullptr || offset + 2 > kChunkSize)
    {
        return {};
    }
    const std::uint8_t* entry = g_NamePool.chunks[chunk] + offset;
    const std::uint32_t len = static_cast<std::uint32_t>(entry[0] | (entry[1] << 8)) >> 6;
    if (len == 0 || offset + 2 + len > kChunkSize)
    {
        return {};
    }
    return std::string(reinterpret_cast<const char*>(entry + 2), len);
}

// The three sealed objects of the quest reference these names (by position in the table).
constexpr std::size_t kSealed[3] = {6, 25, 47};

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
    const std::string seal = "lab45|name-pool|chunk<<16|offset/2";
    std::ostringstream out;
    out << "FLAG{LAB45_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab45
