import sympy as sp
x = sp.Symbol('x')
print(sp.diff(3*x**2+1,x))

from scipy.misc import derivative
def f(x):
    return 3*x**2+1
def d(x):
    return derivative(f,x)
    
print(d(2.0))
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
y= np.linspace(-3,3)
plt.plot(y, f(y))
plt.plot(y,d (y))