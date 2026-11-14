// [Lab 32] CTest harness: the guards array is the root object, the Merchant is the donor, and both
// original tables are registered READ-ONLY (in a real binary they live in .rdata). vcopy / vset / vswap
// from stdin, then the bribe is checked.
// Before any virtual call, every guard's vptr must point to a known table with all kSlots slots:
// a shadow copy shorter than kSlots -> exit 1 (the game would call past its end), unknown memory -> exit 2.
// Exit: 0 bribe accepted (flag), 1 refused / Marshal notices / short table, 2 malformed command or not allowed.
#include <iostream>

#include "dojo_selftest.hpp"
#include "lab32_core.hpp"

int main()
{
    dojo::Harness h;
    h.object = reinterpret_cast<unsigned char*>(&lab32::g_Guards);
    h.objectSize = sizeof(lab32::g_Guards);
    h.donor = reinterpret_cast<unsigned char*>(&lab32::g_Merchant);
    h.regions.push_back({h.donor, sizeof(lab32::g_Merchant)});
    unsigned char* guardTable = nullptr;
    unsigned char* merchantTable = nullptr;
    h.regions.push_back({h.object, h.objectSize});
    if (!dojo::ReadPtr(h, h.object, guardTable) || !dojo::ReadPtr(h, h.donor, merchantTable))
    {
        std::cout << "FAILED: no vptr\n";
        return 2;
    }
    h.regions.push_back({guardTable, lab32::kSlots * sizeof(void*), true});
    h.regions.push_back({merchantTable, lab32::kSlots * sizeof(void*), true});

    const int rc = dojo::Run(h);
    if (rc != 0)
    {
        std::cout << "FAILED: harness rc=" << rc << "\n";
        return rc;
    }
    for (const lab32::Guard& g : lab32::g_Guards)
    {
        const void* vptr = lab32::VptrOf(&g);
        bool known = vptr == guardTable || vptr == merchantTable;
        for (const std::vector<void*>& shadow : h.shadows)
        {
            if (vptr == static_cast<const void*>(shadow.data()))
            {
                if (shadow.size() < lab32::kSlots)
                {
                    std::cout << "FAILED: the shadow table is shorter than the class's " << lab32::kSlots << " slots\n";
                    return 1;
                }
                known = true;
            }
        }
        if (!known)
        {
            std::cout << "FAILED: a vptr points to unknown memory\n";
            return 2;
        }
    }
    if (!lab32::CheckWin())
    {
        std::cout << "FAILED: the bribe does not work for the Captain alone (through his own table)\n";
        return 1;
    }
    std::cout << lab32::MakeFlag() << "\n";
    return 0;
}
