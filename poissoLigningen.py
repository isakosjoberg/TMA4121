"""
@author: Isak Olav Sjøberg

"""
import numpy as np
from matplotlib import pyplot as plt

Nx, Ny = 100, 100
radius = 0.4  


x = np.linspace(-0.5, 0.5, Nx)
y = np.linspace(-0.5, 0.5, Ny)
R = np.sqrt(x**2 + y**2) 

f = np.zeros((Ny, Nx))
f[Ny//2, Nx//2] = 1e5 

f[R > radius] = 0  


u = np.zeros((Ny, Nx))

for it in range(5000):
    u_old = u.copy() #u.copy() er en måte å kopiere ett array på, veldig nttig. Her f.eks får vi da hele tiden det gamle arrayet slik at vi hele tiden får lagret det.
    u[1:-1, 1:-1] = 0.25 * (u_old[1:-1, 2:] + u_old[1:-1, :-2] + u_old[2:, 1:-1] + u_old[:-2, 1:-1] - f[1:-1, 1:-1])
 
fig = plt.figure(dpi=150)
ax = fig.add_subplot()
contour = ax.contourf(x, y, u, 50, cmap='viridis')
fig.colorbar(contour)
ax.set_title('Elektrostatisk potensialfordeling i et sirkulært område')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.axis('equal')
plt.show()
