# Project Euler #2 
# find the sum of the even-valued terms (below 4 million) from the fibonacci sequence.
    # the next term in a fibonacci sequence is created by adding up the two numbers before it

# initialize variables:
x= 1
y= 1
z= 0
evensum= 0

while z < 4000000:
    # definition of fibonacci:
    z= (x + y)

    # sum only includes the even numbers:
    if z%2 == 0:
        evensum= evensum + z
    
    # assigns x to y, and y to z:
    x= y
    y= z

print(evensum)