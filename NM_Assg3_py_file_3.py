from scipy.optimize import bisect
import numpy as np

def f(x):
    return np.sin(np.cos(np.exp(x)))

a, b = -1, 1

root = bisect(f, a, b)

value = f(root)

print(f" Root : {root}")
print(f" Value at Root : {value}")
