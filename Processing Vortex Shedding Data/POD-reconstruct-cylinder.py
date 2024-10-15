import numpy as np

# Assume modes is a matrix of size (Nx*Ny, num_modes) where each column is a POD mode
# Assume data_matrix is a matrix of size (Nx*Ny, T) where each column is a snapshot in time
# Assume temporal_coefficients is a matrix of size (num_modes, T)

# Reconstructing the flow field
reconstructed_data = np.dot(modes, temporal_coefficients)

# To compare against original:
error = np.linalg.norm(data_matrix - reconstructed_data) / np.linalg.norm(data_matrix)
print(f"Reconstruction error: {error:.5f}")


# Select only the first k most energetic modes
k = 5  # For example, keep the first 5 modes
reconstructed_data_approx = np.dot(modes[:, :k], temporal_coefficients[:k, :])

# Compute approximation error
approx_error = np.linalg.norm(data_matrix - reconstructed_data_approx) / np.linalg.norm(data_matrix)
print(f"Approximate reconstruction error with {k} modes: {approx_error:.5f}")


