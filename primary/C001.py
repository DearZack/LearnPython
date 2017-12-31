#枚举1,2,3,4所组成的没有重复数字的三位数

a = 0;
for i in range(1, 5):#range(1,5) #代表从1到5(不包含5)
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) and (i != k) and (j != k):
                print(i * 100 + j * 10 + k);
                a = a + 1;
print("一共" + str(a) + "个");