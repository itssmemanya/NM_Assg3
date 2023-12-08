import numpy as np
from scipy.integrate import trapezoid, simps, romberg

# Definig given function
def f(x):
    return np.exp(x)

a = 0
b = 1
x_axis = np.linspace(a, b, 100)

# Numerical Integration
trapezoidal = trapezoid(f(x_axis), x_axis)
simpson = simps(f(x_axis), x=x_axis)
rombergf = romberg(f, a, b)

# Printing the results
print(" Trapezoidal Rule : ", trapezoidal)
print(" Simpson's Rule : ", simpson)
print(" Romberg Method :", rombergf)
