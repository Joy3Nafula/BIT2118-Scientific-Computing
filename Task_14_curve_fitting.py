import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Deep learning inference batch sizes and measured latency (milliseconds)
batch_sizes = np.array([1, 4, 8, 16, 32, 64, 128], dtype=float)
inference_latency_ms = np.array([12.0, 18.5, 29.0, 48.0, 85.0, 155.0, 290.0], dtype=float)

# Quadratic model for batch processing latency scaling
def latency_model(x, a, b, c):
    return a * x**2 + b * x + c

parameters, covariance = curve_fit(latency_model, batch_sizes, inference_latency_ms)
a, b, c = parameters
predicted_latency = latency_model(batch_sizes, a, b, c)
rmse = np.sqrt(np.mean((inference_latency_ms - predicted_latency) ** 2))

print(f"Fitted Model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted latency at batch size 256: {latency_model(256, a, b, c):.2f} ms")

x_plot = np.linspace(batch_sizes.min(), 256, 300)
plt.scatter(batch_sizes, inference_latency_ms, label="Measured Inference Latency")
plt.plot(x_plot, latency_model(x_plot, a, b, c), label="Fitted Curve", color="orange")
plt.xlabel("Deep Learning Batch Size")
plt.ylabel("Latency (ms)")
plt.title("ML Model Inference Latency Curve Fitting")
plt.legend()
plt.grid(True)
plt.show()

"""
E. Real-World Application: Machine Learning Model Inference Latency Fitting
Assumptions: An MLOps pipeline evaluates deep learning model inference latency across various batch sizes. As the batch size increases, hardware utilization changes, leading to a non-linear scaling of processing time.
Input Data: An array of batch sizes and their corresponding experimentally measured inference latencies in milliseconds.
Output: The fitted quadratic equation, the root-mean-square error of the approximation, a prediction for a batch size of 256, and a comparison plot.
Interpretation: I adapted this script to model how my machine learning model performance scales under different batch configurations. The curve fitting output successfully generates a predictive formula mapping batch size to inference latency. This allows me to mathematically balance throughput against latency requirements in production deployment pipelines.
"""