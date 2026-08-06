import matplotlib.pyplot as plt
import numpy as np

# Data
categories = np.array(["Data Structures", "Scala for DS", "Operating System", "Python for DS"])
scores = np.array([65, 70, 74, 60])

# Horizontal Bar Chart
plt.barh(categories, scores)

# Title and Labels
plt.title("Student Scores")
plt.xlabel("Scores")
plt.ylabel("Subjects")

# Display the chart
plt.show()
