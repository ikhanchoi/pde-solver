import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def Heat_FTCS_solve(u):
	for n in range(Nt):
		for i in range(1,Nx):
			u[n+1,i] = u[n,i] + r*(u[n,i+1]-2*u[n,i]+u[n,i-1])
	return u

def Heat_BTCS_solve(u):
	d = np.zeros(Nx) # we do not use d[0],e[0],f[0]
	e = np.zeros(Nx-1)
	f = np.zeros(Nx)

	for n in range(Nt):
		# forward
		d[1] = 1+2*r
		e[1] = -r
		f[1] = u[n,1]
		for i in range(1,Nx-1):
			d[i+1] = d[i]*(1+2*r) + e[i]*r
			if i < Nx-2:
				e[i+1] = d[i]*(-r)
			f[i+1] = d[i]*u[n,i+1] + r*f[i]
		# backward
		u[n+1,Nx-1] = f[Nx-1] / d[Nx-1]
		for i in range(Nx-1,1,-1):
			u[n+1,i-1] = (f[i-1] - e[i-1]*u[n+1,i]) / d[i-1]
	return u


Nt = 1000
Nx = 20
t = np.linspace(0,1,Nt+1)
x = np.linspace(0,1,Nx+1)
dt = t[1] - t[0]
dx = x[1] - x[0]
r = dt/(dx**2)

# initialization
u = np.empty((Nt+1,Nx+1))
u[0,:] = 1
u[:,0] = 0
u[:,-1] = 0

# solve
u = Heat_FTCS_solve(u)


# animation
fig,ax = plt.subplots()
def update(t):
	ax.cla()
	ax.set_xlim(0,1)
	ax.set_ylim(0,1)
	ax.set_title("t={:.2f}".format(t*dt))
	ax.grid()
	ax.plot(x,u[t,:])
	#if t == 100:
	#	fig.savefig("fig.png")
ani = FuncAnimation(fig, update, Nt+1, interval=100)
#ani.save("ani.mp4")
plt.show()

# 3dplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)
ax.set_title("dt={:.6f}, dx={:.2f}".format(dt,dx))
ax.grid()
x,t = np.meshgrid(x,t)
ax.plot_surface(t,x,u)
#fig.savefig("fig.png")
plt.show()