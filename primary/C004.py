#输入年月日，输出这天是第几天
year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
all = 0;
if (year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
    months[1] = 29
for i in range(month - 1):
    all += months[i]
all += day
print(all)