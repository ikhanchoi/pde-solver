#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include "window.h"
#include "input.h"
#include "shader.h"
#include "mesh.h"
#include "model.h"
#include "stb_image.h"
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

int main() {

	GLFWwindow* window = WindowInitializer(3,3).createWindow();

	InputManager input_manager(window);
	float x = 0, y = 0;

	Shader ourShader("../shader.vert", "../shader.frag");
	ourShader.use();

	stbi_set_flip_vertically_on_load(true);
	glEnable(GL_DEPTH_TEST);

	Model ourModel("../backpack/backpack.obj");

	int FPS = 30;
	float sec_per_update = 1.0f/FPS;
	float sec_per_render = 1.0f/FPS; // Limiting FPS
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
			glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

			// view/projection transformations
			glm::mat4 projection = glm::perspective(0.5f, 4.0f/3.0f, 0.1f, 100.0f);
			glm::mat4 view = glm::mat4(1.0f);//camera.GetViewMatrix();
			view = glm::translate(view, glm::vec3(0.0f,0.0f,-10.0f));
			ourShader.setMat4("projection", projection);
			ourShader.setMat4("view", view);

			// render the loaded model
			glm::mat4 model = glm::mat4(1.0f);
			model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f)); // translate it down so it's at the center of the scene
			model = glm::scale(model, glm::vec3(1.0f, 1.0f, 1.0f));	// it's a bit too big for our scene, so scale it down
			ourShader.setMat4("model", model);
			ourModel.Draw(ourShader);
			glfwSwapBuffers(window);
		}
	}
	glfwTerminate();
	return 0;
}