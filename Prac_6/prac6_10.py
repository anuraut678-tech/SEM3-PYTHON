import matplotlib.pyplot as plt
import numpy as np

# Data
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
sales_2023 = np.array([150, 200, 250, 300, 280, 350])
sales_2024 = np.array([180, 220, 270, 320, 300, 400])

# Plot 2023 Sales
plt.plot(months, sales_2023,
         color="blue",
         linestyle="--",
         marker="o",
         label="2023")

# Plot 2024 Sales
plt.plot(months, sales_2024,
         color="green",
         linestyle="-",
         marker="s",
         label="2024")

# Title and Labels
plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")

# Legend
plt.legend()

# Highlight highest sales month of 2024
max_index = np.argmax(sales_2024)
plt.annotate("Highest Sales",
             xy=(months[max_index], sales_2024[max_index]),
             xytext=(months[max_index], sales_2024[max_index] + 20),
             arrowprops=dict(facecolor="black", arrowstyle="->"))

# Save the plot
plt.savefig("sales_comparison.png")

# Display the plot
plt.show()
