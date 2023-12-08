from scipy.optimize import newton
import numpy as np

def f(x):
    return np.sin(np.cos(np.exp(x)))

def derivative(x):
    return -np.exp(x) * np.sin(np.exp(x)) * np.cos(np.cos(np.exp(x)))

root_1 = newton(f, -1, fprime=derivative)

root_2 = newton(f, -0.1, fprime=derivative)

root_3 = newton(f,-0.1)

print(f" Root with initial guess -1 : {root_1}")
print(f" Root with initial guess -0.1 : {root_2}")
print(f" Root with initial guess -0.1 with secant method : {root_3}")
