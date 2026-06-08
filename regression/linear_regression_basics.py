"""
Train a simple Linear Regression model.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = pd.DataFrame(
    {
        "Study Hours": [1, 2, 3, 4, 5],
        "Exam Score": [50, 60, 70, 80, 90]
    }
)

# Features (input)
X = data[["Study Hours"]]

# Target (output)
y = data[["Exam Score"]]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict a score for 6 study hours
prediction = model.predict([[6]])

print("Dataset:")
print(data)

print()
print("Predicted score for 6 study hours:", prediction[0])

# Model parameters
print()
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)