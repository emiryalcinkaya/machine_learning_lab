"""
Evaluate a Linear Regression model.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
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

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print("Model Score:", score)