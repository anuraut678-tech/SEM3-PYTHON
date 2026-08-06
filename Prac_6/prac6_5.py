import matplotlib.pyplot as plt
import numpy as np

# Data
categories = np.array(["Data Structures", "Scala for DS", "Operating System", "Python for DS"])
scores = np.array([65, 70, 74, 60])

# Explode the "Python for DS" slice
explode = (0, 0, 0, 0.1)

# Pie Chart
plt.pie(scores, labels=categories, autopct="%1.1f%%", explode=explode)

# Title
plt.title("Student Scores")

# Display the chart
plt.show()
