from ode_ivp import *
from visualize import *

def f(x, t):
	return x - t**2 + 1

t = np.linspace(0, 10, 200+1) # h = 0.5 -> (2-0)/h + 1 == 5
x = solve_euler(f, 0.5, domain=t)


Plot2d(x,t)