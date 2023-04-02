project(conandemo)

find_package(jsoncpp CONFIG REQUIRED)

add_library(${PROJECT_NAME} Foo.cpp)

target_link_libraries(${PROJECT_NAME} JsonCpp::JsonCpp)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "Foo.h")

install(TARGETS ${PROJECT_NAME})