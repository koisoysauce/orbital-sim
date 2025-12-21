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
def euler_step(bodies, step):
    accels = get_accel_N(bodies)
    for i in range(len(bodies)):
        # Update velocities
        bodies[i].velocity = bodies[i].velocity + step * accels[i]

        # Update positions
        bodies[i].position = bodies[i].position + step * bodies[i].velocity

# Implement RK4 Method

def RK4_step(bodies, step):
    # # k1
    # k1v_b1 = get_accel(body1.position, body2.position, body2.mass)
    # k1v_b2 = get_accel(body2.position, body1.position, body1.mass)

    # k1x_b1 = body1.velocity
    # k1x_b2 = body2.velocity

    # pos_k1v_b1 = body1.position + step / 2 * k1x_b1
    # pos_k1v_b2 = body2.position + step / 2 * k1x_b2

    # # k2
    # k2v_b1 = get_accel(pos_k1v_b1, pos_k1v_b2, body2.mass)
    # k2v_b2 = get_accel(pos_k1v_b2, pos_k1v_b1, body1.mass)

    # k2x_b1 = body1.velocity + step / 2 * k1v_b1
    # k2x_b2 = body2.velocity + step / 2 * k1v_b2

    # pos_k2v_b1 = body1.position + step / 2 * k2x_b1
    # pos_k2v_b2 = body2.position + step / 2 * k2x_b2

    # # k3
    # k3v_b1 = get_accel(pos_k2v_b1, pos_k2v_b2, body2.mass)
    # k3v_b2 = get_accel(pos_k2v_b2, pos_k2v_b1, body1.mass)

    # k3x_b1 = body1.velocity + step / 2 * k2v_b1
    # k3x_b2 = body2.velocity + step / 2 * k2v_b2

    # pos_k3v_b1 = body1.position + step * k3x_b1
    # pos_k3v_b2 = body2.position + step * k3x_b2

    # # k4
    # k4v_b1 = get_accel(pos_k3v_b1, pos_k3v_b2, body2.mass)
    # k4v_b2 = get_accel(pos_k3v_b2, pos_k3v_b1, body1.mass)

    # k4x_b1 = body1.velocity + step * k3v_b1
    # k4x_b2 = body2.velocity + step * k3v_b2
    k1x = []
    k2x = []
    k3x = []
    k4x = []

    k1v = []
    k2v = []
    k3v = []
    k4v = []

    # make another variable to modify positions for new accelerations
    bodies_mod = []
    for i in bodies:
        bodies_mod.append(Body(i.name, i.mass, i.radius, i.position.copy(), i.velocity.copy()))

    # k1
    for i in range(len(bodies)):
        k1v.append(get_accel_N(bodies_mod)[i])
        k1x.append(bodies[i].velocity)
        
    # Update all positions
    for i in range(len(bodies)):
        bodies_mod[i].position = bodies[i].position + step / 2 * k1x[i]

    # k2
    for i in range(len(bodies)):
        k2v.append(get_accel_N(bodies_mod)[i])
        k2x.append(bodies[i].velocity + step / 2 * k1v[i])

    # Update positions
    for i in range(len(bodies)):
        bodies_mod[i].position = bodies[i].position + step / 2 * k2x[i]

    # k3
    for i in range(len(bodies)):
        k3v.append(get_accel_N(bodies_mod)[i])
        k3x.append(bodies[i].velocity + step / 2 * k2v[i])

    # Update positions
    for i in range(len(bodies)):
        bodies_mod[i].position = bodies[i].position + step / 2 * k3x[i]

    # k4
    for i in range(len(bodies)):
        k4v.append(get_accel_N(bodies_mod)[i])
        k4x.append(bodies[i].velocity + step * k3v[i])

    # # Update velocities and positions
    # body1.velocity = body1.velocity + step / 6 * (k1v_b1 + 2 * k2v_b1 + 2 * k3v_b1 + k4v_b1)
    # body2.velocity = body2.velocity + step / 6 * (k1v_b2 + 2 * k2v_b2 + 2 * k3v_b2 + k4v_b2)
    # body1.position = body1.position + step / 6 * (k1x_b1 + 2 * k2x_b1 + 2 * k3x_b1 + k4x_b1)
    # body2.position = body2.position + step / 6 * (k1x_b2 + 2 * k2x_b2 + 2 * k3x_b2 + k4x_b2)
    for i in range(len(bodies)):
        bodies[i].velocity = bodies[i].velocity + step / 6 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i])
        bodies[i].position = bodies[i].position + step / 6 * (k1x[i] + 2 * k2x[i] + 2 * k3x[i] + k4x[i])

# TODO: Learn Symplectic Integrators (Leapfrog, Verlet)
