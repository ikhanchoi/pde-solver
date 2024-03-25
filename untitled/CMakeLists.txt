cmake_minimum_required(VERSION 3.27)
project(untitled)

set(CMAKE_CXX_STANDARD 17)

find_package(glfw3 REQUIRED)
set(LIBS ${LIBS} glfw)


# stb_image
set(STB_IMAGE_DIR ${CMAKE_SOURCE_DIR}/stb_image)
include_directories(${STB_IMAGE_DIR})
add_library(STB_IMAGE "${STB_IMAGE_DIR}/stb_image.cpp")
set(LIBS ${LIBS} STB_IMAGE)


# imgui
set(IMGUI_DIR ${CMAKE_SOURCE_DIR}/imgui)
include_directories(${IMGUI_DIR} ${IMGUI_DIR}/backends)
set(IMGUI
		${IMGUI_DIR}/imgui.cpp
		${IMGUI_DIR}/imgui_demo.cpp
		${IMGUI_DIR}/imgui_draw.cpp
		${IMGUI_DIR}/imgui_tables.cpp
		${IMGUI_DIR}/imgui_widgets.cpp
		${IMGUI_DIR}/backends/imgui_impl_glfw.cpp
		${IMGUI_DIR}/backends/imgui_impl_opengl3.cpp)
set(SRCS ${SRCS} ${IMGUI})

add_executable(untitled main.cpp ${SRCS})
target_link_libraries(untitled ${LIBS})
