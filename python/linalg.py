import numpy as np

def Tridiagonal_solve(A, y):
	'''

	b0 x0 + c0 x1                 = y0
	a1 x0 + b1 x1 + c1 x2         = y1
	        a2 x1 + b2 x2 + c2 x3 = y2 ...

	(b0b1-a1c0) x1 + (b0c1) x2         = b0 y1 - a1 y0
	        a2  x1 +    b2  x2 + c2 x3 = y2 ...

	Define d,e,f such that 
	d[i-1] x[i-1] + e[i-1] x[i]               = f[i-1]
	 a[i]  x[i-1] +  b[i]  x[i] + c[i] x[i+1] =  y[i]
	->
	(d[i-1]b[i]-e[i-1]a[i])x[i] + (d[i-1]c[i])x[i+1] = d[i-1]y[i]-a[i]f[i-1]
	i.e.
		d[i] = d[i-1] * b[i] - e[i-1] * a[i]
		e[i] = d[i-1] * c[i]
		f[i] = d[i-1] * y[i] - a[i] * f[i-1]


	i = n
	d[n-1] x[n-1] + e[n-1] x[n] = f[n-1]
	a[n] x[n-1] + b[n] x[n] = y[n]

	x[n] = f[n]/d[n]

	x[i-1] = (f[i-1] - e[i-1]x[i]) / d[i-1]


	'''
	n = y.size - 1

	a = np.diag(A, k=-1)
	a = np.insert(a, 0, 0.) # a[0] is not used
	b = np.diag(A)
	c = np.diag(A, k=1)

	d = np.zeros(n+1)
	e = np.zeros(n)
	f = np.zeros(n+1)
	x = np.zeros(n+1)

	# forward
	d[0] = b[0]
	e[0] = c[0]
	f[0] = y[0]
	for i in range(1,n+1):
		d[i] = d[i-1] * b[i] - e[i-1] * a[i]
		if i < n:
			e[i] = d[i-1] * c[i]
		f[i] = d[i-1] * y[i] - a[i] * f[i-1]

	# backward
	x[n] = f[n] / d[n]
	for i in range(n,0,-1):
		x[i-1] = (f[i-1] - e[i-1] * x[i]) / d[i-1]

	return x
