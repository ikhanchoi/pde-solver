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



def solve_1d_poisson_dirichlet(f, u0, u1, domain=None):
	'''
	Solves

		u''(x) = f(x),
		u(0) = u0,
		u(1) = u1.
	
	Example
	-------
		f = lambda x : np.sin(10*x)
		x = np.linspace(0, 1, 1000+1)
		u = solve_1d_poisson_dirichlet(f, u0=0, u1=0.05, domain = x)
	'''
	x = domain
	X = domain.size - 1
	h = x[1] - x[0]

	y = np.zeros(X+1)
	y[0] = - u0 / (h ** 2)
	y[X] = - u1 / (h ** 2)
	for j in range(X+1):
		y[j] += (-1) * f(x[j])

	A = np.diag(np.ones(X), k=-1)
	A += np.diag(np.full(X+1, -2))
	A += np.diag(np.ones(X), k=1)

	u = solve_tridiagonal(A, y)
	u *= (h ** 2)

	return u