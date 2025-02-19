

# Class design

rendering system, animation system, physics system, audio system, input system





## Initialization

### Window

### Externals

shaders -> program
a primitive -> vertex attribute object

### Internals

initial imgui parameters

initial camera matrices
initial lighting parameters




program, vao, camera uniforms, lighting uniforms
렌더 컴포넌트

## Loop

### Physics

### Input

### Logic

finite state machine


### Render

externals should be prepared

For each pair of program and vao, (1) get camera matrices (2) get lighting parameters (3) draw.





## Resource manager

크게 shader, model, sound 등



resource: mesh, textures, motion, sound 등이 있다. shader는 자원이지만 디자이너가 만들지는 않다 보니 resource이라고는 잘 안 하는 듯하다. 애셋을 원하는 형태로 안정적이게 로딩하는 기능을 가지며, 컴포넌트에 직접적으로 관련되지는 않는다.

object: component들을 가질 수 있는 것.

component: 업데이트에 의해 매 프레임 변경되는 속성값들과 반응하는 방식을 규정하는 규칙들을 갖고(내적 패러미터, 멤버 변수), 매 프레임마다 시스템으로부터 주변의 변화를 인식하여(외적 패러미터, 메소드 인자), 내적 패러미터를 갱신하고 시스템에 필요한 정보를 보고하는 update 메소드를 가진 클래스.

system: 특정 종류의 component들의 리스트를 들고 있어, 다른 component가 update 시의 참조할 수 있어야

render system: model/effect/camera/light component들의 리스트를 들고 있어서, camera와 light 정보를 보고받고, model이나 effect의 draw 메소드를 호출하는 클래스.

model: gltf파일 하나를 가지고 camera와 light 정보를 인자로 받아, 화면에 이미지를 출력하는 draw 메소드를 가지는 컴포넌트. render system에 보고할 정보는 없다. model/effect 컴포넌트가 다른 종류의 컴포넌트와 다른 한 가지는 update 메소드 대신 draw 메소드를 가진다는 것.

submesh: (말단 노드에 대응) vao를 최대 하나 가진다. 포맷/레이아웃이 똑같은 여러 mesh의 경우 하나의 vao에 넣는 것이 좋지만 그런 경우 처음부터 그렇게 모델링이 되었다고 가정해서 submesh와 vao를 일대일대응시키자.

material: texture들과 여러 parameter들을 shader program 하나로 묶은 서브컴포넌트. shader를 여러 개 만들어서 if문으로 선택하게도 할 수 있을 것이지만 일단 하나만 받자.

camera component: 위치와 각도 방향 및 카메라의 종류에. update 시


- 물리: 즉 강체인지 유체인지 등의 유형정보, collision 등의 정보, physical parameter.
- 인풋: FSM, FSM에 영향을 미칠 수 있는 인풋정보와 상호작용 정보, FSM parameter.

texture_diffuse1 0
texture_specular1 1
texture_normal1 2






대상을 만들어내는 일종의 클래스
같은 모델이 여러 장면에 나올 수도 있고 여러 대상으로 나올 수도 있다.
모델의 종류: 생물, 무생물, 현상 등


### mesh

### texture
우리는 texture를 assets에 한정시켜 specular map과 같은 이미지는 texture로 보고 material로는 보지 않을 것이다.





## shaders

정점별(attributes) < 대상별(material) < 장면별(camera, light interaction)
shader와 program에 사용되는 값들은 프레임마다 갱신해야 한다.
program은 object에 따라 다르게 적용된다.
즉, object 하나하나는 자신이 스크린에 어떻게 그려질 지를 지시할 program을 하나 갖고 있어야 한다.


### vertex shader
- in(layout): mesh(버텍스 버퍼에 저장된 메쉬 좌표값)
- uniform(interaction): cameras, 분위기/감정/진행도 등의 상황
- uniform: 시각효과(스카이박스, 착시 등)
- out: TexCoords

카메라행렬 계산, 정점보간

### fragment shader
- uniform: material(PBR 패러미터, texture 파일 인디케이터)
- uniform(interaction): lights, 분위기/감정/진행도 등의 상황
- in: TexCoords
- out(layout): FragColor

온갖 종류 효과 계산
그래픽 계산의 가장 큰 병목



어떻게 클래스를 디자인해야 submesh와 texture를 shader의 적절한 변수에 쉽게 대응시킬 수 있을까?





### Visual design elements: data delivered to Rendering engine

Line, Shape, Form
	vertex data
		position vector
	movement data
		curvilinear/rectilinear
		rigged bones, motion cycle data
	random data
		visual effects
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










### input system



### physics system



### ai system












# Shader programming

## meshes

높이 맵
착시효과
기하학적 변형


## cameras




## textures


## lights





transform feedback
asynchronous pixel transfers







# Physics simulation







