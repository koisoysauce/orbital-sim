from math import *
import numpy as np

# Acceleration from Newton's Law of Universal Gravitation

def get_accel(body1pos, body2pos, body2mass):
    G = 6.674e-11
    r = body2pos - body1pos # relative to body1
    # r_mag = sqrt((body1.position[0] - body2.position[0]) ** 2 + (body1.position[1] - body2.position[1]) ** 2 + (body1.position[2] - body2.position[2]) ** 2)
    eps = 1e-3  # small softening length for numerical safety
    r_mag = np.linalg.norm(r) + eps # This is more efficient and accurate

    a1 = G * body2mass * r / r_mag ** 3 # Should be towards body2

    return a1 # Return acceleration of first argument with regards to second argument

# Net accelerations from N bodies

def get_accel_N(bodies):
    accels = []
    total = np.zeros(3)
    # I need to go through all bodies for each body to get their respective accelerations
    for i in bodies:
        for n in bodies:
            if not i is n:
                total += get_accel(i.position, n.position, n.mass)
        accels.append(total)
        total = np.zeros(3)
    return accels
