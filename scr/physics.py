# We need the acceleration from Newton's Law of Universal Gravitation

from math import *
import numpy as np

def get_accel(body1pos, body2pos, body2mass):
    G = 6.674e-11
    r = body2pos - body1pos # relative to body1
    # r_mag = sqrt((body1.position[0] - body2.position[0]) ** 2 + (body1.position[1] - body2.position[1]) ** 2)
    r_mag = np.linalg.norm(r) # This is more efficient and accurate

    a1 = G * body2mass * r / r_mag ** 3 # Should be towards body2

    return a1 # Return acceleration of first argument with regards to second argument