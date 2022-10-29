#include "input.h"

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods) {
	if(key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
		glfwSetWindowShouldClose(window, true);
}


InputSystem::InputSystem(GLFWwindow* window) {
	this->window = window;
	glfwSetKeyCallback(window, key_callback);
}

void InputSystem::update(actor) {


	if(glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
	if(glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
	if(glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
	if(glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)

	if(glfwGetKey(window, GLFW_KEY_P) == GLFW_PRESS)
		std::cout << "P is pressed." << std::endl;

}


