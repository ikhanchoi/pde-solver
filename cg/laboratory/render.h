#ifndef RENDER_H
#define RENDER_H


#include <GL/glew.h>

#include <vector>
using namespace std;

#include "mesh.h"
#include "material.h"



class Actor {
private:
public:
	void setRenderComponent(){

	}
};




class RenderComponent {
private:
	vector<tMesh> _meshes;
	vector<tMaterial> _materials;
	int size = 0;

public:
	void setMesh(const tMesh& mesh){
		_meshes.push_back(mesh);
		size++;
	}
	void setMaterial(const tMaterial &material){
		_materials.push_back(material);
	}
	void update(){
		// material parameters updated, for example, by inputs
		// mesh and textures are rarely updated
	}
	void draw(/* cameras and lights passed to shader programs */){

		for (int i = 0; i < size; i++){
			vector<tSubmesh> submeshes = _meshes[i].getSubmeshes();
			vector<tTexture> textures = _materials[i].getTextures();
			_materials[i].getProgram().use();

			for(GLuint j = 0; j < textures.size(); j++) {
				glActiveTexture(GL_TEXTURE0 + j);
				glBindTexture(GL_TEXTURE_2D, textures[j].getId());
			}

			for(auto & submesh : submeshes) {
				glBindVertexArray(submesh.getVAO());
				GLint indicesSize = 0;
				glGetBufferParameteriv(GL_ELEMENT_ARRAY_BUFFER, GL_BUFFER_SIZE, &indicesSize);
				glDrawElements(GL_TRIANGLES, static_cast<GLsizei>(indicesSize/sizeof(unsigned int)),
							   GL_UNSIGNED_INT, 0);
			}

			for(GLuint j = 0; j < textures.size(); j++) {
				glActiveTexture(GL_TEXTURE0 + j);
				glBindTexture(GL_TEXTURE_2D, 0);
			}

			glBindVertexArray(0);
			glActiveTexture(GL_TEXTURE0);
		}
	}

};

#endif
