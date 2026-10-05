import numpy as np

# Sentinel-Stream: Sliding-window micro-transaction threshold checking
# A common carding tactic is rapid micro-authorizations. 
# We intercept three $0.10 pings.
transactions = [0.10, 0.10, 0.10]
velocity_sum = sum(transactions)
fraud_threshold = 0.30

print(f"Calculated aggregate velocity: {velocity_sum}")
print("Flagged by strict equality (==):", velocity_sum == fraud_threshold)
print("Flagged by tolerance check (isclose):", np.isclose(velocity_sum, fraud_threshold))

# Calculate the representation error causing the strict check to fail
absolute_error = abs(velocity_sum - fraud_threshold)
print(f"Absolute float error in aggregation: {absolute_error:.18f}")

"""
E. Real-World Application: Sentinel-Stream Fraud Detection Logic
Assumptions: The sliding-window feature store intercepts three $0.10 transactions and aggregates them to check against a hardcoded $0.30 velocity threshold.
Input Data: A list of float micro-transactions.
Output: Boolean flags demonstrating if the threshold logic triggers, and the absolute error magnitude.
Interpretation: The script shows how accumulated float imprecision in a financial transaction stream can cause a false negative if the logic uses strict equality. Because 0.10 + 0.10 + 0.10 equals 0.30000000000000004 in binary, the strict `==` check fails to flag the fraud. Using `np.isclose()` successfully flags the behavior, highlighting why tolerance checks are critical in backend financial engineering.
"""