// [Lab 18] CTest harness: "act enter" runs the lazy init, then a pointer chain from g_pGameManager is
// applied from stdin. Only the three heap objects are registered as reachable memory.
// Exit: 0 treasure opened (flag), 1 not opened / pointer still NULL, 2 malformed command / bad address.
#include <iostream>
#include <string>

#include "dojo_selftest.hpp"
#include "lab18_core.hpp"

int main()
{
    dojo::Harness h;
    h.pointerRoot = &lab18::g_pGameManager;
    h.act = [&h](const std::string& name)
    {
        if (name != "enter")
        {
            return false;
        }
        lab18::GameManager* gm = lab18::EnterDungeon();
        h.regions.push_back({reinterpret_cast<const unsigned char*>(gm), sizeof(*gm)});
        h.regions.push_back({reinterpret_cast<const unsigned char*>(gm->player), sizeof(*gm->player)});
        h.regions.push_back(
            {reinterpret_cast<const unsigned char*>(gm->player->inventory), sizeof(*gm->player->inventory)});
        return true;
    };
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab18::CheckWin())
    {
        std::cout << "FAILED: the Treasure Room stays locked\n";
        return 1;
    }
    std::cout << lab18::MakeFlag() << "\n";
    return 0;
}
