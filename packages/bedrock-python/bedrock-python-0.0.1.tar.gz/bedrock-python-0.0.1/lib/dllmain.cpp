#include "Windows.h"
#include "iostream"
#include "py.h"
#include "base_plugin.h"
#include "plugin_manager.h"

BOOL WINAPI DllMain(
        _In_ HINSTANCE hinstDLL,  // handle to DLL module
        _In_ DWORD fdwReason,     // reason for calling function
        _In_ LPVOID lpvReserved)  // reserved
{
    // Perform actions based on the reason for calling.
    switch (fdwReason) {
        case DLL_PROCESS_ATTACH: {
            // Initialize once for each new process.
            // Return FALSE to fail DLL load.
            py::scoped_interpreter guard{};
//            py::exec(R"(
//                print('Hello World')
//            )");
//
//            py::exec(R"(
//                import sys
//                print(sys.path)
//            )");

//            auto plugin_module = py::module::import("sample_plugin.sample_plugin");
//            plugin_module.attr("hello")();
//
//            auto plugin = plugin_module.attr("SamplePlugin")();
//            plugin.attr("run")();

            auto plugin_manager = PluginManager();

            printf("Initialising Plugin Manager...\n");
            plugin_manager.load_plugins(std::filesystem::current_path() / "plugins");

            break;
        }
        case DLL_THREAD_ATTACH:
            // Do thread-specific initialization.
            break;

        case DLL_THREAD_DETACH:
            // Do thread-specific cleanup.
            break;

        case DLL_PROCESS_DETACH:

            if (lpvReserved != nullptr) {
                break; // do not do cleanup if process termination scenario
            }

            // Perform any necessary cleanup.
            break;
    }
    return TRUE;  // Successful DLL_PROCESS_ATTACH.
}