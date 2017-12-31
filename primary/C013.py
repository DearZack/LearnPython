# 水仙花数

for i in range(101, 1000):
    a = int(i / 100)
    b = int(i / 10) % 10
    c = i % 10
    if a * a * a + b * b * b + c * c * c == i:
        print(i)
