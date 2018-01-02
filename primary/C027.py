def output(s):
    l = len(s)
    if l == 0:
        return
    for a in range(l):
        print(s[l - a - 1])


s = input("字符：")
output(s)



