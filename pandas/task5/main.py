import re
import pandas as pd
pattern = '[а-яА-Я]*'
def func(string):
    a = re.fullmatch(pattern, string)
    if a: return True
    return False 

n = int(input())
df = pd.DataFrame({'data' : [input() for i in range(n)]})
mask = df.apply(lambda x: func(x.data), axis=1)
print(*list(df[mask].data), sep=', ')
