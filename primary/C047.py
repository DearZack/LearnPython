#两个值互换

def cheange(a,b):
    a,b = b,a
    return (a, b)

if __name__ == '__main__':
    x = 20
    y = 10
    print("x = %d    y = %d" % (x, y))
    x, y = cheange(x, y)
    print("x = %d    y = %d" % (x, y))