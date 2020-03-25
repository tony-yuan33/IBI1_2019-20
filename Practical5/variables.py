a = 999
b = 999999
c = b / 7
d = c / 11
e = d / 13
print(e < a, e > a)

def z(x, y): return (x and not y) or (y and not x)
def w(x, y): return x != y

# By reflexivity, only one heterogeneous pair is tested.
print(z(True, True)==w(True, True), z(False, False)==w(False, False), z(True, False)==w(True, False))