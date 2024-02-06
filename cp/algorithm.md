『프로그래밍 대회에서 배우는 알고리즘 문제해결 전략』 (구종만 저)을 저만의 언어로 정리하는 프로젝트입니다.




# 알고리즘 설계 패러다임



top-down(DFS), bottom-up(BFS)
visited, parent: instead of tracking all path info
memoization, tabulation


부분문제를 나누는 방식의 힌트: 대체로 길이를 가지고 수학적 귀납법 하는 느낌으로?
탑다운/바텀업 문제에 따라 선택하기
	탑다운: 기저사례를 리스트업하기 힘들 때
	바텀업: 부분문제를 합치는 경우의 수를 리스트업하기 힘들 때


## 최적부분구조

- 스테이지를 인식하자 - 부분문제나 노드 등
- 인자도 반환도 전역변수로 잡을 수 있다는 것을 기억하자
- 전역변수를 인자나 반환으로 설정할 수록 은닉적이지만 복잡해진다
- 인자: 부분문제를 전부 리스트하거나 기저문제를 판단할 때 쓸 "현재" 정보를 넣는다
- 반환: 구하고자 하는 값으로 부분문제가 어떻게 합쳐지는지 추적할 수 있는 정보를 넣는다

재귀 시에 두 종류의 인풋
- 주로 int: 다음 찾기/문제 합치기/dp 갱신 등에서 아예 수정되어 들어감
- 주로 배열: stage 시작 초장에 수정되는 것 -> 보통 전역으로 잡는 게 초기화도 좋고

1. 종단조건(재귀인 경우)
2. 인풋업뎃(있을 경우)
3. 문제풀기(다음찾기/문제합치기/dp업뎃)

### 분할정복법
optimal substructure, non-overlapping subproblems
prun-and-search


### 탐욕법
optimal substructure, greedy choice property
분할정복에서 한쪽 문제가 바로 결정될 수 있는 것을 말함
탐욕선택을 위한 기준을 정할 것, 이것도 부분문제를 말하는 것으로 대부분 길이이다


### 동적계획법
optimal substructure, overlapping subproblems



## 
트리 탐색의 경우
결정문제는 퇴각검색, 최적화문제는 분기한정


탐색공간과 promising condition이 거의 분리된 경우
DFS에 조건 추가하기
제약충족문제



네트워크 플로우
시간복잡도(분할상환분석)
계산복잡도







# computational problems

## 결정 문제

## 탐색 문제

순열, 조합
부분집합
	비트마스크
	이진트리
분할


## 개수 문제
탐색 + 결정

## 최적화 문제
탐색 + 함수특징응용
탐색 + 결정

제곱, 구간합, 기울기


## 변환 문제
삽입, 삭제, 정렬, 뒤집기, 필터링, 복원

## 연산 문제
정수곱, 행렬곱






- - -


# 유명한 문제
marriage problem
traveling salesman problem
longest increasing subsequence
knapsack problem(fractional knapsack)
activity selection problem
satisfiability problem
hamiltonian cycle problem
longest path problem
integer linear programming problem
independent set problem
eight queens problem
sudoku solving problem
maze(flood fill)
string searching/matching


matrix multiplication
markov chain, hidden markov model
fast fourier transform
combinatorial game, ai
huffman code
metaheuristic: local search, simulated annealing







# Part 3

## 6. Brute force
FESTIVAL 기울기의 성질로 탐색공간 제한
BOGGLE 부분문제 설명
PICNIC 중복으로 세는 문제 smallest로 처리
BOARDCOVER 

재귀호출
최적화 문제: TSP

## 7. Divide and conquer
QUADTREE 부분문제 설명
FENCE 그밖의 15장 스위핑, 19장 스택, 25장 disjoint set 해법
FANMEETING 카라츠바 응용

정렬 문제: 머지 소트, 퀵 소트
카라츠바 알고리즘

## 8. Dynamic programming (part 1)
###
JUMPGAME 그냥 dag reachability 판별
WILDCARD 구간분할문제 아마존

### 최적화
TRIANGLEPATH 너무 dp 최적화의 전형적인 예제 문제
LIS JLIS PI 어레이에서 부분최적화 문제 뽑는 방법
QUANTIZATION 단순함수 근사 오차 문제, 정렬+구간분할법+최소제곱법

### 개수
TILING2
TRIPATHCNT
SNAIL
ASYMTILING
POLY

NUMB3RS 마르코프 체인

### 이론
overlapping subproblem
memoization(reference transparency)
optimal substructure

구간의 분할들을 탐색공간으로 할 때 memoization이 강력



## 9. Dynamic programming (part 2)
### 최적화 실제 답도 구하기
PACKING 배낭문제
OCR 히든 마르코프 문제

### k번째 답
MORSE k번째 원소 찾기
KLIS
DRAGON

### 캐시의 형태
ZIMBABWE 숫자바꾸기+대소판별+배수판별 동시에 만족하는 수 개수 구하기
RESTORE

일반적으로 어레이나 매트릭스로 정수 및 정수의 페어를 인풋으로 받았지만 다른 경우도 가능
map으로 벡터인풋 캐시 만들기
정수와 일대일대응시키는 함수 만들어서 정수인풋 캐시 만들기
	부울리안 배열 비트마스크, 순열 등

### 조합게임
TICTACTOE
NUMBERGAME 미니맥스

canWin 의 캐시화

### 메모리 아끼기
SUSHI 메모리가 너무 크고 중복 가능한 배낭 문제
GENIOUS

반복적 dp, 슬라이딩윈도우




## 10. Greedy algorhitm

SHCEDULE(?) 회의실 예약 문제, 스케줄링 문제
MATCHORDER 동적계획으로 풀면 너무 오래 걸리는 문제
LUNCHBOX
STRJOIN
MINASTIRITH


### 이론
greedy choice property
	가장 ~가 작은 ~를 포함하는 최적해가 존재한다
optimal substructure
	재귀로 묻는 부분문제에 최적으로 답했다면 전체문제도 최적


## 11. Combinatorial search

## 12. Optimization by decision making


# Part 4

## 13. Numerical analysis

## 14. Number theory

## 15. Computational geometry






# Part 5 선형 자료구조

## 16. Bitmask

## 17. Partial sum

## 18. List

## 19. Queue and stack

## 20. String


# Part 6 트리

## 21. Implementations and search

## 22. Binary search tree

## 23. Heap

## 24. Segment tree

## 25. Disjoint set

## 26. TRIE


# Part 7 그래프

## 27. Graph representations

## 28. DFS

## 29. BFS

## 30. Shortest path algorithm

## 31. Minimum spanning tree

## 32. Network flow



