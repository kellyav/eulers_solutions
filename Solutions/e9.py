# Euler problem 9.     https://projecteuler.net/problem=9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
    # For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a +b +c =1000.

    # Find the product abc.


# note that since a+b+c=1000,    
    # If c >500, then a+b > c doesn't hold. 
    # If c <334 and b > a, then c > b doesn't hold
# => 500 > c > 334  

for a in range(1,333):
    for b in range(a,499):
        c= (a*a+ b*b)**.5       
        if a+b+c==1000:
            solution= a*b*c
            print('The solution to Eulers problem 9: ', solution)

