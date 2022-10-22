import DMT
from DMT.model.util import *

# 미완성입니다 ㅠㅠㅠ


CHOSEONG = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'] # 19
JUNGSEONG = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'] # 21
JONGSEONG = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'] # 28

all_phonemes = []
for cho in CHOSEONG:
	if cho != 'ㅇ':
		all_phonemes.append((cho,1))
for jung in JUNGSEONG:
	all_phonemes.append((jung,2))
for jong in JONGSEONG:
	if jong != '':
		all_phonemes.append((jong,3))
n_phonemes = len(all_phonemes)



import re
def decompose(text):
	sylbs = list(text)
	result = []
	for sylb in sylbs:
		if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*',sylb) is not None:
			char_code = ord(sylb) - 44032
			char1 = int(char_code/588)
			result.append(CHOSEONG[char1])

			char2 = int((char_code - (588*char1))/28)
			result.append(JUNGSEONG[char2])

			char3 = int((char_code - (588*char1) - (28*char2)))
			result.append(JONGSEONG[char3])
		else:
			result.append(sylb)
	return result



from g2pk import G2p
g2p = G2p()
def g2p_phonemize(text):
	normalized_text = g2p(text, descriptive=True, group_vowels=True)
	decomposed_list = decompose(normalized_text)

	trimmed_list = []
	for phoneme in decomposed_list:
		if phoneme in CHOSEONG + JUNGSEONG + JONGSEONG:
			trimmed_list.append(phoneme)

	tagged_list = []
	for i, phoneme in enumerate(trimmed_list):
		if i % 3 == 0 and phoneme != 'ㅇ':
			tagged_list.append((phoneme,1)) # CHO
		if i % 3 == 1:
			tagged_list.append((phoneme,2)) # JUNG
		if i % 3 == 2 and phoneme != '':
			tagged_list.append((phoneme,3)) # JONG
			
	return tagged_list


import torch
def tensorize(line):
	phon_list = g2p_phonemize(line)
	tensor = torch.zeros(len(phon_list), 1, n_phonemes)
	for li, phoneme in enumerate(phon_list):
		tensor[li][0][all_phonemes.index(phoneme)] = 1
	return tensor # We will embed this one-hot coded tensor


import torch.nn as nn
from torch import optim
import torch.nn.functional as F


