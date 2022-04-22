#ICSE 2018 Grade 12 15(b)
#Rishi Manoj (CS21BTECH11045)

#This code prints the the equation of the line parallel to the given line

import numpy as np
import sympy as smp

#direction vector components of the given line
n1 = np.array([3,2,-1])

#direction vector and point vector components of the line parallel to the given line
n = n1
P = np.array([7,-5,0])

print("The equation of the required line is : ")
print(P,"+ lambda",n)
