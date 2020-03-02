# Euler's Problem 10:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

# import pandas and numpy modules 
import pandas as pd 
import numpy as np

def E10(n):
    lop= listofprimes(n)
    L= len(lop)
    series = pd.Series(lop) 

# taking the (cummulative) sum of primes:
    sop= series.cumsum()    
    sop.index = np.arange(1, len(sop) + 1)
    
    solution= sop[L]
    return solution


#euler 10 timing:
import time
n= 2000000

t9= time.time()
sumofprimesbelown= E10(n)
print('Sum of all the primes below n is: ', sumofprimesbelown, ', which is the solution for this problem.')
elapsed9 = time.time() - t9
print('This is how long the function takes to run: ', elapsed9,'\n')
