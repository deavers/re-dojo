// [Lab 17] CTest harness: applies Cheat Engine-like edits to g_Hero from stdin, then checks the legend.
// Exit: 0 legend (flag), 1 not yet, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab17_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab17::g_Hero);
    h.objectSize = sizeof(lab17::g_Hero);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab17::CheckWin(lab17::g_Hero))
    {
        std::cout << "FAILED: no legend yet\n";
        return 1;
    }
    std::cout << lab17::MakeFlag(lab17::g_Hero) << "\n";
    return 0;
}
