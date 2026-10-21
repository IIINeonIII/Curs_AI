import pandas as pd

data = {
    'nume':['John','Chris','Adele','Mark'],
    'functie':['Analist', 'Manager','Programator','Tester'],
    'salariu':[5000, 7000, 6000, 4500],
    'oras':['Bucuresti','Cluj','Iasi','Brasov']
}

print(data)

# we put the data from dict into a data frame and then put the df in an excel file we create

df = pd.DataFrame(data)
print(df)


df.to_excel('test.xlsx', index=False, engine='openpyxl')


df1 = pd.read_excel('test.xlsx')
print(df1)

# this function can have various arguments that allow us to filter the data

df2 = pd.read_excel('test.xlsx', usecols=['nume','functie'])
print(df2)

df3 = pd.read_excel('test.xlsx', skiprows=[1,2,3])
print(df3)

df4 = pd.read_excel('test.xlsx', header=None, names=['Fraier','Timp', 'Numere', 'Geo'])
print(df4)





