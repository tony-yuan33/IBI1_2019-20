# What does this piece of code do?
# Answer: Finds a random prime in [1..100].

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False: # Exits when p == True.
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:
            p=False # There exists i in [2..`sqrt`(n)] such that i divides n

# Finds an n in [1..100] such that it does not have a factor in [2..ceil(sqrt(n))].
# In other words, n is a prime, because if n = ab with a, b > 2, then either a < sqrt(n)
# or b < sqrt(n). Either way, one factor lies in the range [2..sqrt(n)].
     
print(n)
