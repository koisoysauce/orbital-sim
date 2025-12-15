# We need the acceleration from Newton's Law of Universal Gravitation

from math import *
import numpy as np

def get_accel(bodyL, bodyS_pos):
    G = 6.674 * 10 ** -11
    mu = G * bodyL.mass
    
    r = bodyS_pos - bodyL.position
    r_mag = np.linalg.norm(r) # just pythag theorem to get distance

    return - mu * r / r_mag ** 3