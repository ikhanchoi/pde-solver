#ifndef MAIN_CPP_MESH_H
#define MAIN_CPP_MESH_H

#include <glad/glad.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <string>
#include <vector>
using namespace std;

#include "shader.h"


struct Vertex {
	glm::vec3 Position;
	glm::vec3 Normal;
	glm::vec2 TexCoords;
	glm::vec3 Tangent;
	glm::vec3 Bitangent;
	int m_BoneIDs[4];
	float m_Weights[4];
};

struct Texture {
	unsigned int id;
	string type;
	string path;
};

class Mesh {
private:
	unsigned int VBO, EBO;

public:
	vector<Vertex>       vertices;
	vector<unsigned int> indices;
	vector<Texture>      textures;
	unsigned int VAO;

	Mesh(vector<Vertex> vertices, vector<unsigned int> indices, vector<Texture> textures);
	void draw(Shader &shader);
};


#endif
