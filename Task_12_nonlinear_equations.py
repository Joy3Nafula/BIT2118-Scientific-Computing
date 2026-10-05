import numpy as np
from scipy.optimize import root

# Find the intersection point of two vehicle trajectories:
# Vehicle 1 trajectory (Parabolic curve): y = 0.5 * x^2
# Vehicle 2 trajectory (Linear line): y = 2 * x + 1

def trajectories(z):
    x, y = z
    return [
        y - 0.5 * (x**2),
        y - (2 * x + 1)
    ]

for guess in ([1.0, 1.0], [-2.0, -1.0]):
    solution = root(trajectories, guess)
    print("Initial guess:", guess)
    print("Intersection coordinates (x, y):", np.round(solution.x, 4))
    print("Residuals:", trajectories(solution.x))
    print("Converged:", solution.success)
    print()

"""
E. Real-World Application: Autonomous Vehicle Trajectory Intersection
Assumptions: Two autonomous vehicles are approaching a merging lane or junction. Vehicle 1 follows a parabolic turning path defined by y = 0.5 * x^2, while Vehicle 2 follows a linear path defined by y = 2 * x + 1.
Input Data: A system of two nonlinear residual equations representing the overlapping spatial trajectories and two different initial spatial coordinate guesses.
Output: The precise (x, y) coordinates where the two vehicle paths intersect, verified by near-zero residuals.
Interpretation: I modified this script to solve a collision-avoidance trajectory problem for autonomous driving simulations. By feeding the overlapping path functions into `scipy.optimize.root`, the numerical solver successfully calculated the exact coordinates where the two vehicle paths cross. This allows safety systems to check for potential spatial conflicts and adjust vehicle pacing accordingly.
"""