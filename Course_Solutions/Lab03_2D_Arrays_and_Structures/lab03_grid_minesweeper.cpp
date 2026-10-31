// ============================================================================
// [Lab 03] Contiguous Structs & 2D Memory Grids (Tier E- | Difficulty: 1.3/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 02. Classic desktop games like Windows Minesweeper (winmine.exe)
//   store the entire game board as a contiguous 2D byte array in memory.
//   Instead of guessing where traps are, a reverse engineer opens Cheat Engine's
//   Hex Memory Viewer and reads the hidden board state directly from RAM!
//
// MEMORY MAP OF DUNGEON CELL BYTES:
//   0x00 = Unexplored Safe Tile
//   0x01 = Visited Safe Tile
//   0x77 = ANCIENT RELIC (Collect all 3 to win!)
//   0x8F = LETHAL SPIKE TRAP (Instant death if stepped on!)
// ============================================================================

#include <iostream>
#include <cstdint>
#include <iomanip>

#pragma pack(push, 1)
struct DungeonState {
    char     magicSignature[8]; // "DUNGEON"
    int32_t  playerRow;         // Offset +0x08
    int32_t  playerCol;         // Offset +0x0C
    int32_t  relicsCollected;   // Offset +0x10
    int32_t  stepsTaken;        // Offset +0x14
    uint8_t  board[6][6];       // Offset +0x18 (36 contiguous bytes!)
};
#pragma pack(pop)

DungeonState g_Dungeon = {
    "DUNGEON",
    0, 0, 0, 0,
    {
        { 0x01, 0x00, 0x8F, 0x00, 0x77, 0x00 },
        { 0x00, 0x8F, 0x00, 0x00, 0x8F, 0x00 },
        { 0x00, 0x77, 0x00, 0x8F, 0x00, 0x00 },
        { 0x8F, 0x00, 0x00, 0x00, 0x00, 0x8F },
        { 0x00, 0x00, 0x8F, 0x00, 0x77, 0x00 },
        { 0x00, 0x00, 0x00, 0x8F, 0x00, 0x00 }
    }
};

void RenderBoard(bool revealDebug) {
    std::cout << "\n    Col: 0   1   2   3   4   5\n";
    std::cout << "       +---+---+---+---+---+---+\n";
    for (int r = 0; r < 6; ++r) {
        std::cout << "Row " << r << "  |";
        for (int c = 0; c < 6; ++c) {
            if (r == g_Dungeon.playerRow && c == g_Dungeon.playerCol) {
                std::cout << " @ |";
            } else if (g_Dungeon.board[r][c] == 0x01) {
                std::cout << " . |";
            } else if (revealDebug) {
                uint8_t v = g_Dungeon.board[r][c];
                if (v == 0x8F) std::cout << " X |";
                else if (v == 0x77) std::cout << " $ |";
                else std::cout << "   |";
            } else {
                std::cout << " ? |";
            }
        }
        std::cout << "\n       +---+---+---+---+---+---+\n";
    }
}

int main() {
    std::cout << "Select Training Mode:\n  [1] Apprentice Mode (Shows Struct Base Address)\n  [2] Hardcore Mode (Blind)\n> ";
    int mode = 1;
    if (!(std::cin >> mode)) return 0;
    bool blind = (mode == 2);

    while (g_Dungeon.relicsCollected < 3) {
        std::cout << "\n====================================================================\n";
        std::cout << "  [LAB 03 | TIER E-] CRYPT OF MINESWEEPER (2D Grid & Structs)\n";
        std::cout << "====================================================================\n";
        std::cout << "  Player Coords : (Row " << g_Dungeon.playerRow << ", Col " << g_Dungeon.playerCol << ")\n";
        std::cout << "  Relics Found  : " << g_Dungeon.relicsCollected << " / 3\n";
        if (!blind) {
            std::cout << "  Struct Base   : 0x" << std::hex << std::uppercase << (uintptr_t)&g_Dungeon << "\n";
            std::cout << "  Board[6][6]   : 0x" << (uintptr_t)&g_Dungeon.board[0][0]
                      << " (Open in CE Memory Viewer! 0x77=Relic, 0x8F=Trap)\n" << std::dec;
        }
        RenderBoard(false);

        std::cout << "Move: [W] Up  [S] Down  [A] Left  [D] Right  [Q] Quit\n> ";
        char cmd;
        if (!(std::cin >> cmd)) break;
        if (cmd == 'q' || cmd == 'Q') return 0;

        int nr = g_Dungeon.playerRow;
        int nc = g_Dungeon.playerCol;
        if (cmd == 'w' || cmd == 'W') nr--;
        else if (cmd == 's' || cmd == 'S') nr++;
        else if (cmd == 'a' || cmd == 'A') nc--;
        else if (cmd == 'd' || cmd == 'D') nc++;

        if (nr < 0 || nr >= 6 || nc < 0 || nc >= 6) {
            std::cout << ">> Bump! Solid dungeon wall.\n";
            continue;
        }

        g_Dungeon.playerRow = nr;
        g_Dungeon.playerCol = nc;
        g_Dungeon.stepsTaken++;

        uint8_t tile = g_Dungeon.board[nr][nc];
        if (tile == 0x8F) {
            std::cout << "\n[KABOOM!] You stepped on a 0x8F Spike Trap at (" << nr << ", " << nc << ")!\n";
            std::cout << "Tip: Inspect the 36-byte board[6][6] in Cheat Engine's Hex View,\n";
            std::cout << "     or overwrite all 0x8F bytes in RAM with 0x00!\n";
            RenderBoard(true);
            return 0;
        } else if (tile == 0x77) {
            g_Dungeon.relicsCollected++;
            g_Dungeon.board[nr][nc] = 0x01;
            std::cout << "\n>> [RELIC FOUND!] Collected Ancient Relic (" << g_Dungeon.relicsCollected << "/3)!\n";
        } else {
            g_Dungeon.board[nr][nc] = 0x01;
        }
    }

    std::cout << "\n********************************************************************\n";
    std::cout << "  [QUEST COMPLETE - TIER E- CLEARED!]\n";
    std::cout << "  You read a live 2D byte array from RAM just like winmine.exe!\n";
    std::cout << "  Next Step: Proceed to Lab 04 (Dynamic Heap & Pointer Chains).\n";
    std::cout << "********************************************************************\n";
    return 0;
}
