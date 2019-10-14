import numpy as np
from linalg import *


def solve_euler(f, x0, domain=None):
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
	domain : array of size n_t
		Array of mesh points. Recommended to generate it with np.linspace.

	Returns
	-------
	x : array of size n_t
		Numerical solution.
	'''
	t = domain
	x = np.zeros(domain.size)

	x[0] = x0
	for i in range(domain.size - 1):
		x[i+1] = x[i] + (t[i+1] - t[i]) * f(t[i], x[i])
		
	return x



def solve_1d_poisson_dirichlet(f, x0, x1, domain=None):
	'''
	Solves

		x''(t) = f(t),
		x(0) = x0,
		x(1) = x1.
	
	Example
	-------
		f = lambda t : np.sin(10*t)
		t = np.linspace(0, 1, 1000+1)
		x = solve_1d_poisson_dirichlet(f, x0=0, x1=0.05, domain = t)
	'''
	t = domain
	h = t[1] - t[0]
	n = domain.size - 1

	y = np.zeros(n+1)
	y[0] = - x0 / (h ** 2)
	y[n] = - x1 / (h ** 2)
	for i in range(n+1):
		y[i] += (-1) * f(t[i])

	A = np.diag(np.ones(n), k=-1)
	A += np.diag(np.full(n+1, -2))
	A += np.diag(np.ones(n), k=1)

	x = solve_tridiagonal(A, y)
	x *= (h ** 2)

	return x