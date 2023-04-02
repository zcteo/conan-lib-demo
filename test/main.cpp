//
// Created by EricTeo on 2023/3/31.
//

#include <gtest/gtest.h>
#include "Foo.h"

TEST(Test, test)
{
    Foo foo;
    foo.sayJson();
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}