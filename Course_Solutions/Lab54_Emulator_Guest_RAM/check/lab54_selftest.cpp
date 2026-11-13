// [Lab 54] CTest harness: powers the console on (random host placement of guest RAM), registers the
// machine object and the guest RAM buffer, then applies edits from stdin (chains through Machine::ram).
// Exit: 0 high score accepted (flag), 1 rejected, 2 malformed command / bad address.
#include <iostream>
#include <random>

#include "dojo_selftest.hpp"
#include "lab54_core.hpp"

int main()
{
    std::random_device rd;
    lab54::PowerOn(rd());

    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab54::g_Machine);
    h.objectSize = sizeof(lab54::g_Machine);
    h.regions.push_back({lab54::g_Machine.ram, lab54::g_Machine.ramSize});

    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab54::CheckWin())
    {
        std::cout << "FAILED: the high score table rejects you\n";
        return 1;
    }
    std::cout << lab54::MakeFlag() << "\n";
    return 0;
}
