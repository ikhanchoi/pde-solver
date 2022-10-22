
from unidecode import unidecode
from nltk.metrics import edit_distance
from nltk.probability import MLEProbDist, LidstoneProbDist
import numpy as np
import re

vowels = set(['a','e','i','o','u','w','y'])

def phonemize(token):
	return unidecode(token)



def standardize(a, b, dialect_sentence, standard_sentence):
	# phon_Dtoken이 input으로 들어오는 함수라고 생각하면 된다
	# 커서와 길이는 탐색을 빨리 끝내려고 받는 인자
	# dialect_sentence와 standard_sentence의 유사도를 이용해서 Stoken에 해당하는 것을 standard_sentence 안에서 찾을 것이다

	# dialect_sentence[a:b] 그라믄    ab = geurameun
	# standard_sentence[c:d] 그러면    cd = geureomyeon

	ab = phonemize(dialect_sentence[a:b])
	candi = []
	for c in range( max(a-5,0), min(a+30,len(standard_sentence)) ):
		fch = phonemize(standard_sentence[c])[0]
		if len(ab) == 0:
			print(dialect_sentence,a,b)
		if fch is not ab[0] and (fch not in vowels or ab[0] not in vowels):
			continue

		cd = "" #initial
		d_list = []
		dist_list = []

		for d in range( c+1, min(c+20,len(standard_sentence)+1) ):
			if count_whitespace(standard_sentence[c:d])>=3: # exclude 3 white space std token
				break
			cd += phonemize(standard_sentence[d-1])
			
			dist = fch_dist_ratio(ab, cd)
			if dist <= 0.7:
				d_list.append(d)
				dist_list.append(dist)

		# at most one candi for each c
		if d_list:
			i = np.argmin(np.array(dist_list))
			candi.append((c, d_list[i], dist_list[i]))
				
	if not candi:
	#		if count_whitespace(dialect_sentence[a:b])<1 :
	#			return dialect_sentence[a:b]
	#		else:
		return "failed"
	cand0,cand1,cand2 = zip(*candi)	
	n = np.argmin(np.array(cand2))

	return standard_sentence[cand0[n]:cand1[n]]


def dist_ratio(str1, str2):
	return (0.1 + edit_distance(str1,str2))/(len(str2))


def fch_dist_ratio(str1, str2):
	if str1[0] == str2[0]:
		return dist_ratio(str1,str2)
	else:
		fch_dist = 0
		if str1[0] in vowels and str2[0] in vowels:
			fch_dist = 1
		else:
			fch_dist = 0.4*len(str2)
		return (0.1 + fch_dist + edit_distance(str1,str2))/(len(str2))

def phonological_dist(char1, char2):
	dist = 0 ##################################
	return dist


def count_whitespace(standard_token):
	count = 0
	for char in standard_token:
		if char == ' ':
			count+=1
	return count



def nosmoothing():
	return lambda fd, bins: MLEProbDist(fd, bins)


def lidstone(gamma):
	return lambda fd, bins: LidstoneProbDist(fd, gamma, bins)


def edits1(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))





from datetime import datetime
import dill

def save_model(model, name=None, time=None):
	if name == None:
		name = model._name + datetime.today().strftime("%Y%m%d%H%M")
	if time != None:
		name = name + '(' + str(round(time,2)) + 's)'
	with open('model/'+name+'.pkl','wb') as f:
		dill.dump(model, f)
	print('Saved as "'+name+'.pkl".')

def load_model(name):
	with open('model/'+name+'.pkl','rb') as f:
		return dill.load(f)

def load_parallel_corpus(name):
	standard_sentences = []
	dialect_sentences = []
	n = 0
	with open('data/'+name+'.tsv', 'r', encoding='utf-8-sig') as c:
		next(c)
		for i, line in enumerate(c):
			line = line.split('\t')
			dialect_sentences.append(line[0])
			standard_sentences.append(line[1].strip('\n'))
	return zip(dialect_sentences, standard_sentences)
