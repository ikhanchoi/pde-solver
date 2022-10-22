from util import *
from nltk.probability import FreqDist, ConditionalFreqDist, ConditionalProbDist

import numpy as np
import time
from itertools import product


vowels = set(['a','e','i','o','u','w','y'])
letters = 'abcdefghijklmnopqrstuvwxyz'

class PhonemicHMM(object):


	def __init__(self, trained_model=None):
		self._name = "phonemic_hmm"
		self._states = trained_model._states if trained_model else ['F']
		self._symbols = trained_model._symbols if trained_model else []
		self._starting = trained_model._starting if trained_model else FreqDist()
		self._transitions = trained_model._transitions if trained_model else ConditionalFreqDist()
		self._outputs = trained_model._outputs if trained_model else ConditionalFreqDist()

	def train(self, corpus):
		# HMM algorithm
		# symbol: phonemized dialect token
		# state: standard token

		parallel_corpus = load_parallel_corpus(corpus)

		# member variables: domains
		known_symbols = set(self._symbols)
		known_states = set(self._states)

		# for each pair of lines
		for (dialect_sentence, standard_sentence) in parallel_corpus:
			# for each dialect token (double for loop)
			for a in range(len(dialect_sentence)):
				last = None

				#-----------------------\\
				# Rule 1.
				if a != 0 and dialect_sentence[a-1] != ' ':
					continue
				#-----------------------//

				for b in range(a+1,len(dialect_sentence)+1):
					# get standard token
					dialect_token = dialect_sentence[a:b]
					symb = phonemize(dialect_token)
					stat = standardize(a, b, dialect_sentence, standard_sentence)
					num_whitespace = count_whitespace(stat)
					# print(dialect_token+' -> '+stat)		# FOR DEBUGGING !!!
					
					#-----------------------\\
					# Rule 2.
					if stat == 'failed':
						break
					if len(stat)-num_whitespace > 6:
						break # in order to reduce # of states
					#-----------------------//

					# add the nodes of HMM model
					if symb not in known_symbols:
						self._symbols.append(symb)
						known_symbols.add(symb)
					if stat not in known_states:
						self._states.append(stat)
						known_states.add(stat)

					#-----------------------\\
					# Rule 3.
					if dialect_token.endswith(' ') or b == len(dialect_sentence):
						self._transitions[last]['F'] += 1
						self._transitions[stat]['F'] += 1
					#-----------------------//

					#-----------------------\\
					# Rule 4.
					self._outputs[stat][symb] += 1

					if last is None:
						self._starting[stat] += 1
					else:
						self._transitions[last][stat] += 2
					#-----------------------//

					#-----------------------\\
					# Rule 5.
					self._transitions[stat]['F'] += num_whitespace
					if num_whitespace>=3:
						break
					#-----------------------//

					#-----------------------\\
					# Rule 6.
					if phonemize(stat) not in known_symbols:
						self._symbols.append(phonemize(stat))
						known_symbols.add(phonemize(stat))
					if len(stat) - num_whitespace > 1:
						self._outputs[stat][phonemize(stat)] += len(stat)*len(stat)
					#-----------------------//
										
					# update last_Stoken
					last = stat

		self._transitions['F']['F'] = 1
		return self


	def translate(self, Dtext):

		if len(Dtext) == 1:
			return Dtext

		path_time = time.time()
		symb_path = self.get_symbol_path(Dtext)
		print("\n┌-------- Symbol_path : ", symb_path)
		print("Finding Symbol path : ", round(time.time() - path_time,2), ' s')

		path_time = time.time()
		stat_path = self.get_state_path(symb_path)
		print("Finding State path : ", round(time.time() - path_time,2), ' s')
		print("\n└-------- Hidden_state_path: ", stat_path, "\n")

		# recurrence procedure base case
		if len(stat_path) == len(Dtext) + 1:
			return stat_path[len(stat_path)-2]

		F_idx = stat_path.index('F')
		trunc_text = Dtext[F_idx:].lstrip(' ')

		print("< 변환 완료: " + stat_path[F_idx-1] + " >\n")
		print("< 변환 대기: " + trunc_text + " >")

		return stat_path[F_idx-1] + self.translate(trunc_text)


	def get_symbol_path(self, Dtext):
		symb_path = []
		for l in range(1,min(10,len(Dtext)+1)):
			if count_whitespace(Dtext[:l-1]) >= 2:
				break
			symb_path.append(self.trfm_dict(Dtext[:l]).lstrip(' '))
		return symb_path

	def trfm_dict(self, dialect_sentence):
		symbols = set(self._symbols)
		dialect_sentence = dialect_sentence.lstrip(' ')
		if len(dialect_sentence) == 0:
			return ""
		if phonemize(dialect_sentence) in symbols:
			return phonemize(dialect_sentence)
		# inp : geuramo jjom
		# est : geurameun jom

		inps = []
		ests = []
		bs = []
		for b in range(1,len(dialect_sentence)+1): #####  여기 최적화 spell.py의 아이디어 사용하자.

			inp = phonemize(dialect_sentence[:b])

			'''
			for est in self._symbols:
				est = est.rstrip('\n')
				if est[0] == inp[0] and abs(len(inp)-len(est)) <= 0.3*len(inp) + 4:
					inps.append(inp)
					ests.append(est)
					bs.append(b)
			'''
			edits = edits2(inp)
			for edit in edits:
				if edit in symbols:
					inps.append(inp)
					ests.append(edit)
					bs.append(b)
			

		# the following occurs when there is no exact 
		i = min(range(len(ests)), key=lambda i: dist_ratio(inps[i],ests[i]))
		return ests[i] + self.trfm_dict(dialect_sentence[bs[i]:])
			# the whitespace at left will be stipped when the trfm_dict is called.



	def get_state_path(self, symb_path):
		'''
		Finds the best state path using the Viterbi algorithm.
		'''
		T = len(symb_path)
		N = len(self._states)
		V = np.ones((T, N), np.float16)
		B = {}


		# thinning the state space
		thin_time = time.time()
		states = set()
		for sj in set(self._states):
			if any(self._outputs[sj][symb_path[t]] != 0 for t in range(T)):
				for l in range(1,len(sj)+1):
					states.add(sj[:l])
		N = len(states)
		print("N = ", N, '\n')
		print(states)
		print("Thinning states : ", round(time.time()-thin_time,2), 's')

		# probabilitize the frequency distributions

		freqdist = FreqDist(samples=states)
		condfreqdist = ConditionalFreqDist(cond_samples=set(product(states,states)))
		for sj in states:
			freqdist[sj] += 10000
			freqdist['F'] += 10000
			condfreqdist[sj]['F'] += 10000
			for si in states:
				if len(si) < len(sj):
					condfreqdist[si][sj] += 10000

		estimator = nosmoothing() ###
		priors = estimator(self._starting & freqdist, N)
		transitions = ConditionalProbDist(self._transitions.__and__(condfreqdist), nosmoothing(), N)
		outputs = ConditionalProbDist(self._outputs, lidstone(0.05), len(self._symbols))


		# find the starting log probabilities for each state
		symbol = symb_path[0]
		for i, si in enumerate(states):
			V_init = priors.logprob(si) + outputs[si].logprob(symbol)
			if V_init > -1e+100:
				V[0, i] = V_init
			B[0, si] = None
			# automatically starting prob of F vanishes due to outputs prob.

		# find the maximum log probabilities for reaching each state at time t
		for t in range(1, T):
			symbol = symb_path[t]
			print(">>> Some states similar to '", symbol, "' are estimated. ( T =",t,")\n")

			# sj != 'F'
			for j, sj in enumerate(states):

				# CASE (1)
				if outputs[sj].prob(symbol) == 0:
					B[t,sj] = 'nowhere'
					continue

				print(" The state '", sj, "' is finding proper back pointer.")
				
				best = (1, 'nowhere') # initialization for no continue at (2),(3)
				for i, si in enumerate(states):
					
					# CASE (2) & CASE (3)
					if V[t-1, i] == 1:
						continue
					if self._transitions[si][sj] == 0:
						continue

					va = V[t-1, i] + transitions[si].logprob(sj)
					if va > best[0] or best[0] == 1: # update best if exists
						best = (va, si)
						print(" ", si, "->", sj, ": va = ", va)

				V[t, j] = best[0]
				B[t,sj] = best[1]
				if best[0] <= 0: # iff V[t,j] != 1
					V[t, j] += outputs[sj].logprob(symbol)

				print(" The transition ", B[t,sj], "->", sj, " is most probable with V = ", V[t,j], '\n')

			# if all states except 'F' are killed by 'nowhere',
			# then set `Break = True` and cut the sentence.
			Break = True
			for j, sj in enumerate(states):
				if B[t,sj] != 'nowhere': 
					Break = False
					break
			if Break == True:
				T = t
				print(">>> Double loop procedure halted at time T =", T, '\n')
				break


		if T == len(symb_path):
			print(">>> Double loop procedure ended at time T =", T, '\n')


		# find the highest probability final state
		best = (-1e+100, "best time", "best state")
		for t in range(T-1, 0, -1):
			for i, si in enumerate(states):
				if V[t, i] == 1:
					continue
				val = (V[t, i] + transitions[si].logprob('F'))/(t+1)
				print(" #", t, si, "-> F: val =", val)
				if 0 > val > best[0]:
					best = (val, t, si)

		if best[2] == "best state":
			return ['???','F']

		# traverse the back-pointers B to find the state sequence
		current = best[2]
		sequence = [current]
		for t in range(best[1], 0, -1):
			last = B[t, current]
			sequence.append(last)
			current = last

		sequence.reverse()

		if sequence[-1] != 'F':
			sequence.append('F')

		return sequence






