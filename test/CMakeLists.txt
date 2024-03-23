project(unit_test)

find_package(GTest REQUIRED)
find_package(Threads REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} GTest::gtest Threads::Threads conandemo)

add_test(NAME ${PROJECT_NAME} COMMAND ${PROJECT_NAME})
