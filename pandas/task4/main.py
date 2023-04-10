import numpy as np
import pandas as pd

winners=pd.read_csv('https://github.com/bykov-alexei/data-science-course/blob/master/Python3/moscow%20schools%20-%20winners.csv?raw=true')

# print(winners[(winners.Stage == '4') & (winners.Status == 'победитель') & (winners.Subject == 'Математика' )].shape[0]) 
# print(winners[(winners.Stage == '3') & (winners.Status == 'призёр') & (winners.Subject == 'Информатика' ) & (winners.Class == '9')].shape[0]) 
# print(winners[winners.Status == 'победитель'].groupby('ShortName').ShortName.count().idxmax())