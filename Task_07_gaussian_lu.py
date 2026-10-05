import numpy as np
from scipy.linalg import lu_factor, lu_solve

# A: Chemical composition of 3 pre-mixed Arabian fragrance bases
# Base 1: 4 parts Vanilla, 1 part Amber, 0 parts Oud
# Base 2: 1 part Vanilla, 4 parts Amber, 1 part Oud
# Base 3: 0 parts Vanilla, 1 part Amber, 3 parts Oud
A_bases = np.array([
    [4.0, 1.0, 0.0],
    [1.0, 4.0, 1.0],
    [0.0, 1.0, 3.0]
])

# b: Target scent profiles requested by three different users
# Each vector represents total desired parts of [Vanilla, Amber, Oud]
target_profiles = [
    np.array([20.0, 15.0, 5.0]),   # Profile 1: Warm Vanilla dominant 
    np.array([8.0, 25.0, 10.0]),   # Profile 2: Heavy Amber
    np.array([5.0, 10.0, 25.0])    # Profile 3: Intense Oud / Woody
]

# Factor the base compositions once since my raw materials don't change
lu, piv = lu_factor(A_bases)

for i, profile in enumerate(target_profiles, start=1):
    blend_ratio = lu_solve((lu, piv), profile)
    print(f"Custom Profile {i} Recipe")
    print(f"Mix Base 1: {blend_ratio[0]:.2f} ml, Base 2: {blend_ratio[1]:.2f} ml, Base 3: {blend_ratio[2]:.2f} ml\n")

"""
E. Real-World Application: Custom Perfume Blending Optimization
Assumptions: A perfumery uses three pre-mixed raw fragrance bases (Matrix A) made of Vanilla, Amber, and Oud. The system receives multiple target scent profiles (the b vectors) from different clients.
Input Data: A 3x3 matrix of the base formulations and a list of three 1D arrays representing the desired target note distributions.
Output: The exact milliliter mixing ratios required from Base 1, Base 2, and Base 3 to perfectly match each client's target profile.
Interpretation: I structured this script to automate fragrance blending. Since the chemical makeup of my three inventory bases is constant, I factor them once using LU decomposition. I can then feed the system endless target profiles—like a warm vanilla scent or a heavy oud—and `lu_solve` will instantly compute the precise blending recipe for each without wasting computation time recalculating the base matrix.
"""