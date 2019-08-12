import numpy as np
from numpy import pi
n = 100
N = 100
a = np.zeros(n)
b = np.linspace(-10, 10, n)

c = 4 * np.sin(b) + 5 * np.sin(2 * b)

for i in range(n):
    d = np.sin(b * 2 * pi * i)
    a[i] = np.sum(d)


for i in range(n):
    if(abs(a[i]) > 0.1):
        print(i, a[i])