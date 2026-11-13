# cmake -P script for <id>_build of a .NET lab: copy the project out of the repo, build it there.
# Vars: DOTNET, SRC (project directory in the repo), WORK (build-tree directory), PROJECT_FILE.
file(REMOVE_RECURSE ${WORK}/src)
file(COPY ${SRC}/ DESTINATION ${WORK}/src)
execute_process(
    COMMAND ${DOTNET} build ${WORK}/src/${PROJECT_FILE} -c Release -o ${WORK}/out --nologo
    RESULT_VARIABLE rc
    OUTPUT_VARIABLE out
    ERROR_VARIABLE err)
message("${out}${err}")
if(NOT rc EQUAL 0)
    message(FATAL_ERROR "dotnet build failed (${rc})")
endif()
