from physics import *
from body import *

# Euler's method will return the next velocity and position values (not completely accurate)
# This method has a lot more trouble with ellipses that are not circles
# def euler_step(body1, body2, step):

#     # Update velocities
#     body1.velocity = body1.velocity + step * get_accel(body1.position, body2.position, body2.mass)
#     body2.velocity = body2.velocity + step * get_accel(body2.position, body1.position, body1.mass)

#     # Update positions
#     body1.position = body1.position + step * body1.velocity
#     body2.position = body2.position + step * body2.velocity
# def euler_step(bodies, step):
#     accels = get_accel_N(bodies)
#     for i in range(len(bodies)):
#         # Update velocities
#         bodies[i].velocity = bodies[i].velocity + step * accels[i]

#         # Update positions
#         bodies[i].position = bodies[i].position + step * bodies[i].velocity
def euler_step(bodies, step):
    positions = np.array([body.position for body in bodies])
    masses = np.array([body.mass for body in bodies])
    accels = get_accels(positions, masses)

    for i in range(len(bodies)):
        # Update velocities
        bodies[i].velocity += step * accels[i]

        # Update positions
        bodies[i].position += step * bodies[i].velocity

# Implement RK4 Method

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

# TODO: Learn Symplectic Integrators (Leapfrog, Verlet)
