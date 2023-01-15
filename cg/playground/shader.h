#ifndef SHADER_H
#define SHADER_H

#include <glad/glad.h>
#include <glm/glm.hpp>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

class Shader {
private:
	unsigned int ID;

	static void checkCompileErrors(unsigned int shader, const std::string& type) {
		int success;
		char infoLog[1024];
		if(type != "PROGRAM") {
			glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
			if(!success) {
				glGetShaderInfoLog(shader, 1024, NULL, infoLog);
				std::cout << "ERROR::SHADER_COMPILATION_ERROR of type: " << type << "\n" << infoLog << "\n -- --------------------------------------------------- -- " << std::endl;
			}
		}
		else {
			glGetProgramiv(shader, GL_LINK_STATUS, &success);
			if(!success) {
				glGetProgramInfoLog(shader, 1024, NULL, infoLog);
				std::cout << "ERROR::PROGRAM_LINKING_ERROR of type: " << type << "\n" << infoLog << "\n -- --------------------------------------------------- -- " << std::endl;
			}
		}
	}

public:
	Shader() {
		ID = glCreateProgram();
	}
	Shader(const string& path1, const string& path2) {
		ID = glCreateProgram();
		setShader(path1);
		setShader(path2);
	}

	void setShader(const string& path) const {
		const char* code;
		std::string str;
		std::ifstream fs;
		fs.exceptions (std::ifstream::failbit | std::ifstream::badbit);
		try {
			fs.open(path);
			std::stringstream ss;
			ss << fs.rdbuf();
			str = ss.str();
			fs.close();
		}
		catch(std::ifstream::failure& e) {
			std::cout << "ERROR::SHADER::FILE_NOT_SUCCESSFULLY_READ: " << e.what() << std::endl;
		}
		code = str.c_str();

		unsigned int shader;
		if(path.substr(path.find_last_of('.')+1) == "vert")
			shader = glCreateShader(GL_VERTEX_SHADER);
		if(path.substr(path.find_last_of('.')+1) == "frag")
			shader = glCreateShader(GL_FRAGMENT_SHADER);

		glShaderSource(shader, 1, &code, NULL);
		glCompileShader(shader);
		checkCompileErrors(shader, "SHADER");

		glAttachShader(ID, shader);
		glDeleteShader(shader);
		glLinkProgram(ID);
		checkCompileErrors(ID, "PROGRAM");

	}

	void use() const {
		glUseProgram(ID);
	}
	unsigned int getID() const {
		return ID;
	}

	void setBool(const std::string &name, bool value) const {
		glUniform1i(glGetUniformLocation(ID, name.c_str()), (int)value);
	}
	void setInt(const std::string &name, int value) const {
		glUniform1i(glGetUniformLocation(ID, name.c_str()), value);
	}
	void setFloat(const std::string &name, float value) const {
		glUniform1f(glGetUniformLocation(ID, name.c_str()), value);
	}
	void setMat4(const std::string &name, const glm::mat4 &mat) const  {
		glUniformMatrix4fv(glGetUniformLocation(ID, name.c_str()), 1, GL_FALSE, &mat[0][0]);
	}

};


#endif
