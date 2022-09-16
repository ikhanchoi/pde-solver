


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



