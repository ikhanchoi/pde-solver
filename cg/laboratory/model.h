#ifndef MODEL_H
#define MODEL_H


#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include "stb_image.h"
#include <assimp/Importer.hpp>
#include <assimp/scene.h>
#include <assimp/postprocess.h>


#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <map>
#include <vector>

#include "mesh.h"
#include "material.h"
using namespace std;


unsigned int TextureFromFile(const char* path, const string& directory, bool gamma = false);



class tModel {
private:
	Assimp::Importer _importer;
	vector<tSubmesh> _submeshes;
	vector<tTexture> _textures;

public:
	tModel(const string& path) {
		// initialize scene data structure from path
		const aiScene* scene = _importer.ReadFile(path,
				aiProcess_Triangulate |
				aiProcess_GenSmoothNormals |
				aiProcess_FlipUVs |
				aiProcess_CalcTangentSpace);
		// error message
		if(!scene || scene->mFlags & AI_SCENE_FLAGS_INCOMPLETE || !scene->mRootNode) {
			cout << "ERROR::ASSIMP_MESH_NOT_LOADED " << _importer.GetErrorString() << "\n";
			return;
		}
		// process meshes recursively
		processMesh(scene, scene->mRootNode);
		// process materials by for loop
		for(unsigned int i = 0; i < scene->mNumMaterials; i++)
			processMaterial(scene->mMaterials[i]);
	}

	void processMesh(const aiScene* scene, aiNode* node) {
		for(unsigned int i = 0; i < node->mNumChildren; i++)
			processMesh(scene, node->mChildren[i]);
		for(unsigned int i = 0; i < node->mNumMeshes; i++){
			aiMesh* mesh = scene->mMeshes[node->mMeshes[i]];
			vector<Vertex> vertices;
			vector<GLuint> indices;
			// process vertices
			for(unsigned int j = 0; j < mesh->mNumVertices; j++) {
				Vertex vertex;
				vertex.Position.x = mesh->mVertices[j].x;
				vertex.Position.y = mesh->mVertices[j].y;
				vertex.Position.z = mesh->mVertices[j].z;
				if (mesh->HasNormals()) {
					vertex.Normal.x = mesh->mNormals[j].x;
					vertex.Normal.y = mesh->mNormals[j].y;
					vertex.Normal.z = mesh->mNormals[j].z;
				}
				if(mesh->mTextureCoords[0]) {
					// a vertex can contain up to 8 different texture coordinates. We thus make the assumption that we won't
					// use models where a vertex can have multiple texture coordinates so we always take the first set (0).
					vertex.TexCoords.x = mesh->mTextureCoords[0][j].x;
					vertex.TexCoords.y = mesh->mTextureCoords[0][j].y;
					vertex.Tangent.x = mesh->mTangents[j].x;
					vertex.Tangent.y = mesh->mTangents[j].y;
					vertex.Tangent.z = mesh->mTangents[j].z;
					vertex.Bitangent.x = mesh->mBitangents[j].x;
					vertex.Bitangent.y = mesh->mBitangents[j].y;
					vertex.Bitangent.z = mesh->mBitangents[j].z;
				}
				else
					vertex.TexCoords = glm::vec2(0.0f, 0.0f);
				vertices.push_back(vertex);
			}
			// process face indices
			for(unsigned int j = 0; j < mesh->mNumFaces; j++) {
				aiFace face = mesh->mFaces[j];
				for(unsigned int k = 0; k < face.mNumIndices; k++)
					indices.push_back(face.mIndices[k]);
			}
			_submeshes.emplace_back(vertices, indices);
		}
	}

	void processMaterial(aiMaterial* material) {
		aiString aiPath;
		for(int t = 0; t < 22; t++ ) {
			auto type = static_cast<aiTextureType>(t);
			for(int i = 0; i < material->GetTextureCount(type); i++) {
				material->GetTexture(type, 0, &aiPath);
				string path(aiPath.C_Str());
				_textures.emplace_back(path, GL_TEXTURE_2D);
			}
		}
	}

