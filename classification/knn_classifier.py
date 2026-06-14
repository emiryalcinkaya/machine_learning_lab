"""
Train a simple K-Nearest Neighbors classifier.
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Sample dataset
data = pd.DataFrame(
    {
        "Study Hours": [1, 2, 3, 4, 5, 6],
        "Sleep Hours": [5, 6, 5, 7, 8, 8],
        "Passed": [0, 0, 0, 1, 1, 1]
    }
)

# Features
X = data[["Study Hours", "Sleep Hours"]]

# Target
y = data["Passed"]

# Create and train the model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict new students
prediction_1 = model.predict([[2, 5]])
prediction_2 = model.predict([[6, 8]])

print("Dataset:")
print(data)

print()
print("Prediction for student with 2 study hours and 5 sleep hours:", prediction_1[0])
print("Prediction for student with 6 study hours and 8 sleep hours:", prediction_2[0])