# this function to check if the given number is prime or not. 
def is_prime(n):
    if n % 2 == 0:
        return False
    else:      
        for i in range(3, int(n**0.5+1),2): 
            if n % i == 0:
                return False
        return True
# iterator
number = 3

# list of primes
primes = [2]
#print(number)




