# Euler's Problem 50:

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that
# adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?


# import pandas and numpy modules 
import pandas as pd
import numpy as np
import listofprimes from listofprimes
import is_prime from is_prime 
import E10 from e10

# this solution uses e10.py to get the sum of primes, as well as my listofprimes(n) function
lop= listofprimes(n)
sop= E10(n)
L= len(lop)
bestd= 0

for i in range(1, L):
    s= 0
    for j in range(i+bestd, L):
        s= sop[j]- sop[i]
        if s> lop[L-1]:        
            break 
        m= []
        m= np.argwhere(lop==s)
        if len(m)==1:
            d= j-i
            if d> bestd:
                besti= i
                bestj=j
                bestd= d
                bestm= m

E50solution= lop[bestm]
print(E50solution)
