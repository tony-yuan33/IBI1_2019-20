n = 27
while n != 1:
    if n & 1:
        n = 3 * n + 1
    else:
        n >>= 1
    print(n)