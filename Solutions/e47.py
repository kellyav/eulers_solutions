# Euler problem 47.     https://projecteuler.net/problem=47

# The first two consecutive numbers to have two distinct prime factors are:
# 14= 2 × 7
# 15= 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:
# 644= 2² × 7 × 23
# 645= 3 × 5 × 43
# 646= 2 × 17 × 19.

# Question:
    #Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


Limit= 150000;         # can change this, limits the number of numbers to check
factors= [0]*Limit;
count= 0
for i in range(2,Limit):
    if factors[i]==0:       # aka if i is prime,
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print(i-3)          # print the first number
            break
    else:
        count = 0

#print(factors, '\n')    # prints the entire list of factors
#print(factors[i],'\n')   
#print('this is i: ', i)

# works! yay
#The first four numbers that have four distinct prime factors are located in the array as: 134043,134044, 134045 and 134046
