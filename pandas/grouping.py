"""
Group data using Pandas.
"""

import pandas as pd

employees = pd.DataFrame(
    {
        "Department": ["IT", "IT", "HR", "HR"],
        "Salary": [5000, 6000, 4000, 4500]
    }
)

print(
    employees.groupby("Department")["Salary"].mean()
)