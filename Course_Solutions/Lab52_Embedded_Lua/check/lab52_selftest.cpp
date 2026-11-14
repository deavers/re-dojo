// [Lab 52] CTest harness: models what an injected DLL does. Commands on stdin:
//   luado <offset> <lua code>   read a pointer from g_Engine + offset; it must be the game's real
//                               lua_State (otherwise rejected, never dereferenced); run the code there
//   tick                        end a turn (the script's tick())
// Exit: 0 admitted (flag), 1 not admitted / Lua error, 2 malformed command or wrong lua_State pointer.
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>

#include "lab52_core.hpp"

static int RunCommands()
{
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
        if (cmd == "tick")
        {
            lab52::Tick();
            continue;
        }
        if (cmd != "luado")
        {
            return 2;
        }
        std::string offText, code;
        if (!(in >> offText))
        {
            return 2;
        }
        std::getline(in >> std::ws, code);
        std::size_t off = 0;
        try
        {
            off = static_cast<std::size_t>(std::stoull(offText, nullptr, 0));
        }
        catch (const std::exception&)
        {
            return 2;
        }
        if (off + sizeof(void*) > sizeof(lab52::g_Engine))
        {
            return 2;
        }
        void* candidate = nullptr;
        std::memcpy(&candidate, reinterpret_cast<const unsigned char*>(&lab52::g_Engine) + off, sizeof(void*));
        if (candidate != static_cast<void*>(lab52::g_Engine.L))
        {
            std::cout << "FAILED: that is not the game's lua_State\n";
            return 2;
        }
        lua_State* L = static_cast<lua_State*>(candidate);
        if (luaL_dostring(L, code.c_str()) != LUA_OK)
        {
            std::cout << "FAILED: Lua error: " << lua_tostring(L, -1) << "\n";
            lua_pop(L, 1);
            return 1;
        }
    }
    return 0;
}

int main()
{
    if (!lab52::Boot())
    {
        std::cout << "FAILED: boot\n";
        return 2;
    }
    const int rc = RunCommands();
    if (rc != 0)
    {
        return rc;
    }
    if (!lab52::CheckWin())
    {
        std::cout << "FAILED: the Guild refuses\n";
        return 1;
    }
    std::cout << lab52::MakeFlag() << "\n";
    return 0;
}
