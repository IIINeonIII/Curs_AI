import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


data = pd.read_csv(r'D:\data_processing\fires_thefts.csv')

data = data.dropna()
data = data.drop_duplicates()

print(data.head())

data['fires'] = pd.to_numeric(data['fires'], errors='coerce')
data['thefts'] = pd.to_numeric(data['thefts'], errors='coerce')
data = data.dropna()

X = data[['fires']]
y = data['thefts']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))


print("R2 score: %.1f" % r2)
print("RMSE: %.1f" % rmse)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

plt.scatter(X, y, color='red', label='data')

x_range = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
y_range = model.predict(x_range)

plt.plot(x_range, y_range, color='blue', label='Regression Line')

plt.xlabel("Fires")
plt.ylabel("Thefts")
plt.title("Correlation between Thefts and Fires")
plt.legend()
plt.show()


new_value = np.array([[5]])
prediction = model.predict(new_value)

print("Prediction for 5 fires:", prediction)