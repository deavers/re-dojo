// ============================================================================
// [Lab 39] .NET: Decompile Your Own C# Game (Tier C+ | Difficulty: 4.7/10)
// ============================================================================
// PURPOSE:
//   Builds on Lab 07. Managed code keeps almost everything a native binary loses:
//   type names, method names, readable control flow. Open Lab39.dll in a .NET
//   decompiler (dnSpyEx / ILSpy), find how the merchant forges his passphrase,
//   reproduce it, and say it. (Optional second path: patch the IL check in
//   dnSpyEx and save the module - not checked automatically.)
//
// Exit codes: 0 accepted (flag printed), 1 wrong passphrase, 2 empty or too long,
//             3 end of input.
// ============================================================================

using System;
using System.Text;

namespace ReDojo.Lab39
{
    internal static class Bazaar
    {
        // The passphrase is never stored as text: it is forged from these gears at run time.
        private static readonly int[] Gears = { 105, 127, 125, 99, 114, 9, 3, 30, 103, 15, 0, 45, 41, 50, 35 };

        private static string ForgePassphrase()
        {
            var chars = new char[Gears.Length];
            for (int i = 0; i < Gears.Length; i++)
            {
                chars[i] = (char)((Gears[i] ^ (0x2A + i * 5)) - i);
            }
            return new string(chars);
        }

        // The flag mixes a neutral tag with the accepted passphrase.
        private static string MakeFlag(string passphrase)
        {
            string seal = "lab39|" + passphrase;
            ulong h = 0xCBF29CE484222325UL;
            foreach (byte b in Encoding.ASCII.GetBytes(seal))
            {
                h ^= b;
                h *= 0x100000001B3UL;
            }
            return "FLAG{LAB39_" + h.ToString("X16") + "}";
        }

        private static int Main()
        {
            Console.WriteLine("====================================================================");
            Console.WriteLine("  [LAB 39 | TIER C+] THE CLOCKWORK BAZAAR (.NET Decompilation)");
            Console.WriteLine("====================================================================");
            Console.Write("The clockwork merchant waits for the passphrase: ");

            string? input = Console.ReadLine();
            if (input == null)
            {
                Console.WriteLine();
                Console.WriteLine(">> The merchant's gears stop turning.");
                return 3;
            }
            input = input.Trim();
            if (input.Length == 0 || input.Length > 64)
            {
                Console.WriteLine(">> [FAILED] Say something sensible.");
                return 2;
            }
            if (!string.Equals(input, ForgePassphrase(), StringComparison.Ordinal))
            {
                Console.WriteLine(">> [FAILED] Wrong passphrase. The merchant's code is not hidden - read it.");
                return 1;
            }
            Console.WriteLine();
            Console.WriteLine("********************************************************************");
            Console.WriteLine("  [QUEST COMPLETE - TIER C+ CLEARED!] The merchant opens his vault.");
            Console.WriteLine("  " + MakeFlag(input));
            Console.WriteLine("********************************************************************");
            return 0;
        }
    }
}
