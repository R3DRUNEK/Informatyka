import numpy as np
import matplotlib.pyplot as plt
import pygame

N = 8
y = np.zeros(N)
x1 = np.linspace(0, 10, N, endpoint=True, retstep=True)
x2 = np.linspace(0, 10, N, endpoint=False, retstep=True)
print(x1)
print(x2)
plt.plot(x1, y, 'o')

plt.plot(x2, y + 0.5, 'o')

plt.ylim([-0.5, 1])

plt.show()



