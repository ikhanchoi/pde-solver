#include "window.h"


void error_callback(int code, const char* description) {
	fprintf(stderr, "Error %d: %s\n", code, description);
}
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
	glViewport(0, 0, width, height);
}

WindowInitializer::WindowInitializer(int major, int minor) {
	int valid_versions[] = {10, 11, 12, 13, 14, 15,
							20, 21,
							30, 31, 32, 33,
							40, 41, 42, 43, 44, 45, 46};
	if(std::find(std::begin(valid_versions), std::end(valid_versions), 10 * major + minor)){
		this->major = major;
		this->minor = minor;
	}
	else /* error */;
}

GLFWwindow* WindowInitializer::createWindow() {

	glfwSetErrorCallback(error_callback);

	if(!glfwInit()) /* return -1; */;

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, major);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, minor);

	if(major >= 3 && minor >= 2)
		glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
#ifdef __APPLE__ // for macOS
	if(major >= 3)
		glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

	GLFWwindow* window = glfwCreateWindow(800, 600, "Learn OpenGL", NULL, NULL);
	if(!window){ glfwTerminate(); /* return -1; */ }

	glfwMakeContextCurrent(window);

	glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

	if(!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) /* return -1; */;

	return window;
}