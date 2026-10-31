@echo off
setlocal enabledelayedexpansion

echo ============================================================================
echo   RE:DOJO - Hardened OPSEC Build Script (MSVC / MinGW)
echo ============================================================================

if not exist "build\bin" mkdir "build\bin"
if not exist "build\obj" mkdir "build\obj"

:: Try to locate MSVC vcvars64.bat via vswhere
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "%VSWHERE%" (
    for /f "usebackq tokens=*" %%i in (`"%VSWHERE%" -latest -property installationPath`) do (
        set "VSINSTALL=%%i"
    )
)

where cl.exe >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if defined VSINSTALL (
        if exist "!VSINSTALL!\VC\Auxiliary\Build\vcvars64.bat" (
            echo [*] Initializing Visual Studio x64 Developer Environment...
            call "!VSINSTALL!\VC\Auxiliary\Build\vcvars64.bat" >nul
        )
    )
)

where cl.exe >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [+] Compiling with MSVC cl.exe ^(x64, OPSEC Path-Stripped ^& Deterministic PE^)...
    set "CFLAGS=/nologo /EHsc /std:c++20 /O1 /Brepro /Fo:build\obj\"
    set "LFLAGS=/link /INCREMENTAL:NO /Brepro /PDBALTPATH:%%_PDB%%"

    cl !CFLAGS! "Course_Solutions\Lab01_Static_Scalars\lab01_static_scalars.cpp" /Fe:build\bin\lab01_static_scalars.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab02_Data_Types_and_Bitmasks\lab02_datatypes_bitmasks.cpp" /Fe:build\bin\lab02_datatypes_bitmasks.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab03_2D_Arrays_and_Structures\lab03_grid_minesweeper.cpp" /Fe:build\bin\lab03_grid_minesweeper.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab04_MultiLevel_Pointers\lab04_pointer_chains.cpp" /Fe:build\bin\lab04_pointer_chains.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab05_Code_Injection_and_NOP\lab05_code_injection.cpp" /Fe:build\bin\lab05_code_injection.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab06_Shared_Code_Disambiguation\lab06_shared_code.cpp" /Fe:build\bin\lab06_shared_code.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab07_ReClass_and_VMT_Hooking\lab07_vtable_reclass.cpp" /Fe:build\bin\lab07_vtable_reclass.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab08_3D_Math_and_WorldToScreen\lab08_3d_w2s_simulator.cpp" /Fe:build\bin\lab08_3d_w2s_simulator.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab09_Internal_DLL_and_Hooks\lab09_internal_hook_target.cpp" /Fe:build\bin\lab09_internal_hook_target.exe !LFLAGS!
    cl !CFLAGS! "Course_Solutions\Lab10_Integrity_and_AntiTamper_Boss\lab10_integrity_boss.cpp" /Fe:build\bin\lab10_integrity_boss.exe !LFLAGS!

    cl !CFLAGS! "Crackmes_and_CTF\01_Apprentice_Gate\crackme01_strings.cpp" /Fe:build\bin\crackme01_strings.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\02_Mathematical_Lock\crackme02_serial_math.cpp" /Fe:build\bin\crackme02_serial_math.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\03_XOR_and_Rol_Cipher\crackme03_xor_rol.cpp" /Fe:build\bin\crackme03_xor_rol.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\04_Struct_License_File\crackme04_binary_license.cpp" /Fe:build\bin\crackme04_binary_license.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\05_AntiDebug_Sentinel\crackme05_antidebug.cpp" /Fe:build\bin\crackme05_antidebug.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\06_Custom_Stack_VM\crackme06_bytecode_vm.cpp" /Fe:build\bin\crackme06_bytecode_vm.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\07_Control_Flow_Maze_and_MBA\crackme07_cff_mba.cpp" /Fe:build\bin\crackme07_cff_mba.exe !LFLAGS!
    cl !CFLAGS! "Crackmes_and_CTF\08_Symbolic_Execution_Vault\crackme08_z3_symbolic.cpp" /Fe:build\bin\crackme08_z3_symbolic.exe !LFLAGS!

    cl !CFLAGS! "Tools_and_Scripts\01_External_Trainer_Template\external_memory_trainer.cpp" /Fe:build\bin\external_memory_trainer.exe !LFLAGS!
    cl /nologo /LD /EHsc /std:c++20 /Brepro /Fo:build\obj\ "Tools_and_Scripts\03_Internal_DLL_Skeleton\dllmain_internal_hook.cpp" /Fe:build\bin\internal_hook_lab09.dll !LFLAGS!

    echo.
    echo [+] All 10 Course Labs, 8 Crackmes, External Trainer, and Internal DLL built cleanly in build\bin\!
    goto :eof
)

where g++.exe >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [+] Compiling with MinGW g++ ^(OPSEC Path-Stripped^)...
    set "GFLAGS=-std=c++20 -O1 -ffile-prefix-map=.= -fdebug-prefix-map=.="
    g++ !GFLAGS! "Course_Solutions/Lab01_Static_Scalars/lab01_static_scalars.cpp" -o "build/bin/lab01_static_scalars.exe"
    g++ !GFLAGS! "Course_Solutions/Lab02_Data_Types_and_Bitmasks/lab02_datatypes_bitmasks.cpp" -o "build/bin/lab02_datatypes_bitmasks.exe"
    g++ !GFLAGS! "Course_Solutions/Lab03_2D_Arrays_and_Structures/lab03_grid_minesweeper.cpp" -o "build/bin/lab03_grid_minesweeper.exe"
    g++ !GFLAGS! "Course_Solutions/Lab04_MultiLevel_Pointers/lab04_pointer_chains.cpp" -o "build/bin/lab04_pointer_chains.exe"
    g++ !GFLAGS! "Course_Solutions/Lab05_Code_Injection_and_NOP/lab05_code_injection.cpp" -o "build/bin/lab05_code_injection.exe"
    g++ !GFLAGS! "Course_Solutions/Lab06_Shared_Code_Disambiguation/lab06_shared_code.cpp" -o "build/bin/lab06_shared_code.exe"
    g++ !GFLAGS! "Course_Solutions/Lab07_ReClass_and_VMT_Hooking/lab07_vtable_reclass.cpp" -o "build/bin/lab07_vtable_reclass.exe"
    g++ !GFLAGS! "Course_Solutions/Lab08_3D_Math_and_WorldToScreen/lab08_3d_w2s_simulator.cpp" -o "build/bin/lab08_3d_w2s_simulator.exe"
    g++ !GFLAGS! "Course_Solutions/Lab09_Internal_DLL_and_Hooks/lab09_internal_hook_target.cpp" -o "build/bin/lab09_internal_hook_target.exe"
    g++ !GFLAGS! "Course_Solutions/Lab10_Integrity_and_AntiTamper_Boss/lab10_integrity_boss.cpp" -o "build/bin/lab10_integrity_boss.exe"
    echo [+] Build finished in build\bin\!
    goto :eof
)

echo [!] Neither MSVC (cl.exe) nor MinGW (g++.exe) was found in PATH.
