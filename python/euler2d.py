import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Euler_solve(u):
	#
	T,X,Y = u.shape

	return u

def Poisson_solve(p,f):
	# Neumann boundary

	return p

def Advection_solve(r,u):
	# Semi-Lagrangian

	return r


T = 100
X = 50
Y = 100


u = np.empty((T,X,Y)), np.empty((T,X,Y))
u[:,0,:] = 0,0,0 # top
u[:,:,0] = 0,0,0 # left
u[:,-1,:] = 0,0,0 # bottom
u[:,:,-1] = 0,0,0 # right

p = np.empty((T,X,Y))
