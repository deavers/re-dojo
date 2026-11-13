// [Lab 15] CTest harness: applies Cheat Engine-like edits to g_Ship from stdin, then checks the hyperjump.
// Exit: 0 hyperjump (flag), 1 no jump, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab15_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab15::g_Ship);
    h.objectSize = sizeof(lab15::g_Ship);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab15::CheckWin(lab15::g_Ship))
    {
        std::cout << "FAILED: the hyperjump does not engage\n";
        return 1;
    }
    std::cout << lab15::MakeFlag() << "\n";
    return 0;
}
