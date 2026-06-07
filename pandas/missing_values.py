"""
Handle missing values in a Pandas DataFrame.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
        "Grade": [85, None, 78, 65]
    }
)

print(students)

print()
print("Missing Values:")
print(students.isna())