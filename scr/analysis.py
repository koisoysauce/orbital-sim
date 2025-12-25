import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from constants import *
from integrators import *
from physics import *
plt.style.use("dark_background")

'''Energy plot'''
def update_energy(frame):
    euler_step(temp_bodies_euler, timestep)
    RK4_step(temp_bodies_RK4, timestep)
    vel_verlet_step(temp_bodies_verlet, timestep)

    # Add new values
    energy_error_euler.append(total_energy(temp_bodies_euler) - E0)
    energy_error_RK4.append(total_energy(temp_bodies_RK4) - E0)
    energy_error_verlet.append(total_energy(temp_bodies_verlet) - E0)
    timesteps.append(frame + 1)
    
    # Update properties
    energy_error_euler_plot.set_data(timesteps, energy_error_euler)
    energy_error_RK4_plot.set_data(timesteps, energy_error_RK4)
    energy_error_verlet_plot.set_data(timesteps, energy_error_verlet)

    for i in range(len(axs_energy)):
        axs_energy[i].relim()
        axs_energy[i].autoscale_view()
    
    return [energy_error_euler_plot, energy_error_RK4_plot, energy_error_verlet_plot]

# Graph Total Energy Error vs Timestep

fig_energy, axs_energy = plt.subplots(nrows=3, ncols=1, sharex=True)
fig_energy.suptitle("Total Energy Error vs. Timestep")
axs_energy[0].set_title("Symplectic Euler")
axs_energy[1].set_title("Runge Kutta 4")
axs_energy[2].set_title("Velocity Verlet")
axs_energy[0].set_ylabel("Energy Error (J)")
axs_energy[1].set_ylabel("Energy Error (J)")
axs_energy[2].set_xlabel("timestep")
axs_energy[2].set_ylabel("Energy Error (J)")

# Get initial total energy
E0 = total_energy(bodies)

# Get static plot

temp_bodies_euler = [body.copy() for body in bodies]
temp_bodies_RK4 = [body.copy() for body in bodies]
temp_bodies_verlet = [body.copy() for body in bodies]

timesteps = [0]
energy_error_euler = [0]
energy_error_RK4 = [0]
energy_error_verlet = [0]

energy_error_euler_plot, = axs_energy[0].plot(timesteps, energy_error_euler, 'r-', label='euler')
energy_error_RK4_plot, = axs_energy[1].plot(timesteps, energy_error_RK4, 'g-', label='RK4')
energy_error_verlet_plot, = axs_energy[2].plot(timesteps, energy_error_verlet, 'b-', label='verlet')

# Initiate animation
ani_energy = animation.FuncAnimation(fig_energy, update_energy, interval=20, blit=False, cache_frame_data=False)

plt.show()

'''Angular Momentum Plot'''
def update_momentum(frame):
    euler_step(temp_bodies_euler, timestep)
    RK4_step(temp_bodies_RK4, timestep)
    vel_verlet_step(temp_bodies_verlet, timestep)

    timesteps.append(frame + 1)
    momentum_error_euler.append(total_angular_momentum(temp_bodies_euler) - L0)
    momentum_error_RK4.append(total_angular_momentum(temp_bodies_RK4) - L0)
    momentum_error_verlet.append(total_angular_momentum(temp_bodies_verlet) - L0)

    # Update properties
    momentum_error_euler_plot.set_data(timesteps, momentum_error_euler)
    momentum_error_RK4_plot.set_data(timesteps, momentum_error_RK4)
    momentum_error_verlet_plot.set_data(timesteps, momentum_error_verlet)

    for i in range(len(axs_momentum)):
        axs_momentum[i].relim()
        axs_momentum[i].autoscale_view()

    return [momentum_error_euler_plot, momentum_error_RK4_plot, momentum_error_verlet_plot]

# Graph Total Angular Momentum vs. timestep
fig_momentum, axs_momentum = plt.subplots(nrows=3, ncols=1, sharex=True)
fig_momentum.suptitle("Total Angular Momentum Error vs. Timestep")
axs_momentum[0].set_title("Symplectic Euler")
axs_momentum[1].set_title("Runge Kutta 4")
axs_momentum[2].set_title("Velocity Verlet")
axs_momentum[1].set_ylabel("Angular Momentum Error (kgm²/s)")
axs_momentum[2].set_xlabel("timestep")

# Get initial angular momentum
L0 = total_angular_momentum(bodies)

# Get static plot

temp_bodies_euler = [body.copy() for body in bodies]
temp_bodies_RK4 = [body.copy() for body in bodies]
temp_bodies_verlet = [body.copy() for body in bodies]

timesteps = [0]
momentum_error_euler = [0]
momentum_error_RK4 = [0]
momentum_error_verlet = [0]

momentum_error_euler_plot, = axs_momentum[0].plot(timesteps, momentum_error_euler, 'r-', label='euler')
momentum_error_RK4_plot, = axs_momentum[1].plot(timesteps, momentum_error_RK4, 'g-', label='RK4')
momentum_error_verlet_plot, = axs_momentum[2].plot(timesteps, momentum_error_verlet, 'b-', label='verlet')

# Initiate animation
ani_momentum = animation.FuncAnimation(fig_momentum, update_momentum, interval=20, blit=False, cache_frame_data=False)

plt.show()
