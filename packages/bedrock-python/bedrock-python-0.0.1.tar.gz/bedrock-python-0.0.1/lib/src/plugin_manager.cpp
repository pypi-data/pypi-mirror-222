//
// Created by Vincent on 22/07/2023.
//

#include "plugin_manager.h"
#include <iostream>
#include "toml++/toml.h"
#include "python_plugin.h"

std::vector<py::object> PluginManager::load_plugins(const std::filesystem::path &directory) {
    std::vector<py::object> plugins;

    for (const auto &entry: std::filesystem::directory_iterator(directory)) {
        if (entry.is_directory()) {
            auto &plugin_path = entry.path();
            if (std::filesystem::exists(plugin_path / "plugin.toml")) {
                auto plugin = load_plugin(plugin_path);
                plugins.push_back(plugin);
            }
        }
    }

    return plugins;
}

py::object PluginManager::load_plugin(const std::filesystem::path &path) {
    auto plugin = std::shared_ptr<BasePlugin>();
    auto config = toml::parse_file((path / "plugin.toml").string());

    std::string main = config["main"].value_or("");
    auto pos = main.find_last_of('.');
    auto module_name = path.filename().string() + "." + main.substr(0, pos);
    auto class_name = main.substr(pos + 1);

    auto plugin_obj = py::module_::import(module_name.c_str()).attr(class_name.c_str())();
    return plugin_obj;
}
