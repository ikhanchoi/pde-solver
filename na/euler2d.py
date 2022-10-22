import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def grad(u):
	return (u[n,i+1,j]-u[n,i-1,j])/(2*dx), (u[n,i,j+1]-u[n,i,j-1])/(2*dy)



def Euler_solve(u):
	#

	us[n+1,:,:] = u[n,:,:]
	us[n+1,:,:] -= dt*np.sum([u[n,:,:],v[n,:,:]]*grad(u[n,:,:]))

	return u

def Poisson_solve(p,f):
	# Neumann boundary

	return p

def Advection_solve(r,u):
	# Semi-Lagrangian

	return r


Nt = 100
Nx = 50
Ny = 100
dt
dx
dy





u = np.empty((Nt+1,Nx+1,Ny))
v = np.empty((Nt+1,Nx,Ny+1))
p = np.empty((Nt+1,Nx,Ny))
px = np.empty((Nt+1,Nx,Ny)) # gradient
py 

# initial condition


# boundary conditions
u[:,0,:] = 0 # top
u[:,:,0] = 0 # left
u[:,-1,:] = 0 # bottom
u[:,:,-1] = 0 # right






