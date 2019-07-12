from pylab import *

def f(x):
	f = exp(x)*log(x) - x*x
	return f


def root_bisection(f,a,b,tolerance=1.0e-6):
	dx = abs(b-a)
	while dx > tolerance:
		x = (a+b)/2.0
		if (f(a)*f(x)) < 0:
			b = x
		else:
			a = x
		dx = abs(b-a)
	return x

root_bisection(f,1,2)

def root_newton(f,df,guess,tolerance=1.0e-6):
	dx = 2*tolerance
	while dx > tolerance:
		x1 = x - f(x)/df(x)
		dx = abs(x-x1)
		x = x1
	return x
