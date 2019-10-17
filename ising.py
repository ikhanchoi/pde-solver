import numpy as np


L = 4
nbr = {i : ((i // L) * L + (i+1) % L, (i+L) % L**2,
			(i // L) * L + (i-1) % L, (i-L) % L**2)
			for i in range(L**2) }

# enumerate_ising.py

def gray_flip(tau, L2):
	k = tau[0]
	if k > L2:
		return tau, k
	tau[k-1] = tau[k]
	tau[k] = k + 1
	if k != 1: tau[0] = 1

	return tau, k

S = [-1] * L**2 # spin configurations = microstate
E = -2 * L**2 # total energy
N = {}
N[E] = 1 # number of the microstates of energy E

tau = np.arange(L**2+1) # permutations

for i in range(1, 2**L**2):
	tau, k = gray_flip(tau, L**2)
	h = sum(S[n] for n in nbr[k])
	E += 2 * h * S[k]
	S[k] *= -1

	if E in N:
		N[E] += 1
	else: N[E] = 1


# thermo_ising_py
t = np.arange(.5, 10.5, 0.5)
for T in t:
	Z = 0.
	E_av = 0.
	M_av = 0.
	E2_av =0.
	for E in N.keys():
		weight = np.exp(-E/T) * N[E]
		Z += weight
		E_av += weight * E
		E2_av += weight * E**2
	E_av /= Z
	E2_av /= Z

	cv = (E2_av - E_av**2) / L**2 / T**2 # specific heat
	# print(T, E_av/float(L**2), cv)

	# cv의 최고점이 2/log(1+sqrt(2))에서 나타남




#이거 direct sampling이 너무 후져서 MCMC (Metropolis-Hastings)쓸 거야
# markov_ising.py
# local Markov chain이라는데 뭘까

import random
nsteps = int(1e+6)
T = 2.5 # 2와 3 사이에서 phase transition between ferromagnet and paramagnet
beta = 1./T
S = [random.choice([1,-1]) for k in range(L**2)]
for step in range(nsteps):
	k = random.randint(0, L**2-1)
	delta_E = 2. * S[k] * sum(S[nn] for nn in nbr[k])
	if random.uniform(0., 1.) < np.exp(-beta * delta_E):
		S[k] *= -1
M = sum(S) # magnetization
print(np.abs(M)/L**2) # absolute magnetization per site

# critical  temperature 근처에서의 spin flipping은 시간을 잡아먹는다
# large-scale correlation of the local MC algorithm close to 
# critical slowing down(it is also known in experiment)

# cluster algorithm이 critical temperature 근처에서의 slowing down을 해결



# Wolff cluster algorithm