import pandas as pd

dict = { 'name' : ['Bill', 'Bob', 'Alice', 'Beatrice', 'Emil', 'Patrick'],
         'grade': [ 40, 35, 99, 65, 90, 50] }

df_students = pd.DataFrame(dict)
print(df_students)


df_students['percentage'] = (df_students['grade']/df_students['grade'].max()*100)
print(df_students)

df_students['percentage'] = (df_students['percentage'].round())
print(df_students)

df_students['anonymised_name'] = df_students['name'].apply(lambda x : x[0] + '...' + x[-1])
print(df_students)

# 12

df_sorted = df_students.sort_values(by=['grade', 'name'], ascending=[False, True])


# student_data1 = pd.Dataframe
















