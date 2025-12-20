# N-Body Orbital Simulator

A Python simulation that models the motion of multiple bodies under gravity using Newton's Law of Universal Gravitation  
and numerical integration methods (Euler and Runge–Kutta 4). Supports 2 or more interacting bodies.

---

## ✨ Features

- N-body gravitational simulation (arbitrary number of bodies)  
- Euler and Runge–Kutta 4 numerical integrators  
- Numpy-based vector math for efficient calculations  
- Real-time 3D matplotlib animation  
- Customizable initial positions, velocities, and masses  
- Trails visualize the orbits of each body  

---

## Physics Model

The simulation is based on Newton’s Law of Universal Gravitation:

a = −GM r / |r|³

where:
- r is the position vector relative to another body  
- G is the gravitational constant  
- M is the mass of the influencing body  

The equations of motion are:

dr/dt = v  
dv/dt = a(r)

These differential equations are solved with Euler’s method or RK4 for each body.

---

### Euler's Method

Euler's method updates positions and velocities incrementally:

yₙ₊₁ = yₙ + step · f(tₙ, yₙ)

Although this method is simple, it can be inaccurate for highly elliptical or multi-body orbits.

---

### Runge Kutta 4th-Order Method

RK4 improves accuracy by sampling slopes at multiple points within a time step:

xₙ₊₁ = xₙ + step / 6 · (k1 + 2·k2 + 2·k3 + k4)

This method reduces error for complex orbits and multiple interacting bodies.