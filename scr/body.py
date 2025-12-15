import numpy as np

class Body:

    # init creates a variable for this class
    def __init__(self, name, mass, radius, position, velocity):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position # This will be in a numpy array [x, y]
        self.velocity = velocity # This will be in a numpy array [vx, vy]
        

# We can get these variables by calling the initialized variable like so
# variable_name.name
# variable_name.mass
# so on

'''Example Use:
earth = Body("Earth", 31.6, np.array([0, 0]), np.array([0, 0]))
spacecraft = Body("Spacecraft", 0,1, np.array([0, 0]), np.array([0, 0]))

print(earth.mass)
print(spacecraft.position)
'''
