







# OpenGL

## Core-profile에 관하여

디버깅 팁들?









# Creating a Window

## CMake
CMake의 기본개념
	target(executable과 library), link
find_package 가 찾을 수 있게 경로 알려주는 방법

## 확장 라이브러리들에 대하여
GLAD vs GLEW, GLFW vs GLUT

glad에서 inlay hint가 없다
근데 맥에서는 glad를 뺐을 때 잠시 확인할 수 있다
왜?


Q. 어떻게 좀 inlay hint 띄울 수 없나?
Q. KRH가 없어도 왜 돌아가나?






# Hello Window

Viewport

렌더 루프
- 콜백함수
- glfwSwapBuffers(window)
	every operation is done on the back buffer, to prevent flickering
- glfwPollEvents()

## Contexts?





# Hello Triangle

## 파이프라인 이해하기

1. 창 만들기
2. 셰이더
3. 텍스쳐
4. 버텍스
5. 렌더 루프
	셰이더-텍스처-버텍스-드로우




## 버텍스 스페시피케이션

- glVertexAttribPointer
	(index, size, type, normalized, stride, offset)
	offset부터 size만큼의 데이터를 하나의 input으로 만든다
	stride씩 뛰면서 input들의 array를 만든다
	index(=location)는 그냥 표지이다

셰이더에 정점 데이터 넣기 전에 먹기 좋게 자르는 작업 수행
각 인덱스마다 ㅇㅇ


인덱스로 그릴 때 프리미티브마다 인터폴레이션이 들어가므로 사각형을 어떤 두 삼각형으로 쪼개냐에 따라 그라데이션이 다르게 칠해짐





## 렌더루프 관련
- glDrawArrays
	VBO
	vertex, normal, color -> primitives
- glDrawElements
	EBO

```c++
glBindBuffer(GL_ARRAY_BUFFER, 0); // we can do this; VAO has stored the address of VBO
//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0); // we cannot do this; VAO stores this unbind-call for EBO
glBindVertexArray(0); // no need to unbind
```

배경 


물체
	context 만들어진 창, bind된 VAO, use선언된 셰이더
	이 세 개가 주어지면 그릴 수 있는 듯?






# Shaders


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

Q. 왜 셰이더 코드와 텍스처 이미지 로드할 때 앞에 ../ 붙여줘야 하나?
A. 셰이더 코드를 컴파일할 때 워킹 디렉토리는 실행파일이 존재하는 곳이다..?
예를 들어 clion에서 상대경로 지정할 때 실행파일이 서브디렉토리에 생기므로..?
불확실


버텍스 셰이더와 프래그먼트 셰이더 확장자 상관없다
Q. 적어도 초기 튜토리얼에서는 vert와 frag 사이에 아무것도 하지 않는데, 그렇다면 셰이더 파일 하나만 있어도 되는 건가?
Q. 셰이더 프로그램의 최종결과물은 rgba를 나타내는 vec4이기만 하면 되는 건가?



# Textures



wrapping, filtering

loading, applying






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


Attribute
Uniform
Texture





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