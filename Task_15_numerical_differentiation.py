import numpy as np
import matplotlib.pyplot as plt

# Telemetry data: time in seconds and velocity in m/s
time_sec = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
velocity_ms = np.array([0.0, 5.2, 11.0, 17.5, 24.0, 30.5, 37.0], dtype=float)
acceleration = np.zeros_like(velocity_ms)

# Forward difference at the start
acceleration[0] = (velocity_ms[1] - velocity_ms[0]) / (time_sec[1] - time_sec[0])

# Central differences for interior points
for i in range(1, len(time_sec) - 1):
    acceleration[i] = (
        (velocity_ms[i + 1] - velocity_ms[i - 1]) / 
        (time_sec[i + 1] - time_sec[i - 1])
    )

# Backward difference at the end
acceleration[-1] = (velocity_ms[-1] - velocity_ms[-2]) / (time_sec[-1] - time_sec[-2])

for t, v, a in zip(time_sec, velocity_ms, acceleration):
    print(f"t={t:.0f}s, velocity={v:.1f}m/s, estimated acceleration = {a:.2f} m/s^2")

plt.plot(time_sec, acceleration, marker="s", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Estimated Acceleration (m/s^2)")
plt.title("Vehicle Acceleration Derived from Velocity Data")
plt.grid(True)
plt.show()

"""
E. Real-World Application: Autonomous Vehicle Acceleration Telemetry
Assumptions: An autonomous vehicle's internal sensors record velocity data at regular one-second intervals. We need to compute instantaneous acceleration to evaluate driving smoothness and dynamic limits.
Input Data: Time stamps in seconds and recorded velocity values in meters per second.
Output: Estimated acceleration at each time step using numerical differentiation, along with a visualization graph.
Interpretation: I adapted this script to calculate vehicle acceleration from velocity telemetry. By applying central differences to neighboring speed measurements, the script accurately estimates how quickly the vehicle accelerates or decelerates at any given moment. This is essential for tuning control systems and evaluating ride comfort in automated vehicles.
"""