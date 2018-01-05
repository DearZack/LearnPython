MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar on is %d' % MAXIMUM(a, b))
    print('The lower on is %d' % MINIMUM(a, b))


#语法理解
"""
MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
lambda后面的x,y 为该表达式参数  （x > y）真为1，假为0


网络

根据参数是否为1 决定s为yes还是no
>>> s = lambda x:"yes" if x==1 else "no"
>>> s(0)
'no'
>>> s(1)
'yes'
"""