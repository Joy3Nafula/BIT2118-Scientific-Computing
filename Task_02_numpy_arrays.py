import numpy as np

# 24 hourly barn temperature readings in degrees Celsius
barn_temps_c = np.array([
    14.5, 14.2, 13.8, 13.5, 14.0, 15.5,
    17.0, 19.5, 21.0, 22.5, 24.0, 24.5,
    25.2, 25.0, 24.1, 22.8, 21.0, 19.5,
    18.2, 17.0, 16.1, 15.5, 15.0, 14.8
])

mean_barn = np.mean(barn_temps_c)
min_barn = np.min(barn_temps_c)
max_barn = np.max(barn_temps_c)

# Vectorized operation to find absolute deviation from ideal 20.0 C
deviation_from_ideal = np.abs(barn_temps_c - 20.0)

print(f"Daily mean barn temperature: {mean_barn:.2f} C")
print(f"Minimum barn temperature: {min_barn:.2f} C")
print(f"Maximum barn temperature: {max_barn:.2f} C")
print("Hourly deviation from ideal 20C (first six hours):", np.round(deviation_from_ideal[:6], 2))