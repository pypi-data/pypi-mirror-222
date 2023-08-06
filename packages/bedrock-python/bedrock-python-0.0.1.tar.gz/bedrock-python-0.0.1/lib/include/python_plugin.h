//
// Created by Vincent on 21/07/2023.
//

#ifndef PYTHON_PLUGIN_H
#define PYTHON_PLUGIN_H

#include "base_plugin.h"

class PythonPlugin : public BasePlugin {
public:
    /* Inherit the constructors */
    using BasePlugin::BasePlugin;

    void run() override;
};


#endif //PYTHON_PLUGIN_H
