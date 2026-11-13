// [Lab 32] CTest harness: the guards array is the root object, the Merchant is the donor, and both
// original tables are registered READ-ONLY (in a real binary they live in .rdata). vcopy / vset from
// stdin build a shadow VMT, then the bribe is checked.
// Exit: 0 bribe accepted (flag), 1 refused / Marshal notices, 2 malformed command or not allowed.
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
    if (!lab32::CheckWin())
    {
        std::cout << "FAILED: the bribe does not work for the Captain alone\n";
        return 1;
    }
    std::cout << lab32::MakeFlag() << "\n";
    return 0;
}
