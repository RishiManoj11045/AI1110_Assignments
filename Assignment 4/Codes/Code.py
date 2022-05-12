#NCERT Grade 11 Probability Miscellaneous Exercise Q.2
#Rishi Manoj (CS21BTECH11045)

#This code prints the probability of getting 3 diamonds and 1 spade from a well-shuffled deck of 52 cards.

import math
diamond = math.comb(13,3)
spade = math.comb(13,1)
total_outcome = math.comb(52,4)

Pr = diamond*spade/total_outcome
print("Theoritical Probability = ",Pr)
