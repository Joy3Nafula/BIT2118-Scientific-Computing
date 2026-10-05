import numpy as np
import matplotlib.pyplot as plt

# Newton's Law of Cooling applied to a server room rack during AC failure:
# dT/dt = -k (T - T_ambient)
T_ambient_server = 45.0  # High ambient room temperature during failure
T_initial_rack = 22.0     # Initial server rack temperature
k_server = 0.08           # Heating rate constant as servers absorb ambient heat
h_step = 1.0              # 1 minute time step
end_time_server = 30.0    # 30 minute simulation

def heating_rate(T):
    return k_server * (T_ambient_server - T)

time = np.arange(0, end_time_server + h_step, h_step)
rack_temp = np.zeros_like(time)
rack_temp[0] = T_initial_rack

for i in range(len(time) - 1):
    rack_temp[i + 1] = rack_temp[i] + h_step * heating_rate(rack_temp[i])

# Exact solution for validation
exact_server = T_ambient_server + (T_initial_rack - T_ambient_server) * np.exp(-k_server * time)

print(f"Euler rack temperature after 30 min: {rack_temp[-1]:.2f} C")
print(f"Exact rack temperature after 30 min: {exact_server[-1]:.2f} C")
print(f"Final absolute error: {abs(rack_temp[-1] - exact_server[-1]):.4f} C")

plt.plot(time, rack_temp, marker="o", label="Euler Approximation", color="red")
plt.plot(time, exact_server, label="Exact Analytical Solution", linestyle="--", color="black")
plt.xlabel("Time (minutes)")
plt.ylabel("Server Rack Temperature (C)")
plt.title("Server Rack Heating during AC Failure")
plt.legend()
plt.grid(True)
plt.show()

"""
E. Real-World Application: Server Rack Thermal Surge Simulation
Assumptions: The air conditioning fails in a data center, causing the ambient room temperature to jump to 45°C. I need to predict how quickly a server rack initially at 22°C will heat up over 30 minutes.
Input Data: Ambient room temperature of 45°C, starting rack temperature of 22°C, a heating rate constant of 0.08, and 1-minute time steps.
Output: Estimated server rack temperature after 30 minutes calculated via Euler's method, compared against the exact analytical solution, with a visualization graph.
Interpretation: I adapted this script to model a thermal emergency in a server room. Instead of cooling down, the server rack absorbs heat from the hot ambient air. The Euler method successfully stepped through the differential equation, showing the rack temperature rising sharply before starting to plateau as it approaches 45°C. This modeling helps evaluate how much emergency shutdown buffer time administrators have before hardware overheats.
"""