"""
Calculate basic statistics using NumPy.
"""

import numpy as np

grades = np.array([65, 72, 88, 95, 78, 84, 91])

print("Grades:", grades)
print("Mean:", np.mean(grades))
print("Median:", np.median(grades))
print("Maximum:", np.max(grades))
print("Minimum:", np.min(grades))
print("Sum:", np.sum(grades))
print("Standard Deviation:", np.std(grades))