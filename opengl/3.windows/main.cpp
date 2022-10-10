#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "window.h"
#include "input.h"


int main() {

	GLFWwindow* window = WindowInitializer(1,0).createWindow();

	InputManager input_manager(window);
	float x = 0, y = 0;

	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);


	float FPS = 60;
	float sec_per_update = 1.0/80;
	float sec_per_render = 1.0/FPS; // Limiting FPS
	float current, updated, rendered, lag = 0.0f, delta_time;

	while(!glfwWindowShouldClose(window)) {
		current = glfwGetTime();
		lag += current - updated;
		delta_time = current - rendered;

		while(lag >= sec_per_update) {
			updated = current;
			lag -= sec_per_update;
			input_manager.keyUpdate(x,y);
		}

		if(delta_time >= sec_per_render) {
			rendered = current;
				
			glClear(GL_COLOR_BUFFER_BIT);
			glBegin(GL_TRIANGLES);
				glColor3f(1.0f, 0.0f, 0.0f);
				glVertex2f(-0.5f + x, -0.5f + y);
				glVertex2f(0.5f + x, -0.5f + y);
				glVertex2f(0.0f + x, 0.5f + y);
			glEnd();
			
			glfwSwapBuffers(window);
		}
		glfwPollEvents();
	}
}