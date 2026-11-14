// ============================================================================
// RE:DOJO - shared CTest harness for memory labs (test-only, never part of a lab binary)
// ============================================================================
// A memory lab is solved in Cheat Engine. CI has no Cheat Engine, so the lab's selftest
// binary applies the same edits a solver would make, read as commands from stdin:
//
//   act <name>                                  scripted game action (lab callback)
//   poke <offset> <type> <value>                write into the lab's root object
//   chain <obj|ptr> <off> [<off>...] <type> <value>
//                                               start at the root object (obj) or at the
//                                               static root pointer (ptr), follow a pointer
//                                               at every offset but the last, write at the last
//   vcopy <off> <nslots>                        VMT labs: copy the table that the pointer at
//                                               object+off points to into a harness-owned buffer
//                                               (a "shadow VMT") and point object+off at the copy
//   vswap <off> donor                           VMT labs: point object+off at the donor's original table
//   vset <off> <slot> donor <dslot>             VMT labs: in the table referenced by object+off,
//                                               replace slot <slot> with slot <dslot> of the donor
//                                               object's table. Original tables are registered
//                                               READ-ONLY, so patching a shared table is rejected.
//
// Types: i8 u8 i16 u16 i32 u32 i64 u64 f32 f64 str8 str16 (str16 = UTF-16LE, ASCII text only)
// Every read and write is bounds-checked against registered regions: a wrong answer can
// never crash the harness, it only fails.
// Run() result: 0 = all commands applied, 1 = valid but not reachable (null pointer),
//               2 = malformed command or out-of-bounds address.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <cstring>
#include <functional>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

