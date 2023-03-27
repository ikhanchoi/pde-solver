
#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_opengl3.h"

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <stb_image.h>

#include "window.h"
#include "input.h"
#include "shader.h"
#include "camera.h"
#include "model.h"

int main() {

	GLFWwindow* window = createWindow(3,3,1280,960);


	/* 1. Initialize internal objects */

	// systems

	// scenes

	// cameras
	//  transformable, getter of view/projection matrix, movable(how to process input)
	float x = 0.0f, z = 0.0f;
	float v = 0.1f;

	// lights




	/* 2. Load external objects */

	// shaders
	Shader default_shader("../default.vert", "../default.frag");

	// models
	//  model = mesh + material
	//  transformable(getter of model matrix), drawable, collider/floor
	exModel backpack("../../backpack/backpack.obj");






	ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);



	bool show_demo_window = true;
	bool show_another_window = false;

	while(!glfwWindowShouldClose(window)) {


		// 1. Physics



		// 2. Input
		// 인풋을 받아 오브젝트들의 상태를 바꾸는 것까지 여기서 처리
		glfwPollEvents();
		if(ImGui::IsKeyDown(ImGuiKey_W))
			z -= v;
		if(ImGui::IsKeyDown(ImGuiKey_A))
			x -= v;
		if(ImGui::IsKeyDown(ImGuiKey_S))
			z += v;
		if(ImGui::IsKeyDown(ImGuiKey_D))
			x += v;


		// 3. Logic
		// "내부적 게임 규칙에 따라" 수치나 상황이 바뀌는 것을 업데이트


		// 4. Render

		glClearColor(clear_color.x * clear_color.w, clear_color.y * clear_color.w, clear_color.z * clear_color.w, clear_color.w);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		glm::mat4 projection = glm::perspective(0.5f, 4.0f/3.0f, 0.1f, 100.0f);
		default_shader.setMat4("projection", projection);

		glm::mat4 view = glm::mat4(1.0f);//camera.GetViewMatrix();
		view = glm::translate(view, glm::vec3(-x,0.0f,-10.0f-z));
		default_shader.setMat4("view", view);

		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f));
		model = glm::scale(model, glm::vec3(1.0f, 1.0f, 1.0f));
		default_shader.setMat4("model", model);

		backpack.Draw(default_shader);



		// imgui
		ImGui_ImplOpenGL3_NewFrame();
		ImGui_ImplGlfw_NewFrame();
		ImGui::NewFrame();

		ImGui::ShowDemoWindow();

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


		glfwSwapBuffers(window);


	}



	ImGui_ImplOpenGL3_Shutdown();
	ImGui_ImplGlfw_Shutdown();
	ImGui::DestroyContext();

	glfwTerminate();
	return 0;
}