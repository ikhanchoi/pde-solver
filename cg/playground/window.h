#ifndef MAIN_CPP_WINDOW_H
#define MAIN_CPP_WINDOW_H

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <algorithm>

class WindowInitializer {
private:
	int major, minor;
public:
	WindowInitializer(int major, int minor);
	GLFWwindow* createWindow();
};


#endif
