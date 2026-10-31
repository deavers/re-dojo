// ============================================================================
// [Crackme 06] Custom Bytecode Stack Virtual Machine (Tier A | Diff: 6.8/10)
// ============================================================================
// SKILLS LEARNED:
//   Builds on Crackme 05. How do VMProtect, Themida, and game scripting VMs
//   (LuaJIT, QuakeC, GameMaker) work? Instead of compiling logic to native
//   x86_64 instructions, the logic is compiled into custom VM bytecode executed
//   by a Virtual Machine interpreter loop (`while (running) { switch(op) ... }`)!
//
// QUEST OBJECTIVE:
//   1. Locate the `VM_Interpreter` opcode table and `g_BytecodeProgram[]`.
//   2. Write a small Python disassembler (or use the starter script in
//      `Tools_and_Scripts/04_Python_RE_Toolkit`) to recover the 8-char password!
// ============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <cstdint>

enum VmOpcode : uint8_t {
    OP_PUSH_IMM   = 0x01, // Push next byte onto VM stack
    OP_PUSH_INPUT = 0x02, // Push user input[imm] onto VM stack
    OP_ADD        = 0x10, // Pop A, Pop B -> Push (B + A) & 0xFF
    OP_XOR        = 0x11, // Pop A, Pop B -> Push (B ^ A) & 0xFF
    OP_ROL3       = 0x12, // Pop A -> Push ROL8(A, 3)
    OP_ASSERT_EQ  = 0x20, // Pop A, Pop B -> If A != B, fail VM!
    OP_HALT_WIN   = 0xFF  // All checks passed!
};

static inline uint8_t VmRol3(uint8_t v) {
    return static_cast<uint8_t>((v << 3) | (v >> 5));
}

// Each 7-byte block validates 1 character of the 8-byte secret key ("VM_KING!")
// Transform: ((input[i] ^ key1) + key2) & 0xFF == expected
static const uint8_t g_BytecodeProgram[] = {
    // Char 0: ('V' ^ 0x12) + 0x05 == (0x56 ^ 0x12) + 5 = 0x44 + 5 = 0x49
    OP_PUSH_INPUT, 0x00, OP_PUSH_IMM, 0x12, OP_XOR, OP_PUSH_IMM, 0x05, OP_ADD, OP_PUSH_IMM, 0x49, OP_ASSERT_EQ,
    // Char 1: ('M' ^ 0x23) + 0x07 == (0x4D ^ 0x23) + 7 = 0x6E + 7 = 0x75
    OP_PUSH_INPUT, 0x01, OP_PUSH_IMM, 0x23, OP_XOR, OP_PUSH_IMM, 0x07, OP_ADD, OP_PUSH_IMM, 0x75, OP_ASSERT_EQ,
    // Char 2: ('_' ^ 0x34) + 0x09 == (0x5F ^ 0x34) + 9 = 0x6B + 9 = 0x74
    OP_PUSH_INPUT, 0x02, OP_PUSH_IMM, 0x34, OP_XOR, OP_PUSH_IMM, 0x09, OP_ADD, OP_PUSH_IMM, 0x74, OP_ASSERT_EQ,
    // Char 3: ('K' ^ 0x45) + 0x0B == (0x4B ^ 0x45) + 11 = 0x0E + 11 = 0x19
    OP_PUSH_INPUT, 0x03, OP_PUSH_IMM, 0x45, OP_XOR, OP_PUSH_IMM, 0x0B, OP_ADD, OP_PUSH_IMM, 0x19, OP_ASSERT_EQ,
    // Char 4: ('I' ^ 0x56) + 0x0D == (0x49 ^ 0x56) + 13 = 0x1F + 13 = 0x2C
    OP_PUSH_INPUT, 0x04, OP_PUSH_IMM, 0x56, OP_XOR, OP_PUSH_IMM, 0x0D, OP_ADD, OP_PUSH_IMM, 0x2C, OP_ASSERT_EQ,
    // Char 5: ('N' ^ 0x67) + 0x0F == (0x4E ^ 0x67) + 15 = 0x29 + 15 = 0x38
    OP_PUSH_INPUT, 0x05, OP_PUSH_IMM, 0x67, OP_XOR, OP_PUSH_IMM, 0x0F, OP_ADD, OP_PUSH_IMM, 0x38, OP_ASSERT_EQ,
    // Char 6: ('G' ^ 0x78) + 0x11 == (0x47 ^ 0x78) + 17 = 0x3F + 17 = 0x50
    OP_PUSH_INPUT, 0x06, OP_PUSH_IMM, 0x78, OP_XOR, OP_PUSH_IMM, 0x11, OP_ADD, OP_PUSH_IMM, 0x50, OP_ASSERT_EQ,
    // Char 7: ('!' ^ 0x19) + 0x03 == (0x21 ^ 0x19) + 3 = 0x38 + 3 = 0x3B
    OP_PUSH_INPUT, 0x07, OP_PUSH_IMM, 0x19, OP_XOR, OP_PUSH_IMM, 0x03, OP_ADD, OP_PUSH_IMM, 0x3B, OP_ASSERT_EQ,

    OP_HALT_WIN
};

