from math import sqrt
from turtle import color
import numpy as np
import math
import matplotlib.pyplot as plt

plt.figure()

def miA(x):
    if x > 15:
        eq = 1+((x-15)**(-2))
        uA = 1/eq
    else:
        uA = 0
        
    return uA

def miB(x):
    eq = 1+((x-17)**4)
    uB = 1/eq
    return uB


d = 14
x = np.zeros((100))
y = np.zeros((100))
z = np.zeros((100))


# create data
for i in range(0,100):
    y[i] = miA(d)
    z[i] = miB(d)
    x[i] = d
    d = d + 0.1

#x = [12,13,14,15,16,17,18,19,20,21]
#y = [miA(12),miA(13),miA(14),miA(15),miA(16),miA(17),miA(18),miA(19),miA(20),miA(21)]

#z = [miB(12),miB(13),miB(14),miB(15),miB(16),miB(17),miB(18),miB(19),miB(20),miB(21)]
  
# plot line
plt.plot(x,y)
plt.plot(x,z)
plt.grid()
plt.show()