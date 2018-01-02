num = int(input("数字："))
len = 0;
while num > 0:
    print(num % 10)
    num = int(num /10)
    len += 1
print("长度：" + str(len))