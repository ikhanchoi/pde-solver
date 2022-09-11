


# 1. Introduction

3. Contexts

libraries and cmake
buffer objects


4. Windows
	- input
	- drawing commands
7. Shaders
	- GLSL shader stages, compilation
	- vertex shader:
	- fragment shader: color interpolation

5. Attributes
	- VAO VBO EBO
    - model loading
6. Textures
	- wrapping
    - filtering



Camera -> vertex shader
	three transformations
		model: 
		view: camera class
		projection: 
	depth testing
	face culling

Lighting -> fragment shader

Physics?




# 2. OpenGL

## Core-profile

디버깅 팁들?










# 3. Creating a Window

## 3.1. Sample code

CMakeLists.txt


## 3.2. Libraries

### GLFW vs GLUT


### GLAD vs GLEW
glfw 이전에 include해야 한다

glad에서 inlay hint가 없다
근데 맥에서는 glad를 뺐을 때 잠시 확인할 수 있다
왜?

Q. 어떻게 좀 inlay hint 띄울 수 없나?
Q. KRH가 없어도 왜 돌아가나?




## 3.3. CMake


CMake의 기본개념
target(executable과 library), link
find_package 가 찾을 수 있게 경로 알려주는 방법









# 4. Hello Window

## 4.1. Sample code

## 4.2. OpenGL pipeline
창 만들기와 렌더 루프 사이에 버텍스, 텍스쳐, 셰이더를 준비

- Vertex processing (눈으로 인식하기)
- Vertex post-processing
- Primitive assembly (스케치하기)
- Rasterization and fragment shading (색칠하기)
- Per-sampling processing


## 4.3. Initialization

### GLFW
### GLAD
### Context


## 4.4. Input


## 4.5. Render loop

###
- 콜백함수
- glfwSwapBuffers(window)
	every operation is done on the back buffer, to prevent flickering
- glfwPollEvents()











# 5. Hello Triangle

## 5.1. Sample Code


## 5.2. Vertex specification

### Vertex stream

aPos aColor aTexCoord

### VBO

### VAO

셰이더에 정점 데이터 넣기 전에 먹기 좋게 자르는 작업 수행
각 인덱스마다

```c++
glVertexAttribPointer(index, size, type, normalized, stride, offset)
```

offset부터 size만큼의 데이터를 하나의 input으로 만든다
stride씩 뛰면서 input들의 array를 만든다
index(=location)는 그냥 표지이다






## 5.3. Drawing commands
- glDrawArrays
	VBO
	vertex, normal, color -> primitives
- glDrawElements
	EBO

```c++ {.line-numbers}
glBindBuffer(GL_ARRAY_BUFFER, 0);
//glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
glBindVertexArray(0); // no need to unbind
```

$f(x)$

첫번째 줄 가능; VAO has stored the address of VBO
두번째 줄 불가능; VAO stores this unbind-call for EBO


배경 


물체
	context 만들어진 창, bind된 VAO, use선언된 셰이더
	이 세 개가 주어지면 그릴 수 있는 듯?

Q. 시간 데이터 받는 거 1초에 얼만큼 값이 들어가는 거지? 속도 계산 필요할 때 있을 거 같은데











# 6. Shaders

## 6.1. Sample code



## 6.2. Shader stages

OpenGL의 렌더링 파이프라인은 다음 다섯 가지의 셰이더 stage를 정의한다.
스테이지가 실행되는 것을 invocation이라고 부르며, 매우 특수한 경우를 제외하고 각각의 invocation들은 상호작용할 수 없다.

- Vertex shaders
- Tesselation shaders
  - control shader와 evaluation shader
- Geometry shaders
  - Layered rendering, Transform feedback
- Fragment shaders
- Compute shaders

Vertex attributes, uniforms, textures

다섯가지 타입(fubid)과 두가지 컨테이너(vec,mat)
rgba, stpq

버텍스 셰이더와 프래그먼트 셰이더 확장자 상관없다
Q. 적어도 초기 튜토리얼에서는 vert와 frag 사이에 아무것도 하지 않는데, 그렇다면 셰이더 파일 하나만 있어도 되는 건가?
Q. 셰이더 프로그램의 최종결과물은 rgba를 나타내는 vec4이기만 하면 되는 건가?


