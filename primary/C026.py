#阶乘递归
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n -1)

for i in range(6):
    print(str(i) + "! = " + str(fact(i)))