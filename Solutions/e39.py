# Euler Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
    # {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

initial= 0 
solution= [initial]*1000
for a in range(1,333):
    for b in range(a,499): 
        c_squared= a*a + b*b
        c= int((a*a + b*b)**.5)
        p= a+b+c
        if not p< 1000:   # aka if p >= 1000, limits the amount of p's that are checked to be under the given interval
            break
        if c*c == c_squared:     # is c fits the (pythagorean) conditions, then add it to the solution list. 
            solution[p] += 1
            
# use python's built in function for finding the position of a maximum element: M.index(max(M))
maxsolution= (solution.index(max(solution)))

print('Value of p where the number of solutions maximized at is', maxsolution)
# this is the position in the array [solutions] where the maximum value is (and the answer to the problem).
