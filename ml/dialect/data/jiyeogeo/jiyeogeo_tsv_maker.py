# generates parallel corpus
import re

f_all = open("jiyeogeo_parallel_corpus(all).tsv", 'w', encoding='utf-8')
f_all.write('dialect\tstandard\n')

regions = ['chungbuk', 'gangwon', 'gyeongbuk', 'gyeonggi', 'gyeongnam', 'jeonnam']
for region in regions:
	with open(region+".txt", encoding='utf-8-sig') as f:
		bigstr = f.read()

	bigstr = bigstr[:re.search('어휘',bigstr).start()]
	outputs = []
	while re.search('[#@]', bigstr) and re.search('{', bigstr) and re.search('}', bigstr):
		d_sent = bigstr[re.search('[#@]', bigstr).start()+1:re.search('{', bigstr).start()]
		s_sent = bigstr[re.search('{', bigstr).start()+1:re.search('}', bigstr).start()]
		bigstr = bigstr[re.search('}', bigstr).start()+1:]

		d_sent = d_sent.replace(d_sent[d_sent.find("("):d_sent.find(")")+1], '')
		s_sent = s_sent.replace(s_sent[s_sent.find("("):s_sent.find(")")+1], '')
		d_sent = re.sub('[^가-힣 ]', '', d_sent)
		s_sent = re.sub('[^가-힣 ]', '', s_sent)
		d_sent = re.sub(' [음어아예] ', '', d_sent)
		s_sent = re.sub(' [음어아예] ', '', s_sent)
		d_sent = d_sent.strip()
		s_sent = s_sent.strip()

		if len(d_sent) > 1:
			outputs.append(d_sent+'\t'+s_sent+'\n')

	with open("jiyeogeo_parallel_corpus("+region+").tsv", 'w', encoding='utf-8') as f:
		f.write('dialect\tstandard\n')
		for line in outputs:
			f.write(line)
			f_all.write(line)

f_all.close()