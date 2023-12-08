import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline, lagrange
import matplotlib.pyplot as plt

# Given data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])
x_axis = np.linspace(0, 5, 100)

# Linear spline
linear_spline = InterpolatedUnivariateSpline(x, y, k=1)
plt.scatter(x, y, label='Data Points')
plt.plot(x_axis, linear_spline(x_axis), label='Linear Spline')
plt.legend()
plt.title('Linear Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Quadratic spline
quadratic_spline = InterpolatedUnivariateSpline(x, y, k=2)
plt.scatter(x, y, label='Data Points')
plt.plot(x_axis, quadratic_spline(x_axis), label='Quadratic Spline')
plt.legend()
plt.title('Quadratic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Cubic spline
cubic_spline = InterpolatedUnivariateSpline(x, y, k=3)
plt.scatter(x, y, label='Data Points')
plt.plot(x_axis, cubic_spline(x_axis), label='Cubic Spline')
plt.legend()
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Lagrange polynomial of degree 5
lagrange_polynomial = lagrange(x, y)
plt.scatter(x, y, label='Data Points')
plt.plot(x_axis, lagrange_polynomial(x_axis), label='Lagrange Polynomial')
plt.legend()
plt.title('Lagrange Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Plotting all of them together to compare
plt.scatter(x, y, label='Data Points')
plt.plot(x_axis, lagrange_polynomial(x_axis), label='Lagrange Polynomial')
plt.plot(x_axis, linear_spline(x_axis), label='Linear Spline')
plt.plot(x_axis, quadratic_spline(x_axis), label='Quadratic Spline')
plt.plot(x_axis, cubic_spline(x_axis), label='Cubic Spline')
plt.legend()
plt.title('Lagrange Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
