import numpy as np

# Bounding box coordinates for a Toyota Land Cruiser Prado J250 detection
# Format: [x, y] corners from a computer vision model
prado_bbox = np.array([
    [10.0, 10.0],  # Bottom-left
    [40.0, 10.0],  # Bottom-right
    [40.0, 25.0],  # Top-right
    [10.0, 25.0]   # Top-left
])

# The camera perspective tilted slightly, requiring a 10-degree correction
correction_angle = np.deg2rad(10)
rotation = np.array([
    [np.cos(correction_angle), -np.sin(correction_angle)],
    [np.sin(correction_angle),  np.cos(correction_angle)]
])

# The vehicle moved closer, requiring a 1.2x scale increase on both axes
scale = np.array([
    [1.2, 0.0],
    [0.0, 1.2]
])

transformation = rotation @ scale
adjusted_bbox = prado_bbox @ transformation.T

print("Original Prado Bounding Box:\n", prado_bbox)
print("Adjusted Bounding Box:\n", np.round(adjusted_bbox, 2))
print("Area Scaling Factor (Determinant):", np.round(np.linalg.det(transformation), 2))

"""
E. Real-World Application: Object Detection Bounding Box Transformation
Assumptions: An autonomous driving computer vision model has drawn a bounding box around a Toyota Land Cruiser Prado J250. The camera experiences a 10-degree tilt and the vehicle moves 20% closer in the next frame.
Input Data: A 4x2 matrix representing the x,y coordinates of the vehicle's bounding box.
Output: The updated bounding box coordinates after applying the perspective rotation and scaling transformation matrices.
Interpretation: I constructed this script to simulate how machine learning pipelines adjust spatial data. By combining a 10-degree rotation matrix with a 1.2x uniform scaling matrix, I successfully computed the new pixel coordinates for the vehicle's bounding box in a single vectorized matrix multiplication step. The determinant of 1.44 confirms the new bounding box area is exactly 1.44 times larger than the original.
"""