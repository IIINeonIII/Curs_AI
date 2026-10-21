import pandas as pd
import matplotlib.pyplot as plt


# data = { 'Month' : ['January', 'February', 'March', 'April', 'May', 'June' ],
#          'Profit' : [10, 20, 30, 30, 50, 40] }
#
#
# df1 = pd.DataFrame(data)
#
# df1["Growth"] = df1["Profit"].pct_change()*100
#
# mean_growth = df1["Growth"].mean()
#
# month_max = df1.loc[df1["Growth"].idxmax(), "Month"]
#
# print(df1)
# print("Mean growth:", mean_growth)
# print("Best month:", month_max)
#
#
#
# plt.figure(figsize=(10,5))
# plt.bar(df1["Month"], df1["Growth"], color="skyblue", edgecolor='b')
# plt.axhline(y=mean_growth, color="k", linestyle="--", label = f"Mean Growth: {mean_growth:.2f}%")
# plt.title("Monthly Growth")
# plt.xlabel("Month")
# plt.ylabel("Growth")
# plt.legend()
# plt.grid(axis='y', linestyle='--', alpha=0.5)
# plt.show()



# 2

data2 = {"Day" : ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
         "Temperature" : [10, 13, 7, 8, 12, 15]}

df2 = pd.DataFrame(data2)

df2["Day-to-day variation"] = df2["Temperature"].diff()

mean_temp = df2["Temperature"].mean().round(1)

hottest_day = df2.loc[df2["Temperature"].idxmax(), "Day"]    # loc function turns the index result from idxmax() into the corresponding value
coldest_day = df2.loc[df2["Temperature"].idxmin(), "Day"]

print(df2)
print(mean_temp)



plt.figure(figsize=(8,5))
plt.plot(df2["Day"], df2["Temperature"], marker='o', color='orange', linewidth=2)
plt.axhline(y=mean_temp, color='red', linestyle='--', label=f'Mean Temperature: {mean_temp:.1f}')

plt.fill_between(df2["Day"], df2["Temperature"], mean_temp, color='orange', alpha=0.2)


plt.title("Temperature evolution in a week")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


