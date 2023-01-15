
#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_opengl3.h"

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <stb_image.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

#include "window.h"
#include "input.h"
#include "shader.h"
#include "camera.h"
#include "mesh.h"
#include "model.h"

int main() {

	GLFWwindow* window = createWindow(3,3,1280,960);

	Shader default_shader("../default.vert", "../default.frag");

	Model backpack("../../backpack/backpack.obj");



	bool show_demo_window = true;
	bool show_another_window = false;
	ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);

	float x = 0.0f, z = 0.0f;
	float v = 0.1f;

	while(!glfwWindowShouldClose(window)) {

		glfwPollEvents();


		glClearColor(clear_color.x * clear_color.w, clear_color.y * clear_color.w, clear_color.z * clear_color.w, clear_color.w);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);



		if(ImGui::IsKeyDown(ImGuiKey_W))
			z -= v;
		if(ImGui::IsKeyDown(ImGuiKey_A))
			x -= v;
		if(ImGui::IsKeyDown(ImGuiKey_S))
			z += v;
		if(ImGui::IsKeyDown(ImGuiKey_D))
			x += v;



		glm::mat4 projection = glm::perspective(0.5f, 4.0f/3.0f, 0.1f, 100.0f);
		default_shader.setMat4("projection", projection);

		glm::mat4 view = glm::mat4(1.0f);//camera.GetViewMatrix();
		view = glm::translate(view, glm::vec3(-x,0.0f,-10.0f-z));
		default_shader.setMat4("view", view);

		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f));
		model = glm::scale(model, glm::vec3(1.0f, 1.0f, 1.0f));
		default_shader.setMat4("model", model);




		// render
		backpack.Draw(default_shader);






		// imgui start
		ImGui_ImplOpenGL3_NewFrame();
		ImGui_ImplGlfw_NewFrame();
		ImGui::NewFrame();

		{
			ImGui::ShowDemoWindow();
		}

		{
			static float f = 0.0f;
			static int counter = 0;

			ImGui::Begin("Hello, world!");

			ImGui::Text("This is some useful text.");
			ImGui::Checkbox("Demo Window", &show_demo_window);
			ImGui::Checkbox("Another Window", &show_another_window);

			ImGui::SliderFloat("float", &f, 0.0f, 1.0f);
			ImGui::ColorEdit3("clear color", (float*)&clear_color);

			if (ImGui::Button("Button"))
				counter++;
			ImGui::SameLine();
			ImGui::Text("counter = %d", counter);
			ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / ImGui::GetIO().Framerate, ImGui::GetIO().Framerate);
			ImGui::End();
		}

		if (show_another_window) {
			ImGui::Begin("Another Window", &show_another_window);
			ImGui::Text("Hello from another window!");
			if (ImGui::Button("Close Me"))
				show_another_window = false;
			ImGui::End();
		}

		ImGui::Render();
		ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
		// imgui end


		glfwSwapBuffers(window);


	}



	ImGui_ImplOpenGL3_Shutdown();
	ImGui_ImplGlfw_Shutdown();
	ImGui::DestroyContext();


	glfwTerminate();
	return 0;
}