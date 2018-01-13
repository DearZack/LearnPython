if __name__ == '__main__':
    from sys import stdout

    filename = input("文件名：")
    fp = open(filename, "w")
    ch = input("字符：")
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input("字符：")
    fp.close()
