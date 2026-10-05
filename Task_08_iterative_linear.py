import numpy as np
import matplotlib.pyplot as plt

# Simplified steady-state heat model for 5 interior points along an Ubuntu laptop's copper heat pipe.
A_heatpipe = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: CPU side is 85 C, cooling fan side is 35 C
b_heatpipe = np.array([85., 0., 0., 0., 35.])

def gauss_seidel(A, b, tol=1e-6, max_iter=200):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            # Update using newest available values
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
            
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            break
    return x, errors

x_gs, err_gs = gauss_seidel(A_heatpipe, b_heatpipe)
x_exact = np.linalg.solve(A_heatpipe, b_heatpipe)

print("Gauss-Seidel estimated heat pipe temperatures:", np.round(x_gs, 2))
print("Direct exact solution for verification:", np.round(x_exact, 2))

plt.semilogy(err_gs, label="Gauss-Seidel Convergence", color='red')
plt.xlabel("Iteration")
plt.ylabel("Maximum temperature adjustment")
plt.title("Convergence of Laptop Heat Pipe Temperatures")
plt.legend()
plt.grid(True)
plt.show()

"""
E. Real-World Application: Laptop Heat Pipe Thermal Distribution
Assumptions: A copper heat pipe in a heavy-workload Linux laptop has 5 physical measurement nodes. The left boundary touches the CPU (running at 85 C during a machine learning task), and the right boundary touches the exhaust fan (35 C).
Input Data: A tridiagonal 5x5 matrix representing 1D thermal conductivity, and a boundary condition vector of [85., 0., 0., 0., 35.].
Output: The steady-state temperatures at each of the 5 nodes along the heat pipe, and a graph showing how fast the Gauss-Seidel algorithm converged.
Interpretation: I modified this script to estimate how heat dissipates along my laptop's cooling hardware. The output shows a perfect thermal gradient descending linearly from the CPU to the fan (roughly 76.6 C down to 43.3 C). The Gauss-Seidel iterative method rapidly solved this sparse system to a high degree of precision without requiring a computationally expensive full matrix inversion, which is ideal for running lightweight background thermal monitoring scripts.
"""