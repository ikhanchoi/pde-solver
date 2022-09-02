import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

Nt = 1000
Nx = 100
Ny = 100
N = Nx*Ny

T = 1
beta = 1/T


def Metropolis_flip(s):
	i,j = np.random.randint(Nx), np.random.randint(Ny)
	dH = 2*s[i,j]*(s[(i+1)%Nx,j]+s[i,(j+1)%Ny]+s[(i-1)%Nx,j]+s[i,(j-1)%Ny])

	if dH < 0. or np.random.rand() < np.exp(-beta*dH):
		s[i,j] *= -1
	return s

def Glauber_flip(s, beta):
	i,j = np.random.randint(Nx), np.random.randint(Ny)
	dH = 2*s[i,j]*(s[(i+1)%Nx,j]+s[i,(j+1)%Ny]+s[(i-1)%Nx,j]+s[i,(j-1)%Ny])

	if np.random.rand() < 1/(1+np.exp(beta*dH)):
		s[i,j] *= -1
	return s

def Wolff_flip(s, beta):
	i,j = np.random.randint(Nx), np.random.randint(Ny)
	Pocket, Cluster = [(i,j)], [(i,j)]

	while Pocket != []:
		i,j = Pocket[np.random.randint(len(Pocket))]
		for nb in [((i+1)%Nx,j), (i,(j+1)%Ny), ((i-1)%Nx,j), (i,(j-1)%Ny)]:
			if s[nb] == s[i,j] and nb not in Cluster and np.random.rand() < 1-np.exp(-beta):
				Pocket.append(nb)
				Cluster.append(nb)
		Pocket.remove((i,j))

	for i,j in Cluster:
		s[i,j] *= -1
	return s


def magnetization(s):
	M = 0
	for i in range(Nx):
		for j in range(Ny):
			M += s[i,j]
	return M/N
def energy(s):
	E = 0
	for i in range(Nx):
		for j in range(Ny):
			E += -s[i,j]*(s[(i+1)%Nx,j]+s[i,(j+1)%Ny])
	return E/N



s = np.random.choice([1,-1], size=(Nx,Ny))
states = []
for _ in range(Nt):
	for _ in range(100):
		s = Metropolis_flip(s)
	states.append(np.copy(s))

fig,ax = plt.subplots()
def update(frame):
	ax.cla()
	ax.imshow(states[frame])
	ax.set_title("t={:.2f}  M={:.2f}  E={:.2f}".format(frame,magnetization(states[frame]),energy(states[frame])))

ani = FuncAnimation(fig, update, Nt, interval=50)
plt.show()