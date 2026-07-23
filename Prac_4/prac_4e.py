#4e. Python code to Create a filter Array thet returns the maximum value.

print("S106 Ananya raut")

import numpy as np

arr = np.array([31, 24, 45, 32, 90, 12])

max_value = np.max(arr)

filtered_arr = arr[arr == max_value]

print("Original Array:", arr)
print("Maximum Value:", max_value)
print("Filtered Array:", filtered_arr)



