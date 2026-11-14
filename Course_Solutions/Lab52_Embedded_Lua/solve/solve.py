"""[Lab 52] Reference solution (SPOILER). Commands for check/lab52_selftest.

g_Engine +0x10 holds the game's lua_State*. An injected DLL (see Lab 09) would do:
  L   = *(lua_State**)((char*)&g_Engine + 0x10);        // address of g_Engine: pattern scan / pointer scan
  load = GetProcAddress(GetModuleHandleA("lua54.dll"), "luaL_loadstring");
  call = GetProcAddress(GetModuleHandleA("lua54.dll"), "lua_pcallk");
  load(L, CODE); call(L, 0, 0, 0, 0, NULL);
The selftest models exactly that with "luado <offset> <code>".
"""

CODE = 'hero.gold = 1000000; hero.title = "Archmage"'


def answer() -> str:
    return f"luado 0x10 {CODE}\n"


WRONG = [
    # +0x08 is flags/turn, not the lua_State pointer: rejected before anything is dereferenced.
    f"luado 0x08 {CODE}\n",
    # Too much gold: the Guild wants exactly 1000000.
    'luado 0x10 hero.gold = 2000000; hero.title = "Archmage"\n',
    # Not enough gold.
    'luado 0x10 hero.gold = 999999; hero.title = "Archmage"\n',
    # New globals instead of the hero table's fields.
    'luado 0x10 gold = 1000000; title = "Archmage"\n',
    # Gold as a string: the Guild checks the type.
    'luado 0x10 hero.gold = "1000000"; hero.title = "Archmage"\n',
    # The sandbox has no os library: a Lua error, not an escape.
    "luado 0x10 os.exit(0)\n",
    # Lua syntax error.
    "luado 0x10 hero.gold = \n",
]
