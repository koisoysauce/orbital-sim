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

# TODO: finish other functions and add more plots to energy error, then add momentum error plot
def update(frame):
    euler_step(temp_bodies_euler, timestep)
    RK4_step(temp_bodies_RK4, timestep)
    vel_verlet_step(temp_bodies_verlet, timestep)

    # Add new values
    energy_error_euler.append(total_energy_error(temp_bodies_euler) - E0)
    energy_error_RK4.append(total_energy_error(temp_bodies_RK4) - E0)
    energy_error_verlet.append(total_energy_error(temp_bodies_verlet) - E0)
    timesteps.append(frame + 1)
    
    # Update properties
    energy_error_euler_plot.set_data(timesteps, energy_error_euler)
    energy_error_RK4_plot.set_data(timesteps, energy_error_RK4)
    energy_error_verlet_plot.set_data(timesteps, energy_error_verlet)

    for i in range(len(axs)):
        axs[i].relim()
        axs[i].autoscale_view()
    
    return [energy_error_euler_plot, energy_error_RK4_plot, energy_error_verlet_plot]

# Graph Total Energy Error vs Timestep

fig, axs = plt.subplots(nrows=3, ncols=1, sharex=True)
fig.suptitle("Total Energy Error vs. Timestep")
axs[0].set_title("Euler")
axs[1].set_title("Runge Kutta 4")
axs[2].set_title("Velocity Verlet")
axs[0].set_ylabel("Energy Error (J)")
axs[1].set_ylabel("Energy Error (J)")
axs[2].set_xlabel("timestep")
axs[2].set_ylabel("Energy Error (J)")

# Get initial total energy
E0 = total_energy_error(bodies)

# Get static plot

temp_bodies_euler = [body.copy() for body in bodies]
temp_bodies_RK4 = [body.copy() for body in bodies]
temp_bodies_verlet = [body.copy() for body in bodies]

timesteps = [0]
energy_error_euler = [0]
energy_error_RK4 = [0]
energy_error_verlet = [0]

energy_error_euler_plot, = axs[0].plot(timesteps, energy_error_euler, 'r-', label='euler')
energy_error_RK4_plot, = axs[1].plot(timesteps, energy_error_RK4, 'g-', label='RK4')
energy_error_verlet_plot, = axs[2].plot(timesteps, energy_error_verlet, 'b-', label='verlet')

# Initiate animation
ani = animation.FuncAnimation(fig, update, interval=20, blit=False, cache_frame_data=False)

plt.show()
