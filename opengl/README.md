# LearnOpenGL Roadmap

## Getting started

### Transformations

좌표는 vec4, 벡터는 vec3로 표현하는 습관을 들여보면 어떨까? 계속 테스트하면서 고민 좀 해보자.


다음 세 가지 모두 3차원 변환이므로 4행 성분은 0001이다.
translate: vec3로
scale: vec3로 성분별
rotate: float 각과 vec3 축으로

perspective: float fov, float aspect,

S3 -> SO(3)
단위사원수가 순허수에 컴쥬게이션으로 액트하는 게 회전 변환


### Coordinate systems
Local(Object)
	model
World
	view
View(Eye)
	projection
Clip
Screen

### Camera


fps 카메라




## Ligting

### Colors
	vec3 fragColor = lightColor * objectColor;
	FragColor = vec4(fragColor, 1.0); //
실제 물리와 너무 다르다 이렇게 그냥 곱해버려도 되는 근거가 뭘까
광원을 위한 새로운 VAO 따로 만들기

1. 그래픽스 상에서 밝기(brightness)와 세기(intensity)를 어떻게 이해해야 할까?

2. 스펙트럼을 고려하지 않아도 괜찮은 상황에는 어떤 것이 있을까?

slavish obedience to physical laws를 피하자

Two methods of color composition
- maximum intensity projection
- alpha blending


### Basic lighting
퐁 모델: 앰비언트, 디퓨즈, 스페큘라
그래픽스에서 퐁 모델이 웬만한 기본 틀이 될 것이다.
최종 반환값 형태는 lightColor * (strength * lambertFactor) * objectColor

	vec3 amb = ambientStrength;
	vec3 diff = diffuseStrength * max(dot(normal, lightDir), 0.0);
	vec3 spec = specularStrength * pow(max(dot(viewDir, reflectDir), 0,0), shininess)
	vec3 fragColor = lightcolor * (amb + diff + spec) * objectColor;

diffuseStrength는 어지간해서 1.0임
vec3 fragPos(world 좌표)와 vec3 normal(world 좌표)를 정점 셰이더에서 얻어와야 함
normal의 world 좌표 얻는 방법에 대해서 좀 더 고민해보자. mat3 model 이 orthogonal up to scale이기 때문에 transpose inverse 없이 scaling만 잘해주면 될 거 같은 느낌인데..
정점 셰이더에서 계산하게 되면 보간이 적용되는데, Phong 셰이딩 대신 Gouraud 셰이딩이라 함
Dir 벡터는 반사지점을 원점으로 하는 컨벤션을 따르도록 하자.

### Materials
대략 빛과 반응할 수 있는 속성값

	struct Material{
		vec3 ambient;
		vec3 diffuse;
		vec3 specular;
		float shininess;
	};
	uniform Material material;

a,d,s 값은 물체의 속성으로도 광원의 속성으로도 설정할 수 있다:

	vec3 diffuse = light.diffuse * diff * material.diffuse;

material.diffuse에는 objectColor가 반영되어 있음

### Lighting maps
텍스쳐와 똑같이 glActiveTexture와 glBindTexture를 사용
디퓨즈 맵과 스페큘라 맵으로 나뉜다

머티리얼의 diffuse 값을 sampler2D 타입으로 받아보자. 텍스쳐도 똑같이 sampler2D 타입으로 받을 수 있다.

	vec diffuseColor = light.diffuse * diff * vec3(texture(material.diffuse, texCoords));

### Light casters
directional, point, spotlight

	struct dirLight {
		vec3 direction;
		vec3 ambient, diffuse, specular;
	};

	struct ptLight {
		vec3 position;
		float con, lin, quad;
		vec3 ambient, diffuse, specular;
	};

attenuation of point light
	역제곱 법칙을 따라 감쇠한다
	그러나 0의 특이점 상수항과 선형항도 보통 넣는다
	이차항계수와 상수항계수를 1, 선형계수를 0으로 두면 무난하다
	이차항계수를 건드리는 것은 물리적으로 좋지 못하다: 적절한 선형계수 스케일링으로 광원 자체의 intensity를 건드리는 효과와 근사적으로 같기 때문
나중에 볼 gamma correction과 함께 다뤄보자

	float dist = length(light.position - fragPos);
	float atten = 1.0/(이차식)

	struct spotLight {
		vec3 position;
		vec3 direction;
		float cosCutoff;
		vec3 ambient, diffuse, specular;
	}

