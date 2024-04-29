from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.random.normal(size=500)
y = np.random.normal(size=500)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Computa los histogramas
hist, xedges, yedges = np.histogram2d(x, y, bins=20, range=[[-3, 3], [-3, 3]])

# Construye las coordenadas x, y para los cubos
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construye el arreglo para alturas
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, 0.5, 0.5, dz, zsort='average')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Frecuencia')

plt.show()
