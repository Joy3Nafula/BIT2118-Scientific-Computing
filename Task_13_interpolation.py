import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Foaling barn humidity monitoring: recorded every 2 hours (percentage)
hours_barn = np.array([6, 8, 10, 12, 14, 16, 18], dtype=float)
humidity_pct = np.array([75.0, 70.0, 62.0, 55.0, 53.0, 58.0, 68.0])

linear_hum = interp1d(hours_barn, humidity_pct, kind="linear")
cubic_hum = CubicSpline(hours_barn, humidity_pct)

# Estimate humidity every 15 minutes (= 0.25 hours)
quarter_hour_times = np.arange(6, 18 + 0.25, 0.25)
linear_estimates = linear_hum(quarter_hour_times)
cubic_estimates = cubic_hum(quarter_hour_times)

target_time = 11.0 # 11:00 AM
print(f"Linear humidity estimate at 11:00: {float(linear_hum(target_time)):.2f}%")
print(f"Cubic spline humidity estimate at 11:00: {float(cubic_hum(target_time)):.2f}%")

plt.scatter(hours_barn, humidity_pct, label="Bi-hourly Sensor Logs", color="purple")
plt.plot(quarter_hour_times, linear_estimates, label="Linear Interpolation", linestyle="--")
plt.plot(quarter_hour_times, cubic_estimates, label="Cubic Spline", color="green")
plt.xlabel("Hour of Day")
plt.ylabel("Relative Humidity (%)")
plt.title("Foaling Barn Humidity Resampling")
plt.legend()
plt.grid(True)
plt.show()

"""
E. Real-World Application: Foaling Barn Humidity Resampling
Assumptions: An IoT humidity sensor in the horse boarding facility's foaling barn records data every two hours. An automated climate control script requires high-resolution estimates every 15 minutes to adjust ventilation fans smoothly.
Input Data: Bi-hourly time stamps and relative humidity percentage readings.
Output: Estimated humidity values at 11:00 AM using both linear and cubic interpolation, accompanied by a comparison plot.
Interpretation: I adapted this script to handle sensor data resampling for my horse boarding facility's environmental control system. Since the physical sensors log data only once every two hours, interpolation allows me to calculate smooth intermediate estimates every 15 minutes. The cubic spline curve models the gradual fluctuation of moisture throughout the day much more realistically than straight linear segments, preventing abrupt fan adjustments.
"""