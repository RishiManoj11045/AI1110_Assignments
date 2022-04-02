#To find the term that is to be subtracted from the given polynomial
#to make it divisible by another polynomial

import numpy as np
import sympy as smp
from sympy import poly,roots
from sympy.abc import x

#input parameter

px = 16*x**3-8*x**2+4*x+7
dx = 2*x+1

#output

qx,rx = smp.div(px,dx)

#rx is the required one that is to be subtracted from the given polynomial(px)
#so that another polynomial(dx) is a factor of the resulting polynomial after subtraction
print(qx,",",rx)
