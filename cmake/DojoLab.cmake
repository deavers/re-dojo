# ============================================================================
# RE:DOJO - lab registration + autocheck (CTest)
#
#   dojo_add_lab(ID lab11 TARGET lab11_integer_widths
#                SOURCE  Course_Solutions/Lab11_Integer_Widths/lab11_integer_widths.cpp
#                [SELFTEST Course_Solutions/Lab11_Integer_Widths/check/lab11_selftest.cpp]
#                DIR     Course_Solutions/Lab11_Integer_Widths
#                [LABELS windows ...] [LIBS lua54 ...])
#
# Creates the lab executable (+ <TARGET>_selftest if SELFTEST is given) and three tests:
#   <ID>_build        builds the target(s)                         (fixture setup)
#   <ID>_solve_ok     reference solution passes: exit 0, sha256(FLAG) == check/expected.json
#   <ID>_wrong_fails  every wrong input from solve/solve.py fails with exit 1 or 2 and no FLAG
#                     (a crash or timeout is a FAIL); the real lab binary quits cleanly on empty stdin
# The tests drive the SELFTEST binary when present (memory labs), otherwise the lab binary
# itself (crackmes read stdin). Runner: Tools_and_Scripts/lab_runner.py (stdlib only).
# Labels: every lab test gets 'lab'; pass LABELS windows / unity to keep Linux CI off them.
# The runner starts with python -I (isolated: no PYTHONPATH, no user site, no cwd on sys.path), so a
# solve.py import (e.g. z3) resolves only from the configured interpreter: -DPython3_EXECUTABLE=<python with z3>.
# ============================================================================

find_package(Python3 COMPONENTS Interpreter REQUIRED)
set(DOJO_LAB_RUNNER ${CMAKE_SOURCE_DIR}/Tools_and_Scripts/lab_runner.py)

function(dojo_add_lab)
    cmake_parse_arguments(L "" "ID;TARGET;SOURCE;SELFTEST;DIR" "LABELS;LIBS" ${ARGN})
    foreach(req ID TARGET SOURCE DIR)
        if(NOT L_${req})
            message(FATAL_ERROR "dojo_add_lab: ${req} is required")
        endif()
    endforeach()

    add_executable(${L_TARGET} ${L_SOURCE})
    if(L_LIBS)
        target_link_libraries(${L_TARGET} PRIVATE ${L_LIBS})
    endif()
    set(_targets ${L_TARGET})
    set(_run_target ${L_TARGET})
    if(L_SELFTEST)
        add_executable(${L_TARGET}_selftest ${L_SELFTEST})
        if(L_LIBS)
            target_link_libraries(${L_TARGET}_selftest PRIVATE ${L_LIBS})
        endif()
        target_include_directories(${L_TARGET}_selftest PRIVATE ${CMAKE_SOURCE_DIR}/${L_DIR}
                                   ${CMAKE_SOURCE_DIR}/Tools_and_Scripts/lab_template)
        list(APPEND _targets ${L_TARGET}_selftest)
        set(_run_target ${L_TARGET}_selftest)
    endif()

    set(_labels lab ${L_LABELS})
    set(_build_args)
    foreach(t ${_targets})
        list(APPEND _build_args --target ${t})
    endforeach()

    add_test(NAME ${L_ID}_build
             COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --config $<CONFIG> ${_build_args})
    set_tests_properties(${L_ID}_build PROPERTIES FIXTURES_SETUP ${L_ID}_bin LABELS "${_labels}")

    foreach(mode ok wrong)
        if(mode STREQUAL "ok")
            set(_name ${L_ID}_solve_ok)
            set(_extra)
        else()
            set(_name ${L_ID}_wrong_fails)
            set(_extra --real-exe $<TARGET_FILE:${L_TARGET}>)
        endif()
        add_test(NAME ${_name}
                 COMMAND ${Python3_EXECUTABLE} -I ${DOJO_LAB_RUNNER} ${mode}
                         --lab-dir ${CMAKE_SOURCE_DIR}/${L_DIR} --exe $<TARGET_FILE:${_run_target}> ${_extra})
        set_tests_properties(${_name} PROPERTIES FIXTURES_REQUIRED ${L_ID}_bin LABELS "${_labels}" TIMEOUT 60)
    endforeach()
endfunction()
