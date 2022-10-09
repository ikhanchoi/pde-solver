




# 8. Transformations

R3라서 좌표 세개가 아니라 RP3라서 좌표 네개, 따라서 변환들은 4차 행렬로 나타낼 거

행렬 곱 조작들: translate, scale, rotate; perspective

행렬들은 유니폼으로 정점 셰이더에 넘겨줌


## Normal vector transformation


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
구체적으로 각 행렬들이 glm에서 어떻게 만들어질 수 있는지들을 보자.
glm documentation에 들어가면 stable extensions 에서 확인하는 것이 가능

GLM_EXT_matrix_transform
glm::lookAt(eye, center, up)
glm::rotate(mat, angle, axis)
glm::scale(mat, ratio_vec)
glm::translate(mat, vec)

GLM_EXT_matrix_projection

GLM_EXT_matrix_clip_space



MV matrix를 만드는 효과적인 방법들
- angles to axes
- lookat to axes
- rotation about arbitrary axis
- quaternion
- mat4 class?


### Model matrix
모델을 월드의 어디에 놓은 거냐는 것에 대한 행렬
Model 성분별 혹은 방향성 가지는 스케일링까지는 존재 
translation, scaling, rotation:
orientation preserving similarity transformations

키보드 신호나 물리엔진을 돌려 나온 결과들이 개입될 것이다.

### View matrix
camera를 simulate하기 위해 주로 조작해야 하는 행렬

translation, rotation:
rigid motions




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

뒤통수 convention
Right(x) Up(y) Direction(z) 순서로 오른손


fov and aspects


lookAt(position, target, up)
은 view matrix를 만들어준다
- position vector 로 translation 먼저 함 Position을 (0,0,0)으로 보내는 행렬을 역행렬로서 구하게 되면
$$ \begin{pmatrix}1&0&0&P_x\\0&1&0&P_y\\0&0&1&P_z\\0&0&0&1\end{pmatrix}^{-1}=\begin{pmatrix}1&0&0&-P_x\\0&1&0&-P_y\\0&0&1&-P_z\\0&0&0&1\end{pmatrix} $$
- direction = position - target, right = up x direction 로 camera frame 구함
- Right를 (1,0,0), Up을 (0,1,0), Direction을 (0,0,1)로 보내는 행렬을 구하는데 이때 직교행렬의 역행렬이 전치행렬인 것 사용하면
$$ \begin{pmatrix}R_x&U_x&D_x\\R_y&U_y&D_y\\R_z&U_z&D_z\end{pmatrix}^{-1}=\begin{pmatrix}R_x&R_y&R_z\\U_x&U_y&U_z\\D_x&D_y&D_z\end{pmatrix}
$$


## Euler angle
SO(3)를 위한 한 좌표계


RxRyRz
roll->yaw->pitch?

Tait-Bryan angles, Aircraft principal axes

$D_x=\cos(yaw)\cos(pitch)$
$D_y=\sin(pitch)$
$D_z=\sin(yaw)\cos(pitch)$

yaw가 0이면 D=(1,0,0)
yaw = -phi
pitch = 90-theta

## Three camera implementations
fly like camera
FPS camera
flight simulation camera



