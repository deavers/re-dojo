// ============================================================================
// [Lab 52] Embedded Lua 5.4: lua_State - engine state, win check and flag
// ============================================================================
// Shared by lab52_embedded_lua.cpp (the target) and check/lab52_selftest.cpp (CTest).
// The game logic lives in a Lua script running inside the game's own lua_State. The state
// pointer is kept in the static engine object g_Engine. Lua comes from lua54 (third_party/lua),
// a shared library: on Windows lua54.dll exports the whole Lua C API.
// ============================================================================
#pragma once

#include <cstddef>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <string>

#include "lua.hpp"

namespace lab52
{

struct Engine
{
    std::uint64_t frame;    // +0x00
    std::uint32_t flags;    // +0x08
    std::uint32_t turn;     // +0x0C
    lua_State* L;           // +0x10  the game's Lua state
    const char* scriptName; // +0x18
};

static_assert(sizeof(void*) == 8, "the reference offsets assume a 64-bit build");
static_assert(offsetof(Engine, L) == 0x10, "lua_State pointer offset");

inline Engine g_Engine{};

// The realm script. The win needs hero.gold >= 1000000 and hero.title == "Archmage";
// tick() only ever adds 1 gold and nothing in the script changes the title.
constexpr char kScript[] = R"lua(
hero = { name = "Wanderer", gold = 25, title = "Apprentice" }
function tick()
  hero.gold = hero.gold + 1
end
)lua";

// Sandbox like many games: only base, table, string and math; no io / os / package, no file loading.
inline bool Boot()
{
    lua_State* L = luaL_newstate();
    if (L == nullptr)
    {
        return false;
    }
    luaL_requiref(L, LUA_GNAME, luaopen_base, 1);
    luaL_requiref(L, LUA_TABLIBNAME, luaopen_table, 1);
    luaL_requiref(L, LUA_STRLIBNAME, luaopen_string, 1);
    luaL_requiref(L, LUA_MATHLIBNAME, luaopen_math, 1);
    lua_pop(L, 4);
    lua_pushnil(L);
    lua_setglobal(L, "dofile");
    lua_pushnil(L);
    lua_setglobal(L, "loadfile");
    if (luaL_dostring(L, kScript) != LUA_OK)
    {
        lua_close(L);
        return false;
    }
    g_Engine.L = L;
    g_Engine.scriptName = "realm.lua";
    return true;
}

inline void Tick()
{
    lua_getglobal(g_Engine.L, "tick");
    if (lua_pcall(g_Engine.L, 0, 0, 0) != LUA_OK)
    {
        lua_pop(g_Engine.L, 1);
    }
    g_Engine.frame += 1;
    g_Engine.turn += 1;
}

// Reads hero.gold / hero.title without trusting the script: wrong types simply do not win.
inline bool ReadHero(double& gold, std::string& title)
{
    lua_State* L = g_Engine.L;
    bool ok = false;
    if (lua_getglobal(L, "hero") == LUA_TTABLE)
    {
        const bool goldOk = lua_getfield(L, -1, "gold") == LUA_TNUMBER;
        gold = goldOk ? lua_tonumber(L, -1) : 0.0;
        const bool titleOk = lua_getfield(L, -2, "title") == LUA_TSTRING;
        title = titleOk ? lua_tostring(L, -1) : "";
        lua_pop(L, 2);
        ok = goldOk && titleOk;
    }
    lua_pop(L, 1);
    return ok;
}

inline bool CheckWin()
{
    double gold = 0.0;
    std::string title;
    return g_Engine.L != nullptr && ReadHero(gold, title) && gold >= 1000000.0 && title == "Archmage";
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
    const std::string seal = "lab52|lua_State|hero.gold>=1000000|Archmage";
    std::ostringstream out;
    out << "FLAG{LAB52_" << std::hex << std::uppercase << std::setw(16) << std::setfill('0') << Fnv1a64(seal) << "}";
    return out.str();
}

} // namespace lab52
