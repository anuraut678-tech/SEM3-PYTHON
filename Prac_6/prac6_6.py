import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([5, 7, 8, 7, 6, 9, 5])
y = np.array([99, 86, 87, 88, 100, 86, 103])

# Scatter Plot
plt.scatter(x, y, color="green", s=100)

# Title and Labels
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()
