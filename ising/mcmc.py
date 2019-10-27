import numpy as np

import sys
sys.path.insert(0, '..')
import visualize


L = 100
n_step = 10000

def nbr(x,y):
	return [((x+1)%L, y), ((x-1)%L, y), (x, (y+1)%L), (x, (y-1)%L)]



t = np.arange(2, 3, 0.1)
T = t.size
beta = 1.0 / t
M = np.zeros(T)

image = []
for n in range(T):
	S = np.random.choice([1,-1], size = (L, L))
	for step in range(n_step):
		r = tuple(np.random.randint(L, size = 2))
		pocket, cluster = [r], [r]

		while pocket:
			for p in pocket:
				for q in nbr(*p):
					if S[q] == S[p] and q not in cluster:
						if np.random.uniform(0.0,1.0) < 1 - np.exp(-2*beta[n]):
							pocket.append(q)
							cluster.append(q)
			pocket.remove(p)
		for q in cluster:
			S[q] *= -1
		print("t=",t[n],",   ",step,"/",n_step)

	M[n] = sum(sum(S))
	image.append(S)

print(image[1])
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