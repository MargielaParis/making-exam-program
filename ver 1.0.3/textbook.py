uri = "/./Users/jinsh/Desktop/AutoTextbook/"

with open(uri + 'Korean.txt', encoding='UTF8') as kor:
	klines = kor.readlines()
with open(uri + 'English.txt', encoding='UTF8') as eng:
	elines = eng.readlines()

with open(uri + 'Results/EnKr.txt', 'w', encoding='UTF8') as enkr:
	for i in range(len(klines)):
		splk = klines[i].split('. ')
		sple = elines[i].split('. ')
		for j in range(len(splk)):
			if((splk[j] == '\n'  and sple[j] == '\n') or (splk[j] == '' and sple[j] == '')):
				continue
			enkr.write(sple[j]+'.\n')
			enkr.write(splk[j]+'.\n')
with open(uri + 'Results/forTest.txt', 'w', encoding='UTF8') as test:
	for i in range(len(klines)):
		splk = klines[i].split('. ')
		for j in range(len(splk)):
			if(splk[j] == '\n' or splk[j] == ''):
				continue
			test.write('\n____________________________________________________________________________________________\n')
			if (len(splk[j]) >= 54):
				test.write('____________________________________________________________________________________________\n')
			test.write(splk[j] + '.\n')
with open(uri + 'Results/forTest2.txt', 'w', encoding='UTF8') as test:
	for i in range(len(elines)):
		sple = elines[i].split('. ')
		for j in range(len(sple)):
			if(sple[j] == '\n' or sple[j] == ''):
				continue
			test.write(sple[j] + '.\n\n')
			test.write('____________________________________________________________________________________________\n')
			if (len(sple[j]) >= 103):
				test.write('____________________________________________________________________________________________\n')
