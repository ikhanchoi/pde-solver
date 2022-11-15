#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "window.h"
#include "input.h"



class Triangle : IMovable {
	float* vertices;
	float* color;
	float velocity;
public:
	Triangle(float* vertices, float* color, float velocity) {
		this->vertices = vertices;
		this->color = color;
		this->velocity = velocity;
	}

	void move() override {

	}
};

int main() {

	GLFWwindow* window = WindowInitializer(1,0).createWindow();

	InputSystem inputSystem(window);


	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	float vertices[6] = {
			-0.5f, -0.5f,
			-0.5f, -0.5f,
			 0.0f,  0.5f
	};
	float color[3] = {1.0f, 0.0f, 0.0f};
	float velocity = 0.01f;

	auto* triangle = new Triangle(vertices, color, velocity);


	glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
	while(!glfwWindowShouldClose(window)) {
		glfwPollEvents();
		

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glDrawArrays(GL_TRIANGLES, 0, 3);

		glfwSwapBuffers(window);
	}
}