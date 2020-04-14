# Euler Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import is_prime from is_prime

# initialize the list of primes to include 2
primes = [2]
val = 3
primefactors=[]

n = 600851475143
while val < n:
    is_prime = True
    for p in primes:
        if val % p == 0:
            is_prime = False
            val += 2
    if is_prime:
        primes.append(val)
        if n % val == 0:
            n /= val
            primefactors.append(val) 
print('This is the largest prime factor of 600851475143:', val, '\n which is the solution to Eulers problem 3. \n')
#print('These are the other prime factors of 600851475143: ',primefactors)
