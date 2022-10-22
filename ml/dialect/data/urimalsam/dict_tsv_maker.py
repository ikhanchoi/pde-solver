# generates dictionary

corpus = []
with open("urimalsam1.txt", encoding='utf-8-sig') as f1:
	for line in f1:
		corpus.append(line.strip('\n'))
with open("urimalsam2.txt", encoding='utf-8-sig') as f2:
	for line in f2:
		corpus.append(line.strip('\n'))

outputs = []
for i in range(len(corpus)):
	if corpus[i].startswith('#00'): # 표제어
		outputs.append(corpus[i+1][:-5].replace('-',''))
		outputs.append('\t')
	if corpus[i].startswith('#02'): # 품사
		outputs.append(corpus[i+1])
		outputs.append('\t')
	if corpus[i].startswith('#50'): # 뜻풀이
		outputs.append(corpus[i+1][corpus[i+1].find('‘')+1:corpus[i+1].find('’')])
		outputs.append('\n')

with open("urimalsam_dict.tsv",'w', encoding='utf-8') as f:
	f.write('dialect\tpos\tstandard\n')
	for line in outputs:
		f.write(line)