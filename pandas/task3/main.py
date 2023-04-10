import numpy as np
import pandas as pd

# wines = pd.read_csv('wines.csv')
wines=pd.read_csv('https://github.com/bykov-alexei/data-science-course/blob/master/Pandas/wines.csv?raw=true')
# wines = wines.head(1000)

# print(wines.winery.loc[wines.price.idxmax()])

# country = wines.country
# print(country.loc[country == 'Israel'].count())

# print(wines.loc[wines.country == 'Italy'].points.mean())

# print(wines.loc[wines.description.notna()].country.value_counts())

# df = wines.loc[wines.description.notna()].country.value_counts()
# print(df[df == 109].index)

# print(wines.loc[(wines.description.notna())&(wines.country == 'France')]['province'].value_counts().idxmin())

# wines['adress'] = wines.country + ', ' + wines.province
# print(wines[['adress', 'points']].groupby(by='adress').mean().idxmax())
# df.groupby(['country', "province"]).points.mean().idxmax() # более короткое решение

# нерешенная !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# set2 = set(wines[wines.points >= 95].country.unique())
# set1 = set(wines.country.unique())
# print(len(set1.difference(set2)))

# print(wines.groupby('taster_name').points.mean().idxmin())

# print(wines[wines.taster_name == 'Roger Voss'].groupby('country').points.mean().sort_values(ascending=False).head(3))
