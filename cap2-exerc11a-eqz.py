from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,y):
    return (((x**2)/4)+((y**2)/2))** 0.5

u = np.linspace(-2,2,10)
v = np.linspace(-2,2,10)
u, v = np.meshgrid(u,v)

x=u
y=v
z=f(u,v)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x,y,z,30)
plt.show()