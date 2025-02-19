
#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_opengl3.h"

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include "stb_image.h"

#include "window.h"
#include "input.h"
#include "material.h"
#include "camera.h"
#include "model.h"
#include "render.h"
using namespace std;

int main() {
	GLFWwindow* window = createWindow(3,3,1280,960);



	/* 1. Initialize externals */
	// Since the current directory is cmake-build-debug, we need to indicate the parent directory

	// load shader assets
	Shader vertex_shader("../assets/shaders/default.vert");
	Shader fragment_shader("../assets/shaders/default.frag");

	// set shader assets to programs
	Program program;
	program.setShader(vertex_shader);
	program.setShader(fragment_shader);



	//  model = mesh + material
	//  transformable(getter of model matrix), drawable, collider/floor
	Model backpack("../assets/models/backpack/backpack.obj");
	tModel tbackpack("../assets/models/backpack/backpack.obj");


	// extract vaos and textures from files via Loader,
	// make Mesh and Material objects and initialize with setVaos, setProgram, setTexures

	RenderComponent render_component;

	tMesh mesh;
	mesh.setSubmeshes(tbackpack.getSubmeshes());
	render_component.setMesh(mesh);

	tMaterial material;
	material.setProgram(program);
	material.setTextures(tbackpack.getTextures());
	render_component.setMaterial(material);






	/* 2. Initialize internals */

	ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);

	bool show_demo_window = true;
	bool show_another_window = false;

	// systems

	// scenes

	// cameras
	//  transformable, getter of view/projection matrix, movable(how to process input)
	float x = 0.0f, z = 0.0f;
	float v = 0.1f;

	// lights


	/* 3. Loop */
	while(!glfwWindowShouldClose(window)) {


		// (1) Physics



		// (2) Input
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
			ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / ImGui::GetIO().Framerate,
						ImGui::GetIO().Framerate);
			ImGui::End();
		}

		if (show_another_window) {
			ImGui::Begin("Another Window", &show_another_window);
			ImGui::Text("Hello from another window!");
			if (ImGui::Button("Close Me"))
				show_another_window = false;
			ImGui::End();
		}


		// (3) Logic
		// "내부적 게임 규칙에 따라" 수치나 상황이 바뀌는 것을 업데이트


		// (4) Render


		glm::mat4 projection = glm::perspective(0.5f, 4.0f/3.0f, 0.1f, 100.0f);
//		program.setMat4("projection", projection);
		glUniformMatrix4fv(glGetUniformLocation(program.getId(), "projection"), 1, GL_FALSE, &projection[0][0]);

		glm::mat4 view = glm::mat4(1.0f);//camera.GetViewMatrix();
		view = glm::translate(view, glm::vec3(-x,0.0f,-10.0f-z));
//		program.setMat4("view", view);
		glUniformMatrix4fv(glGetUniformLocation(program.getId(), "view"), 1, GL_FALSE, &view[0][0]);

		glm::mat4 model = glm::mat4(1.0f);
		model = glm::translate(model, glm::vec3(0.0f, 0.0f, 0.0f));
		model = glm::scale(model, glm::vec3(1.0f, 1.0f, 1.0f));
//		program.setMat4("model", model);
		glUniformMatrix4fv(glGetUniformLocation(program.getId(), "model"), 1, GL_FALSE, &model[0][0]);


		// Draw
		glClearColor(clear_color.x * clear_color.w,
					 clear_color.y * clear_color.w,
					 clear_color.z * clear_color.w,
					 clear_color.w);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		program.use();
		render_component.draw();
		//backpack.Draw(program.getId());

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