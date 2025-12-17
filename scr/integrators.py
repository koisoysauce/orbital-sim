from physics import *
import numpy as np

# Euler's method will return the next velocity and position values (not completely accurate)
# This method has a lot more trouble with ellipses that are not circles
def euler_step(body1, body2, step):
    # bodyS.position = bodyS.position + step * bodyS.velocity
    # bodyS.velocity = bodyS.velocity + step * get_accel(bodyL, bodyS)

    # Update positions
    body1.position = body1.position + step * body1.velocity
    body2.position = body2.position + step * body2.velocity

    # Update velocities
    body1.velocity = body1.velocity + step * get_accel(body1, body2)
    body2.velocity = body2.velocity + step * get_accel(body2, body1)

# Implement RK4 Method

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
