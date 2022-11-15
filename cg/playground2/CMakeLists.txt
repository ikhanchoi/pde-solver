cmake_minimum_required(VERSION 3.23)
project(opengl)

set(CMAKE_CXX_STANDARD 14)

include_directories(glad/include)
include_directories(imgui)
include_directories(imgui/backends)
find_package(glfw3 3.3 REQUIRED)
find_package(glm REQUIRED)
find_package(assimp REQUIRED)

set(source_files window.cpp input.cpp shader.cpp mesh.cpp stb_image.cpp)
set(imgui_files
		imgui/imgui.cpp imgui/imgui_demo.cpp imgui/imgui_draw.cpp imgui/imgui_tables.cpp imgui/imgui_widgets.cpp
		imgui/backends/imgui_impl_glfw.cpp imgui/backends/imgui_impl_opengl3.cpp)
add_executable(opengl main.cpp ${source_files} ${imgui_files} glad/src/glad.c)

target_link_libraries(opengl glfw assimp::assimp "-framework OpenGL")