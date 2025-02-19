cmake_minimum_required(VERSION 3.27)
project(gltf_viewer)

set(CMAKE_CXX_STANDARD 17)

# glew, glfw, glm
find_package(GLEW REQUIRED)
find_package(glfw3 REQUIRED)
find_package(glm REQUIRED)

# imgui
add_library(imgui STATIC
    lib/imgui/imgui.cpp
	lib/imgui/imgui_demo.cpp
    lib/imgui/imgui_draw.cpp
    lib/imgui/imgui_tables.cpp
    lib/imgui/imgui_widgets.cpp
    lib/imgui/backends/imgui_impl_glfw.cpp
    lib/imgui/backends/imgui_impl_opengl3.cpp)
target_include_directories(imgui PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/imgui
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/imgui/backends)
target_link_libraries(imgui PRIVATE glfw)

# tiny_gltf
add_library(tiny_gltf INTERFACE)
target_include_directories(tiny_gltf INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/lib/tiny_gltf)


add_executable(gltf_viewer src/main.cpp)
target_link_libraries(gltf_viewer PRIVATE GLEW::GLEW glfw imgui tiny_gltf)
