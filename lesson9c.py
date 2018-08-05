import pandas as pd
import numpy as np

table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
z = df.groupby(['class']).mean()
a = df.groupby(['class']).sum()
print (pd.concat([z,a],axis=1,join='outer'))

print('')

print(df.corr())

# print(something) # total score
# print(something) # mean score
# print(something) # correlation coefficient