from integrators import *
from physics import *
from body import *
from constants import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use("dark_background")

# Function for the animation, updating the data of the position of the bodies and their trails

def update(_):
    vel_verlet_step(bodies, timestep)

    for i in range(len(bodies)):
        # Add new position to trail properties

        xyz_trails[i][0].append(bodies[i].position[0])
        xyz_trails[i][1].append(bodies[i].position[1])
        xyz_trails[i][2].append(bodies[i].position[2])

        # Update properties

        plots[i].set_data([bodies[i].position[0]], [bodies[i].position[1]])
        plots[i].set_3d_properties([bodies[i].position[2]])
        trails[i].set_data(xyz_trails[i][0], xyz_trails[i][1])
        trails[i].set_3d_properties(xyz_trails[i][2])
    return plots + trails

# Graph the positions of the spacecraft with respect to Earth

fig = plt.figure()
# ax = p3.Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
# Set aspect ratio to equal to prevent deformation of expected visualization
ax.set_aspect('equal')
# Style graph transparent
# RGBA tuple: last value = alpha (0 = transparent)
ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
ax.zaxis.pane.set_facecolor((0, 0, 0, 0))
ax.xaxis._axinfo["grid"].update(linewidth=0.1)
ax.yaxis._axinfo["grid"].update(linewidth=0.1)
ax.zaxis._axinfo["grid"].update(linewidth=0.1)

ax.set_xlim3d(-1e11, 1e11)
ax.set_ylim3d(-1e11, 1e11)
ax.set_zlim3d(-1e11, 1e11)
ax.set_title("Sun-Earth-Moon Simulation")

xyz_trails = []

for i in bodies:
    # List of x, y, z values per body
    xyz_trails.append([[i.position[0]], [i.position[1]], [i.position[2]]])

# Static initial plots

plots = []
trails = []

for i in range(len(bodies)):
    plots.append(ax.plot(bodies[i].position[0], bodies[i].position[1], bodies[i].position[2], 'o', color=colors[i])[0])
    trails.append(ax.plot(xyz_trails[i][0], xyz_trails[i][1], xyz_trails[i][2], '-', color=colors[i], alpha=0.5)[0])

# Initiate animation

ani = animation.FuncAnimation(fig, update, interval=20, blit=False, cache_frame_data=False)

plt.show()
