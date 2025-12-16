# Orbital Mechanics Simulator

A 2D orbital simulation written in Python that models the motion of a spacecraft  
around a central body using Newton's Law of Universal Gravitation  
and numerical integration methods (Euler and Runge–Kutta 4).

---

## ✨ Features

- 2D gravitational orbital simulation  
- Euler and RK4 numerical integrators  
- Numpy-based vector math  
- Real-time matplotlib animation  
- Adjustable time step and initial conditions  

---

## Physics Model

The simulation is based on Newton’s Law of Universal Gravitation:

a = −GM r / |r|³


where:
- r is the position vector relative to the central body  
- G is the gravitational constant  
- M is the mass of the central body  

The equations of motion are:

dr/dt = v
dv/dt = a(r)


These differential equations are solved with Euler’s method or RK4.

---

### Euler's Method

Euler's method is the simplest method to solving an  
ordinary differential equation (ODE).

This method assumes that the function stays at a constant rate  
for a short step t.

The equation is shown as:

yₙ₊₁ = yₙ + t · f(tₙ, yₙ)


where:
- yₙ is the current value  
- h is the time step size  
- f(tₙ, yₙ) is the derivative at the current point  

Although this method is the simplest, it is not the most accurate.

This is because Euler's method assumes the entire step has the same slope throughout,  
but in reality, the slope is constantly changing.

---

### Runge Kutta 4th-Order Method

The Runge Kutta is an extension of the Euler's Method in which Euler's step  
is the first order of the Runge Kutta Method.

This means that Runge Kutta is more likely to give a more accurate approximation  
of the next value compared to Euler's method.

With this method, we essentially get the slope of the function at the starting point  
and then predict its first value, k1. (First-Order)

We then will get the midpoint of the linear equation found from first-order  
and will get the slope of the function at that point, k2. (Second-Order)

We then again get the midpoint of the linear equation found from second-order  
and get the slope of the function at that point, k3. (Third-Order)

For the fourth-order, we get the slope of the function from the point that we found  
in third-order, k4.

We can then use these slopes to approximate the final point using the average.

Each order that uses a half-step has a weight of 1/3.  
The orders that don't have a weight of 1/6.

After we get the average, we will multiply this by the step and add to the  
initial value to get the approximated value.

The final equation will look like so:

xₙ₊₁ = xₙ + step / 6 · (k1 + 2 · k2 + 2 · k3 + k4)