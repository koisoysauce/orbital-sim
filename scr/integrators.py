from physics import *
import numpy as np

# Euler's method will return the next velocity and position values (not completely accurate)
# This method has a lot more trouble with ellipses that are not circles
def euler_step(bodyL, bodyS, step):
    bodyS.position = bodyS.position + step * bodyS.velocity
    bodyS.velocity = bodyS.velocity + step * get_accel(bodyL, bodyS.position)

# Implement RK4 Method

'''Runge Kutta 4th Order Method Explained'''

# The Runge Kutta is an extension of the Euler's Method
# in which Euler's step is the first order of the Runge Kutta Method.
# This means that Runge Kutta is more likely to give a more accurate approximation 
# of the next value compared to Euler's method

# With this method, we essentially get the slope of the function at the starting point and then predict its first value, k1. (First-Order)
# We then will get the midpoint of the linear equation found from first-order and will get the slope of the function at that point, k2. (Second-Order)
# We then again get the midpoint of the linear equation found from second-order and gets the slope of the function at that point, k3. (Third-Order)
# For the fourth-order, we get the slope of the function from the point that we found in third-order, k4.

# We can then use these slopes to approximate the final point using the average
# Each order that uses a half-step has a weight of 1/3
# The orders that don't have a weight of 1/6
# After we get the average, we will multiply this by the step and add to the initial value to get the approximated value.

# The final equation will look like so:
# x_{n + 1} = x_{n} + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

def RK4_step(bodyL, bodyS, step):
    # k1
    k1x = bodyS.velocity
    k1v = get_accel(bodyL, bodyS.position)

    # k2
    k2x = bodyS.velocity + step / 2 * k1v
    k2v = get_accel(bodyL, bodyS.position + step / 2 * k1x) 
    #   Utilizing k1x here because position is a factor in acceleration, not velocity
    
    # k3
    k3x = bodyS.velocity + step / 2 * k2v
    k3v = get_accel(bodyL, bodyS.position + step / 2 * k2x)

    # k4
    k4x = bodyS.velocity + step * k3v
    k4v = get_accel(bodyL, bodyS.position + step * k3x)

    bodyS.position += step / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
    bodyS.velocity += step / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)

