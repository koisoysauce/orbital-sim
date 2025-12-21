from integrators import *
from physics import *
from body import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use("dark_background")

'''Equal mass'''
# Earth mass: 5.97e24kg; radius: 6.371e6km
# body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, -7800.0, 0]))
# body2 = Body("Earth", 5.97e24, 6.371e6, np.array([5e6, 0, 0]), np.array([0.0, 7800.0, 2600.0]))

'''Earth and satellite'''
# body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, 0, 0]))
# body2 = Body("Satellite", 100, 50, np.array([7e6, 0, 0]), np.array([0, 7800.0, 7800]))

# bodies = [body1, body2]
# colors = ['b', 'r']

'''Our Solar System'''
body1 = Body("Sun", 1.989e30, 7e8, np.array([0, 0, 0]), np.array([0, 0, 0]))
body2 = Body("Earth", 5.97e24, 6.371e6, np.array([1.5e11, 0, 0]), np.array([0, 3e4, 0]))
body3 = Body("Moon", 7.35e22, 1.737e6, np.array([1.5e11 + 3.84e8, 0, 0]), np.array([0, 3e4 + 1e3, 0]))

bodies = [body1, body2, body3]
colors = ['y', 'b', 'r']

# Function for the animation, updating the data of the position of the bodies and their trails

def update(_):
    RK4_step(bodies, tstep)

    # body1_x_trail.append(body1.position[0])
    # body1_y_trail.append(body1.position[1])
    # body1_z_trail.append(body1.position[2])

    # body2_x_trail.append(body2.position[0])
    # body2_y_trail.append(body2.position[1])
    # body2_z_trail.append(body2.position[2])

    # body1_plot.set_data([body1.position[0]], [body1.position[1]])
    # body1_plot.set_3d_properties([body1.position[2]])
    # body1_trail.set_data(body1_x_trail, body1_y_trail)
    # body1_trail.set_3d_properties(body1_z_trail)

    # body2_plot.set_data([body2.position[0]], [body2.position[1]])
    # body2_plot.set_3d_properties([body2.position[2]])
    # body2_trail.set_data(body2_x_trail, body2_y_trail)
    # body2_trail.set_3d_properties(body2_z_trail)

    # return (body1_plot, body2_plot, body1_trail, body2_trail)
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

ax.set_xlim3d(-1e12, 1e12)
ax.set_ylim3d(-1e12, 1e12)
ax.set_zlim3d(-1e12, 1e12)
ax.set_title("Sun-Earth-Moon Simulation")
# ax.set_xlim3d(-2e7, 2e7)
# ax.set_ylim3d(-2e7, 2e7)
# ax.set_zlim3d(-2e7, 2e7)
# ax.set_title("2 Body Orbital")

# List of data that will be updating per frame

# body1_x_trail = [body1.position[0]]
# body1_y_trail = [body1.position[1]]
# body1_z_trail = [body1.position[2]]

# body2_x_trail = [body2.position[0]]
# body2_y_trail = [body2.position[1]]
# body2_z_trail = [body2.position[2]]
xyz_trails = []

for i in bodies:
    # List of x, y, z values per body
    xyz_trails.append([[i.position[0]], [i.position[1]], [i.position[2]]])

# Static initial plots

# body1_plot, = ax.plot(body1.position[0], body1.position[1], body1.position[2], 'bo')
# body1_trail, = ax.plot(body1_x_trail, body1_y_trail, body1_z_trail, 'b-')

# body2_plot, = ax.plot(body2.position[0], body2.position[1], body2.position[2], 'ro')
# body2_trail, = ax.plot(body2_x_trail, body2_y_trail, body2_z_trail, 'r-')
plots = []
trails = []

for i in range(len(bodies)):
    plots.append(ax.plot(bodies[i].position[0], bodies[i].position[1], bodies[i].position[2], 'o', color=colors[i])[0])
    trails.append(ax.plot(xyz_trails[i][0], xyz_trails[i][1], xyz_trails[i][2], '-', color=colors[i], alpha=0.5)[0])

# Initiate animation

tstep = 10000
ani = animation.FuncAnimation(fig, update, interval=20, blit=False, cache_frame_data=False)

plt.show()
