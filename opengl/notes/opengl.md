
# Visual design elements
Data delivered to Rendering engine

Line, Shape, Form
	vertex data
		position vector
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


## 정점 속성과 유니폼 속성
셰이더에 인풋으로 들어가는 정보들
attribute location(=index)를 먼저 찾아야 한다

정점 셰이더에서는 유니폼을 쓰지 않음




transform feedback
asynchronous pixel transfers


## 좌표
- normalized device coordinates
	viewport transformation
- screen-space coordinates


## Contexts?



# OpenGL 다큐멘테이션

## Inlay hint for glad


## 창 관련
- glfwSwapBuffers(window)
	every operation is done on the back buffer, to prevent flickering
- glfwPollEvents()


## 버퍼 관련
- glVertexAttribPointer
	(index, size, type, normalized, stride, offset)
	offset부터 size만큼의 데이터를 하나의 input으로 만든다
	stride씩 뛰면서 input들의 array를 만든다
	index(=location)는 그냥 표지이다

셰이더에 정점 데이터 넣기 전에 먹기 좋게 자르는 작업 수행
각 인덱스마다 

- glDrawArrays
	VBO
- glDrawElements
	EBO

```c++
glBindBuffer(GL_ARRAY_BUFFER, 0); // we can do this; VAO has stored the address of VBO
//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0); // we cannot do this; VAO stores this unbind-call for EBO
glBindVertexArray(0); // no need to unbind
```


## 셰이더 관련
다섯가지 타입(fubid)과 두가지 컨테이너
rgba, stpq

정점 셰이더
	layout (location = 0)
	gl_Position