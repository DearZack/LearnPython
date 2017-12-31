#企业奖级分级提成，题目太长不写了
i= int(input('净利润：'))
arr =[1000000, 600000, 400000, 200000, 100000, 0]
ratio = [0.01,0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for index in  range(0, 6):
    if i > arr[index]:
        r += (i - arr[index]) * ratio[index]
        i = arr[index]
print(r)