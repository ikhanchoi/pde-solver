import numpy as np

import sys
sys.path.insert(0, '..')
import visualize


L = 32
n_step = 1000

dx = [1,0,-1,0,0]
dy = [0,1,0,-1,0]
nbr = {(x,y) :  [ ((x+dx[i]) % L, (y+dy[i]) % L) for i in range(5) ] for
	   (x,y) in [ (p//L, p%L) for p in range(L**2) ] }



t = np.linspace(0.2, 4.0, 20)
T = t.size
beta = 1.0 / t
M = np.zeros(T)

image = []
for n in range(T):
	S = np.random.choice([1,-1], size = (L, L))
	for step in range(n_step):
		r = tuple(np.random.randint(L, size = 2))
		F_old, cluster = [r], [r]

		while F_old:
			F_new = []
			for p in F_old:
				for q in nbr[p]:
					if S[q] == S[p] and q not in cluster:
						if np.random.uniform(0,1) < 1 - np.exp(-2*beta[n]):
							F_new.append(q)
							cluster.append(q)
			F_old = F_new
		for q in cluster:
			S[q] *= -1
		if step % 10 == 0:
			print("t=%.1f" % t[n], ",   ", step, "step /", n_step)

	M[n] = sum(sum(S))
	image.append(S)

for n in range(T):
	print("Tiem", t[n], ":")
	print(image[n])

print(np.abs(M) / L**2)
visualize.Plot2d_array(np.abs(M) / L**2,t)


'''
for n in range(T):
	S = np.random.choice([1,-1], size = (L, L))
	for step in range(n_step):
		p = tuple(np.random.randint(L, size = 2))
		delta_E = 2 * S[p] * sum([S[q] for q in nbr(*p)])
		if np.random.uniform(0,1) < np.exp(-beta[n] * delta_E):
			S[p] *= -1
		if step > n_step/2:
			M[n] += sum(sum(S))
	M[n] /= (n_step/2)
	print(M[n] / L**2)

'''