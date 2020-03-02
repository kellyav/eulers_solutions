# this function to check if the given number is prime or not. retuns True or False accordingly. 
def is_prime(n):
    if n % 2 == 0:
        return False
    else:      
        for i in range(3, int(n**0.5+1),2): 
            if n % i == 0:
                return False
        return True
