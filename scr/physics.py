from math import *
import numpy as np

# # Acceleration from Newton's Law of Universal Gravitation

# get_accel will take in 2 numpy arrays of equal length

# The position of the elements in positions and masses is equal 
# to the position of the elements in the bodies

def get_accels(positions, masses):
    G = 6.674e-11 # Gravitational Constant
    accels = np.zeros((len(positions), 3))
    total = 0 # This will be the calculated total acceleration per body
    for i in range(len(positions)):
        for n in range(len(positions)):
            if i != n:
                r = positions[n] - positions[i]
                r_mag = np.linalg.norm(r)
                total += G * masses[n] * r / r_mag ** 3
        accels[i] = total
        total = 0
    return accels
