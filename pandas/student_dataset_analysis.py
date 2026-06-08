"""
Analyze student data using Pandas.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet"],
        "Grade": [85, 92, 78, 65, 95]
    }
)

print("Dataset:")
print(students)

print()
print("Average Grade:")
print(students["Grade"].mean())

print()
print("Highest Grade:")
print(students["Grade"].max())

print()
print("Students With Grades Above 80:")
print(students[students["Grade"] > 80])