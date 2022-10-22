# generates parallel corpus
import re
corpus = []
with open("urimalsam1.txt", encoding='utf-8-sig') as f1:
	for line in f1:
		corpus.append(line.strip('\n'))
with open("urimalsam2.txt", encoding='utf-8-sig') as f2:
	for line in f2:
		corpus.append(line.strip('\n'))

outputs = []
for i in range(len(corpus)):
	if corpus[i].startswith('#58'): # 용례
		a = iter(list(range(1,100))) # 100 == 적당히 큰 수
		for j in a:
			d_sent = corpus[i+j]
			s_sent = corpus[i+j+1]
			if s_sent.startswith('#'):
				break
			if s_sent.startswith('번역 ') and (not d_sent.endswith("(제주)")):
				d_sent = d_sent.replace(d_sent[d_sent.find("("):d_sent.find(")")+1], '')
				s_sent = s_sent.replace(s_sent[s_sent.find("("):s_sent.find(")")+1], '')
				d_sent = d_sent.replace(d_sent[d_sent.find("≪"):d_sent.find("≫")+1], '')
				s_sent = s_sent.replace(s_sent[s_sent.find("≪"):s_sent.find("≫")+1], '')
				d_sent = re.sub('[^가-힣 ]', '', d_sent)
				s_sent = re.sub('[^가-힣 ]', '', s_sent)
				s_sent = s_sent.lstrip('번역 ')
				outputs.append(d_sent+'\t'+s_sent+'\n')

with open("urimalsam_parallel_corpus.tsv", 'w', encoding='utf-8') as f:
	f.write('dialect\tstandard\n')
	for line in outputs:
		f.write(line)