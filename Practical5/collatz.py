n = 27
while n != 1: # Exits upon first encounter of n == 1.
    if n & 1: # n odd
        n = 3 * n + 1
    else: # n even
        n >>= 1 # div 2
    print(n) # Output n for this round of transformation.