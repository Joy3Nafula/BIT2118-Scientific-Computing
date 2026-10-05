import numpy as np
from scipy.integrate import simpson

# Vehicle speed measurements recorded every 2 seconds (in meters per second)
time_seconds = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
speed_ms = np.array([0.0, 4.5, 12.0, 18.5, 15.0, 8.0, 0.0])

distance_trapezoid = np.trapezoid(speed_ms, time_seconds)
distance_simpson = simpson(speed_ms, x=time_seconds)

print(f"Total distance using trapezoidal rule: {distance_trapezoid:.3f} meters")
print(f"Total distance using Simpson's rule: {distance_simpson:.3f} meters")
print(f"Difference between estimates: {abs(distance_simpson - distance_trapezoid):.3f} meters")

"""
E. Real-World Application: Total Distance Traveled from Velocity Telemetry
Assumptions: An autonomous vehicle records its speed at regular two-second intervals. We need to calculate the total physical distance traveled over the 12-second window by integrating the velocity-versus-time curve.
Input Data: Time stamps in seconds and recorded vehicle speed values in meters per second.
Output: Total integrated distance computed via both trapezoidal and Simpson's integration methods.
Interpretation: I adapted this script to calculate cumulative distance from velocity logs. Integrating speed over time yields the total distance covered. Both numerical integration techniques successfully computed the distance, with Simpson's rule providing a smooth parabolic approximation of the vehicle's acceleration and braking phases.
"""