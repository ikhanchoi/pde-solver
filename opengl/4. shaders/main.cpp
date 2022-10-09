#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "window.h"
#include "input.h"
#include "shader.h"

int main() {

	GLFWwindow* window = WindowInitializer(3,3).createWindow();

	InputManager input_manager(window);
	float x = 0, y = 0;

	ShaderLoader program("../shader.vert", "../shader.frag");
	program.use();

	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	float vertices[] = {
		-0.5f, -0.5f, 0.0f,
		0.5f, -0.5f, 0.0f,
		0.0f,  0.5f, 0.0f
	};
	unsigned int VAO, VBO;
	glGenVertexArrays(1, &VAO);
	glGenBuffers(1, &VBO);
	glBindVertexArray(VAO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
	glEnableVertexAttribArray(0);



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
			glfwPollEvents();
		}

		if(delta_time >= sec_per_render) {
			rendered = current;
			glClear(GL_COLOR_BUFFER_BIT);
			glDrawArrays(GL_TRIANGLES, 0, 3);
			glfwSwapBuffers(window);
		}
	}
	glfwTerminate();
	return 0;
}