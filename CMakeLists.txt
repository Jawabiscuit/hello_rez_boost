cmake_minimum_required(VERSION 2.8)

include(RezBuild)

execute_process(COMMAND "${CMAKE_COMMAND}" "-E" "environment")

file(GLOB_RECURSE _files "$ENV{REZ_BUILD_PROJECT_NAME}.exe")
list(GET _files 0 _file)
rez_install_files(
    ${_file}
    RELATIVE "src/build"
    DESTINATION .
)