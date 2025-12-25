import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constants import *
from integrators import *
from physics import *
plt.style.use("dark_background")

# Functions calculate y-values by step
# TODO: fix calculations because they are probably wrong
def total_energy_error(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])
    G = 6.674e-11 # Gravitational Constant

    E = 0
    # # Get total kinetic energy
    # E += np.sum(0.5 * masses * velocities ** 2)
    # Get total gravitational energy
    for i in range(len(bodies)):
        E += 0.5 * masses[i] * np.linalg.norm(velocities[i]) ** 2
        for n in range(len(bodies)):
            if i != n:
                r = np.linalg.norm(positions[i] - positions[n])
                E -= G * masses[i] * masses[n] / r
    
    return E

def angular_momentum_error(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])

    L = 0

    for i in range(len(bodies)):
        for n in range(len(bodies)):
            if i != n:
                r = positions[i] - positions[n]
                L += r * masses[i] * velocities[i]

    return L

# def radial_distance(bodies):
#     return

# def update(_):
    
#     return
# TODO: finish other functions and add more plots to energy error, then add momentum error plot
def update_euler(frame):
    vel_verlet_step(bodies, timestep)

    # Add new values
    energy_error.append(total_energy_error(bodies) - E0)
    timesteps.append(frame + 1)
    
    # Update properties
    energy_error_plot.set_data(timesteps, energy_error)

    ax.relim()
    ax.autoscale_view()
    
    return [energy_error_plot]

def update_RK4(_):
    return

def update_verlet(_):
    return

# Graph Total Energy Error vs Timestep

fig, ax = plt.subplots()

# Get initial total energy
E0 = total_energy_error(bodies)

# Get static plot

timesteps = [0]
energy_error = [0]

energy_error_plot = ax.plot(timesteps, energy_error, 'r-')[0]

# Initiate animation
ani = animation.FuncAnimation(fig, update_euler, interval=20, blit=False, cache_frame_data=False)

plt.show()
