

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
