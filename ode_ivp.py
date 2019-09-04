import numpy as np


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

