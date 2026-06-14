"""
Train a simple Logistic Regression model.
"""

import pandas as pd 
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = pd.DataFrame(
    {
        "Study Hours": [1, 2, 3, 4, 5, 6],
        "Passed": [0, 0, 0, 1, 1, 1]
    }
)

# Features (input)
X = data[["Study Hours"]]

# Target (output)
y = data["Passed"]

# Create and train the model
model = LogisticRegression()
model.fit(X, y)

# Predictions
prediction_2 = model.predict([[2]])
prediction_5 = model.predict([[5]])

print("Dataset:")
print(data)

print()
print("Prediction for 2 study hours:", prediction_2[0])

print("Prediction for 5 study hours:", prediction_5[0])