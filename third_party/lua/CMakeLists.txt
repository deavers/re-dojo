# Lua 5.4.9 as the shared library lua54 (third-party, unmodified sources; see README.md).
enable_language(C)

file(GLOB LUA54_SOURCES ${CMAKE_CURRENT_SOURCE_DIR}/src/*.c)
list(REMOVE_ITEM LUA54_SOURCES
     ${CMAKE_CURRENT_SOURCE_DIR}/src/lua.c
     ${CMAKE_CURRENT_SOURCE_DIR}/src/luac.c)

add_library(lua54 SHARED ${LUA54_SOURCES})
set_target_properties(lua54 PROPERTIES C_STANDARD 99 C_STANDARD_REQUIRED ON)
target_include_directories(lua54 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
# LUA_BUILD_AS_DLL: dllexport while building lua54.dll, dllimport for the labs that link it. Windows only:
# luaconf.h expands it to __declspec unconditionally, and a Linux .so exports its symbols by default.
if(WIN32)
    target_compile_definitions(lua54 PUBLIC LUA_BUILD_AS_DLL)
endif()
if(UNIX)
    target_compile_definitions(lua54 PRIVATE LUA_USE_POSIX)
    target_link_libraries(lua54 PRIVATE m)
endif()
# Third-party code: no warnings from it (the repo's -Werror is for its own C++ only).
if(MSVC)
    target_compile_options(lua54 PRIVATE /W0)
else()
    target_compile_options(lua54 PRIVATE -w)
endif()