bool ExecuteVirtualMachine(const std::string& userInput) {
    if (userInput.size() != 8) return false;

    std::vector<uint8_t> stack;
    size_t vip = 0; // Virtual Instruction Pointer (VIP)

    while (vip < sizeof(g_BytecodeProgram)) {
        uint8_t opcode = g_BytecodeProgram[vip++];
        switch (opcode) {
            case OP_PUSH_IMM: {
                stack.push_back(g_BytecodeProgram[vip++]);
                break;
            }
            case OP_PUSH_INPUT: {
                uint8_t idx = g_BytecodeProgram[vip++];
                stack.push_back(static_cast<uint8_t>(userInput[idx]));
                break;
            }
            case OP_ADD: {
                uint8_t a = stack.back(); stack.pop_back();
                uint8_t b = stack.back(); stack.pop_back();
                stack.push_back(static_cast<uint8_t>((b + a) & 0xFF));
                break;
            }
            case OP_XOR: {
                uint8_t a = stack.back(); stack.pop_back();
                uint8_t b = stack.back(); stack.pop_back();
                stack.push_back(static_cast<uint8_t>(b ^ a));
                break;
            }
            case OP_ROL3: {
                uint8_t a = stack.back(); stack.pop_back();
                stack.push_back(VmRol3(a));
                break;
            }
            case OP_ASSERT_EQ: {
                uint8_t expected = stack.back(); stack.pop_back();
                uint8_t actual   = stack.back(); stack.pop_back();
                if (actual != expected) return false;
                break;
            }
            case OP_HALT_WIN:
                return true;
            default:
                return false;
        }
    }
    return false;
}

int main() {
    std::cout << "====================================================================\n";
    std::cout << "  [CRACKME 06 | TIER A] THE VIRTUAL MACHINE (Custom Stack Bytecode)\n";
    std::cout << "====================================================================\n";
    std::cout << "Enter 8-character VM Authorization Key: ";

    std::string input;
    std::cin >> input;

    if (ExecuteVirtualMachine(input)) {
        std::cout << "\n********************************************************************\n";
        std::cout << "  [CRACKME 06 SOLVED - TIER A CLEARED!]\n";
        std::cout << "  You reversed a Custom Stack Virtual Machine! Key: FLAG{" << input << "}\n";
        std::cout << "  Next Challenge: Crackme 07 (O-LLVM Control-Flow Flattening & MBA).\n";
        std::cout << "********************************************************************\n";
        return 0;
    } else {
        std::cout << ">> [VM EXCEPTION] Virtual Machine assertion failed! Disassemble g_BytecodeProgram[]!\n";
        return 1;
    }
}
