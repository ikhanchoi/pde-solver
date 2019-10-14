import numpy as np
import matplotlib.pyplot as plt

from linalg import *
from ode import *
from visualize import *


'''
f = lambda t : np.sin(10*t)
t = np.linspace(0, 1, 1000+1)
x = solve_1d_poisson_dirichlet(f, x0=0, x1=0.05, domain = t)
Plot2d_array(x,t)
'''


x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
f = lambda x,y: np.sin(np.sqrt(x**2 + y**2))
Plot3d_function(f, x, y)