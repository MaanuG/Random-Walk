import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Number of steps in the random walk
num_steps = 500

# Generate random steps: -1 or 1 for x, y, and z directions
steps = np.random.choice([-1, 1], size=(num_steps, 3))

# Compute the cumulative sum to get the walk path
walk = np.cumsum(steps, axis=0)

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Random Walk Animation')

# Setting the axis limits
max_range = np.max(np.abs(walk)) + 5
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_zlim(-max_range, max_range)

# Initialize an empty line that will be updated
line, = ax.plot([], [], [], lw=2, color='blue', alpha=0.7)
start_point = ax.scatter([0], [0], [0], color='red', s=100, label="Start")  # Start marker
end_point = ax.scatter([], [], [], color='green', s=100, label="End")  # End marker

# Function to update the animation
def update(num):
    # Update the line data
    line.set_data(walk[:num, 0], walk[:num, 1])
    line.set_3d_properties(walk[:num, 2])

    # Move the end marker
    end_point._offsets3d = ([walk[num-1, 0]], [walk[num-1, 1]], [walk[num-1, 2]])

    return line, end_point

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=30, blit=False)

# Show the plot
plt.legend()
plt.show()
