// [Lab 19] CTest harness: builds a randomly laid-out world (new seed on every process start), registers
// every object of the graph as reachable memory, then applies a pointer chain from g_World from stdin.
// The runner starts this binary several times, so a path must survive different heap layouts.
// Exit: 0 crown bought (flag), 1 not enough gold / NULL, 2 malformed command / bad address.
#include <iostream>
#include <random>

#include "dojo_selftest.hpp"
#include "lab19_core.hpp"

int main()
{
    std::random_device rd;
    lab19::BuildWorld(rd());

    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab19::g_World);
    h.objectSize = sizeof(lab19::g_World);
    const lab19::Registry* reg = lab19::g_World.registry;
    h.regions.push_back({reinterpret_cast<const unsigned char*>(reg), sizeof(*reg)});
    h.regions.push_back({reinterpret_cast<const unsigned char*>(reg->list), sizeof(lab19::Entity*) * reg->capacity});
    for (std::uint32_t i = 0; i < reg->count; ++i)
    {
        h.regions.push_back({reinterpret_cast<const unsigned char*>(reg->list[i]), sizeof(lab19::Entity)});
    }
    h.regions.push_back({reinterpret_cast<const unsigned char*>(lab19::g_World.heroSnapshot), sizeof(lab19::Entity)});

    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    if (!lab19::CheckWin())
    {
        std::cout << "FAILED: the hero still cannot afford the Crown\n";
        return 1;
    }
    std::cout << lab19::MakeFlag() << "\n";
    return 0;
}
