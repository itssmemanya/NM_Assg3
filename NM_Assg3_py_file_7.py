import numpy as np
from scipy.integrate import trapezoid, simps, romberg

# Defining given functions
def f1(x):
    return x*np.log(x)
def f2(x):
    return 2/(4+x**2)
def f3(x):
    return np.tan(x)

# Numerical Integration
x1 = np.linspace(1,2,4)
y1 = trapezoid(f1(x1),x1)
z1 = simps(f1(x1),x1) 

x2 = np.linspace(0,2,6)
y2 = trapezoid(f2(x2),x2)
z2 = simps(f2(x2),x2)

x3 = np.linspace(0,3*np.pi/8,8)
y3 = trapezoid(f3(x3),x3)
z3 = simps(f3(x3),x=x3)

# Printing Results
print(" Results of integration with given conditions : ")
print(" Function ",'    '," Trapezoidal ",'     '," Simpsons ")
print(" x ln(x) ",'   ',y1,' ',z1)
print(" 2/(4+x^2) ",' ',y2,' ',z2)
print(" tan(x) ",'    ',y3,' ',z3)
