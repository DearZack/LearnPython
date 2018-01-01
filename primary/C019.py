#完数

def get(n):
    list = [];
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
    return list


for i in range(1, 1000):
    list = get(i)
    temp = 0
    for j in range(len(list)):
        temp += list[j]
    if temp == i:
        print(i)
    temp = 0