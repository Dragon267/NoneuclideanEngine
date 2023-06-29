import math
import matplotlib.pyplot as plt
import numpy as np

def show_sphere(ax, radius, num_points):
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, np.pi, num_points)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='red', alpha=0.3)

def convert_to_sphere(x, y):
    xx = math.cos(y) * math.cos(x)
    yy = math.sin(y) * math.cos(x)
    zz = math.sin(x)
    return [xx, yy, zz]

def get_points():
    data = open("logs/points.txt", 'r').read().split("\n")
    points = []
    for line in data:
        try:
            x = float(line.split(" ")[0])
            y = float(line.split(" ")[1])
            print(f"Point: {x}, {y}")
            points.append(
                    convert_to_sphere(x,y)
            )
        except:
            continue
    print(f"Points size: {len(points)}")
    return np.array(points)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Read initial points from file
points = get_points()

# Initialize plot
scatter_plot = ax.scatter([], [], [])

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Dynamic 3D Scatter Plot')

# Function to update the plot
def update_plot():
    try:
        show_sphere(ax, 0.95, 10)
        # Read current points from file
        new_points = get_points()

        # Update scatter plot data
        scatter_plot._offsets3d = ([], [], [])  # Clear previous data
        scatter_plot._offsets3d = (new_points[:, 0], new_points[:, 1], new_points[:, 2])

        # Update plot limits if necessary
        ax.autoscale_view()

        # Redraw the plot
        fig.canvas.draw()
    except:
        return

# Update and redraw the plot in a loop
while True:
    update_plot()
    plt.pause(1)  # Pause for 1 second before updating again
