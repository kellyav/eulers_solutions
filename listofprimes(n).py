import sympy as sp

#my personal code for checking whether a certain value is prime. returns true/ false accordingly.
import is_prime from is_prime

def listofprimes(n): 
        for i in range(2, n + 1): 
            if sp.is_prime(i): 
                print(i)
        return [2] + [i for i in range(2, n+1) if sp.isprime(i)]
