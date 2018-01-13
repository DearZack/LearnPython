if __name__ == '__main__':
    from sys import stdout

    fp1 = open('test1', 'r')
    fp2 = open('test2', 'r')
    str1 = fp1.read()
    str2 = fp2.read()
    str = str1 + str2
    print(str)
    fp = open('test3', 'w')
    fp.write(str)
    fp.close()