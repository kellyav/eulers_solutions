def factorial(x):
    if x<0: 
        print("Factorial doesn't exist for negative numbers!")
    elif x == 0:
        return 1
    else:
        return x*factorial(x-1)