	vector<tSubmesh> getSubmeshes() {
		return _submeshes;
	}
	vector<tTexture> getTextures() {
		return _textures;
	}

};












class Model {
public:
	// model data
	vector<Texture> textures_loaded;	// stores all the textures loaded so far, optimization to make sure textures aren't loaded more than once.
	vector<Mesh>    meshes;
	string directory;
	bool gammaCorrection;

	// constructor, expects a filepath to a 3D model.
	Model(string const& path, bool gamma = false) : gammaCorrection(gamma) { loadModel(path); }

	// draws the model, and thus all its meshes
	void Draw(unsigned int program){
		// program.use();
		for(auto& mesh : meshes)
			mesh.draw(program);
	}

private:
	void loadModel(string const &path) {
		Assimp::Importer importer;
		const aiScene* scene = importer.ReadFile(path, aiProcess_Triangulate | aiProcess_GenSmoothNormals | aiProcess_FlipUVs | aiProcess_CalcTangentSpace);
		if(!scene || scene->mFlags & AI_SCENE_FLAGS_INCOMPLETE || !scene->mRootNode) {
			cout << "ERROR::ASSIMP:: " << importer.GetErrorString() << "\n";
			return;
		}
		directory = path.substr(0, path.find_last_of('/'));
		processNode(scene->mRootNode, scene);
	}

	void processNode(aiNode* node, const aiScene* scene) {
		for(int i = 0; i < node->mNumChildren; i++) {
			processNode(node->mChildren[i], scene);
		}
		for(int i = 0; i < node->mNumMeshes; i++) {
			meshes.push_back(processMesh(scene->mMeshes[node->mMeshes[i]], scene));
		}
	}

	Mesh processMesh(aiMesh* mesh, const aiScene* scene) {
		// data to fill
		vector<Vertex> vertices;
		vector<unsigned int> indices;
		vector<Texture> textures;

		// walk through each of the mesh's vertices
		for(unsigned int i = 0; i < mesh->mNumVertices; i++) {
			Vertex vertex;
			glm::vec3 vector; // we declare a placeholder vector since assimp uses its own vector class that doesn't directly convert to glm's vec3 class so we transfer the data to this placeholder glm::vec3 first.
			// positions
			vector.x = mesh->mVertices[i].x;
			vector.y = mesh->mVertices[i].y;
			vector.z = mesh->mVertices[i].z;
			vertex.Position = vector;
			// normals
			if (mesh->HasNormals()) {
				vector.x = mesh->mNormals[i].x;
				vector.y = mesh->mNormals[i].y;
				vector.z = mesh->mNormals[i].z;
				vertex.Normal = vector;
			}
			// texture coordinates
			if(mesh->HasTextureCoords(0)) {
				glm::vec2 vec;
				// a vertex can contain up to 8 different texture coordinates. We thus make the assumption that we won't
				// use models where a vertex can have multiple texture coordinates so we always take the first set (0).
				vec.x = mesh->mTextureCoords[0][i].x;
				vec.y = mesh->mTextureCoords[0][i].y;
				vertex.TexCoords = vec;
			}
			if(mesh->HasTangentsAndBitangents()) {
				// tangent
				vector.x = mesh->mTangents[i].x;
				vector.y = mesh->mTangents[i].y;
				vector.z = mesh->mTangents[i].z;
				vertex.Tangent = vector;
				// bitangent
				vector.x = mesh->mBitangents[i].x;
				vector.y = mesh->mBitangents[i].y;
				vector.z = mesh->mBitangents[i].z;
				vertex.Bitangent = vector;
			}
			//else vertex.TexCoords = glm::vec2(0.0f, 0.0f);

			vertices.push_back(vertex);

		}
		// now wak through each of the mesh's faces (a face is a mesh its triangle) and retrieve the corresponding vertex indices.
		for(unsigned int i = 0; i < mesh->mNumFaces; i++) {
			aiFace face = mesh->mFaces[i];
			// retrieve all indices of the face and store them in the indices vector
			for(unsigned int j = 0; j < face.mNumIndices; j++)
				indices.push_back(face.mIndices[j]);
		}
		// process materials
		aiMaterial* material = scene->mMaterials[mesh->mMaterialIndex];
		// we assume a convention for sampler names in the shaders. Each diffuse texture should be named
		// as 'texture_diffuseN' where N is a sequential number ranging from 1 to MAX_SAMPLER_NUMBER.
		// Same applies to other texture as the following list summarizes:
		// diffuse: texture_diffuseN
		// specular: texture_specularN
		// normal: texture_normalN



		// 1. diffuse maps
		vector<Texture> diffuseMaps = loadMaterialTextures(material, aiTextureType_DIFFUSE, "texture_diffuse");
		textures.insert(textures.end(), diffuseMaps.begin(), diffuseMaps.end());
		// 2. specular maps
		vector<Texture> specularMaps = loadMaterialTextures(material, aiTextureType_SPECULAR, "texture_specular");
		textures.insert(textures.end(), specularMaps.begin(), specularMaps.end());
		// 3. normal maps
		std::vector<Texture> normalMaps = loadMaterialTextures(material, aiTextureType_HEIGHT, "texture_normal");
		textures.insert(textures.end(), normalMaps.begin(), normalMaps.end());
		// 4. height maps
		std::vector<Texture> heightMaps = loadMaterialTextures(material, aiTextureType_AMBIENT, "texture_height");
		textures.insert(textures.end(), heightMaps.begin(), heightMaps.end());

		// return a mesh object created from the extracted mesh data
		return Mesh(vertices, indices, textures);
	}

