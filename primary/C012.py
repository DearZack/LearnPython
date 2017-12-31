# 枚举101-200之间的素数

from math import sqrt
from sys import stdout

count = 0
leap = 1
for m in range(101, 201):
    k = int(sqrt(m))
    for i in range(2, k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m)
        count += 1
    leap = 1

print("一共" + str(count) + '个')
