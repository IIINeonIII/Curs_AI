import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('training_data_with_weather_info_week_1.csv',
                 usecols=['Id', 'Country/Region', 'Date', 'temp', 'min', 'max','stp', 'slp', 'dewp', 'prcp','fog', 'wdsp'])


df_Bangladesh = df[df['Country/Region'] == 'Bangladesh'].copy()

print(df_Bangladesh.head(15))

print(f'Total number of Bangladesh entries:', len(df_Bangladesh))

print(f'List of Bangladesh columns', df_Bangladesh.columns.to_list())
print(df_Bangladesh.index)

# Task

print(df['Country/Region'].value_counts())
print(df['Country/Region'].nunique())

print(df['Country/Region'].iloc[-1])


df_Bangladesh.index = range(1, len(df_Bangladesh) + 1)

print(df_Bangladesh.head(7))
print(df_Bangladesh.loc[3])    # uses personalised index
print(df_Bangladesh.iloc[3])   # uses default 0 index

# Task 6
df_Bangladesh["Date"] = pd.to_datetime(df_Bangladesh["Date"])

df_obs = df_Bangladesh[df_Bangladesh["Date"].between("2020-03-01", "2020-03-10") ]
print(df_obs)


df_obs = df_Bangladesh[df_Bangladesh["Date"].between(pd.Timestamp("2020-03-01"), pd.Timestamp("2020-03-10")) ]
print(df_obs)

df["Date"] = pd.to_datetime(df["Date"])

df_obs_all = df[df["Date"] == "2020-02-01"]
print(df_obs_all)

# Task 7

number_of_missing = df["slp"].isna().sum()
print(number_of_missing)

df_cleaned = df.dropna(subset=["slp"]).reset_index(drop=True)
print(f'New shape after cleaning: {df_cleaned.shape}')

# Task 8

temp_mean = df["temp"].mean()
print(temp_mean)

df_lowtemp = df[df["temp"] < temp_mean]
print(len(df_lowtemp))

df_highmin = df[df["min"] > temp_mean]
print(len(df_highmin))
print(df_highmin[["Country/Region", "Date", "min"]].head(5))

# Task 10

fog_count = df["fog"].sum()

percentage_fog = fog_count / len(df) * 100
print(f'Fog observed {fog_count} times, reprezenting {percentage_fog:.2f} % of the total readings.')


# Task 11

avg_temp_country = df.groupby("Country/Region")["temp"].mean().sort_values(ascending=False)
print(avg_temp_country.head(5))

# Task 12

avg_wind = df["wdsp"].mean()
df_wind = df.sort_values(by="wdsp", ascending=False)
print(f'Average global wind speed: {avg_wind:.2f} m/s')
# print(f'Windiest country on Earth {df_wind.head(1)[['Country/Region','wdsp']]}')

avg_wind_country = df.groupby("Country/Region")["wdsp"].mean().sort_values(ascending=False)

avg_per_country = (avg_wind_country.sort_values(ascending=False))
print(avg_per_country.head(5))

wind_max = avg_wind_country.idxmax()
print(wind_max)
wind = avg_wind_country.max()
print(wind)

# Task 13


df_canada = df[df["Country/Region"] == "Canada"]

df_canada_period = df_canada[df_canada["Date"].between("2020-01-01", "2020-03-31")]
df_canada_period["Date"] = pd.to_datetime(df_canada_period["Date"])

df_canada_period = df_canada_period.sort_values(by="Date")

avg_temp_date = df_canada_period.groupby("Date")["temp"].mean()
# print(avg_temp_date)


plt.figure(figsize=(10,5))
plt.plot(avg_temp_date.index, avg_temp_date.values, marker='o', linestyle='-', color='r')

plt.title('Temperature evolution in Canada ( 2020 )')
plt.xlabel('Date')
plt.ylabel('Average Temperature')
plt.grid(True)

# plt.show()



# Task 16


df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

avg_temp_country = (df.groupby(["Country/Region", "Month"])["temp"].mean().reset_index().rename(columns={"temp": "average monthly temperature"}))

print(avg_temp_country.head(15))


togo_temps = avg_temp_country[avg_temp_country["Country/Region"] == "Togo"]
print(togo_temps)

coldest_march = avg_temp_country[avg_temp_country["Month"] == 3]
lowest_temps = coldest_march.nsmallest(5, 'average monthly temperature')
print(lowest_temps.head(5))


# T 17

countries = df["Country/Region"].unique()[:5]
print(countries)

df_selected = df[df["Country/Region"].isin(countries)][["Date", "Country/Region", "temp"]]

df_pivot = df_selected.pivot_table(index="Date", columns="Country/Region", values="temp", aggfunc = "mean").reset_index()


df_pivot.columns.name = None

print(df_pivot.head(5))












