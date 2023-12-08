import numpy as np
from scipy.integrate import romberg

# Defining given functions
def f1(x):
    return x**2 *np.log(x)
def f2(x):
    return x**2 * np.exp(-x)
def f3(x):
    return np.cos(x)**2

# Numerical Integration
y1 = romberg(f1, 1e-10, 1.5)
y2 = romberg(f2, 0, 1)
y3 = romberg(f3, 0, np.pi/4)

# Printing Results
print(" Results of integration : ")
print(" Function ",' '," Romberg ")
print(" x2 ln(x) ",' ',y1)
print(" x2e−x ",'    ',y2)
print(" (cos x)2 ",' ',y3)
