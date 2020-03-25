a = 999
b = 999999
print(b % 7 == 0) # True
c = b / 7
d = c / 11
e = d / 13
print(e < a, e > a) # False, False

# For any three-digit positive integer n=(abc)[10], the number m=(abcabc)[10]
# is 1001*n. It is because (abcabc) = (abc000) + (abc) = (abc)*1000 + (abc).

def z(x, y): return (x and not y) or (y and not x)
def w(x, y): return x != y

# By reflexivity, only one heterogeneous pair is tested.
print(z(True, True)==w(True, True), z(False, False)==w(False, False), z(True, False)==w(True, False)) # True, True, True