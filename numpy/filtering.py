"""
Filter data using NumPy conditions.
"""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("Original:", numbers)

print("Greater Than 40:", numbers[numbers > 40])
print("Less Than 50:", numbers[numbers < 50])
print("Equals To 30:", numbers[numbers == 30])