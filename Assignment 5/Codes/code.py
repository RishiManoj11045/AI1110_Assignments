import random
import numpy as np
import math

def nCr(n,r):
    f = math.factorial
    return f(n)/(f(r)*f(n-r))

#Number of tosses of a fair coin
N = 3

#Probability of getting no heads
X0 = nCr(N,0)*(1/2)**3

#Probability of getting 1 head
X1 = nCr(N,1)*(1/2)**3

#Probability of getting 2 heads
X2 = nCr(N,2)*(1/2)**3

#Probability of getting 3 heads
X3 = nCr(N,3)*(1/2)**3

#Mean number of heads in three tosses
Mean = 0*X0 + 1*X1 + 2*X2 + 3*X3
print("Mean number of heads in three tosses of a fair coin = ",Mean)
