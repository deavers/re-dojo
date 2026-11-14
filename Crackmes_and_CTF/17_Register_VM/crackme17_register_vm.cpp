// ============================================================================
// [Crackme 17] The Register Machine (Tier S- | Difficulty: 7.4/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 06 (stack VM). This VM has four 32-bit registers, a
//   compare flag and an absolute jump. The key check is not C++ code at all:
//   it is bytecode. Find the dispatch loop, recover what each opcode does,
//   write a disassembler for the program, and invert the checks - each one
//   depends on the result of the previous one through an accumulator register.
//
// Input: an 8-character key.
// Exit codes: 0 accepted (flag printed), 1 rejected by the bytecode, 2 wrong length
//             or a broken program, 3 end of input.
// ============================================================================

#include <iostream>
#include <cstddef>
#include <cstdint>
#include <string>

namespace
{

enum Op : std::uint8_t
{
    kLdi = 0x10,  // LDI  r, imm32   r = imm32 (little-endian)
    kLdb = 0x11,  // LDB  r, idx     r = input[idx]
    kAdd = 0x20,  // ADD  a, b       a = a + b
    kXor = 0x21,  // XOR  a, b       a = a ^ b
    kMov = 0x24,  // MOV  a, b       a = b
    kCmp = 0x30,  // CMP  a, b       flag = (a == b)
    kJne = 0x31,  // JNE  addr16     if !flag: pc = addr16
    kOk = 0x40,   // HALT_OK
    kFail = 0x41, // HALT_FAIL
};

const std::uint8_t kProgram[] = {
    0x10, 0x02, 0x34, 0x12, 0x00, 0x00, 0x11, 0x00, 0x00, 0x10, 0x01, 0x5A,
    0x00, 0x00, 0x00, 0x21, 0x00, 0x01, 0x20, 0x00, 0x02, 0x10, 0x03, 0x3C,
    0x12, 0x00, 0x00, 0x30, 0x00, 0x03, 0x31, 0xF7, 0x00, 0x24, 0x02, 0x00,
    0x11, 0x00, 0x01, 0x10, 0x01, 0x77, 0x00, 0x00, 0x00, 0x21, 0x00, 0x01,
    0x20, 0x00, 0x02, 0x10, 0x03, 0x80, 0x12, 0x00, 0x00, 0x30, 0x00, 0x03,
    0x31, 0xF7, 0x00, 0x24, 0x02, 0x00, 0x11, 0x00, 0x02, 0x10, 0x01, 0x94,
    0x00, 0x00, 0x00, 0x21, 0x00, 0x01, 0x20, 0x00, 0x02, 0x10, 0x03, 0x53,
    0x13, 0x00, 0x00, 0x30, 0x00, 0x03, 0x31, 0xF7, 0x00, 0x24, 0x02, 0x00,
    0x11, 0x00, 0x03, 0x10, 0x01, 0xB1, 0x00, 0x00, 0x00, 0x21, 0x00, 0x01,
    0x20, 0x00, 0x02, 0x10, 0x03, 0xD3, 0x13, 0x00, 0x00, 0x30, 0x00, 0x03,
    0x31, 0xF7, 0x00, 0x24, 0x02, 0x00, 0x11, 0x00, 0x04, 0x10, 0x01, 0xCE,
    0x00, 0x00, 0x00, 0x21, 0x00, 0x01, 0x20, 0x00, 0x02, 0x10, 0x03, 0x70,
    0x14, 0x00, 0x00, 0x30, 0x00, 0x03, 0x31, 0xF7, 0x00, 0x24, 0x02, 0x00,
    0x11, 0x00, 0x05, 0x10, 0x01, 0xEB, 0x00, 0x00, 0x00, 0x21, 0x00, 0x01,
    0x20, 0x00, 0x02, 0x10, 0x03, 0x2F, 0x15, 0x00, 0x00, 0x30, 0x00, 0x03,
    0x31, 0xF7, 0x00, 0x24, 0x02, 0x00, 0x11, 0x00, 0x06, 0x10, 0x01, 0x08,
    0x00, 0x00, 0x00, 0x21, 0x00, 0x01, 0x20, 0x00, 0x02, 0x10, 0x03, 0x89,
    0x15, 0x00, 0x00, 0x30, 0x00, 0x03, 0x31, 0xF7, 0x00, 0x24, 0x02, 0x00,
    0x11, 0x00, 0x07, 0x10, 0x01, 0x25, 0x00, 0x00, 0x00, 0x21, 0x00, 0x01,
    0x20, 0x00, 0x02, 0x10, 0x03, 0xA6, 0x15, 0x00, 0x00, 0x30, 0x00, 0x03,
    0x31, 0xF7, 0x00, 0x24, 0x02, 0x00, 0x40, 0x41,
};

constexpr std::size_t kKeyLength = 8;

// Returns 0 accepted, 1 rejected, 2 broken program (out-of-range operand or pc).
int RunVm(const std::string& input)
{
    std::uint32_t reg[4] = {};
    bool flag = false;
    std::size_t pc = 0;
    const std::size_t n = sizeof(kProgram);
    const auto need = [&](std::size_t bytes) { return pc + bytes <= n; };
    for (int steps = 0; steps < 10000; ++steps)
    {
        if (!need(1))
        {
            return 2;
        }
        const std::uint8_t op = kProgram[pc];
        if (op == kOk)
        {
            return 0;
        }
        if (op == kFail)
        {
            return 1;
        }
        if (op == kLdi && need(6) && kProgram[pc + 1] < 4)
        {
            reg[kProgram[pc + 1]] = static_cast<std::uint32_t>(kProgram[pc + 2]) |
                                    (static_cast<std::uint32_t>(kProgram[pc + 3]) << 8) |
                                    (static_cast<std::uint32_t>(kProgram[pc + 4]) << 16) |
                                    (static_cast<std::uint32_t>(kProgram[pc + 5]) << 24);
            pc += 6;
        }
        else if (op == kLdb && need(3) && kProgram[pc + 1] < 4 && kProgram[pc + 2] < input.size())
        {
            reg[kProgram[pc + 1]] = static_cast<std::uint8_t>(input[kProgram[pc + 2]]);
            pc += 3;
        }
        else if ((op == kAdd || op == kXor || op == kMov || op == kCmp) && need(3) && kProgram[pc + 1] < 4 &&
                 kProgram[pc + 2] < 4)
        {
            std::uint32_t& a = reg[kProgram[pc + 1]];
            const std::uint32_t b = reg[kProgram[pc + 2]];
            if (op == kAdd)
            {
                a = a + b;
            }
            else if (op == kXor)
            {
                a = a ^ b;
            }
            else if (op == kMov)
            {
                a = b;
            }
            else
            {
                flag = (a == b);
            }
            pc += 3;
        }
        else if (op == kJne && need(3))
        {
            const std::size_t target = static_cast<std::size_t>(kProgram[pc + 1]) |
                                       (static_cast<std::size_t>(kProgram[pc + 2]) << 8);
            pc = flag ? pc + 3 : target;
        }
        else
        {
            return 2;
        }
    }
    return 2;
}

} // namespace

int main()
{
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 17 | TIER S-] THE REGISTER MACHINE\n";
    std::cout << "====================================================================\n";
    std::cout << "Feed the machine an 8-character key: ";

    std::string key;
    if (!(std::cin >> key))
    {
        std::cout << "\n>> The machine idles.\n";
        return 3;
    }
    if (key.size() != kKeyLength)
    {
        std::cout << ">> [FAILED] The machine accepts exactly 8 characters.\n";
        return 2;
    }
    const int rc = RunVm(key);
    if (rc != 0)
    {
        std::cout << ">> [FAILED] HALT_FAIL. Disassemble the bytecode and follow the registers.\n";
        return rc;
    }
    std::cout << "\n********************************************************************\n";
    std::cout << "  [CRACKME 17 SOLVED - TIER S- CLEARED!]\n";
    std::cout << "  FLAG{" << key << "}\n";
    std::cout << "********************************************************************\n";
    return 0;
}
