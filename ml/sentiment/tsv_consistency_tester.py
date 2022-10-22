with open("ratings_test.tsv", encoding='utf-8-sig') as f:
	for line in f:
		a = line.split('\t')
		if a[1] == '':
			print(a[0])
		if len(a) != 3:
			print(a[0])