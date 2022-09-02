#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
using namespace glm;
#include <iostream>


// callbacks
void framebuffer_size_callback(GLFWwindow* window, int width, int height){
	glViewport(0, 0, width, height);
}
void processInput(GLFWwindow *window){
	if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
		glfwSetWindowShouldClose(window, true);
}


int main(){
	if(!glfwInit()) return -1;
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // for Mac OS

	GLFWwindow* window = glfwCreateWindow(800, 600, "Learn OpenGL", NULL, NULL);
	if(!window){ glfwTerminate(); return -1; }
	glfwMakeContextCurrent(window);
	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

	if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) return -1;

	// glViewport(0, 0, 800, 600);





	/* build and compile our shader programs */
	// 1. Compile vertex shader
	unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
	const char* vertexShaderSource =
		"#version 330 core\n"
		"layout (location = 0) in vec3 aPos;\n"
		"void main(){\n"
		"   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
		"}\0";
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	glCompileShader(vertexShader);

	// 2. Compile fragment shader
	unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	const char* fragmentShaderSource =
		"#version 330 core\n"
		"out vec4 FragColor;\n"
		"void main(){\n"
		"	FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
		"}\0";
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
	glCompileShader(fragmentShader);

	// 3. Link the shader program
	unsigned int shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);

	// 4. Clean up shaders
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);







	/* set up vertex data and buffer */
	float vertex_data[] = {
		0.5f,  0.5f, 0.0f,  // top right
		0.5f, -0.5f, 0.0f,  // bottom right
		-0.5f,  -0.5f, 0.0f,  // top left
		-0.5f, 0.5f, 0.0f
	};
	unsigned int index_data[] = { 0, 1, 3, 1, 2, 3 };

	// Gen
	unsigned int VAO, VBO, EBO;
	glGenVertexArrays(1, &VAO);
	glGenBuffers(1, &VBO);
	glGenBuffers(1, &EBO);

	// Bind and copy
	glBindVertexArray(VAO);

	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(vertex_data), vertex_data, GL_STATIC_DRAW);

	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(index_data), index_data, GL_STATIC_DRAW);

	glEnableVertexAttribArray(0);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3*sizeof(float), (void*)0);

	// Unbind
	glBindBuffer(GL_ARRAY_BUFFER, 0); // we can do this because VAO has stored the VBO data
	//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0); // we cannot do this because VAO stores this unbind-call for EBO
	glBindVertexArray(0); // no need to unbind




	// render loop
	while(!glfwWindowShouldClose(window)){
		processInput(window);

		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT);

		glUseProgram(shaderProgram);

		// Bind VAO and draw
		glBindVertexArray(VAO);
		glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
		glBindVertexArray(0); // no need to do this


		glfwSwapBuffers(window);
		glfwPollEvents();
	}
	glfwTerminate();
	return 0;
}