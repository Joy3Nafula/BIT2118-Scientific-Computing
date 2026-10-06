import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Chemical reaction kinetics: Second-order reactant consumption A -> Products
# dA/dt = -k * A^2
k_rate = 0.5
A_initial = [2.0]  # Initial concentration of reactant A (mol/L)

def chemical_reaction(t, A):
    return [-k_rate * (A[0] ** 2)]

t_eval_chem = np.linspace(0, 10, 200)
solution_chem = solve_ivp(
    chemical_reaction,
    (0, 10),
    A_initial,
    t_eval=t_eval_chem,
    rtol=1e-8,
    atol=1e-10
)

# Exact analytical solution for second-order reaction: A(t) = A_0 / (1 + k * A_0 * t)
exact_chem = A_initial[0] / (1.0 + k_rate * A_initial[0] * solution_chem.t)

print("Solver success:", solution_chem.success)
print(f"Reactant concentration at t=10s: {solution_chem.y[0, -1]:.4f} mol/L")
print(f"Maximum error against exact solution: {np.max(np.abs(solution_chem.y[0] - exact_chem)):.3e}")

plt.plot(solution_chem.t, solution_chem.y[0], label="solve_ivp Numerical")
plt.plot(solution_chem.t, exact_chem, linestyle="--", label="Exact Analytical", color="black")
plt.xlabel("Time (s)")
plt.ylabel("Reactant Concentration (mol/L)")
plt.title("Chemical Reaction Kinetics Simulation")
plt.legend()
plt.grid(True)
plt.show()

"""
E. Real-World Application: Chemical Reaction Kinetics Simulation
Assumptions: A second-order chemical reaction consumes reactant A over a 10-second window. The rate of consumption depends quadratically on the concentration.
Input Data: Reaction rate constant k = 0.5, initial concentration A_0 = 2.0 mol/L, and a time span from 0 to 10 seconds.
Output: The numerical concentration values of reactant A over time, compared against the exact analytical solution with a validation plot.
Interpretation: I adapted this script to model chemical reaction dynamics using SciPy's advanced ODE solver. Unlike simple manual integration, `solve_ivp` automatically manages step sizes to handle non-linear differential equations with high precision. The output plot shows the concentration dropping sharply at first due to high initial concentration, and then slowing down as reactant A is depleted.
"""