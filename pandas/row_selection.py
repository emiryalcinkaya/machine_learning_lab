"""
Select rows from a Pandas DataFrame.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet"],
        "Grade": [85, 92, 78]
    }
)

print("First Student:")
print(students.loc[0])

print()

print("Second Student:")
print(students.loc[1])

print()

print("Third Student:")
print(students.loc[2])