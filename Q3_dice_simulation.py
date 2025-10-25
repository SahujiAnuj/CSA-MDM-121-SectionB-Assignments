import random

# Number of simulations
trials = 10000

# Counter for sum = 7
count_sum7 = 0

# Simulation of rolling two dice
for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum7 += 1

# Estimated probability
estimated_prob = count_sum7 / trials

# Theoretical probability
# There are 6 × 6 = 36 possible outcomes
# Favorable outcomes for sum = 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 outcomes
theoretical_prob = 6 / 36

# Display results
print("Number of trials:", trials)
print("Estimated probability of sum = 7:", estimated_prob)
print("Theoretical probability of sum = 7:", theoretical_prob)
print("Difference:", abs(estimated_prob - theoretical_prob))
