from integrators import *
from physics import *
from body import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
plt.style.use("dark_background")

# Two bodies

'''Equal mass'''
# Earth mass: 5.97e24kg; radius: 6.371e6km
# body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, -7800.0, 0]))
# body2 = Body("Earth", 5.97e24, 6.371e6, np.array([5e6, 0, 0]), np.array([0.0, 7800.0, 2600.0]))

'''Earth and satellite'''
body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, 0, 0]))
body2 = Body("Satellite", 100, 50, np.array([5e6, 0, 0]), np.array([0, 7800.0, 7800]))

# Function for the animation, updating the data of the position of the bodies and their trails

def update(_):
    RK4_step(body1, body2, tstep)

    body1_x_trail.append(body1.position[0])
    body1_y_trail.append(body1.position[1])
    body1_z_trail.append(body1.position[2])

    body2_x_trail.append(body2.position[0])
    body2_y_trail.append(body2.position[1])
    body2_z_trail.append(body2.position[2])

    body1_plot.set_data([body1.position[0]], [body1.position[1]])
    body1_plot.set_3d_properties([body1.position[2]])
    body1_trail.set_data(body1_x_trail, body1_y_trail)
    body1_trail.set_3d_properties(body1_z_trail)

    body2_plot.set_data([body2.position[0]], [body2.position[1]])
    body2_plot.set_3d_properties([body2.position[2]])
    body2_trail.set_data(body2_x_trail, body2_y_trail)
    body2_trail.set_3d_properties(body2_z_trail)

    return (body1_plot, body2_plot, body1_trail, body2_trail)

# Graph the positions of the spacecraft with respect to Earth

fig = plt.figure()
# ax = p3.Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
# Style graph transparent
# RGBA tuple: last value = alpha (0 = transparent)
ax.xaxis.pane.set_facecolor((0, 0, 0, 0))
ax.yaxis.pane.set_facecolor((0, 0, 0, 0))
ax.zaxis.pane.set_facecolor((0, 0, 0, 0))
ax.xaxis._axinfo["grid"].update(linewidth=0.1)
ax.yaxis._axinfo["grid"].update(linewidth=0.1)
ax.zaxis._axinfo["grid"].update(linewidth=0.1)

# ax.set_xlim3d(-1e8, 1e8)
# ax.set_ylim3d(-1e8, 1e8)
# ax.set_zlim3d(-1e8, 1e8)
ax.set_xlim3d(-2e7, 2e7)
ax.set_ylim3d(-2e7, 2e7)
ax.set_zlim3d(-2e7, 2e7)
ax.set_title("2 Body Orbital")

# List of data that will be updating per frame

body1_x_trail = [body1.position[0]]
body1_y_trail = [body1.position[1]]
body1_z_trail = [body1.position[2]]

body2_x_trail = [body2.position[0]]
body2_y_trail = [body2.position[1]]
body2_z_trail = [body2.position[2]]

# Static initial plots

body1_plot, = ax.plot(body1.position[0], body1.position[1], body1.position[2], 'bo')
body1_trail, = ax.plot(body1_x_trail, body1_y_trail, body1_z_trail, 'b-')

body2_plot, = ax.plot(body2.position[0], body2.position[1], body2.position[2], 'ro')
body2_trail, = ax.plot(body2_x_trail, body2_y_trail, body2_z_trail, 'r-')

# Initiate animation

tstep = 10
ani = animation.FuncAnimation(fig, update, interval=20, blit=False, cache_frame_data=False)

plt.show()
# # plt.figure()
# # ax.axis("equal")
# ax.set_title("2 Body Orbital")
# ax.set_xlim(-1e8, 1e8)
# ax.set_ylim(-1e7, 1e7)
# ax.set_zlim(-1e7, 1e7)
# ax.axis("equal")

# # Plot both bodies as undecided to animate it's movement

# body1_plot, = ax.plot([], [], [], 'bo')
# body1_trail, = ax.plot([], [], [], 'b-', alpha=0.5)
# body2_plot, = ax.plot([], [], [], 'ro')
# body2_trail, = ax.plot([], [], [], 'r-', alpha=0.5)

# body1_x_trail = []
# body1_y_trail = []
# body1_z_trail = []
# body2_x_trail = []
# body2_y_trail = []
# body2_z_trail = []

# tstep = 50

# while True:
#     RK4_step(body1, body2, tstep)
    
#     # Now we will work on the plotting

#     body1_x_trail.append(body1.position[0])
#     body1_y_trail.append(body1.position[1])
#     body1_z_trail.append(body1.position[2])

#     body2_x_trail.append(body2.position[0])
#     body2_y_trail.append(body2.position[1])
#     body2_z_trail.append(body2.position[2])

#     body1_plot.set_data([body1.position[0]], [body1.position[1]])
#     body1_plot.set_3d_properties([body1.position[2]])
#     body1_trail.set_data(body1_x_trail, body1_y_trail)
#     body1_trail.set_3d_properties(body1_z_trail)

#     body2_plot.set_data([body2.position[0]], [body2.position[1]])
#     body2_plot.set_3d_properties([body2.position[2]])
#     body2_trail.set_data(body2_x_trail, body2_y_trail)
#     body2_trail.set_3d_properties(body2_z_trail)

#     plt.pause(0.001) # Pauses each frame for 0.001 seconds
