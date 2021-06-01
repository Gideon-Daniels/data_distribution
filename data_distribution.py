import numpy as np
import matplotlib.pyplot as plt

# Math-plot-lib is a low level graph plotting library in python that serves as a visualization utility

marks = [70, 45, 90, 12]
names = ["Gideon", "Godwin", "Thando", "Thabo"]

marks = np.array([70, 45, 90, 12])
names = np.array(["Gideon", "Godwin", "Thando", "Thabo"])
plt.title("Marks")
plt.bar(names, marks)  # x-axis , y-axis
plt.show()
