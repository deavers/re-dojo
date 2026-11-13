// [Lab 12] CTest harness: applies Cheat Engine-like edits to g_Alchemy from stdin, then checks the stone.
// Exit: 0 stone formed (flag), 1 not formed, 2 malformed command / out-of-bounds address.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab12_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab12::g_Alchemy);
    h.objectSize = sizeof(lab12::g_Alchemy);
    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab12::CheckWin(lab12::g_Alchemy))
    {
        std::cout << "FAILED: the stone does not form\n";
        return 1;
    }
    std::cout << lab12::MakeFlag() << "\n";
    return 0;
}
