import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

# Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

# Histogram
plt.subplot(2, 2, 4)
data = np.random.normal(size=100)
plt.hist(data, bins=20)
plt.title("Histogram")

# Adjust spacing
plt.tight_layout()

# Display all plots
plt.show()
