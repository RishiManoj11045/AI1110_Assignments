#NCERT Grade 10 Probability Exercise 15.1 Q.17
#Rishi Manoj (CS21BTECH11045)

#This code prints randomn probabilities of drawing a defective, drawing a non-defective bulb.

import numpy as np
from numpy import linalg as LA
from numpy import random as RN 

#Total number of Students.
#Sample size
N = 20

#Generating Events
#X=0 represents number of defective bulbs.
#X=1 represents number of non-defective bulbs.
x = RN.randint(0, high = 2, size=N)

#Finding 0's obtained from above step.
obt_0 = np.count_nonzero(x==0)

#After one non-defective is removed.
#Now the sample size is N-1.
#Finding 1's obtained.
obt_1 = np.count_nonzero(x==1)-1

print("Randomn Probabilities:", obt_0/N, obt_1/(N-1))


