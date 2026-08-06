import matplotlib.pyplot as plt
import numpy as np

# Data
categories = np.array(["Data Structures", "Scala for DS", "Operating System", "Python for DS"])
scores = np.array([65, 70, 74, 60])

# Bar Chart
plt.bar(categories, scores)

# Title and Labels
plt.title("Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")

# Display the chart
plt.show()
