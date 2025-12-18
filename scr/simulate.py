from integrators import *
from physics import *
from body import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

# We need two bodies, one representing a planet and the other representing an object in orbit

# Earth mass: 5.97e24kg; radius: 6.371e6km

'''Equal mass'''
body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0]), np.array([0, -7800.0]))
body2 = Body("Earth", 5.97e24, 6.371e6, np.array([5e6, 0.0]), np.array([0.0, 7800.0]))

'''Earth and satellite'''
# body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0]), np.array([0, 0]))
# body2 = Body("Satellite", 100, 50, np.array([5e6, 0]), np.array([0, 7800.0]))

# Now we can graph the positions of the spacecraft with respect to Earth

plt.figure()
plt.axis("equal")
plt.title("2 Body Orbital")
plt.xlim(-1e8, 1e8)
plt.ylim(-1e7, 1e7)

# Plot both bodies as undecided to animate it's movement

body1_plot, = plt.plot([], [], 'bo')
body1_trail, = plt.plot([], [], 'b-', alpha=0.5)
body2_plot, = plt.plot([], [], 'ro')
body2_trail, = plt.plot([], [], 'r-', alpha=0.5)

body1_x_trail = []
body1_y_trail = []
body2_x_trail = []
body2_y_trail = []

# plt.plot(0, 0, 'bo')
# craft_plot, = plt.plot([], [], 'ro') # The position of the craft
# trail_plot, = plt.plot([], [], 'r-', alpha = 0.5) # The trail that the craft leaves
# x_trail = []
# y_trail = []

tstep = 50
# while abs(x_pos[0] - x_pos[-1]) > 0.01 and abs(y_pos[0] - y_pos[-1]) > 0.01: # Fix this so that it accounts for only one element
while True:
    RK4_step(body1, body2, tstep)
    
    # Now we will work on the plotting

    body1_x_trail.append(body1.position[0])
    body1_y_trail.append(body1.position[1])
    body2_x_trail.append(body2.position[0])
    body2_y_trail.append(body2.position[1])

    body1_plot.set_data([body1.position[0]], [body1.position[1]])
    body1_trail.set_data(body1_x_trail, body1_y_trail)
    body2_plot.set_data([body2.position[0]], [body2.position[1]])
    body2_trail.set_data(body2_x_trail, body2_y_trail)

    plt.pause(0.001) # Pauses each frame for 0.001 seconds
