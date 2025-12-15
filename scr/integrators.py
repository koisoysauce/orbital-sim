from physics import *
import numpy as np

# This method will return the next velocity and position values (not completely accurate)
# This method has a lot more trouble with ellipses that are not circles
def euler_step(bodyL, bodyS, step):
    bodyS.position = bodyS.position + step * bodyS.velocity
    bodyS.velocity = bodyS.velocity + step * get_accel(bodyL, bodyS.position)

# Implement RK4 Method
# TODO: Fix RK4 Method, not perfect
def RK4_step(bodyL, bodyS, step):
    # Update the velocity
    k1v = get_accel(bodyL, bodyS.position)
    k2v = get_accel(bodyL, bodyS.position + step / 2 * k1v)
    k3v = get_accel(bodyL, bodyS.position + step / 2 * k2v)
    k4v = get_accel(bodyL, bodyS.position + step * k3v)
    dv = step / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)

    # Update the position
    k1x = bodyS.velocity
    k2x = bodyS.velocity + 1 / 2 * dv
    k3x = bodyS.velocity + 1 / 2 * dv
    k4x = bodyS.velocity + 1 * dv
    bodyS.position += step / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
    bodyS.velocity += dv
