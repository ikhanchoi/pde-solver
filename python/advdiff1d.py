import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Nt = 1000
Nx = 100
t = np.linspace(0,2,Nt+1)
x = np.linspace(-1,1,Nx+1)
u = np.empty((Nt+1,Nx+1))
dt = t[1] - t[0]
dx = x[1] - x[0]

def Advdiff_solve(u):
	# u_t + eta u_x = eps u_xx
	# FTCS: the stability condition is satisfied
	eta = 1
	eps = 0.1
	for n in range(Nt):
		for i in range(1,Nx):
			u[n+1,i] = u[n,i] - eta*(dt/2/dx)*(u[n,i+1]-u[n,i-1]) + eps*(dt/dx**2)*(u[n,i+1]-2*u[n,i]+u[n,i-1])
	return u

# initialization
for i in range(Nx+1):
	u[0,i] = np.exp(-10*x[i]**2)
u[:,0] = 1
u[:,-1] = 1

# solve
u = Advdiff_solve(u)

fig,ax = plt.subplots()
def update(t):
	ax.cla()
	ax.set_xlim(-1,1)
	ax.set_ylim(0,1)
	ax.set_title("t={:.2f}".format(t*dt))
	ax.grid()
	ax.plot(x,u[t,:])
	#if t == 750:
	#	fig.savefig("fig.png")

ani = FuncAnimation(fig, update, Nt+1, interval=10)
#ani.save("ani.mp4")
plt.show()