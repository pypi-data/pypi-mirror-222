//
// Created by Vincent on 22/07/2023.
//

#ifndef PYBEDROCK_PLUGIN_MANAGER_H
#define PYBEDROCK_PLUGIN_MANAGER_H

#include <memory>
#include <filesystem>
#include "base_plugin.h"
#include "py.h"

class PluginManager {
private:
    py::object load_plugin(const std::filesystem::path &path);

public:
    std::vector<py::object> load_plugins(const std::filesystem::path &directory);
};


#endif //PYBEDROCK_PLUGIN_MANAGER_H
