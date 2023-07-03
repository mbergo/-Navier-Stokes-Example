# Import necessary libraries
import numpy as np

# Function to calculate the velocity field
def calculate_velocities(density, viscosity, length, pressure_gradient):
    # Define parameters
    num_points = 10  # Number of points in the tube
    delta_x = length / (num_points - 1)  # Spacing between points

    # Initialize velocity array
    velocities = np.zeros(num_points)

    # Calculate velocities at each point
    for i in range(num_points):
        # Calculate fluid density
        fluid_density = calculate_density(i)

        # Calculate fluid viscosity
        fluid_viscosity = calculate_viscosity(i)

        # Calculate velocity at point i using the Navier-Stokes equation
        delta_p = pressure_gradient * i * delta_x
        numerator = delta_p
        denominator = 2 * fluid_density * fluid_viscosity
        velocity = numerator / denominator
        velocities[i] = velocity

    return velocities

# Function to calculate fluid density
def calculate_density(i):
    # Simple example: constant density
    constant_density = 1.2  # Constant fluid density (e.g., air)
    return constant_density

# Function to calculate fluid viscosity
def calculate_viscosity(i):
    # Simple example: constant viscosity
    constant_viscosity = 0.001  # Constant fluid viscosity (e.g., air)
    return constant_viscosity

# Inputs required:
tube_length = 1.0  # Length of the tube in meters
pressure_gradient = 10.0  # Pressure gradient applied along the tube

# Calculate the velocity field
velocity_field = calculate_velocities(tube_length, pressure_gradient)

# Print results
print("Velocity Field:")
for i, velocity in enumerate(velocity_field):
    print("Point", i, ":", velocity, "m/s")

