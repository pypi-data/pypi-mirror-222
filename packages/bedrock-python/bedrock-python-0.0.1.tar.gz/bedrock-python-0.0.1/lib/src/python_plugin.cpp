//
// Created by Vincent on 21/07/2023.
//

#include "python_plugin.h"

#include "py.h"

void PythonPlugin::run() {
    /* Trampoline (need one for each virtual function) */
    PYBIND11_OVERLOAD_PURE(
            void,         /* Return type */
            BasePlugin,   /* Parent class */
            run,          /* Name of function in C++ (must match Python name) */
    );
}

PYBIND11_MODULE(plugin, m) {
    py::class_<BasePlugin>(m, "BasePlugin")
            .def("run", &BasePlugin::run);

    py::class_<PythonPlugin, BasePlugin>(m, "PythonPlugin")
            .def(py::init<>())
            .def("run", &BasePlugin::run);
}