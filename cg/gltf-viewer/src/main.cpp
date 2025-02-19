#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

#include "imgui.h"
#include "imgui_impl_glfw.h"
#include "imgui_impl_opengl3.h"

#define TINYGLTF_IMPLEMENTATION
#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "tiny_gltf.h"




int main() {

	/* 1. Window */


	// glfw
    if (!glfwInit()) return -1;
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    GLFWwindow* window = glfwCreateWindow(800, 600, "GLTF Viewer", NULL, NULL);
    if (!window) return -1;
    glfwMakeContextCurrent(window);

	// glew
    glewInit();

	// imgui
	IMGUI_CHECKVERSION();
	ImGui::CreateContext();
	ImGuiIO& io = ImGui::GetIO(); (void)io;
	ImGui::StyleColorsDark();
	ImGui_ImplGlfw_InitForOpenGL(window, true);
	ImGui_ImplOpenGL3_Init("#version 330");







	/* 2. Externals */


	// shaders
	std::ifstream fs;
	std::string code;
	const char* cstr;
	int success;

	fs.exceptions(std::ifstream::failbit|std::ifstream::badbit);
	try {
		fs.open("../assets/shaders/simple.vert");
		std::stringstream ss;
		ss << fs.rdbuf();
		code = ss.str();
		fs.close();
	}
	catch(std::ifstream::failure& e) {
		std::cout << "ERROR::SHADER_NOT_LOADED: " << "\n" << e.what() << "\n";
	}
	cstr = code.c_str();
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &cstr, NULL);
    glCompileShader(vertexShader);
    glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
        std::cerr << "Shader Compilation Error: " << infoLog << std::endl;
    }

	fs.exceptions(std::ifstream::failbit|std::ifstream::badbit);
	try {
		fs.open("../assets/shaders/simple.frag");
		std::stringstream ss;
		ss << fs.rdbuf();
		code = ss.str();
		fs.close();
	}
	catch(std::ifstream::failure& e) {
		std::cout << "ERROR::SHADER_NOT_LOADED: " << "\n" << e.what() << "\n";
	}
	cstr = code.c_str();
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &cstr, NULL);
    glCompileShader(fragmentShader);
    glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(fragmentShader, 512, NULL, infoLog);
        std::cerr << "Shader Compilation Error: " << infoLog << std::endl;
    }

    GLuint shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);



	// models
    tinygltf::TinyGLTF loader;
    tinygltf::Model model;
    std::string err, warn;
    bool ret = loader.LoadASCIIFromFile(&model, &err, &warn, "../assets/models/Box/Box.gltf");
    if (!warn.empty()) std::cout << "Warn: " << warn << std::endl;
    if (!err.empty()) std::cerr << "Err: " << err << std::endl;
    if (!ret) {std::cerr << "Failed to load GLTF model!" << std::endl; return -1;}

	std::vector<float> vertices;
    std::vector<unsigned int> indices;
    if (!model.meshes.empty()) {
        tinygltf::Mesh &mesh = model.meshes[0];
        tinygltf::Primitive &primitive = mesh.primitives[0];

        const tinygltf::Accessor& posAccessor = model.accessors[primitive.attributes["POSITION"]];
        const tinygltf::BufferView& posBufferView = model.bufferViews[posAccessor.bufferView];
        const tinygltf::Buffer& posBuffer = model.buffers[posBufferView.buffer];
        size_t posByteOffset = posAccessor.byteOffset + posBufferView.byteOffset;
        size_t numVertices = posAccessor.count;
		const float* posData = reinterpret_cast<const float*>(&posBuffer.data[posByteOffset]);
		vertices.resize(numVertices * 3);
		for (size_t i = 0; i < numVertices * 3; i++)
    		vertices[i] = posData[i];

		const tinygltf::Accessor& indexAccessor = model.accessors[primitive.indices];
		const tinygltf::BufferView& indexBufferView = model.bufferViews[indexAccessor.bufferView];
		const tinygltf::Buffer& indexBuffer = model.buffers[indexBufferView.buffer];
		size_t indexByteOffset = indexAccessor.byteOffset + indexBufferView.byteOffset;
		size_t numIndices = indexAccessor.count;
	    const unsigned char* bufferData = indexBuffer.data.data() + indexByteOffset;
	    indices.resize(numIndices);
		if (indexAccessor.componentType == TINYGLTF_COMPONENT_TYPE_UNSIGNED_SHORT) {
    	    const uint16_t* indexData = reinterpret_cast<const uint16_t*>(bufferData);
    	    for (size_t i = 0; i < numIndices; i++)
    	        indices[i] = static_cast<unsigned int>(indexData[i]); // 16bit -> 32bit
		} else if (indexAccessor.componentType == TINYGLTF_COMPONENT_TYPE_UNSIGNED_INT) {
    	    const uint32_t* indexData = reinterpret_cast<const uint32_t*>(bufferData);
    	    for (size_t i = 0; i < numIndices; i++)
    	        indices[i] = static_cast<unsigned int>(indexData[i]); // 32bit as it is
    	} else {
    	    std::cerr << "Unsupported index component type: " << indexAccessor.componentType << std::endl;
    	}

    }

    GLuint VAO, VBO, EBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(float), vertices.data(), GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.size() * sizeof(unsigned int), indices.data(), GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glBindVertexArray(0);




	/* 3. Internals */


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




    while (!glfwWindowShouldClose(window)) {

		/* 1. Physics */


		/* 2. Input */


		/* 3. Logic */


		/* 4. Render */

		glUseProgram(shaderProgram);

		// (1) camera matrices
		GLint modelLoc = glGetUniformLocation(shaderProgram, "model");
        GLint viewLoc = glGetUniformLocation(shaderProgram, "view");
        GLint projLoc = glGetUniformLocation(shaderProgram, "projection");

	    glm::mat4 modelMat = glm::mat4(1.0f);
	    glm::mat4 viewMat = glm::lookAt(glm::vec3(0, 0, 5), glm::vec3(0, 0, 0), glm::vec3(0, 1, 0));
	    glm::mat4 projectionMat = glm::perspective(glm::radians(45.0f), 800.0f / 600.0f, 0.1f, 100.0f);

        glUniformMatrix4fv(modelLoc, 1, GL_FALSE, &modelMat[0][0]);
        glUniformMatrix4fv(viewLoc, 1, GL_FALSE, &viewMat[0][0]);
        glUniformMatrix4fv(projLoc, 1, GL_FALSE, &projectionMat[0][0]);

		// (2) lighting parameters



		// (3) draw
		glClearColor(clear_color.x * clear_color.w,
					 clear_color.y * clear_color.w,
					 clear_color.z * clear_color.w,
					 clear_color.w);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glBindVertexArray(VAO);
        glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);
        glBindVertexArray(0);





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
		ImGui::Render();
		ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        glfwSwapBuffers(window);
        glfwPollEvents();
    }


	glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &EBO);
    glDeleteProgram(shaderProgram);


	ImGui_ImplOpenGL3_Shutdown();
	ImGui_ImplGlfw_Shutdown();
	ImGui::DestroyContext();


    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}
