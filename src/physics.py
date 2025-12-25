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

def total_energy(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])
    G = 6.674e-11 # Gravitational Constant

    K = 0
    U = 0
    for i in range(len(bodies)):
        K += 0.5 * masses[i] * np.linalg.norm(velocities[i]) ** 2
        for n in range(len(bodies)):
            if i < n:
                r = positions[i] - positions[n]
                r_mag = np.linalg.norm(r)

                U += -G * masses[i] * masses[n] / r_mag
    E = K + U
    
    return E

# angular momentum in magnitude for the momentum vs. time graph
# Assume all bodies are rotating about the center (0, 0, 0)
def total_angular_momentum(bodies):
    positions = np.array([body.position for body in bodies])
    velocities = np.array([body.velocity for body in bodies])
    masses = np.array([body.mass for body in bodies])

    L = 0
    for i in range(len(bodies)):
        L += np.cross(positions[i], masses[i] * velocities[i])

    return np.linalg.norm(L)
# def total_angular_momentum(bodies):
#     L_total = np.array([0.0, 0.0, 0.0])  # start as 3D vector
#     for body in bodies:
#         L_total += np.cross(body.position, body.velocity * body.mass)
#     return np.linalg.norm(L_total)