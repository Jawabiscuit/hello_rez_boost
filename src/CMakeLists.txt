cmake_minimum_required(VERSION 2.8)
project("hello_boost")

MESSAGE("PROJECT_SOURCE_DIR: ${PROJECT_SOURCE_DIR}")
MESSAGE("PROJECT_BINARY_DIR: ${PROJECT_BINARY_DIR}")

set(BOOST_ROOT $ENV{BOOST})
find_package(Boost REQUIRED)

set(SOURCES example.cpp)

include_directories(${Boost_INCLUDE_DIR})

add_executable(${PROJECT_NAME} ${SOURCES})
