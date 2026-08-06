import matplotlib.pyplot as plt
import numpy as np

# Generate 100 random numbers (Normal distribution)
data = np.random.normal(size=100)

# Histogram with 20 bins
plt.hist(data, bins=20)

# Title and Labels
plt.title("Histogram of Random Numbers")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Add Grid
plt.grid(True)

# Display the plot
plt.show()
