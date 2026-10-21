import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


data_dict = {
    'students': ["Bill", "Bob", "Jane", "Susan", "Kevin", "Mike", "Shanon", "Beatrice", "John"],
    'grades': [5, 4, 8, 6, 5, 8, 8, 9, 7],
    'hours_studied': [4, 4, 10, 5, 2, 8, 9, 11, 10],
    'gender': ["M", "M", "F", "F", "M", "M", "F", "F", "M"]
}

data = pd.DataFrame(data_dict)

# print(data)
#
# X = data[['grades']]
# y = data['hours_studied']
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
#
# y_pred = regressor.predict(X_test)
#
#
# r2 = r2_score(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# print(r2)
# print(mse)
#
#
# plt.scatter(X, y, color='red', label='data')
#
# x_range = np.linspace(X.min(), X.max(), 100).reshape(-1,1)
# y_range = regressor.predict(x_range)
#
# plt.plot(x_range, y_range, color='blue', label='Regression Line')
#
# plt.xlabel("grades")
# plt.ylabel("hours_studied")
# plt.title("Correlation between studied hours and students grades")
# plt.legend()
# plt.show()
#
# new_value = np.array([[6]])
# prediction = regressor.predict(new_value)
# print(prediction)



print("\nAverage hours studied per gender:")
print(data.groupby('gender')['hours_studied'].mean())

print("\nAverage grade per gender:")
print(data.groupby('gender')['grades'].mean())

print("\nDetailed statistics by gender:")
print(data.groupby('gender')['hours_studied'].describe())

# -------------------------------
# Visualization
# -------------------------------

# Scatter plot colored by gender
colors = {'M': 'blue', 'F': 'green'}

plt.figure()

for gender in data['gender'].unique():
    subset = data[data['gender'] == gender]
    plt.scatter(subset['hours_studied'],
                subset['grades'],
                color=colors[gender],
                label=gender)

plt.xlabel("Hours Studied")
plt.ylabel("Grades")
plt.title("Grades vs Hours Studied by Gender")
plt.legend()
plt.show()

# Boxplot of hours studied by gender
plt.figure()
data.boxplot(column='hours_studied', by='gender')
plt.title("Hours Studied Distribution by Gender")
plt.suptitle("")
plt.ylabel("Hours Studied")
plt.show()

# -------------------------------
# Encode gender for regression
# -------------------------------

data['gender_encoded'] = data['gender'].map({'M': 0, 'F': 1})

# -------------------------------
# Regression model
# Predict grades from hours studied + gender
# -------------------------------

X = data[['hours_studied', 'gender_encoded']]
y = data['grades']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predictions
y_pred = regressor.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("\nModel Evaluation")
print("R2 Score:", r2)
print("Mean Squared Error:", mse)

print("\nModel Coefficients:")
print("Hours studied coefficient:", regressor.coef_[0])
print("Gender coefficient:", regressor.coef_[1])
print("Intercept:", regressor.intercept_)

# -------------------------------
# Regression Line Visualization
# -------------------------------

plt.figure()

plt.scatter(data['hours_studied'], data['grades'], color='red', label='Data')

x_range = np.linspace(data['hours_studied'].min(),
                      data['hours_studied'].max(),
                      100)

# Assume gender = 0 (Male) for visualization
x_range_reshaped = np.column_stack((x_range, np.zeros(len(x_range))))

y_range = regressor.predict(x_range_reshaped)

plt.plot(x_range, y_range, color='blue', label='Regression Line (Male)')

plt.xlabel("Hours Studied")
plt.ylabel("Grades")
plt.title("Regression: Grades vs Hours Studied")
plt.legend()
plt.show()

# -------------------------------
# Predictions
# -------------------------------

# Predict grade for 6 hours studied (Male)
prediction_male = regressor.predict([[6, 0]])

# Predict grade for 6 hours studied (Female)
prediction_female = regressor.predict([[6, 1]])

print("\nPrediction for 6 hours studied:")
print("Male predicted grade:", prediction_male)
print("Female predicted grade:", prediction_female)

prediction_male2 = regressor.predict([[10, 0]])
print("\nPrediction for 10 hours studied:")
print("Male predicted grade:", prediction_male2)

prediction_female2 = regressor.predict([[10, 1]])
print("\nPrediction for 10 hours studied:")
print("Female predicted grade:", prediction_female2)





