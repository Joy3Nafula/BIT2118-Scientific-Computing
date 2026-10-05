import numpy as np

# Adjacency matrix for a backend microservices communication graph.
# Node order: API Gateway, Auth Service, Database, Redis Cache
# A '1.' indicates a bidirectional communication channel between the services.
A_services = np.array([
    [0., 1., 1., 1.],  # API Gateway talks to Auth, DB, Cache
    [1., 0., 1., 0.],  # Auth Service talks to API Gateway, DB
    [1., 1., 0., 1.],  # Database talks to API Gateway, Auth, Cache
    [1., 0., 1., 0.]   # Redis Cache talks to API Gateway, DB
])

eigenvalues, eigenvectors = np.linalg.eig(A_services)

# Isolate the dominant eigenvalue/eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

# Normalize to get a clean percentage/fraction for influence
centrality = dominant_vector / dominant_vector.sum()
services = ["API Gateway", "Auth Service", "Database", "Redis Cache"]

print("Microservice Criticality Scores:")
for service, score in zip(services, centrality):
    print(f"{service}: {score:.4f}")

"""
E. Real-World Application: Microservice Bottleneck Identification
Assumptions: A backend system consists of four microservices. The matrix maps which services constantly query one another. 
Input Data: A 4x4 adjacency matrix representing the communication channels between the API Gateway, Auth Service, Database, and Redis Cache.
Output: An eigenvector-based centrality score for each microservice.
Interpretation: I adapted this script to analyze the communication bottlenecks in my backend microservice architecture. By calculating the dominant eigenvector of the service adjacency matrix, I can mathematically pinpoint which microservice acts as the most critical central hub. The output shows that the API Gateway and the Database have the highest centrality scores (the highest traffic interconnectivity), clearly indicating that these specific nodes require the most robust load balancing and redundancy to prevent a single point of failure.
"""