import numpy as np

# Generate random dataset
dataset = np.random.randint(1, 100, size=(10, 5))
print("Original Dataset: \n", dataset)

# Filter values > 50 and replace them with 0
dataset[dataset > 50] = 0
print("Filtered Dataset: \n", dataset)

# Calculate summary stats
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))
print("Variance: ", np.var(dataset))