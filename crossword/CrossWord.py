# для кроссвордов

print('input word: if you know letter input it, if you dont know letter input _')
word = list(input())
n = len(word)
lst_pos = []
for k in range(n):
	if word[k] != '_':
		lst_pos.append(k)
#print('lst_pos = ', lst_pos)

print('--------------------------------')
print('RESULT')
print('--------------------------------')

with open('EnglishWordsList.txt') as file_:
	list_ = file_.readlines()
	for i in list_:
		if len(i.strip()) == n:
			#print('tut', i)
			mas_ = list(i.strip())
			#print(mas_)
			for k in lst_pos:
				if mas_[k] != word[k]:
					#print('break')
					break
			else:
				print(i)
			
