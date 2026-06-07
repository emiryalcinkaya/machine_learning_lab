"""
Filter data in a Pandas DataFrame.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
        "Grade": [85, 92, 78, 65]
    }
)

print("Student With Grades Above 80:")
print(students[students["Grade"] > 80])

print()

print("Students With Grades Below 80:")
print(students[students["Grade"] < 80])