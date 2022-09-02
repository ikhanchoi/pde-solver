
# Visual design elements
Data delivered to Rendering engine

Line, Shape, Form (Primitives)
	vertex data
	movement data
		geometric/organic, curvilinear/rectilinear
Space
	camera position and angle data
	depth data for each vertex
	skybox animation image data
	focus data
		geometry of projection
Texture
	uv mapping coordinates data
	physical parameters data
Color, Value
	color data
	contrast data



# Notes for tutorial


## Hello window
- glfwSwapBuffers(window); glfwPollEvents();
	every operation is done on the back buffer, to prevent flickering

## 
- normalized device coordinates
	viewport transformation
- screen-space coordinates