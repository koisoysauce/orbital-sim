from body import *
import numpy as np
from math import *

'''Equal mass'''
# Earth mass: 5.97e24kg; radius: 6.371e6km
# body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, -7800.0, 0]))
# body2 = Body("Earth", 5.97e24, 6.371e6, np.array([5e6, 0, 0]), np.array([0.0, 7800.0, 2600.0]))

'''Earth and satellite'''
body1 = Body("Earth", 5.97e24, 6.371e6, np.array([0, 0, 0]), np.array([0, 0, 0]))
body2 = Body("Satellite", 100, 50, np.array([7e6, 0, 0]), np.array([0, sqrt(7800.0 ** 2 / 2), sqrt(7800 ** 2 / 2)]))

bodies = [body1, body2]
colors = ['b', 'r']

'''Our Solar System'''
# body1 = Body("Sun", 1.989e30, 7.0e8, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0]))
# body2 = Body("Earth", 5.97e24, 6.371e6, np.array([1.5e11, 0.0, 0.0]), np.array([0.0, 3.0e4, 0.0]))
# body3 = Body("Moon", 7.35e22, 1.737e6, np.array([1.5e11 + 3.84e8, 0.0, 0.0]), np.array([0.0, 3.0e4 + 1.0e3, 0.0]))

# bodies = [body1, body2, body3]
# colors = ['y', 'b', 'r']

timestep = 1000
