import statistics

# Sample dataset
data = [10, 20, 20, 40, 50]
weights = [1, 2, 2, 1, 1]  # For weighted mean

# Mean
mean_value = statistics.mean(data)

# Median
median_value = statistics.median(data)

# Mode
mode_value = statistics.mode(data)

# Weighted Mean
weighted_mean = sum(x * w for x, w in zip(data, weights)) / sum(weights)

# Display results
print("Dataset:", data)
print("Weights:", weights)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Weighted Mean:", weighted_mean)