namespace dojo
{

struct Region
{
    const unsigned char* begin;
    std::size_t size;
    bool readOnly = false;
};

struct Harness
{
    unsigned char* object = nullptr;
    std::size_t objectSize = 0;
    const void* pointerRoot = nullptr; // ADDRESS of a static pointer variable (read with memcpy)
    std::vector<Region> regions;
    std::function<bool(const std::string&)> act;
    unsigned char* donor = nullptr;          // VMT labs: object whose table slots may be borrowed
    std::vector<std::vector<void*>> shadows; // VMT labs: harness-owned table copies
};

inline bool InRegions(const Harness& h, const unsigned char* p, std::size_t len, bool write = false)
{
    const auto addr = reinterpret_cast<std::uintptr_t>(p);
    for (const Region& r : h.regions)
    {
        if (write && r.readOnly)
        {
            continue;
        }
        const auto lo = reinterpret_cast<std::uintptr_t>(r.begin);
        if (addr >= lo && len <= r.size && addr - lo <= r.size - len)
        {
            return true;
        }
    }
    return false;
}

template <typename T>
inline void PutBytes(std::vector<unsigned char>& out, T value)
{
    out.resize(sizeof(T));
    std::memcpy(out.data(), &value, sizeof(T));
}

template <typename T>
inline bool PutSigned(std::vector<unsigned char>& out, const std::string& text)
{
    const long long v = std::stoll(text, nullptr, 0);
    if (v < static_cast<long long>(std::numeric_limits<T>::min()) ||
        v > static_cast<long long>(std::numeric_limits<T>::max()))
    {
        return false;
    }
    PutBytes(out, static_cast<T>(v));
    return true;
}

template <typename T>
inline bool PutUnsigned(std::vector<unsigned char>& out, const std::string& text)
{
    if (!text.empty() && text[0] == '-')
    {
        return false;
    }
    const unsigned long long v = std::stoull(text, nullptr, 0);
    if (v > static_cast<unsigned long long>(std::numeric_limits<T>::max()))
    {
        return false;
    }
    PutBytes(out, static_cast<T>(v));
    return true;
}

// Encodes <value> as <type>. Returns false for an unknown type or an unparsable value.
inline bool Encode(const std::string& type, const std::string& text, std::vector<unsigned char>& out)
{
    try
    {
        if (type == "i8") return PutSigned<std::int8_t>(out, text);
        if (type == "u8") return PutUnsigned<std::uint8_t>(out, text);
        if (type == "i16") return PutSigned<std::int16_t>(out, text);
        if (type == "u16") return PutUnsigned<std::uint16_t>(out, text);
        if (type == "i32") return PutSigned<std::int32_t>(out, text);
        if (type == "u32") return PutUnsigned<std::uint32_t>(out, text);
        if (type == "i64") return PutSigned<std::int64_t>(out, text);
        if (type == "u64") return PutUnsigned<std::uint64_t>(out, text);
        if (type == "f32")
        {
            PutBytes(out, static_cast<float>(std::stod(text)));
            return true;
        }
        if (type == "f64")
        {
            PutBytes(out, std::stod(text));
            return true;
        }
    }
    catch (const std::exception&)
    {
        return false;
    }
    if (type == "str8")
    {
        out.assign(text.begin(), text.end());
        out.push_back(0);
        return true;
    }
    if (type == "str16")
    {
        out.clear();
        for (const char c : text)
        {
            if (static_cast<unsigned char>(c) >= 0x80)
            {
                return false;
            }
            out.push_back(static_cast<unsigned char>(c));
            out.push_back(0);
        }
        out.push_back(0);
        out.push_back(0);
        return true;
    }
    return false;
}

inline bool IsType(const std::string& t)
{
    static const char* const kTypes[] = {"i8",  "u8",  "i16", "u16", "i32",  "u32",
                                         "i64", "u64", "f32", "f64", "str8", "str16"};
    for (const char* k : kTypes)
    {
        if (t == k)
        {
            return true;
        }
    }
    return false;
}

inline bool ParseOffset(const std::string& text, std::size_t& out)
{
    try
    {
        if (text.empty() || text[0] == '-')
        {
            return false;
        }
        out = static_cast<std::size_t>(std::stoull(text, nullptr, 0));
        return true;
    }
    catch (const std::exception&)
    {
        return false;
    }
}

inline std::string RestOfLine(std::istringstream& in)
{
    std::string rest;
    std::getline(in >> std::ws, rest);
    while (!rest.empty() && (rest.back() == '\r' || rest.back() == ' '))
    {
        rest.pop_back();
    }
    return rest;
}

inline unsigned char* At(unsigned char* base, std::size_t off);

inline bool ReadPtr(const Harness& h, unsigned char* at, unsigned char*& out)
{
    if (!InRegions(h, at, sizeof(void*)))
    {
        return false;
    }
    void* v = nullptr;
    std::memcpy(&v, at, sizeof(void*));
    out = static_cast<unsigned char*>(v);
    return out != nullptr;
}

// vcopy / vset. Returns 0 ok, 2 malformed or not allowed (out of region / read-only table).
inline int RunVmtCommand(Harness& h, const std::string& cmd, std::istringstream& in)
{
    std::string offText, a, b, c;
    std::size_t off = 0;
    if (!(in >> offText) || !ParseOffset(offText, off))
    {
        return 2;
    }
    unsigned char* slotOfVptr = At(h.object, off);
    unsigned char* table = nullptr;
    if (!InRegions(h, slotOfVptr, sizeof(void*), true) || !ReadPtr(h, slotOfVptr, table))
    {
        return 2;
    }
    if (cmd == "vswap")
    {
        // Point object+off at the donor's ORIGINAL table (a whole-vptr swap, no copy).
        unsigned char* donorTable = nullptr;
        if (!(in >> a) || a != "donor" || h.donor == nullptr || !ReadPtr(h, h.donor, donorTable))
        {
            return 2;
        }
        std::memcpy(slotOfVptr, &donorTable, sizeof(void*));
        return 0;
    }
    if (cmd == "vcopy")
    {
        std::size_t nslots = 0;
        if (!(in >> a) || !ParseOffset(a, nslots) || nslots == 0 || nslots > 64 ||
            !InRegions(h, table, nslots * sizeof(void*)))
        {
            return 2;
        }
        h.shadows.emplace_back(nslots);
        std::memcpy(h.shadows.back().data(), table, nslots * sizeof(void*));
        unsigned char* copy = reinterpret_cast<unsigned char*>(h.shadows.back().data());
        h.regions.push_back({copy, nslots * sizeof(void*)});
        std::memcpy(slotOfVptr, &copy, sizeof(void*));
        return 0;
    }
    std::size_t slot = 0, dslot = 0;
    if (!(in >> a >> b >> c) || !ParseOffset(a, slot) || b != "donor" || !ParseOffset(c, dslot) ||
        h.donor == nullptr)
    {
        return 2;
    }
    unsigned char* donorTable = nullptr;
    unsigned char* target = At(table, slot * sizeof(void*));
    unsigned char* source = nullptr;
    if (!ReadPtr(h, h.donor, donorTable))
    {
        return 2;
    }
    source = At(donorTable, dslot * sizeof(void*));
    if (!InRegions(h, source, sizeof(void*)) || !InRegions(h, target, sizeof(void*), true))
    {
        return 2; // reading outside the donor table, or writing into a read-only (shared) table
    }
    std::memcpy(target, source, sizeof(void*));
    return 0;
}

// Address arithmetic goes through uintptr_t: a wrong offset must not be undefined behaviour.
inline unsigned char* At(unsigned char* base, std::size_t off)
{
    return reinterpret_cast<unsigned char*>(reinterpret_cast<std::uintptr_t>(base) + off);
}

inline int Run(Harness& h)
{
    h.regions.push_back({h.object, h.objectSize});
    std::string line;
    while (std::getline(std::cin, line))
    {
        if (!line.empty() && line.back() == '\r')
        {
            line.pop_back();
        }
        if (line.empty() || line[0] == '#')
        {
            continue;
        }
        std::istringstream in(line);
        std::string cmd;
        in >> cmd;
        if (cmd == "act")
        {
            std::string name;
            if (!(in >> name) || !h.act || !h.act(name))
            {
                return 2;
            }
            continue;
        }
        if (cmd == "vcopy" || cmd == "vset" || cmd == "vswap")
        {
            const int vr = RunVmtCommand(h, cmd, in);
            if (vr != 0)
            {
                return vr;
            }
            continue;
        }
        unsigned char* cur = nullptr;
        std::vector<std::size_t> offsets;
        std::string tok;
        if (cmd == "poke")
        {
            cur = h.object;
        }
        else if (cmd == "chain")
        {
            std::string start;
            in >> start;
            if (start == "obj")
            {
                cur = h.object;
            }
            else if (start == "ptr" && h.pointerRoot != nullptr)
            {
                void* first = nullptr;
                std::memcpy(&first, h.pointerRoot, sizeof(void*));
                cur = static_cast<unsigned char*>(first);
                if (cur == nullptr)
                {
                    return 1;
                }
            }
            else
            {
                return 2;
            }
        }
        else
        {
            return 2;
        }
        while (in >> tok && !IsType(tok))
        {
            std::size_t off = 0;
            if (!ParseOffset(tok, off))
            {
                return 2;
            }
            offsets.push_back(off);
        }
        if (!IsType(tok) || offsets.empty() || (cmd == "poke" && offsets.size() != 1))
        {
            return 2;
        }
        std::vector<unsigned char> bytes;
        if (!Encode(tok, RestOfLine(in), bytes))
        {
            return 2;
        }
        for (std::size_t i = 0; i + 1 < offsets.size(); ++i)
        {
            unsigned char* slot = At(cur, offsets[i]);
            if (!InRegions(h, slot, sizeof(void*)))
            {
                return 2;
            }
            void* next = nullptr;
            std::memcpy(&next, slot, sizeof(void*));
            if (next == nullptr)
            {
                return 1;
            }
            cur = static_cast<unsigned char*>(next);
        }
        unsigned char* target = At(cur, offsets.back());
        if (!InRegions(h, target, bytes.size(), true))
        {
            return 2;
        }
        std::memcpy(target, bytes.data(), bytes.size());
    }
    return 0;
}

} // namespace dojo
