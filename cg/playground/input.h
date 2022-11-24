#ifndef MAIN_CPP_INPUT_H
#define MAIN_CPP_INPUT_H

#include <GLFW/glfw3.h>
#include <iostream>



void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods) {
	if(key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
	glfwSetWindowShouldClose(window, true);
}


class InputManager {
private:
	GLFWwindow* window;

public:
	InputManager(GLFWwindow* window) {
		this->window = window;
		glfwSetKeyCallback(window, key_callback);
	}

	void keyUpdate(float& x, float& y) {
		float velocity = 0.00005f;

		if(glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
			y += velocity;
		if(glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
			x -= velocity;
		if(glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
			y -= velocity;
		if(glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
			x += velocity;

		if(glfwGetKey(window, GLFW_KEY_P) == GLFW_PRESS)
			std::cout << "P is pressed." << std::endl;

	}
};


#endif
