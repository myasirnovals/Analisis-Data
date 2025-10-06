import matplotlib.pyplot as plt

# Line Plot
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
sales = [100, 120, 140, 160, 180, 200, 220]
plt.plot(years, sales, label="Sales Trend", color="blue", marker="o")
plt.title("Sales Trend")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# bar chart
categories = ["Electronics", "Books", "Clothes", "Home Appliances", "Furniture"]
revenue = [10, 20, 30, 40, 50]
plt.bar(categories, revenue, color="green")
plt.title("Revenue by Category")
plt.show()

# scatter plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [90, 80, 70, 60, 50]
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.show()