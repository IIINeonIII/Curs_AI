# Task 1
import pandas as pd
import numpy as np


dict = { 'name' : [' Bill', ' Bob', 'Alice',' Beatrice','Emil', 'Patrick' ],
         'grade': [ 40, 35, 100, 65, 90, 50] }

df = pd.DataFrame(dict)

df2 = df['grade'].mean()
print(df2)
df3 = df['grade'].median()
print(df3)

print(df.iloc[3])

threshold = df['grade'].mean()

df4 = df[df['grade'] > threshold].sort_values(by='grade', ascending=False).reset_index(drop=True)
print(df4)

# Task 3

s1 = pd.Series(np.random.randint(0, 2,100))
s2 = pd.Series(np.random.randint(0, 2,100))

matching_indexes = s1[s1 == s2].index
print(matching_indexes.to_list())

















