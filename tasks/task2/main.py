# очистить текст от знаков и подсчитать количество слов
import sys
import re
from collections import Counter
text = sys.stdin.read()
text = re.sub('[,;:\-!?.]\s', ' ', text)
text = text.lower()
words = text.split()
words.sort()
#print(words)
cnt = Counter(words)
for i in cnt: print(i, ': ', cnt[i], sep='')
