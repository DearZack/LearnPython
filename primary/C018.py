# s = a + aa +aaa + a...a

import math

count = int(input("个数："))
number = int(input("数字："))
result = 0;
temp = 0;
for i in range(0, count):
    for j in range(0, i + 1):
        temp += 10 ** j * number;
    result += temp;
    temp = 0;
print(result)
