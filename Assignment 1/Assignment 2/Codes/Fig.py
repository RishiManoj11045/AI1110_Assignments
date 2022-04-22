#ICSE 2018 Grade 12 15(b)
#Rishi Manoj (CS21BTECH11045)

#This code plots the given line and the required parallel line along with the point on it.

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mpl
import numpy as np

#Components of given line
xl = np.linspace(-10,10,num=500)
yl = (2*xl-4)/3
zl = (2*xl-8)/-6

#Components of required line parallel to the given line
xm = np.linspace(-10,10,num=500)
ym = (2*xm-29)/3
zm = (2*xm-14)/-6

#Point on the required line
xp = 7
yp = -5
zp = 0

#3D plot of the two lines
fig = plt.figure()
plt3d = plt.axes(projection='3d')
plt3d.scatter(xp, yp, zp)
plt3d.plot(xl, yl, zl, color = "b", label = "$2x-3=3y+1=5-6z$")
plt3d.plot(xm, ym, zm, color = "g", label = "$2x-14=3y+15=-6z$")
plt3d.text(7.3,-4.7,-0.3,"(7,-5,0)")
plt3d.set_xlabel('$x$')
plt3d.set_ylabel('$y$')
plt3d.set_zlabel('$z$')
plt.legend(loc='best')

plt.show()
