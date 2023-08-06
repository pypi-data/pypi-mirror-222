cmake_minimum_required(VERSION 3.25)
project(pybedrock)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11
        GIT_TAG v2.11.1
)
FetchContent_Declare(
        tomlplusplus
        GIT_REPOSITORY https://github.com/marzer/tomlplusplus.git
        GIT_TAG v3.3.0
)

FetchContent_MakeAvailable(pybind11)
FetchContent_MakeAvailable(tomlplusplus)

# add_subdirectory(pybind11)
add_subdirectory(lib)