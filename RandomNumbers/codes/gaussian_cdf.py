import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import mpmath

def Q(z):
	return (1-mpmath.erf(z /math.sqrt(2) ) )/2

pts = 50

n = 10**6
randvar = np.loadtxt('gau.dat',dtype='double')
x = np.linspace(-6,6,pts)
F = [] 
for i in range(0,pts):
	Fcount = np.count_nonzero(randvar < x[i]) 
	F.append(Fcount/n) 

p = []
for i in range(0,pts-1):
	p.append( (F[i+1] - F[i])/ (x[i+1]-x[i]) )
	
p_theory = []
for i in range(0,pts):
	p_theory.append(math.exp(-(x[i]**2)/2) / math.sqrt(2*math.pi))	


#Method1: cumulative
#dx = (x[pts-1]-x[0])/(pts-1)
#F_theory = [p_theory[0]]
#for i in range(1,pts):
#	F_theory.append( F_theory[i-1] + p_theory[i] * dx )

#Method2: using library
#F_theory = np.cumsum(p_theory)* dx

#Method3: using Q and error function
F_theory = []
for i in range(0,pts): 
	F_theory.append( 1-Q(x[i]) )		#for mean =0 and variance = 1
plt.scatter(x.T, F, color="blue",label="Empirical CDF" )   #plotting the empirical CDF
plt.plot(x.T, F_theory, color="orange", label="Theoretical CDF" ) #plotting the experimental CDF
plt.grid()
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.title("Theoretical CDF of X")
plt.legend(loc="best")
print(p)
plt.show()
