add_definitions(-D_ITERATOR_DEBUG_LEVEL=0)

file(
        GLOB_RECURSE SOURCE_FILES
        LIST_DIRECTORIES false
        RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}"
        "*.cpp"
)

include_directories(libpybedrock PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)

add_library(libpybedrock SHARED ${SOURCE_FILES} src/plugin_manager.cpp include/plugin_manager.h)

pybind11_add_module(plugin MODULE src/base_plugin.cpp src/python_plugin.cpp)

target_link_libraries(libpybedrock PRIVATE
        pybind11::embed
        tomlplusplus::tomlplusplus)

install(TARGETS libpybedrock
        LIBRARY DESTINATION pybedrock
        RUNTIME DESTINATION pybedrock)

install(TARGETS plugin
        LIBRARY DESTINATION pybedrock
        )