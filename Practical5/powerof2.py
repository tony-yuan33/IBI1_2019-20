x = 2019
k = 0
li = []

while x > 0:
    while not(x & 1):
        x >>= 1
        k += 1
    li.append('2**' + str(k))
    x >>= 1
    k += 1
li.reverse()
print(' + '.join(li))