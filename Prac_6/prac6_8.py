import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
y2 = np.array([1, 4, 9, 16, 25])

# First Plot
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Plot")

# Second Plot
plt.subplot(1, 2, 2)
plt.bar(x, y2)
plt.title("Bar Chart")

# Display both plots
plt.show()
