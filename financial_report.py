import pandas as pd
import numpy as np

df = pd.read_excel("financial_data.xlsx")
print(df.head())

# num_data = df[['Revenue','Profit', 'Expenses']].to_numpy()
# print(num_data)
#
# profit_margin = num_data[:,1] / num_data[:,0]
# print(profit_margin)

df['Profit Margin'] = df['Profit'] / df['Revenue']
df['Profit Margin'] = df['Profit Margin'].round(2)
print(df['Profit Margin'])

df['Expense Ratio'] = df['Expenses'] / df['Revenue']
df['Expense Ratio'] = df['Expense Ratio'].round(2)
print(df['Expense Ratio'])

print(df.head())

# df = df.sort_values(by=['Company', 'Quarter']).reset_index()
#
# df['Revenue Growth']= np.nan   # creates a new df, filled with empty NaN values
#
# for company in df['Company']:
#     company_mask = df['Company'] == company
#     revenues = df.loc[company_mask]['Revenue'].values     # .values converts returned values into np specific data type from pd data type
#     growth = np.empty_like(revenues, dtype=float)    # empty_like creats an empty array with same dim as the array in arguments ()
#     growth[0] = np.nan
#     growth[1:] = (revenues[1:] - revenues[:-1]) / revenues[:-1]  # growth is empty and same shape as revenues. This line slices through each row of revenues calculating the growth
#     df.loc[company_mask, 'Revenue Growth'] = growth   # fills the rows of the empty Rev Growth df column with the values in growth array
#
# print ("Revenue Growth")
# print(df)

# - pd only method -

# df = (
#     df.sort_values(by=['Company', 'Quarter'])
#       .reset_index(drop=True)
# )
#
# df['Revenue Growth'] = (
#     df.groupby('Company')['Revenue']
#       .pct_change()
# )

df = df.sort_values(by=['Company', 'Quarter']).reset_index(drop=True)

grouped = df.groupby('Company')['Revenue']   # groups the data by company
df['Revenue Growth'] = grouped.pct_change()  # does what we did with the numpy method condensed in one function
df['Revenue Growth'] = df['Revenue Growth'].round(2)

print("Revenue Growth")
print(df)

# 10th percentile

threshold = np.nanpercentile(df['Revenue Growth'], 50)
print(f"\n2.  Growth Rate:  {threshold}")

high_growth_df = df[df['Revenue Growth'] > threshold]

high_growth_df = high_growth_df.sort_values(by='Revenue Growth', ascending=False)

print(high_growth_df[['Company', 'Quarter', 'Revenue Growth']])

# high_growth_counts = high_growth_df.groupby('Company')['Revenue Growth'].count()
# print(high_growth_counts)

high_growth_counts = high_growth_df.groupby('Company').size().reset_index(name='High_Growth_Counts')

print(high_growth_counts)
print(high_growth_counts.columns)


high_growth_companies = high_growth_counts[high_growth_counts['High_Growth_Counts'] >=2]      # boolean matrice (mask) and operations
print(high_growth_companies)

threshold = df['Revenue Growth'].quantile(0.9)
high_growth_counts_2 = (df[df['Revenue Growth'] > threshold].groupby('Company').size().reset_index(name='High_Growth_Counts'))

avg_profit_margin = df.groupby('Company')['Profit Margin'].mean().reset_index(name='Avg_Profit_Margin')
print(avg_profit_margin)

investment_df = pd.merge(high_growth_counts_2, avg_profit_margin, on='Company')
print(investment_df)

investment_df = investment_df.sort_values(by=['High_Growth_Counts', 'Avg_Profit_Margin'], ascending=[False, False]).reset_index(drop=True)

print("Companies to invest in")
print(investment_df)


df6 = pd.read_csv("financial_data.csv", usecols=['Company', 'Quarter', 'Profit'], na_values=['nan', '0'], index_col='Company')
print(df6)

df.to_csv("financial_data_output.csv", index=False)



