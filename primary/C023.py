from sys import stdout
count = int(input("数字："))
for i in range(1, count + 1):
    for j in range(count - i):
        stdout.write(' ')
    for k in range(2 * i - 1):
        stdout.write('*')
    print()