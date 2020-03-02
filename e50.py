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
import is_prime from is_prime
import listofprimes from listofprimes 

n=1000000

def listofprimes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



# iterator
number = 3

# initial list of primes:
primes = [2]

# create the actual list of primes (lop) less than n:
lop= listofprimes(1000000)

# use numpy.ravel to return a flattened array from n-dimensional array:
lop = np.asarray(lop)

# create series from the listofprimes : 
series = pd.Series(lop) 

# taking the sum of primes:
sop= series.cumsum()
sop.index = np.arange(1, len(sop) + 1)

# ^^ these previous parts use problem 10 to get the sum of primes. 

L= len(lop)
bestd= 0

for i in range(1, L):
    s= 0
    for j in range(i+bestd, L):
        s= sop[j]- sop[i]
        if s> lop[L-1]:        
            break 
        m= []
        m= np.argwhere(lop==s)       # this ~should~ work like the find command in matlab... idk i looked this up
        if len(m)==1:
            d= j-i
            if d> bestd:
                besti= i
                bestj=j
                bestd= d
                bestm= m
E50solution= lop[bestm]
print(E50solution)

# first changed to L-1 because lop index starts at 0 so L[0] is the first term
# then realized to convert to an array to better suit the modules later on,
# especially when indexing, an array is better than a list, cant call/index a list as easily 
