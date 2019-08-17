import numpy as np
import matplotlib.pyplot as plt


def solve_euler(f=None, x0=None, t=None):
	'''
	Solves

		x' = f(t,x),
		x(0) = x0.

	Parameters
	----------
	f : function
		Function of the form f(t,x).
	x0 : float
		Initial value.
	t : array of size n_t
		Array of mesh points. Recommended to generate it with np.linspace.

	Returns
	-------
	x : array of size n_t
		Numerical solution.
	'''
	x = np.zeros(t.size)
	x[0] = x0
	for i in range(t.size - 1):
		x[i+1] = x[i] + (t[i+1] - t[i]) * f(t[i], x[i])
	return x


def visualize(x, t):
	plt.plot(t, x, '-')
	plt.axis([t[0], t[-1], 1.3*x.min()-0.3*x.max(), 1.3*x.max()-0.3*x.min()])

	plt.xlabel('t')
	plt.ylabel('x')
	plt.title(r'$dt=$', '%g'%(t[1] - t[0]))
	plt.legend(['numerical'], loc='upper left')
	#plt.grid(True)

	#plt.savefig('figure.png')
	plt.show()





def f(y, t):
	return y - t**2 + 1
t = np.linspace(0, 10, 200+1) # h = 0.5 -> (2-0)/h + 1 == 5
x = solve_euler(f, 0.5, t)
visualize(x,t)