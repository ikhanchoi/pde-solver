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


	float FPS = 60.0f;
	float sec_per_update = 1.0f / FPS;
	float sec_per_render = 1.0f / FPS; // Limiting FPS
	float current = 0.0f, previous = 0.0f, rendered = 0.0f, lag = 0.0f;
	int count_update = 0, count_render = 0;
	while(!glfwWindowShouldClose(window)) {
		current = glfwGetTime();
		lag += current - previous;
		previous = current;

		while(lag >= sec_per_update) {
			lag -= sec_per_update;
			count_update++;
			glfwPollEvents();
			inputSystem.keyUpdate();
		}

		if(current - rendered >= sec_per_render) {
			rendered = current;
			count_render++;
			glClear(GL_COLOR_BUFFER_BIT);
			gl
			glfwSwapBuffers(window);
		}
	}
	std::cout << "Update Per Second: " << count_update / current << std::endl;
	std::cout << "Render Per Second: " << count_render / current << std::endl;
}