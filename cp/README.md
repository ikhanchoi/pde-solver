『프로그래밍 대회에서 배우는 알고리즘 문제해결 전략』 (구종만 저) 을 저만의 언어로 정리하는 프로젝트입니다.

linear, tree, graph
재귀: 백트래킹, 분할정복, 동적계획
탐욕, 조합탐색(가지치기), 결정최적
수학: 수치, 수론, 기하

bit manipulation?
metaheuristic: local search, simulated annealing


## 아웃풋의 형태에 따른 문제 분류
여부 문제
계산 문제
	개수, 합, 최적화,
	탐색공간별 -> 구간, 부분집합, 분할, 순열조합, 그래프 의존 등
	함수특징별: 제곱, 구간합, 기울기 등
연산 문제
	정수곱, 행렬곱
변환 문제
	정렬 문제, 뒤집기, 필터링 등


## 유명한 문제
marriage problem
traveling salesman problem
longest increasing subsequence
knapsack problem(fractional knapsack)
activity selection problem

matrix multiplication
markov chain, hidden markov model
combinatorial game, ai
huffman code


Part 3

# 6. Brute force
FESTIVAL 기울기의 성질로 탐색공간 제한
BOGGLE 부분문제 설명
PICNIC 중복으로 세는 문제 smallest로 처리
BOARDCOVER 

재귀호출, subproblem, reference transparency
최적화 문제: TSP

# 7. Divide and conquer
QUADTREE 부분문제 설명
FENCE 그밖의 15장 스위핑, 19장 스택, 25장 disjoint set 해법
FANMEETING 카라츠바 응용

정렬 문제: 머지 소트, 퀵 소트
카라츠바 알고리즘





# 8. Dynamic programming (part 1)
JUMPGAME 그냥 dag reachability 판별
WILDCARD 구간분할문제 아마존

## 최적화
TRIANGLEPATH 너무 dp 최적화의 전형적인 예제 문제
LIS JLIS PI 어레이에서 부분최적화 문제 뽑는 방법
QUANTIZATION 단순함수 근사 오차 문제, 정렬+구간분할법+최소제곱법

## 개수
TILING2
TRIPATHCNT
SNAIL
ASYMTILING
POLY

NUMB3RS 마르코프 체인

overlapping subproblem, memoization
optimal substructure

구간의 분할들을 탐색공간으로 할 때 memoization이 강력







# 9. Dynamic programming (part 2)
## 최적화 실제 답
PACKING 배낭문제
OCR 히든 마르코프 문제

## k번째 답
MORSE k번째 원소 찾기
KLIS
DRAGON

## 정수 이외 메모이제이션
ZIMBABWE 숫자바꾸기+대소판별+배수판별, 
RESTORE

map으로 벡터인풋 캐시 만들기
정수와 일대일대응시키는 함수 만들어서 정수인풋 캐시 만들기
	부울리안 배열 비트마스크, 순열 등

## 조합게임
TICTACTOE
NUMBERGAME 미니맥스

## 메모리 아끼기
SUSHI 메모리가 너무 크고 중복 가능한 배낭 문제
GENIOUS

반복적 dp 슬라이딩윈도우







# 10. Greedy algorhitm

# 11. Combinatorial search

# 12. Optimization by decision making


Part 4

# 13. Numerical analysis

# 14. Number theory

# 15. Computational geometry


Part 5

# 16. Bitmask

# 17. Partial sum

# 18. List

# 19. Queue and stack

# 20. String


Part 6

# 21. Implementations and search

# 22. Binary search tree

# 23. Heap

# 24. Segment tree

# 25. Disjoint set

# 26. TRIE


Part 7

# 27. Graph representations

# 28. DFS

# 29. BFS

# 30. Shortest path algorithm

# 31. Minimum spanning tree

# 32. Network flow