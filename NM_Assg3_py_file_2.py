import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline, lagrange
import matplotlib as mp

x0 = 0
x1 = 0.6
x2 = 0.9
x_axis = np.array([x0,x1,x2])

y1 = np.array([np.cos(x0),np.cos(x1),np.cos(x2)])

lagrange_1 = lagrange(x_axis, y1)
print (" Value of cos(x) at x = 0.45 by interpolation : ",lagrange_1(0.45))
print(" Absolute Error: ",np.abs(lagrange_1(0.45)-np.cos(0.45)))

y2 = np.array([np.sqrt(1+x0),np.sqrt(1+x1),np.sqrt(1+x2)])

lagrange_2 = lagrange(x_axis, y2)

print (" Value of sqrt(1+x) at x = 0.45 by interpolation : ",lagrange_2(0.45))
print(" Absolute Error: ",np.abs(lagrange_2(0.45)-np.sqrt(1+0.45)))

y3 = np.array([np.log(1+x0),np.log(1+x1),np.log(1+x2)])

lagrange_3 = lagrange(x_axis, y3)

print (" Value of ln(1+x) at x = 0.45 by interpolation : ",lagrange_3(0.45))
print(" Absolute Error: ",np.abs(lagrange_3(0.45)-np.sqrt(1+0.45)))

y4 = np.array([np.tan(x0),np.tan(x1),np.tan(x2)])

lagrange_4 = lagrange(x_axis, y4)

print (" Value of tan(x) at x = 0.45 by interpolation : ",lagrange_4(0.45))
print(" Absolute Error: ",np.abs(lagrange_4(0.45)-np.tan(0.45)))
