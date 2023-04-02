//
// Created by EricTeo on 2023/3/31.
//

#include "Foo.h"
#include "json/json.h"

void Foo::sayJson()
{
    Json::Value json;
    json["hello"] = "world";
    printf("%s\n", json.toStyledString().c_str());
}
