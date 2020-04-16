# Euler problem 53

#How many, not necessarily distinct, values of (n r) (n choose r)
#for 1≤ n ≤100, are greater than one-million?

import time
tStart = time.time()

def factorial(x):
    if x<0: 
        print("Factorial doesn't exist for negative numbers!")
    elif x == 0:
        return 1
    else:
        return x*factorial(x-1)


def combination(n, r):
    if n == r or r == 0: return(1) 
    return (factorial(n))/(factorial(r)*factorial(n-r))
count = 0
for i in range(2, 101):
    for j in range(2, i):
        if combination(i, j) > 1000000:
            count+=1

print("The solution is", count)
print('Run Time was: ' + str(time.time() - tStart))
