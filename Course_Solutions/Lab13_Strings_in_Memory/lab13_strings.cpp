// ============================================================================
// [Lab 13] Strings in Memory (Tier E-- | Difficulty: 0.8/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 12. Text in memory is not always plain ASCII. Learn to scan
//   for UTF-16 strings (Cheat Engine: "String" + "UTF-16"), and to edit a
//   length-prefixed string where a separate byte says how many letters count.
//
// QUEST OBJECTIVES (the Hall of Legends admits you when BOTH are true):
//   1. Hero name is DRAGONSLAYER   (UTF-16; the rename menu only allows 8 letters)
//   2. Guild tag is DOJO           (length-prefixed ASCII; the menu only allows 3)
//
// Exit codes: 0 admitted (flag printed), 3 quit / end of input.
// ============================================================================

#include <iostream>
#include <cstdint>
#include <cstring>
#include <string>

#include "lab13_core.hpp"

using lab13::g_Card;

static bool g_BlindMode = false;

static void PrintAddress(const void* p)
{
    if (!g_BlindMode)
    {
        std::cout << "   [Addr: 0x" << std::hex << std::uppercase << reinterpret_cast<std::uintptr_t>(p) << std::dec
                  << "]";
    }
}

static void PrintState()
{
    std::cout << "\n====================================================================\n";
    std::cout << "  [LAB 13 | TIER E--] THE HALL OF LEGENDS (Strings in Memory)\n";
    std::cout << "====================================================================\n";
    std::cout << "   Hero name (UTF-16)        : " << lab13::NameAscii(g_Card);
    PrintAddress(&g_Card.heroName);
    std::cout << "\n   Guild tag (length-prefix) : [" << lab13::TagAscii(g_Card) << "]";
    PrintAddress(&g_Card.tagLength);
    std::cout << "\n--------------------------------------------------------------------\n";
    std::cout << "  The Hall admits only DRAGONSLAYER of guild [DOJO].\n";
}

static bool IsUpperAscii(const std::string& s)
{
    for (const char c : s)
    {
        if (c < 'A' || c > 'Z')
        {
            return false;
        }
    }
    return !s.empty();
}

int main()
{
    std::cout << "Select Training Mode:\n";
    std::cout << "  [1] Apprentice Mode (Shows memory addresses on screen)\n";
    std::cout << "  [2] Hardcore Mode   (Hides addresses - pure Cheat Engine scan)\n> ";
    int mode = 1;
    if (!(std::cin >> mode))
    {
        return 3;
    }
    g_BlindMode = (mode == 2);

    while (true)
    {
        PrintState();
        std::cout << "Actions:\n";
        std::cout << "  [1] Rename hero      (A-Z, at most 8 letters)\n";
        std::cout << "  [2] Change guild tag (A-Z, at most 3 letters)\n";
        std::cout << "  [9] Knock on the Hall of Legends\n";
        std::cout << "  [0] Quit\n> ";
        int choice = 0;
        if (!(std::cin >> choice) || choice == 0)
        {
            std::cout << "You walk away from the Hall.\n";
            return 3;
        }
        if (choice == 1 || choice == 2)
        {
            std::cout << "New text: ";
            std::string text;
            if (!(std::cin >> text))
            {
                return 3;
            }
            const std::size_t limit = (choice == 1) ? lab13::kMaxNameInGame : lab13::kMaxTagInGame;
            if (!IsUpperAscii(text) || text.size() > limit)
            {
                std::cout << ">> Rejected: A-Z only, at most " << limit << " letters.\n";
            }
            else if (choice == 1)
            {
                std::memset(g_Card.heroName, 0, sizeof(g_Card.heroName));
                for (std::size_t i = 0; i < text.size(); ++i)
                {
                    g_Card.heroName[i] = static_cast<char16_t>(text[i]);
                }
            }
            else
            {
                std::memset(g_Card.guildTag, 0, sizeof(g_Card.guildTag));
                std::memcpy(g_Card.guildTag, text.data(), text.size());
                g_Card.tagLength = static_cast<std::uint8_t>(text.size());
            }
        }
        if (lab13::CheckWin(g_Card))
        {
            std::cout << "\n********************************************************************\n";
            std::cout << "  [QUEST COMPLETE - TIER E-- CLEARED!] The Hall of Legends opens.\n";
            std::cout << "  " << lab13::MakeFlag() << "\n";
            std::cout << "********************************************************************\n";
            return 0;
        }
        if (choice == 9)
        {
            std::cout << ">> The doorman shakes his head. Check how both texts are stored.\n";
        }
    }
}
