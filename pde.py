import numpy as np
import matplotlib.pyplot as plt
from math import pi

def solver(u0, w, dt, T):
	"""
	Solve
		u'' + w^2 u = 0  for t in (0,T],
		u(0) = u0,
		u'(0) = 0,
	by a central finite difference method with time step dt.
	"""
	dt = float(dt)
	Nt = int(round(T/dt))
	u = np.zeros(Nt+1)
	t = np.linspace(0, Nt*dt, Nt+1)

	u[0] = u0
	u[1] = u[0] - 0.5*dt**2*w**2*u[0]
	for n in range(1, Nt):
		u[n+1] = 2*u[n] - u[n-1] - dt**2*w**2*u[n]

	return u, t

def u_exact(t, I, w):
	return I*np.cos(w*t)

def visualize(u, t, I, w):
	plt.plot(t, u, 'r.')
	u_e = u_exact(t, I, w)

	plt.plot(t, u_e, 'b-')
	plt.legend(['numerical', 'exact'], loc='upper left')
	plt.xlabel('t')
	plt.ylabel('u')
	plt.title('dt=%g' % t[1] - t[0])
	plt.axis([t[0], t[-1], 1.2*u.min(), 1.2*u.max()])
	plt.savefig('figure.png')
	plt.show()

u0 = 1
w = 2*pi
dt = 0.05
num_periods = 5
P = 2*pi/w
T = P*num_periods
u, t = solver(u0, w, dt, T)
visualize(u, t, u0, w)