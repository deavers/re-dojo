// [Lab 45] Dump checker: reads "seed <N>" (printed by the game) and a learner's dump from stdin, builds the
// pool for that seed in its own memory and compares.
// Input: first non-empty line "seed <N>" (decimal), then one entry per line "<FName index in hex> <name>",
// any order. Exit: 0 dump complete and correct (flag), 1 wrong / incomplete dump, 2 malformed input.
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include "lab45_core.hpp"

static bool NextLine(std::string& line)
{
    while (std::getline(std::cin, line))
    {
        if (!line.empty() && line.back() == '\r')
        {
            line.pop_back();
        }
        if (!line.empty())
        {
            return true;
        }
    }
    return false;
}

int main()
{
    std::string line;
    std::uint32_t seed = 0;
    {
        if (!NextLine(line))
        {
            std::cout << "FAILED: no seed line\n";
            return 2;
        }
        std::istringstream in(line);
        std::string word, num, extra;
        if (!(in >> word >> num) || word != "seed" || (in >> extra))
        {
            std::cout << "FAILED: the first line must be 'seed <N>'\n";
            return 2;
        }
        try
        {
            seed = static_cast<std::uint32_t>(std::stoul(num, nullptr, 10));
        }
        catch (const std::exception&)
        {
            std::cout << "FAILED: bad seed\n";
            return 2;
        }
    }
    lab45::BuildPool(seed);

    // Truth: walk every chunk from the start, entry by entry, until an empty header.
    std::vector<std::pair<std::uint32_t, std::string>> truth;
    for (std::uint32_t c = 0; c <= lab45::g_NamePool.currentChunk; ++c)
    {
        std::uint32_t off = 0;
        while (off + 2 <= lab45::kChunkSize)
        {
            const std::uint32_t index = (c << 16) | (off / lab45::kStride);
            const std::string name = lab45::Resolve(index);
            if (name.empty())
            {
                break;
            }
            truth.emplace_back(index, name);
            off += (2 + static_cast<std::uint32_t>(name.size()) + 1) & ~1u;
        }
    }

    std::vector<std::pair<std::uint32_t, std::string>> dump;
    while (NextLine(line))
    {
        std::istringstream in(line);
        std::string idx, name, extra;
        if (!(in >> idx >> name) || (in >> extra))
        {
            std::cout << "FAILED: malformed line\n";
            return 2;
        }
        try
        {
            dump.emplace_back(static_cast<std::uint32_t>(std::stoul(idx, nullptr, 16)), name);
        }
        catch (const std::exception&)
        {
            std::cout << "FAILED: bad index\n";
            return 2;
        }
    }
    std::sort(dump.begin(), dump.end());
    std::sort(truth.begin(), truth.end());
    if (dump != truth)
    {
        std::cout << "FAILED: the dump does not match the pool of seed " << seed << " (" << dump.size() << " vs "
                  << truth.size() << " entries)\n";
        return 1;
    }
    std::cout << lab45::MakeFlag(seed) << "\n";
    return 0;
}
