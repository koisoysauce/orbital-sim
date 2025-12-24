from physics import *
from body import *

# Euler's method will return the next velocity and position values (not completely accurate)

# This method follows the symplectic method, where we change the velocity first to ensure
# that the body orbiting stays on track of the ideal orbit

def euler_step(bodies, step):
    positions = np.array([body.position for body in bodies])
    masses = np.array([body.mass for body in bodies])
    accels = get_accels(positions, masses)

    for i in range(len(bodies)):
        # Update velocities
        bodies[i].velocity += step * accels[i]

        # Update positions
        bodies[i].position += step * bodies[i].velocity

# RK4 Method

# This method is more accurate at calculating the next position and velocity
# than the euler method. 
# However, this method cannot follow the symplectic method, so it cannot
# ensure that the body stays within the ideal orbit through a long period of time.

def RK4_step(bodies, step):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])

    k1v = get_accels(positions, masses)
    k1r = velocities

    k2v = get_accels(positions + step / 2 * k1r, masses)
    k2r = velocities + step / 2 * k1v

    k3v = get_accels(positions + step / 2 * k2r, masses)
    k3r = velocities + step / 2 * k2v

    k4v = get_accels(positions + step * k3r, masses)
    k4r = velocities + step * k3v

    new_positions = positions + step / 6 * (k1r + 2 * k2r + 2 * k3r + k4r)
    new_velocities = velocities + step / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)

    for i in range(len(bodies)):
        bodies[i].position = new_positions[i]
        bodies[i].velocity = new_velocities[i]

# TODO: Learn Symplectic Integrators (Leapfrog, Verlet, Yoshida 4th order)

# Velocity Verlet Method

def vel_verlet_step(bodies, step):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])
    accels = get_accels(positions, masses)

    new_positions = positions + velocities * step + 0.5 * accels * step ** 2
    new_accels = get_accels(new_positions, masses)
    new_velocities = velocities + 0.5 * (accels + new_accels) * step

    for i in range(len(bodies)):
        bodies[i].position = new_positions[i]
        bodies[i].velocity = new_velocities[i]
