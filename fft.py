import matplotlib.pyplot as plt
from matplotlib.pylab import plot
import numpy as np
import math

x = np.zeros(100)
for i in range(100):
    x[i] = math.sin(i / 50 * 2 * math.pi)

q = np.arange(0, 100, 1)
plt.subplot(3, 1, 1)
plot(q)

plt.subplot(3, 1, 2)
plot(x)

def fourier(n, x):
    sum = math.fsum([(x[i] * math.sin(2 * math.pi * i)) for i in range(100) ])
    f = sum / (2.0 * math.pi)
    return f

h = [ ( fourier(i, x) ) for i in range(100)]

plt.subplot(3, 1, 3)
plot(h)

plt.show()
