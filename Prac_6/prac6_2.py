import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Customized Line Plot
plt.plot(x, y, color="red", linestyle="--", marker="o")

# Title and Labels
plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

# Display the plot
plt.show()
