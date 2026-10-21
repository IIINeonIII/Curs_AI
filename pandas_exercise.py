import pandas as pd

# dataframes are data structures specific to pandas, that consists of a table with columns

df = pd.read_excel('file.xlsx')
print(df.head())

print('---')

# a dataseries is an unidimensional column, the equivalent to a unidim vector / array from numpy, in a way

s = pd.Series(range(5,0,-2))
print(s)
# int64 data type is used only by pandas, by default

s2 = pd.Series([1,2.5,5])
print(s2)

series_index = pd.Series([1,2,3], index=['a','b','c'])
print(series_index)


dict = {'Name':['Vergil', 'Max', 'Giani'],'Power':[2, 3, 4],'Swag':[3, 4, 5]}  # keys become headers, and the values, data

df_list = pd.DataFrame((dict), index=['(fighter 1)', '(fighter 2)', '(fighter 3)'])
print(df_list)






