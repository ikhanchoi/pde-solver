# 1. Pointer


## 참조자


## 메모리 구조
Code:  실행코드
Data:  전역변수 정적변수
Heap:  동적할당
Stack: 지역변수 매개변수

## 동적할당


RAII
스마트 포인터







# 2. Class

## 스태틱
1. Static variable
	Data 영역에 저장: 지역범위를 가지는 전역변수라 생각하자
	초기화:
		0으로 자동 초기화
		최초 초기화 이후 초기화는 무시됨
	불가능:
		다른 파일에서의 외부참조(extern) 불가
		매개변수로 사용 불가

2. Static object
	Data 영역에 저장
	생성자로 초기화, 0으로 초기화되지는 않음
	소멸자 main 끝날 때 자동호출

3. Static member variable
	모든 object에서 공유
	초기화:
		privte이라 하더라도 객체 생성 전에 전역범위에서 X::v로 초기화
		최초 초기화 이후 초기화는 무시됨

4. Static member function
	모든 class에서 공유
	객체 생성 없이 X::f로 호출
	static member에만 접근가능


static const vs const static
- static const
	클래스 내부 초기화 가능
	헤더 파일에서 초기화 가능
	초기화 이후 값 변경 불가능

const 변수의 값은 컴파일타임에 결정

## 오버라이딩과 오버로딩

## 함수포인터









# 3. Stream







# 4. Virtual
가상함수 테이블






# 5. Template






# 6. Multi-thread


비동기 처리?

