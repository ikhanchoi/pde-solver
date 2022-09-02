cmake_minimum_required(VERSION 3.23)
project(opengl)

set(CMAKE_CXX_STANDARD 14)

# Add header file
set(GLEW_H /opt/homebrew/Cellar/glew/2.2.0_1/include)
set(GLFW_H /opt/homebrew/Cellar/glfw/3.3.8/include)
set(GLM_H /opt/homebrew/Cellar/glm/0.9.9.8/include)
include_directories(${GLEW_H} ${GLFW_H} ${GLM_H})

# Add target link
set(GLEW_LINK /opt/homebrew/Cellar/glew/2.2.0_1/lib/libGLEW.2.2.dylib)
set(GLFW_LINK /opt/homebrew/Cellar/glfw/3.3.8/lib/libglfw.3.dylib)
link_libraries(${OPENGL} ${GLEW_LINK} ${GLFW_LINK})

# Execute compilation command
set(SOURCE_FILES main.cpp)
add_executable(opengl ${SOURCE_FILES})

target_link_libraries(opengl "-framework OpenGL")
