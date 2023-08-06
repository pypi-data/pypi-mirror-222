//
// Created by Vincent on 21/07/2023.
//

#ifndef BASE_PLUGIN_H
#define BASE_PLUGIN_H


class BasePlugin {
public:
    BasePlugin();

    virtual ~BasePlugin() = default;

    virtual void run() = 0;
};

#endif //BASE_PLUGIN_H

