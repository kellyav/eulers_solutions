def combination(n, r):
    if n == r or r == 0: return(1) 
    return (factorial(n))/(factorial(r)*factorial(n-r))
count = 0
for i in range(2, 101):
    for j in range(2, i):
        if combination(i, j) > 1000000:
            count+=1
