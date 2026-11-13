cmake_minimum_required(VERSION 3.16)
project(ReDojo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# ============================================================================
# OPSEC & Privacy Compiler/Linker Hardening
# Strips local OS usernames/paths (C:\Users\<user>\...) & timestamps from PEs
# ============================================================================
if(MSVC)
    add_compile_options(/Brepro "/d1trimfile:${CMAKE_SOURCE_DIR}/")
    add_link_options(/INCREMENTAL:NO /Brepro /PDBALTPATH:%_PDB%)
elseif(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(
        "-ffile-prefix-map=${CMAKE_SOURCE_DIR}=."
        "-fdebug-prefix-map=${CMAKE_SOURCE_DIR}=."
    )
endif()

# Course Solutions (10 Progressive Game Hacking Labs)
add_executable(lab01_static_scalars       Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp)
add_executable(lab02_datatypes_bitmasks   Course_Solutions/Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp)
add_executable(lab03_grid_minesweeper     Course_Solutions/Lab03_2D_Arrays_and_Structures/lab03_grid_minesweeper.cpp)
add_executable(lab04_pointer_chains       Course_Solutions/Lab04_MultiLevel_Pointers/lab04_pointer_chains.cpp)
add_executable(lab05_code_injection       Course_Solutions/Lab05_Code_Injection_and_NOP/lab05_code_injection.cpp)
add_executable(lab06_shared_code          Course_Solutions/Lab06_Shared_Code_Disambiguation/lab06_shared_code.cpp)
add_executable(lab07_vtable_reclass       Course_Solutions/Lab07_ReClass_and_VMT_Hooking/lab07_vtable_reclass.cpp)
add_executable(lab08_3d_w2s_simulator     Course_Solutions/Lab08_3D_Math_and_WorldToScreen/lab08_3d_w2s_simulator.cpp)
add_executable(lab09_internal_hook_target Course_Solutions/Lab09_Internal_DLL_and_Hooks/lab09_internal_hook_target.cpp)
add_executable(lab10_integrity_boss       Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp)

# Crackmes and CTF (8 Progressive Keygenning & De-Obfuscation Targets)
add_executable(crackme01_strings          Crackmes_and_CTF/01_Apprentice_Gate/crackme01_strings.cpp)
add_executable(crackme02_serial_math      Crackmes_and_CTF/02_Mathematical_Lock/crackme02_serial_math.cpp)
add_executable(crackme03_xor_rol          Crackmes_and_CTF/03_XOR_and_Rol_Cipher/crackme03_xor_rol.cpp)
add_executable(crackme04_binary_license   Crackmes_and_CTF/04_Struct_License_File/crackme04_binary_license.cpp)
add_executable(crackme05_antidebug        Crackmes_and_CTF/05_AntiDebug_Sentinel/crackme05_antidebug.cpp)
add_executable(crackme06_bytecode_vm      Crackmes_and_CTF/06_Custom_Stack_VM/crackme06_bytecode_vm.cpp)
add_executable(crackme07_cff_mba          Crackmes_and_CTF/07_Control_Flow_Maze_and_MBA/crackme07_cff_mba.cpp)
add_executable(crackme08_z3_symbolic      Crackmes_and_CTF/08_Symbolic_Execution_Vault/crackme08_z3_symbolic.cpp)

# Tools and Scripts
if(WIN32)
    add_executable(external_memory_trainer Tools_and_Scripts/01_External_Trainer_Template/external_memory_trainer.cpp)
    add_library(internal_hook_lab09 SHARED Tools_and_Scripts/03_Internal_DLL_Skeleton/dllmain_internal_hook.cpp)
endif()

# ============================================================================
# Autocheck for new labs (docs/lab_plan.md, section 3):
#   build -> reference solution passes -> wrong input fails
#   cmake -S . -B build -G "Visual Studio 17 2022" -A x64
#   cmake --build build --config Release --parallel
#   ctest --test-dir build -C Release --output-on-failure
# Code style of new labs: Allman braces, Tools_and_Scripts/lab_template/.clang-format
# ============================================================================
enable_testing()
include(cmake/DojoLab.cmake)
add_test(NAME dojo_runner_selftest COMMAND ${Python3_EXECUTABLE} ${DOJO_LAB_RUNNER} selftest)
set_tests_properties(dojo_runner_selftest PROPERTIES LABELS "lab")

# New labs: one dojo_add_lab(...) per lab, in plan order.
