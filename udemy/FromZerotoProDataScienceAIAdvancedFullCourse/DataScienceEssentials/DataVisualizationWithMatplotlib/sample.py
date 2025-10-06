import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Basic Plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.show()

# line plot
plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# bar chart
categories = ["Apple", "Banana", "Orange"]
values = [10, 20, 30]
plt.bar(categories, values, color="blue")
plt.title("Bar Chart")
plt.show()

# histogram
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.hist(data, bins=3, color="green", edgecolor="black")
plt.title("Histogram")
plt.show()

# scatter plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.scatter(x, y, color="red", marker="*")
plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend(["Dataset 1"])
plt.show()

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

