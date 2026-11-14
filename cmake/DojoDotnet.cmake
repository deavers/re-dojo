# ============================================================================
# RE:DOJO - .NET labs (labs_index.json "ci": "sources_only")
#
#   dojo_add_dotnet_lab(ID lab39 DIR Course_Solutions/Lab39_DotNet_Decompile PROJECT game/Lab39.csproj
#                       ASSEMBLY Lab39)
#
# Always:  <ID>_sources       python check/check_sources.py (no SDK needed; this is what CI runs)
# With a .NET SDK and DOJO_DOTNET_TESTS=ON (default ON locally, CI passes OFF):
#          <ID>_build         copies game/ into the build tree and runs `dotnet build` there (no obj/ in the repo)
#          <ID>_solve_ok      runner "ok" against the built apphost
#          <ID>_wrong_fails   runner "wrong" (+ real binary on empty stdin)
# ============================================================================

option(DOJO_DOTNET_TESTS "Build and test .NET labs with the local .NET SDK" ON)
find_program(DOJO_DOTNET dotnet)
set(DOJO_DOTNET_SDK_OK OFF)
if(DOJO_DOTNET)
    execute_process(COMMAND ${DOJO_DOTNET} --list-sdks OUTPUT_VARIABLE _sdks ERROR_QUIET)
    if(_sdks MATCHES "[0-9]")
        set(DOJO_DOTNET_SDK_OK ON)
    endif()
endif()

function(dojo_add_dotnet_lab)
    cmake_parse_arguments(L "" "ID;DIR;PROJECT;ASSEMBLY" "" ${ARGN})
    add_test(NAME ${L_ID}_sources
             COMMAND ${Python3_EXECUTABLE} -I ${CMAKE_SOURCE_DIR}/${L_DIR}/check/check_sources.py)
    set_tests_properties(${L_ID}_sources PROPERTIES LABELS "lab;dotnet_sources")
    if(NOT (DOJO_DOTNET_TESTS AND DOJO_DOTNET_SDK_OK))
        message(STATUS "${L_ID}: .NET SDK tests not registered (DOJO_DOTNET_TESTS=${DOJO_DOTNET_TESTS}, SDK found=${DOJO_DOTNET_SDK_OK})")
        return()
    endif()
    set(_work ${CMAKE_BINARY_DIR}/dotnet/${L_ID})
    get_filename_component(_proj_dir ${L_PROJECT} DIRECTORY)
    get_filename_component(_proj_name ${L_PROJECT} NAME)
    set(_exe ${_work}/out/${L_ASSEMBLY}${CMAKE_EXECUTABLE_SUFFIX})
    add_test(NAME ${L_ID}_build
             COMMAND ${CMAKE_COMMAND}
                     -DDOTNET=${DOJO_DOTNET}
                     -DSRC=${CMAKE_SOURCE_DIR}/${L_DIR}/${_proj_dir}
                     -DWORK=${_work}
                     -DPROJECT_FILE=${_proj_name}
                     -P ${CMAKE_SOURCE_DIR}/cmake/DojoDotnetBuild.cmake)
    set_tests_properties(${L_ID}_build PROPERTIES FIXTURES_SETUP ${L_ID}_bin LABELS "lab;dotnet" TIMEOUT 300)
    add_test(NAME ${L_ID}_solve_ok
             COMMAND ${Python3_EXECUTABLE} -I ${DOJO_LAB_RUNNER} ok --lab-dir ${CMAKE_SOURCE_DIR}/${L_DIR} --exe ${_exe})
    add_test(NAME ${L_ID}_wrong_fails
             COMMAND ${Python3_EXECUTABLE} -I ${DOJO_LAB_RUNNER} wrong --lab-dir ${CMAKE_SOURCE_DIR}/${L_DIR}
                     --exe ${_exe} --real-exe ${_exe})
    set_tests_properties(${L_ID}_solve_ok ${L_ID}_wrong_fails
                         PROPERTIES FIXTURES_REQUIRED ${L_ID}_bin LABELS "lab;dotnet" TIMEOUT 120)
endfunction()
