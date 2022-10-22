import DMT
from DMT.model.util import *

# Functions

CHOSEONG = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
JUNGSEONG = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
JONGSEONG = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']


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

def compose(chosung, joongsung, jongsung=u''):
    """This function returns a Hangul letter by composing the specified chosung, joongsung, and jongsung.
    @param chosung
    @param joongsung
    @param jongsung the terminal Hangul letter. This is optional if you do not need a jongsung."""

    if jongsung is None: jongsung = u''

    try:
        chosung_index = CHO.index(chosung)
        joongsung_index = JOONG.index(joongsung)
        jongsung_index = JONG.index(jongsung)
    except Exception:
        raise NotHangulException('No valid Hangul character index')

    return unichr(0xAC00 + chosung_index * NUM_JOONG * NUM_JONG + joongsung_index * NUM_JONG + jongsung_index)


def phonetize(text):
	'''
	We want to tensorize `phonetize(text)`.
	
	decomposed_list = decompose(text)
	chojungjong_list = []
	for phoneme in decomposed_list:
		if phoneme in CHOSEONG + JUNGSEONG + JONGSEONG:
			chojungjong_list.append(phoneme)

	labelled_list = []
	for i, phoneme in enumerate(chojungjong_list):
		if i % 3 == 0 and phoneme != 'ㅇ':
			labelled_list.append((phoneme,1)) # CHO
		if i % 3 == 1:
			labelled_list.append((phoneme,2)) # JUNG
		if i % 3 == 2 and phoneme != '':
			labelled_list.append((phoneme,3)) # JONG

	changed_list = []
	changed_cho = None
	for i, pair in enumerate(labelled_list):
		if changed_cho:
			changed_list.append((changed_cho,1))
			changed_cho = None
			break

		changed_phoneme = pair[0]
		changed_seong = pair[1]

		if pair[1] == 2: # JUNG

			if pair[0] in ['ㅑ','ㅒ','ㅕ','ㅖ','ㅛ','ㅠ']:
				changed_list.append(('ㅣ',2))

			if pair[0] in ['ㅔ']:
				changed_phoneme = 'ㅐ'

			changed_list




		elif pair[1] == 3: # JONG
			jong = pair[0]

			if labelled_list[i+1][1] == 1:
				next_cho = labelled_list[i+1][0]
			else next_cho = 'ㅇ'

			# GGeutsori
			if jong in ['ㄲ','ㄳ']:
				changed_phoneme = 'ㄱ'
				if jong == 'ㄳ' and next_cho in ['ㅇ','ㅅ']:
					changed_cho = 'ㅆ'
			elif jong in ['ㄵ','ㄶ']:
				changed_phoneme = 'ㄴ'
				if jong == 'ㄵ' and next_cho == 'ㅇ':
					changed_cho = 'ㅈ'
				if jong == 'ㄵ' and next_cho == 'ㅈ':
					changed_cho = 'ㅉ'
				if jong == 'ㄵ' and next_cho == 'ㅎ':
					changed_cho = 'ㅊ'
			elif jong in ['ㅅ','ㅆ','ㅈ','ㅊ','ㅌ']:
				if next_cho != 'o':
					changed_phoneme = 'ㄷ'
				else:
					changed_cho = jong
					changed_phoneme = None
			elif jong in ['ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ']:
				if jong

				# 아 현타온다  https://github.com/Kyubyong/g2pK
			elif jong in [ㄱ,ㄲ,ㄳ]:
				changed_phoneme = 'ㄱ'

			elif jong == 'ㅎ':
				if next_cho == 'ㄱ':
					changed_cho = 'ㅋ'
				elif next_cho == 'ㄷ':
					changed_cho = 'ㅌ'
				elif next_cho == 'ㅈ':
					changed_cho = 'ㅊ'
				elif next_cho == 'ㅇ':
				else:
					changed_phoneme = 'ㄷ'



			# Gyeongeumhwa
			if changed_phoneme = 'ㄱ':





		if changed_phoneme != None:
			changed_list.append((changed_phoneme,changed_seong))
		changed_cho = None
	
	return changed_list.reverse()
'''

def phonemic_dist(str1,str2):
	'''
	Return log of probability that the two strings are different.
	The length multiplies the logprob (nth power).
	'''
	list1 = g2p_phonemize(str1)
	list2 = g2p_phonemize(str2)




	return 1

from konlpy.tag import Komoran
def analyze_by_match(Dsent, Ssent):
	'''
	Return


	Args:
	- Dsent: dialect sentence (dictionary cleaned)
		:type: hangul_string
	- Ssent: standard sentence
		:type: hangul_string

	Return: analyzed dialect sentence
		:type: [(hangul_token,pos), (hangul_token,pos), ...]
	'''
	
	Stoks = Komoran().pos(Ssent)

	if len(Stoks) == 1:
		return [(Dsent,Stoks[0][1])]

	return 0






def generate_morph_dict(dictionary, corpus):
	'''
	:dictionary: cleaned dictionary for direct substitution
	:corpus: parallel corpus
	'''
	subst_dict = DMT.load_parallel_corpus(dictionary)
	parallel_corpus = DMT.load_parallel_corpus(corpus)





