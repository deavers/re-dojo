// [Lab 16] CTest harness: applies Cheat Engine-like edits to g_Squad from stdin, then checks the march.
// Exit: 0 squad marches (flag), 1 not ready, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab16_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab16::g_Squad);
    h.objectSize = sizeof(lab16::g_Squad);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab16::CheckWin(lab16::g_Squad))
    {
        std::cout << "FAILED: the squad is not ready\n";
        return 1;
    }
    std::cout << lab16::MakeFlag() << "\n";
    return 0;
}
