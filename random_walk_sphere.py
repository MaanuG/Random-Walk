import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define spherical coordinates for the base sphere
theta = np.linspace(0, 2 * np.pi, 60)  # More longitude lines
phi = np.linspace(0, np.pi, 30)  # More latitude lines
theta, phi = np.meshgrid(theta, phi)

# Convert to Cartesian coordinates for the sphere
r = 1  # Sphere radius
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Create a random walk on the sphere
num_steps = 200  # Number of steps in the random walk
theta_walk = np.cumsum(np.random.uniform(-0.2, 0.2, num_steps))  # Small random changes in longitude
phi_walk = np.cumsum(np.random.uniform(-0.1, 0.1, num_steps))  # Small random changes in latitude
phi_walk = np.clip(phi_walk, 0, np.pi)  # Ensure phi stays within valid range

# Convert random walk to Cartesian coordinates
x_walk = r * np.sin(phi_walk) * np.cos(theta_walk)
y_walk = r * np.sin(phi_walk) * np.sin(theta_walk)
z_walk = r * np.cos(phi_walk)

# Create a 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere (with transparent fill and a wireframe grid)
ax.plot_surface(x, y, z, color='gray', alpha=0.3, edgecolor='none')
ax.plot_wireframe(x, y, z, color='black', linewidth=0.4)

# Initialize the random walk path (starting at a point)
line, = ax.plot([0], [0], [0], color='red', linewidth=2, label="Random Walk")

# Set limits for better visualization
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Remove background, grid, and axis lines
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()

# Initialization function: plot the background
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Animation function: update the random walk path
def update(num):
    # Update the data of the line plot with the current walk
    line.set_data(x_walk[:num], y_walk[:num])
    line.set_3d_properties(z_walk[:num])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, init_func=init, interval=50, blit=False)

# Show the plot with the animation
plt.legend()
plt.show()