	// checks all material textures of a given type and loads the textures if they're not loaded yet.
	// the required info is returned as a Texture struct.
	vector<Texture> loadMaterialTextures(aiMaterial* material, aiTextureType type, string typeName) {
		vector<Texture> textures;
		for(unsigned int i = 0; i < material->GetTextureCount(type); i++) {
			aiString str;
			material->GetTexture(type, i, &str);
			// check if texture was loaded before and if so, continue to next iteration: skip loading a new texture
			bool skip = false;
			for(unsigned int j = 0; j < textures_loaded.size(); j++) {
				if(std::strcmp(textures_loaded[j].path.data(), str.C_Str()) == 0) {
					textures.push_back(textures_loaded[j]);
					skip = true; // a texture with the same filepath has already been loaded, continue to next one. (optimization)
					break;
				}
			}
			if(!skip) {   // if texture hasn't been loaded already, load it
				Texture texture;
				texture.id = TextureFromFile(str.C_Str(), this->directory);
				texture.type = typeName;
				texture.path = str.C_Str();
				textures.push_back(texture);
				textures_loaded.push_back(texture);  // store it as texture loaded for entire model, to ensure we won't unnecesery load duplicate textures.
			}
		}
		return textures;
	}

};


unsigned int TextureFromFile(const char *path, const string &directory, bool gamma) {
	string filename = string(path);
	filename = directory + '/' + filename;

	GLuint texture;
	glGenTextures(1, &texture);

	int width, height, nChannel;
	unsigned char* data = stbi_load(filename.c_str(), &width, &height, &nChannel, 0);
	if (data) {
		GLenum format;
		if (nChannel == 1)
			format = GL_RED;
		else if (nChannel == 3)
			format = GL_RGB;
		else if (nChannel == 4)
			format = GL_RGBA;

		glBindTexture(GL_TEXTURE_2D, texture);
		glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, data);
		glGenerateMipmap(GL_TEXTURE_2D);

		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
		glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

		stbi_image_free(data);
	}
	else {
		std::cout << "Texture failed to load at path: " << path << std::endl;
		stbi_image_free(data);
	}
	return texture;
}

#endif
