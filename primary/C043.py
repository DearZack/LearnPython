class Num:
    nun = 1
    def inc(self):
        self.nun += 1
        print('num = %d' % self.nun)

if __name__ == '__main__':
    num = 2
    inst = Num()
    for i in range(3):
        num += 1
        print('The num  = %d' % num)
        inst.inc()