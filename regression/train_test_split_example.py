"""
Split data into training and testing sets.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.DataFrame(
    {
        "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Exam Score": [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
    }
)

X = data[["Study Hours"]]
y = data["Exam Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Features:")
print(X_train)

print()
print("Testing Features:")
print(X_test)

print()
print("Training Target:")
print(y_train)

print()
print("Testing Target:")
print(y_test)