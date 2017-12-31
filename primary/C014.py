#分解质因数并打印

from sys import stdout

n = int(input("数字："))
list = [];
print(str(n) + " = ", end="")
for i in range(2, n):
    while n > i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write(" * ")
            n /= i
        else:
            break
print(int(n))