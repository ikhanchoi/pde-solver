#ifndef MATERIAL_H
#define MATERIAL_H

#include <glm/glm.hpp>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Shader {
private:
	GLuint _id;
	vector<string> _uniforms; // name, type, value..?
public:
	Shader(const string& path) {
		if(path.substr(path.find_last_of('.')+1) == "vert")
			_id = glCreateShader(GL_VERTEX_SHADER);
		if(path.substr(path.find_last_of('.')+1) == "frag")
			_id = glCreateShader(GL_FRAGMENT_SHADER);

		ifstream fs;
		string code;
		fs.exceptions(ifstream::failbit|ifstream::badbit);
		try {
			fs.open(path);
			stringstream ss;
			ss << fs.rdbuf();
			code = ss.str();
			fs.close();
		}
		catch(ifstream::failure& e) {
			cout << "ERROR::SHADER_NOT_LOADED: " << "\n" << e.what() << "\n";
		}

		const char* cstr = code.c_str();
		glShaderSource(_id, 1, &cstr, NULL);
		glCompileShader(_id);

		int success;
		char infoLog[1024];
		glGetShaderiv(_id, GL_COMPILE_STATUS, &success);
		if(!success) {
			glGetShaderInfoLog(_id, 1024, NULL, infoLog);
			cout << "ERROR::SHADER_NOT_COMPILED: " << "\n" << infoLog << "\n";
		}
	}

	unsigned int getId() const {
		return _id;
	}
	void del() {
		glDeleteShader(_id);
	}

};

class Program {
private:
	GLuint _id;

public:
	Program() {
		_id = glCreateProgram();
	}

	void setShader(const Shader& shader) const {
		glAttachShader(_id, shader.getId());
		glLinkProgram(_id);
		int success;
		char infoLog[1024];
		glGetProgramiv(_id, GL_LINK_STATUS, &success);
		if(!success) {
			glGetProgramInfoLog(_id, 1024, NULL, infoLog);
			cout << "ERROR::PROGRAM_NOT_LINKED: " << "\n" << infoLog << "\n";
		}
	}

	unsigned int getId() const {
		return _id;
	}

	void use() const {
		glUseProgram(_id);
	}

	void setUniform() {

	}

};

/*
	void setBool(const std::string& name, bool value) const {
		glUniform1i(glGetUniformLocation(program, name.c_str()), (int)value);
	}
	void setInt(const std::string& name, int value) const {
		glUniform1i(glGetUniformLocation(program, name.c_str()), value);
	}
	void setFloat(const std::string& name, float value) const {
		glUniform1f(glGetUniformLocation(program, name.c_str()), value);
	}
	void setMat4(const std::string& name, const glm::mat4 &mat) const  {
		glUniformMatrix4fv(glGetUniformLocation(program, name.c_str()), 1, GL_FALSE, &mat[0][0]);
	}
*/



class tTexture {
private:
	GLuint _id;
	string _sampler;

public:
	tTexture(const string& path, GLenum type) {

		glGenTextures(1, &_id);
		int w,h,n;
		GLenum format;
		unsigned char* pixels = stbi_load(path.c_str(), &w, &h, &n, 0);

		if (n == 1) format = GL_RED;
		else if (n == 3) format = GL_RGB;
		else if (n == 4) format = GL_RGBA;

		glBindTexture(type, _id);
		glTexImage2D(type, 0, format, w, h, 0, format,
					 GL_UNSIGNED_BYTE, pixels);
		glGenerateMipmap(type);

		glTexParameteri(type, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(type, GL_TEXTURE_WRAP_T, GL_REPEAT);
		glTexParameteri(type, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
		glTexParameteri(type, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		stbi_image_free(pixels);
	}

	void setSampler(const string& sampler) {
		_sampler = sampler;
	}
	string getSampler() const {
		return _sampler;
	}

	GLuint getId() const {
		return _id;
	}
};


class tMaterial {
private:
	vector<tTexture> _textures;
	Program _program;
	// vector<> _; uniform parameters depending on shader programs
public:

	void setProgram(const Program& program) {
		_program = program;
	}
	void setTextures(const vector<tTexture>& texutures) {
		for(unsigned int i = 0; i < texutures.size(); i++)
			setTexture(texutures[i]);
	}
	void setTexture(const tTexture& texture) {
		_textures.push_back(texture);
		glActiveTexture(GL_TEXTURE0 + _textures.size() - 1);
		glUniform1i(glGetUniformLocation(_program.getId(), texture.getSampler().c_str()), _textures.size() - 1);
		glActiveTexture(GL_TEXTURE0);
	}

	vector<tTexture> getTextures() {
		return _textures;
	}
	Program getProgram() {
		return _program;
	}

	void setUniform() {

	}

};



#endif
