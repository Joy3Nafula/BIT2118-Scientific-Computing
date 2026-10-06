import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
db_max_qps = 5000.0      # Maximum queries per second capacity
mean_qps = 4200.0        # Expected average query load
std_qps = 600.0          # Standard deviation of query traffic
N_sims = 100_000

# Simulate random QPS demand scenarios using normal distribution
qps_demand = rng.normal(mean_qps, std_qps, N_sims)
rate_limited = qps_demand > db_max_qps
overload_risk = rate_limited.mean()

print(f"Estimated database rate-limit risk: {overload_risk:.4%}")
print(f"Number of overload scenarios: {rate_limited.sum()} out of {N_sims}")

# Running probability to show convergence
running_probability = np.cumsum(rate_limited) / np.arange(1, N_sims + 1)
indices = np.unique(
    np.logspace(1, np.log10(N_sims), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices],
    color='purple'
)
plt.xlabel("Number of Monte Carlo Simulations")
plt.ylabel("Estimated Rate-Limit Probability")
plt.title("Cloud Database Overload Risk Estimation")
plt.grid(True)
plt.show()

"""
E. Real-World Application: Cloud Database Overload Risk Estimation
Assumptions: A cloud database has a strict rate limit of 5,000 queries per second (QPS). Due to fluctuating web traffic, the expected load averages 4,200 QPS with a standard deviation of 600 QPS. We need to estimate the probability that incoming traffic will exceed capacity during peak windows.
Input Data: Max capacity of 5,000, mean demand of 4,200, demand standard deviation of 600, and 100,000 Monte Carlo simulation runs.
Output: Estimated rate-limit breach probability, absolute number of overload scenarios, and a convergence plot.
Interpretation: I adapted this script to model traffic spikes and rate-limiting risk for my backend database infrastructure. By running 100,000 randomized normal simulations, the Monte Carlo method successfully quantifies the exact probability of an overload event. The logarithmic convergence graph proves that our sample size is large enough to yield a stable, highly accurate risk assessment.
"""