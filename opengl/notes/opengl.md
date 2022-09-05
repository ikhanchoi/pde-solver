
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


## Contexts







# OpenGL 다큐멘테이션

## 확장 라이브러리 관련
glad에서 inlay hint가 없다
근데 맥에서는 glad를 뺐을 때 잠시 확인할 수 있다

clion에서 상대경로 지정할 때 주의할 것
앞에 ../해줘야 함



## 버텍스 관련



- glVertexAttribPointer
	(index, size, type, normalized, stride, offset)
	offset부터 size만큼의 데이터를 하나의 input으로 만든다
	stride씩 뛰면서 input들의 array를 만든다
	index(=location)는 그냥 표지이다

셰이더에 정점 데이터 넣기 전에 먹기 좋게 자르는 작업 수행
각 인덱스마다 


## 그리기 관련
- glDrawArrays
	VBO
- glDrawElements
	EBO

```c++
glBindBuffer(GL_ARRAY_BUFFER, 0); // we can do this; VAO has stored the address of VBO
//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0); // we cannot do this; VAO stores this unbind-call for EBO
glBindVertexArray(0); // no need to unbind
```



## 창 관련
- glfwSwapBuffers(window)
	every operation is done on the back buffer, to prevent flickering
- glfwPollEvents()





## 셰이더 관련
변수
	다섯가지 타입(fubid)과 두가지 컨테이너(vec,mat)
	rgba, stpq

정점 셰이더
	layout (location = 0)
		VAO에서 받아오는 데이터들
	gl_Position
		미리 정의된 uniform 느낌?
		진짜 uniform인진 모르겠다

셰이더 로더 클래스 만들기
1. 코드 읽기
	최종적으로는 const char* 타입으로 변환시킬 것
2. 컴파일하기
	셰이더 만들고, 소스 주고, 컴파일
	프로그램 만들고, 셰이더 어태치하고, 링크
3. 유니폼 유틸리티 함수들 타입별로
	버텍스 어트리뷰트는 안됨