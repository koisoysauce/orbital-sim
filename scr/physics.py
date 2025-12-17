# We need the acceleration from Newton's Law of Universal Gravitation

from math import *
import numpy as np

# def get_accel(bodyL, bodyS_pos):
#     G = 6.674 * 10 ** -11
#     mu = G * bodyL.mass
    
#     r = bodyS_pos - bodyL.position
#     r_mag = np.linalg.norm(r) # just pythag theorem to get distance

#     return - mu * r / r_mag ** 3

# TODO: use body2_pos as a checker if there is addition to it with the use of the RK4 method
def get_accel(body1, body2):
    G = 6.674e-11
    r = body2.position - body1.position # relative to body1
    # r_mag = sqrt((body1.position[0] - body2.position[0]) ** 2 + (body1.position[1] - body2.position[1]) ** 2)
    r_mag = np.linalg.norm(r) # This is more efficient and accurate

    a1 = G * body2.mass * r / r_mag ** 3 # Should be towards body2
    # a2 = G * body1.mass * (-r) / r_mag ** 3 # Should be towards body1

    return a1