#ifndef MAIN_CPP_WINDOW_H
#define MAIN_CPP_WINDOW_H

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <algorithm>

using namespace std;


void error_callback(int code, const char* description) {
	fprintf(stderr, "GLFW Error %d: %s\n", code, description);
}
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
	glViewport(0, 0, width, height);
}



class WindowInitializer {
private:
	int major, minor;
	int width, height;

public:

	WindowInitializer(int major, int minor, int width, int height) {
		int valid_versions[] = {10, 11, 12, 13, 14, 15,
								20, 21,
								30, 31, 32, 33,
								40, 41, 42, 43, 44, 45, 46};
		if(std::find(std::begin(valid_versions), std::end(valid_versions), 10 * major + minor))
			this->major = major, this->minor = minor;
		else cerr << "GLFW Error : version is not supported." << endl;

		this->width = width, this->height = height;
	}

	GLFWwindow* createWindow() const{

		glfwSetErrorCallback(error_callback);

		if(!glfwInit())
			cerr << "GLFW Error : initialization failed." << endl;

		// Window hints
		glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, major);
		glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, minor);
		if(major >= 3 && minor >= 2)
			glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	#ifdef __APPLE__ // for macOS
		if(major >= 3)
			glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
	#endif

		GLFWwindow* window = glfwCreateWindow(width, height, "Learn OpenGL", NULL, NULL);
		if(!window)
			cerr << "GLFW Error : window creation failed." << endl, glfwTerminate();
		glfwMakeContextCurrent(window);

		glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

		if(!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
			cerr << "GLAD Error : initialization failed." << endl;

		return window;
	}
};


#endif
