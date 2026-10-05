import numpy as np
import timeit

# Simulated 1 million credit card transactions in KES (between 500 and 50,000)
rng = np.random.default_rng(42)
transactions_kes = rng.uniform(500, 50000, 1_000_000)

def loop_version():
    fees = []
    for amount in transactions_kes:
        usd = amount / 130.0
        fees.append(usd * 0.025)
    return fees

def vectorized_version():
    usd_amounts = transactions_kes / 130.0
    return usd_amounts * 0.025

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()

print("First five USD processing fees:", np.round(result[:5], 2))
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")

"""
E. Real-World Application: Credit Card Transaction Stream Processing
Assumptions: 1 million transactions require currency conversion. Exchange rate is 1 USD = 130 KES. Processing fee is 2.5%.
Input Data: 1 million uniformly distributed float values representing KES amounts.
Output: The processed USD fee amounts and a benchmark comparison between loops and vectorization.
Interpretation: The script successfully calculates the processing fees for all 1 million transactions simultaneously. The timing output highlights the massive performance advantage of NumPy vectorization over standard Python loops when managing high-velocity transaction streams, ensuring the pipeline scales effectively in production.
"""