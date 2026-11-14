// [Lab 11] CTest harness: applies Cheat Engine-like edits to g_Treasury from stdin, then checks the vault.
// Exit: 0 vault opened (flag), 1 not opened, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab11_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab11::g_Treasury);
    h.objectSize = sizeof(lab11::g_Treasury);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab11::CheckWin(lab11::g_Treasury))
    {
        std::cout << "FAILED: the vault stays shut\n";
        return 1;
    }
    std::cout << lab11::MakeFlag(lab11::g_Treasury) << "\n";
    return 0;
}
