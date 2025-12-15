from integrators import *
from physics import *
from body import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

# We need two bodies, one representing a planet and the other representing an object in orbit

planet = Body("Earth", 5.97 * 10 ** 24, 6.371 * 10 ** 6, np.array([0, 0]), np.array([0, 0]))
spacecraft = Body("Spacecraft", 100, 50, np.array([7e6, 0.0]), np.array([0.0, 7800.0]))

# Now we can graph the positions of the spacecraft with respect to Earth

plt.figure()
plt.axis("equal")
plt.title("2 Body Orbital")
plt.xlim(-1e8, 1e8)
plt.ylim(-1e7, 1e7)

# We need to get an array of the x and y positions

x_pos = [spacecraft.position[0]]
y_pos = [spacecraft.position[1]]

# Plot the earth as a dot and craft as undecided as we will animate it's movement

plt.plot(0, 0, 'bo')
craft_plot, = plt.plot([], [], 'ro') # The position of the craft
trail_plot, = plt.plot([], [], 'r-', alpha = 0.5) # The trail that the craft leaves
x_trail = []
y_trail = []

tstep = 10
# while abs(x_pos[0] - x_pos[-1]) > 0.01 and abs(y_pos[0] - y_pos[-1]) > 0.01: # Fix this so that it accounts for only one element
for i in range(5000):
    euler_step(planet, spacecraft, tstep)
    
    # Now we will work on the plotting

    x_trail.append(spacecraft.position[0])
    y_trail.append(spacecraft.position[1])

    craft_plot.set_data([spacecraft.position[0]], [spacecraft.position[1]])
    trail_plot.set_data(x_trail, y_trail)

    plt.pause(0.001) # Pauses each frame for 0.001 seconds

plt.show()