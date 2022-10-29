

#

## 3. inputs
input system을 어느 정도까지 만들어야 할까
렌더는

## 4. shaders

## 5. meshes


## 6. materials




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


Ambient occlusion
Bloom
Spectral rendering
Anti-aliasing

Normal mapping
Parallax mapping

PBR

Tesselation
Displacement mapping
Toon rendering

Ray tracing
Ray casting
Global illumination
Photon mapping

Subsurface scattering
transluency

Chroma key

코넬 박스, 스탠퍼드 토끼, 유타 주전자


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



# 셰이딩과 상용엔진의 한계
- 대규모 시뮬레이션 최적화 (팩토리오)
- 코드 다이어트를 통한 최적화
- 새로운 물리 상호작용 시스템 (노이타)
- 새로운 기하 시스템 (미에가쿠레)
- 새로운 렌더링 시스템/파이프라인









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
	Mesh
Texture
	Material

Uniform
	Camera
	Light





transform feedback
asynchronous pixel transfers

