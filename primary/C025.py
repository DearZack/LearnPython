#阶乘求和
sun = 0
t = 1;
for n in range(1, 21):
    t *= n
    sun += t
print(sun)