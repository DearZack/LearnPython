num = int(input("数字："))
list = []
a = True
while num > 0:
    list.append(num % 10)
    num = int(num / 10)
length = len(list)

for i in range(int(length / 2)):
    if list[i] != list[length - i - 1]:
        a = False
        break

print(a)