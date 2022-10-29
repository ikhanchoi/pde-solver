#ifndef MAIN_CPP_INPUT_H
#define MAIN_CPP_INPUT_H

#include <GLFW/glfw3.h>
#include <iostream>

class IInputComponent {
public:
	virtual ~IInputComponent() = default;
};

class IMovable : IInputComponent { // acting component for the action "move"
public:
	virtual void move() = 0;
};


class InputSystem {
	GLFWwindow* window;
	/* controls -> action mapping */

public:
	InputSystem(GLFWwindow* window); // callbacks set
	void update();
};



#endif
