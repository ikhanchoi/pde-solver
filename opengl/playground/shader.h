#ifndef MAIN_CPP_SHADER_H
#define MAIN_CPP_SHADER_H

#include <glad/glad.h>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

class Shader {
private:
	unsigned int ID;
	static void checkCompileErrors(unsigned int shader, std::string type);

public:
	Shader(const char* vert_path, const char* frag_path);
	void use();
	unsigned int getID();

	void setBool(const std::string &name, bool value) const;
	void setInt(const std::string &name, int value) const;
	void setFloat(const std::string &name, float value) const;
};


#endif
