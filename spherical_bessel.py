import numpy as np
from scipy.special import spherical_jn
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
x, y = np.meshgrid(x,y)

r= np.sqrt(x**2 + y**2)
z = spherical_jn(0,r)

fig = plt.figure('Spherical Bessel')
ax = fig.add_subplot(111, projection = '3d')
h = ax.plot_surface(x,y,z, cmap = "jet", edgecolor = 'k')
plt.colorbar(h)

ax.set_xlabel('X', fontweight='bold', fontsize= 14)
ax.set_ylabel('Y', fontweight='bold', fontsize=14)
ax.set_zlabel('Z', fontweight='bold', fontsize=14)

ax.set_title('Spherical Bessel', fontweight = 'bold', fontsize=16)
plt.show()