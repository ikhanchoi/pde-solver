『프로그래밍 대회에서 배우는 알고리즘 문제해결 전략』 (구종만 저)을 저만의 언어로 정리하는 프로젝트입니다.


분류기준: 자료구조, 알고리즘, 출력형식, 수학문제


# c++ 팁

## STL container
vector
	push_back, pop_back, clear, resize, size
queue
	push, pop, front, empty, size
stack
	push, pop, top, empty, size
string
	push_back, substr

pair
	중괄호, first, second

map
 	for(auto iter:dp)
set
	for(auto iter:dp)


algorithm
	min, max
	sort(arr,arr+len)
	sort(vec.begin(),vec.end())


## 매크로
#define MAX_N 101
#define MOD 1000000007






# 출력형식별

## 결정 문제

## 탐색 문제




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





# 수학문제
## 수치

## 수론
소수판별


```c++
bool isPrime(int n)	{
	if(n<=1) return false;
	for(int i=2;i<sqrt(n)+.1;i++)
		if(n%i==0)
			return false;
	return true;
}
```


## 기하





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


matrix multiplication
markov chain, hidden markov model
combinatorial game, ai
huffman code
metaheuristic: local search, simulated annealing




- - -




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



