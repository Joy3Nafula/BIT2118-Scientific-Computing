import numpy as np

# x = number of FastAPI verification nodes
# y = number of Redis cache instances
#
# FastAPI node uses 2 CPU units and 4 GB memory
# Redis instance uses 1 CPU unit and 8 GB memory
# Total observed cluster usage: 12 CPU units and 48 GB memory

A = np.array([
    [2.0, 1.0],
    [4.0, 8.0]
])
b = np.array([12.0, 48.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"FastAPI Nodes: {solution[0]:.0f}")
print(f"Redis Instances: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual norm:", np.linalg.norm(residual))

"""
E. Real-World Application: CertGuard Backend Infrastructure Allocation
Assumptions: The CertGuard digital certificate verification system uses two types of servers: FastAPI nodes for the backend API and Redis instances for the caching layer. 
Input Data: Matrix A holds the CPU and RAM consumption per node type. Vector b holds the total monitored cluster consumption (12 CPUs, 48 GB RAM).
Output: The exact count of FastAPI and Redis servers currently active in the cluster.
Interpretation: I designed this script to reverse-engineer my active infrastructure footprint. By solving the system of linear equations, the output accurately determines that the system is currently running exactly 4 FastAPI verification nodes and 4 Redis cache instances to consume the observed resources. The residual norm of 0.0 confirms the calculation is perfectly precise.
"""