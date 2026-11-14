// [Lab 13] CTest harness: applies Cheat Engine-like edits to g_Card from stdin, then checks the Hall.
// Exit: 0 admitted (flag), 1 not admitted, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab13_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab13::g_Card);
    h.objectSize = sizeof(lab13::g_Card);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab13::CheckWin(lab13::g_Card))
    {
        std::cout << "FAILED: the Hall stays closed\n";
        return 1;
    }
    std::cout << lab13::MakeFlag(lab13::g_Card) << "\n";
    return 0;
}
