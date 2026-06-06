"""
Select data using NumPy slicing.
"""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original:", numbers)

print("First Three:", numbers[:3])
print("Last Three:", numbers[-3:])
print("Middle Values:", numbers[2:5])
print("From Index 3:", numbers[3:])