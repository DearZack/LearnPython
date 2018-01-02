#2/1+3/2+5/3+8/5...前20项
x = 1
y = 2
temp = 0
all = 0
for i in range(20):
    all += y /x
    temp = y
    y += x
    x = temp
print(all)