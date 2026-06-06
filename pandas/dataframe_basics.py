"""
Create and use a Pandas DataFrame.
"""

import pandas as pd

students = pd.DataFrame(
    {
        "Name": ["Ali", "Ayşe", "Mehmet"],
        "Grade": [85, 92, 78]
    }
)

print(students)