#输出时间戳

import time

for i in range(3):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(1)