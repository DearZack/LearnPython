if __name__ == '__main__':
    from sys import stdout

    fp = open('test2', "w")
    ch = input("字符：")
    ch = ch.upper()
    fp.write(ch)
    fp = open('test2', 'r')
    print(fp.read())
    fp.close()
