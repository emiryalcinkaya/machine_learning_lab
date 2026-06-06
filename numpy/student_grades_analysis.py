"""
Analyze student grades using NumPy.
"""

import numpy as np

grades = np.array([65, 72, 88, 95, 78, 84, 91, 55, 100, 69])

print("Grades:", grades)

print("Average Grade:", np.mean(grades))
print("Median Grade:", np.median(grades))
print("Highest Grade:", np.max(grades))
print("Lowest Grade:", np.min(grades))
print("Standard Deviation:", np.std(grades))

print("First Five Grades:", grades[:5])
print("Last Three Grades:", grades[-3:])

print("Passed Students:", grades[grades >= 70])
print("Failed Students:", grades[grades < 70])
print("Excellent Grades:", grades[grades >= 90])