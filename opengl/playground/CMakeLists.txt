cmake_minimum_required(VERSION 3.23)
project(opengl)

set(CMAKE_CXX_STANDARD 14)

include_directories(glad/include)
find_package(glfw3 3.3 REQUIRED)
find_package(glm REQUIRED)
find_package(assimp REQUIRED)

set(source_files window.cpp input.cpp shader.cpp mesh.cpp stb_image.cpp)
add_executable(opengl main.cpp ${source_files} glad/src/glad.c)

target_link_libraries(opengl glfw assimp::assimp "-framework OpenGL")