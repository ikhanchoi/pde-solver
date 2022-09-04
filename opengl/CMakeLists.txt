cmake_minimum_required(VERSION 3.23)
project(opengl)

set(CMAKE_CXX_STANDARD 14)

include_directories(glad/include)
find_package(glfw3 3.3 REQUIRED)
find_package(glm REQUIRED)

add_executable(opengl main.cpp glad/src/glad.c)

target_link_libraries(opengl glfw "-framework OpenGL")