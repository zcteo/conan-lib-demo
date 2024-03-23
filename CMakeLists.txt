cmake_minimum_required(VERSION 3.12)

project(conandemo)

set(CMAKE_CXX_STANDARD 11)

option(BUILD_TESTING "build unit test" ON)
option(CONAN_BUILD "build is start by conan" OFF)

if (NOT ${CONAN_BUILD})
    execute_process(COMMAND conan install ${CMAKE_SOURCE_DIR} -if ${CMAKE_BINARY_DIR}
            -of ${CMAKE_BINARY_DIR} -s &:build_type=${CMAKE_BUILD_TYPE} OUTPUT_QUIET)
    include(${CMAKE_BINARY_DIR}/build/${CMAKE_BUILD_TYPE}/generators/conan_toolchain.cmake)
endif ()

add_subdirectory(src)


if (${BUILD_TESTING})
    enable_testing()
    add_subdirectory(test)
endif ()