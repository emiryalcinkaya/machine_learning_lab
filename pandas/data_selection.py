"""
Select columns from a Pandas DataFrame.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet"],
        "Grade": [85, 92, 78]
    }
)

print("Names:")
print(students["Name"])

print()

print("Grades:")
print(students["Grade"])