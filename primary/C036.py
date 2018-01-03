from math import sqrt
def isN(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, 100):
    if isN(i):
        print(i)