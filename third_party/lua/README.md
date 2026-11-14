# third_party/lua — Lua 5.4.9 (unmodified sources)

| | |
| :--- | :--- |
| Version | Lua 5.4.9 (release 2026-08-10) |
| Source | `https://www.lua.org/ftp/lua-5.4.9.tar.gz` |
| SHA-256 | `2335b6c582a52654f94612bf10d2f4672805d05329aa6568b1d8cd9e5c6fb8e6` (matches the checksum published on the lua.org download page; size 373429 bytes) |
| License | MIT — see [`LICENSE`](./LICENSE) (copied verbatim from the notice at the end of `src/lua.h`) |
| Contents | `src/*.c`, `src/*.h`, `src/lua.hpp` from the tarball, byte-for-byte; the tarball's `Makefile`, `README` and `doc/` are not included |

Used only to embed Lua into the repo's **own** lab binaries (Lab 52 and later Lua labs). Built by
[`CMakeLists.txt`](./CMakeLists.txt) as the shared library `lua54` (on Windows `lua54.dll`, so an injected DLL can
reach the Lua API through `GetProcAddress`, like in games that ship a Lua DLL). `lua.c` and `luac.c` (the
standalone interpreter and compiler) are not built. Compiler warnings are silenced for this third-party target
only; the repo's `-Werror` applies to C++ lab code.

To update: download the new tarball from lua.org, compare its SHA-256 with the published one, replace `src/`,
update this table.