### Shader programs

드로잉 커맨드가 실행되면 바인드 되어 있는 program object와 pipeline object가 사용된다


## 6.3. Compilation

### 


### Objects in GLSL
GLSL objects do not follow the paradigm of OpenGL objects

Program object
Shader object
Program pipeline object

런타임 때 컴파일:
셰이더 코드와 텍스처 이미지 로드할 때 경로를 조심해야 한다.
셰이더 코드를 컴파일할 때 워킹 디렉토리는 오브젝트 파일이 존재하는 곳이다..?
예를 들어 clion에서 상대경로 지정할 때 실행파일이 서브디렉토리에 생기므로..?
불확실



## 6.3. Vertex shader
input vertex stream에서 single vertex 받아서 계산 후 output vertex stream의 single vertex를 반환
모든 버텍스들이 버텍스 셰이더를 통과하는 것
보통 프로젝션 이전까지의 변환을 책임

대충 생각해서 버텍스 하나당 버텍스 셰이더가 대략 한 번씩 호출된다 생각하면 됨

정점 셰이더
layout (location = 0)
VAO에서 받아오는 데이터들
gl_Position
미리 정의된 uniform 느낌?
진짜 uniform인진 모르겠다

## 6.4. Fragment shader



셰이더 로더 클래스 만들기
1. 코드 읽기
	최종적으로는 const char* 타입으로 변환시킬 것
2. 컴파일하기
	셰이더 만들고, 소스 주고, 컴파일
	프로그램 만들고, 셰이더 어태치하고, 링크
3. 유니폼 유틸리티 함수들 타입별로
	버텍스 어트리뷰트는 안됨



인덱스로 그릴 때 프리미티브마다 인터폴레이션이 들어가므로 사각형을 어떤 두 삼각형으로 쪼개냐에 따라 그라데이션이 다르게 칠해짐








# 7. Textures

## 7.1. Sample code

## 7.2. Wrapping

## 7.3. Filtering

## 7.4. 
loading, applying


직각삼각형이 아닌 primitive에 texture 입히면 찌그러지나?







# 8. Transformations

R3라서 좌표 세개가 아니라 RP3라서 좌표 네개, 따라서 변환들은 4차 행렬로 나타낼 거

행렬 곱 조작들: translate, scale, rotate; perspective

행렬들은 유니폼으로 정점 셰이더에 넘겨줌




# 9. Coordinates

## 9.1. Sample code


큐브 1개 = 면 6개 = 삼각형 12개 = 정점 36개 이므로
큐브 하나 돌릴 때마다 드로잉 커맨드에 36개씩 버텍스 넣어줘야 함

## 9.2. Spaces

### Local space

### World space

### View space

### Clip space

### Screen space





## 9.3. Matrices



### Model matrix
translation, scaling, rotation:
orientation preserving similarity transformations

모델을 월드의 어디에 놓은 거냐는 것에 대한 것이다 보니
키보드 신호나 물리엔진을 돌려 나온 결과들이 개입될 것이다.

### View matrix
translation, rotation:
rigid motions

camera를 simulate하기 위해 주로 조작해야 하는 행렬.



### Projection matrix
Normalized device coordinates로 스케일링한다

이렇게 projection matrix가 만드는 clipping volume을 frustum이라고 한다
clipping volume 만들 때 near plane과 far plane을 설정해줘서 clipping volume을 compact하게 만든다
클리핑 여기서 한다

projection matrix는 다른 매트릭스에 비해서는 거의 안바뀌기 때문에 렌더 루프 바깥에서 잡는 경우가 많다

- perspective division
  - 이제 translation이나 rotation할 일 없으니까 homogeneous w component 버려도 됨
  - x,y,z 성분 뽑고 z는 깊이니까 음
  - 정점 셰이더 끝날 때 이루어진대. 최소한 이 예제에서는


Orthographic projection과 Perspective projection


### ViewPort transformation


## 9.4. Depth buffer

그냥 활성화시킨다는 것 말고 다루지 않음


# 10. Camera


fov and aspects

direction, right, up
lookAt(position, target, up)


## Euler angle
Aircraft principal axes

yaw = -phi
pitch = 90-theta

## Three camera implementations
fly like camera
FPS camera
flight simulation camera








# 11.

















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