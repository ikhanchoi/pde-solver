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
## 가상함수 테이블


## 추상클래스
```c++
class AbstractClass
{
    virtual void abstractMemberFunction() = 0; // 순수가상함수가 있으므로 추상클래스가 됨
    virtual void abstractMemberFunction1(); // 가상함수
    void abstractMemberFunction2();
};
```

순수가상함수인 메소드를 하나 이상 가지면 추상클래스가 되어 객체를 만들 수 없게 된다.

순수가상소멸자
- 모든 클래스는 기본소멸자를 갖고 있다. 따라서 부모클래스의 소멸자가 순수가상함수여도 자식클래스에서 소멸자 구현을 할 필요가 없다.
- 순수가상함수를 가지고 있지 않은 부모클래스를 추상클래스로 만들 때 사용할 수 있다.
- 일반적인 순수가상함수는 자식클래스에서 구현되지만 순수가상소멸자는 아니므로 부모클래스에서 중괄호를 쳐줘서 형식적으로 구현해줘야 한다.



## 인터페이스

```c++
class IClass
{
public:
    virtual ~IClass() = default;
    virtual void move_x(int x) = 0;
    virtual void move_y(int y) = 0;
    virtual void draw() = 0;
};
```

모든 메소드를 순수가상함수로 만들어버리면 인터페이스라고 말할 수 있게 된다.
이때의 이점은 자식클래스들이 다양한 인터페이스들을 다중상속하여도 반드시 모든 메소드들을 구현해줘야 하므로 충돌을 반드시 피할 수밖에 없게 만든다는 것이다.
추상클래스는 하나만 상속한다는 약속을 하고 인터페이스는 기능에 대한 것을 추상화시키는 것이 좋다.
멤버변수는 넣지 않고 상속하는 자식클래스에 일일이 구현해주어야 한다.


# 5. Template






# 6. Multi-thread


비동기 처리?

