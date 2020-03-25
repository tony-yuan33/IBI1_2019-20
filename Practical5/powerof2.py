x = 2019
k = 0
li = [] # Contains all terms to be displayed.

while x > 0:
    while not(x & 1): # Remove trailing zeros.
        x >>= 1
        k += 1
    li.append('2**' + str(k)) # Append new term
    x >>= 1
    k += 1

li.reverse()
print(' + '.join(li))