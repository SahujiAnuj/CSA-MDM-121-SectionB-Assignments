import numpy as np

# Sample dataset
x = np.array([2, 3, 5, 7, 9])   # Study hours
y = np.array([50, 60, 65, 70, 85])  # Exam scores

# 1) Correlation coefficient (Pearson's r)
correlation_matrix = np.corrcoef(x, y)
correlation_coefficient = correlation_matrix[0, 1]

# 2) Linear regression using least squares
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)

# Slope (b) = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)^2]
b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

# Intercept (a) = ȳ - b * x̄
a = y_mean - b * x_mean

# Regression line equation: y = a + b*x
print("Correlation Coefficient (r):", correlation_coefficient)
print(f"Regression Line: y = {a:.2f} + {b:.2f}x")
