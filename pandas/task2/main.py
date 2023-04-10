import pandas as pd
import numpy as np
s = pd.read_csv('titanic.csv')

# print(s['Survived'].value_counts())
# print(s['Survived'].sum())

# сколько раз встречается в имени обращение Sir
# def func(a):
#     return ('Sir.' in a)
# mask = s.apply(lambda x: func(x.loc['Name']), axis=1)
# print(s[mask])
# print(len(s[mask]))

#print(s[s.Name.str.contains('Sir. ')].Name.count())
print(s.Name)
print(s[s.Name.str.contains('Capt')].Fare)