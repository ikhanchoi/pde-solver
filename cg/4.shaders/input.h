#ifndef MAIN_CPP_INPUT_H
#define MAIN_CPP_INPUT_H

#include <GLFW/glfw3.h>
#include <iostream>

class InputManager {
private:
	GLFWwindow* window;

public:
	InputManager(GLFWwindow* window);
	void keyUpdate(float& x, float& y);
};


#endif
