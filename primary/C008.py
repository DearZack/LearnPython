#输出乘法口诀表


for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + " * " + str(i) + " = " + str(i * j), end='      ')
    print("\n")