각도의 값을 코사인으로 저장해두는 것이 내적 계산과 compatible할 것이다.


### Multiple lights

조명 계산의 캡슐화
밝기가 1을 넘었을 때 계산을 생략하는 테크닉
셰이더 내부 vec3 calc_contrib_light(light, normal, viewDir);와 같은 함수를 구현하여
+=로 contribution을 계속 더하여 조각 셰이더의 아웃풋으로 반환



## Model Loading
### Assimp
### Mesh
### Model



다음주 동안:
assimp만 clion에서 돌려보고 (advanced * 2 + pbr)

그 다음 전공서들 살짝씩 펴보면서
opengl 실험용 프레임워크 구축하는 데 시간 붓자



물리엔진 관련해서 opengl 프로젝트 한 두 개 정도 짜보자
unity 스크립팅 연습은 그냥 깔짝만 대보자










## Advanced OpenGL
### Depth testing
### Stencil testing
### Blending
### Face culling
### Framebuffers
### Cubemaps
### Advanced data
### Advanced GLSL
### Geometry shader
### Instancing
### Anti-aliasing

## Advanced Lighting
### Advanced lighting
### Gamma correction
### Shadows
Shadow mapping
Point shadows
### Normal mapping
### Parallax mapping
### HDR tonemapping
### Bloom
### Deferred shading
### Screen space ambient occlusion

## PBR
### Theory
### Lighting
### IBL
Diffuse irradiance
Specular IBL




## In practice
### Debugging
### Text rendering
### 2D game
breakout
setting up
rendering sprites
levels
collisions: ball, collision detection, collision resolution
particles
postprocessing
powerups
audio
render text
final thought

## Guest articles
### OIT
### Skeletal animation
### CSM
### Scene
scene graph, frustum culling
### Tessellation
height map, tesselation
### DSA
### Compute shader
### Physically based bloom












# Projects

## Exercises

### Camera

- Flight simulation
마우스와 키보드 신호에 딜레이를 받으며 카메라와 비행기가 움직이는 상황을 어떻게 모델링할까?

- Lens
	
- Focusing
먼 곳은 흐리게 가까운 곳은 선명하게

- Motion blur

### Lighting

- Flash light
플래시는 포물면과 가까운 모양으로 좀 더 빛이 멀리나가게 설계가 되어 있다. 감쇠공식을 어떻게 모델링해야 할까?
컷오프의 페더(소프트엣지) 및 부분배경광도 모델링하고자 한다. 중심으로부터 멀어지는 각도에 대한 감쇠공식은 어떻게 모델링해야 할까? (튜토리얼은 렐루마냥 깎았다)
계산량은 어떻게 되는가?

- Lamp
시간에 따라 깜빡이며 랜덤하게 작용하는 광원, 방향도 제한적








## Rendering engine



실험해볼 것들 많을 것 같다
레이 트레이싱, GI, 특히 컴퓨터 친화적인 부분에서 많을 것 같다

멋있는 2d 이미지를 3d로 카피하기
시각효과들





## Physics engine

force field


### Rigid body
collision
rigid body motion

### Soft body
slime
cloth
hair

deformation
destruction

### Fluid
liquid, gel
fire, smoke, plasma, bubble
flow, wave
raindrops
	식물 잎사귀에 떨어지는 물방울, 젖어가는 흙
witchery effects

### Particle
sands
snow
	눈 종류, 바람 상호작용, 사람 상호작용

### Phase transition
soot generation from fire
fogging
melting ice
combustion

### 이동
ships, airplanes, bird flight 





## Map generation

### Skybox
atmospheric scattering
astronomy

### Climate
cloud simulation
raining snowing lightening
rainbow intensity and positioning

### Terrain
terrain formation
ecosystem simulation: forest, marine..
open world













# Visual design elements
Data delivered to Rendering engine

Line, Shape, Form
	vertex data
		position vector
	movement data
		geometric/organic, curvilinear/rectilinear
Texture
	uv mapping coordinates data
	physical parameters data
Space
	camera position and angle data
	depth data for each vertex
	skybox animation image data
	focus data
		geometry of projection
Color, Value
	color data
	contrast data


Attribute
Uniform
Texture

