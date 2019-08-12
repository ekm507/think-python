"""
python code for calculating fourier series

"""

import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
T = 20 * pi
n = 10000
b = np.linspace(0, T, n)

f = 2 * np.sin(b) + 3 * np.sin(2 * b) - 6 * np.cos(10 * b)

"""
f = b
for i in range(n):
    if(i % 50000 == 2500):
        f[i] = 5
    else:
        f[i] = -5
"""
N = 30
ffs = np.zeros(N)
ffc = np.zeros(N)

dt = T / n

#I don't know why, but when I put this in, it works!!
fuck = 10

for i in range(N):
    co = i * 2.0 * pi / T * fuck # seriously why the hell?!
    s = np.sin(co * b)
    c = np.cos(co * b)
    ffs[i] = 2.0 / T * np.sum(f * s) * dt
    ffc[i] = 2.0 / T * np.sum(f * c) * dt

plt.subplot(3, 1, 1)
plt.plot(ffs)
plt.subplot(3, 1, 2)
plt.plot(ffc)
plt.subplot(3, 1, 3)
plt.plot(f)
plt.show()

