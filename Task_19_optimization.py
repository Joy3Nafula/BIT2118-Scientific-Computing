import numpy as np
from scipy.optimize import minimize

# Cloud resource allocation for ML pipeline execution nodes:
# x = number of CPU nodes, y = number of GPU nodes
# Cost per unit: CPU node = $20, GPU node = $50
# Processing throughput units per node: CPU = 10, GPU = 45
# Required total throughput: at least 500 processing units

def pipeline_cost(z):
    x, y = z
    return 20 * x + 50 * y

def throughput_constraint(z):
    x, y = z
    return 10 * x + 45 * y - 500

constraints = {
    "type": "ineq",
    "fun": throughput_constraint
}
bounds = [(0, None), (0, None)]

solution = minimize(
    pipeline_cost,
    x0=[2.0, 2.0],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"CPU nodes allocation: {x:.3f}")
print(f"GPU nodes allocation: {y:.3f}")
print(f"Total pipeline throughput: {10 * x + 45 * y:.2f}")
print(f"Minimum resource cost: ${solution.fun:.2f}")

# Find best integer node allocation
best_integer = None
for a in range(0, 30):
    for b in range(0, 30):
        throughput = 10 * a + 45 * b
        if throughput >= 500:
            total_cost = 20 * a + 50 * b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, throughput)

print("Best integer hardware configuration:", best_integer)

"""
E. Real-World Application: Cloud Machine Learning Pipeline Optimization
Assumptions: An MLOps engineering team needs to allocate CPU and GPU worker nodes to minimize cloud infrastructure costs while guaranteeing a minimum processing throughput of 500 units for a streaming data pipeline.
Input Data: Unit costs ($20 for CPU, $50 for GPU), throughput metrics per node type, and a minimum throughput constraint of 500.
Output: Optimal fractional node allocations, total throughput, minimum cost, and the optimal whole-number hardware configuration.
Interpretation: I adapted this script to optimize cloud resource provisioning for my backend pipelines. By setting up an objective cost function subject to a performance constraint, `scipy.optimize.minimize` successfully calculated the cost-effective blend of computing resources. The integer search loop ensures I get actionable whole-number node counts to deploy directly onto my infrastructure.
"""