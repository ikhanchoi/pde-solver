#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "window.h"
#include "input.h"


int main() {

	GLFWwindow* window = WindowInitializer(1,0).createWindow();

	InputManager input_manager(window);
	float x = 0, y = 0;

	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);


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
			input_manager.keyUpdate(x,y);
		}

		if(current - rendered >= sec_per_render) {
			rendered = current;
			count_render++;
			glClear(GL_COLOR_BUFFER_BIT);
			glBegin(GL_TRIANGLES);
				glColor3f(1.0f, 0.0f, 0.0f);
				glVertex2f(-0.5f + x, -0.5f + y);
				glVertex2f(0.5f + x, -0.5f + y);
				glVertex2f(0.0f + x, 0.5f + y);
			glEnd();
			glfwSwapBuffers(window);
		}
	}
	std::cout << "Update Per Second: " << count_update / current << std::endl;
	std::cout << "Render Per Second: " << count_render / current << std::endl;
}