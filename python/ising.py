import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




def Metropolis_flip(s, beta):
	X,Y = s.shape
	x,y = np.random.randint(X), np.random.randint(Y)
	dH = 2*s[x,y]*(s[(x+1)%X,y]+s[x,(y+1)%Y]+s[(x-1)%X,y]+s[x,(y-1)%Y])

	if dH < 0. or np.random.rand() < np.exp(-beta*dH):
		s[x,y] *= -1
	return s

def Glauber_flip(s, beta):
	X,Y = s.shape
	x,y = np.random.randint(X), np.random.randint(Y)
	dH = 2*s[x,y]*(s[(x+1)%X,y]+s[x,(y+1)%Y]+s[(x-1)%X,y]+s[x,(y-1)%Y])

	if np.random.rand() < 1/(1+np.exp(beta*dH)):
		s[x,y] *= -1
	return s

def Wolff_flip(s, beta):
	X,Y = s.shape
	x,y = np.random.randint(X), np.random.randint(Y)
	Pocket, Cluster = [(x,y)], [(x,y)]

	while Pocket != []:
		x,y = Pocket[np.random.randint(len(Pocket))]
		for nb in [((x+1)%X,y), (x,(y+1)%Y), ((x-1)%X,y), (x,(y-1)%Y)]:
			if s[nb] == s[x,y] and nb not in Cluster and np.random.rand() < 1-np.exp(-beta):
				Pocket.append(nb)
				Cluster.append(nb)
		Pocket.remove((x,y))

	for x,y in Cluster:
		s[x,y] *= -1
	return s





def magnetization(s):
	X,Y = s.shape
	M = 0
	for x in range(X):
		for y in range(Y):
			M += s[x,y]
	return M/N
def energy(s):
	X,Y = s.shape
	E = 0
	for x in range(X):
		for y in range(Y):
			E += -s[x,y]*(s[(x+1)%X,y]+s[x,(y+1)%Y])
	return E/N




X = 100
Y = 100
N = X*Y

temperature = 1
beta = 1/temperature

s = np.random.choice([1,-1], size=(X,Y))

# filming
frameCount = 100
states = []
for _ in range(frameCount):
	for _ in range(1):
		s = Metropolis_flip(s,beta)
	states.append(np.copy(s))

fig = plt.figure()
im = plt.imshow(states[0])
time = plt.text(-30,0,"")
magn = plt.text(-30,10,"")
ener = plt.text(-30,20,"")
def update(frame):
	im.set_array(states[frame])
	time.set_text("t="+str(frame))
	magn.set_text("M="+str(magnetization(states[frame])))
	ener.set_text("E="+str(energy(states[frame])))

ani = FuncAnimation(fig, update, frameCount, interval=50)
plt.show()