from physics import *
import numpy as np

# This method will return the next velocity and position values (not completely accurate)
# This method has a lot more trouble with ellipses that are not circles
def euler_step(bodyL, bodyS, step):
    bodyS.position = bodyS.position + step * bodyS.velocity
    bodyS.velocity = bodyS.velocity + step * get_accel(bodyL, bodyS)

# Try implementing a different ODE solving method later like RK4
