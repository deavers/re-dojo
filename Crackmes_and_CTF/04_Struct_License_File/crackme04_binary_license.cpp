// ============================================================================
// [Crackme 04] Binary File Format & Struct Auditing (Tier C | Diff: 4.3/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 03. Many desktop programs (WinRAR, Sublime, game saves,
//   custom archives) validate a binary file on disk rather than a text string.
//   You will reverse engineer the exact byte layout of `license.dat` (a packed
//   24-byte C structure) and write a Python generator using `struct.pack`!
// ============================================================================

#include <iostream>
#include <fstream>
#include <cstdint>
#include <iomanip>

#pragma pack(push, 1)
struct BinaryLicenseHeader {
    uint32_t magic;        // +0x00: Must be 0x56414544 ("DEAV" in little-endian)
    uint16_t version;      // +0x04: Must be 0x0104 (v1.4)
    uint16_t tierBadge;    // +0x06: Must be 0x0777
    uint64_t citizenId;    // +0x08: Must be >= 0x00000000000186A0 (100,000)
    uint32_t featureFlags; // +0x10: Must have bits 0x80000000 and 0x0000002A set
    uint32_t crcTag;       // +0x14: Must equal (magic ^ (uint32_t)citizenId ^ featureFlags ^ 0xA5A5A5A5)
};
#pragma pack(pop)

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 04 | TIER C] THE ROYAL ARCHIVE (Binary File Format RE)\n";
    std::cout << "====================================================================\n";
    std::cout << "Looking for binary license file: ./license.dat (24 bytes)...\n";

    std::ifstream file("license.dat", std::ios::binary | std::ios::ate);
    if (!file.is_open()) {
        std::cout << ">> [ERROR] `license.dat` not found in current directory!\n";
        std::cout << "   Disassemble this binary in Ghidra to reconstruct the 24-byte\n";
        std::cout << "   `BinaryLicenseHeader` struct and craft `license.dat` with Python!\n";
        return 1;
    }

    std::streamsize size = file.tellg();
    if (size != sizeof(BinaryLicenseHeader)) {
        std::cout << ">> [INVALID SIZE] Expected exactly " << sizeof(BinaryLicenseHeader)
                  << " bytes, got " << size << " bytes.\n";
        return 1;
    }

    file.seekg(0, std::ios::beg);
    BinaryLicenseHeader hdr{};
    file.read(reinterpret_cast<char*>(&hdr), sizeof(hdr));

    if (hdr.magic != 0x56414544U) {
        std::cout << ">> [CHECK 1 FAILED] Invalid Magic Header (0x" << std::hex << hdr.magic << ")!\n";
        return 1;
    }
    if (hdr.version != 0x0104U || hdr.tierBadge != 0x0777U) {
        std::cout << ">> [CHECK 2 FAILED] Invalid Version or TierBadge field!\n";
        return 1;
    }
    if (hdr.citizenId < 100000ULL) {
        std::cout << ">> [CHECK 3 FAILED] CitizenId must be >= 100,000!\n";
        return 1;
    }
    const uint32_t reqBits = 0x8000002AU;
    if ((hdr.featureFlags & reqBits) != reqBits) {
        std::cout << ">> [CHECK 4 FAILED] Required FeatureFlags bits are not set!\n";
        return 1;
    }
    uint32_t expectedCrc = hdr.magic ^ static_cast<uint32_t>(hdr.citizenId & 0xFFFFFFFFULL)
                         ^ hdr.featureFlags ^ 0xA5A5A5A5U;
    if (hdr.crcTag != expectedCrc) {
        std::cout << ">> [CHECK 5 FAILED] Checksum mismatch! Expected 0x"
                  << std::hex << expectedCrc << ", got 0x" << hdr.crcTag << std::dec << "\n";
        return 1;
    }

    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 04 SOLVED - TIER C CLEARED!]\n";
    std::cout << "  Valid `license.dat` forged for Citizen ID #" << hdr.citizenId << "!\n";
    std::cout << "  Next Challenge: Crackme 05 (User-Mode Anti-Debugging Sentinel).\n";
    std::cout << "********************************************************************\n";
    return 0;
}
