
# 加锁

import threading

VALUE = 0

gLock = threading.Lock()  # 对修改值的语句加锁处理即可，访问值得语句，可以不加锁
def add_value():
    global VALUE   # 需要 gloabal 关键字，表示引用外面的值
    gLock.acquire()
    for x in range(1000000):
        VALUE += 1
    gLock.release()
    print("最后value: %d" % VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()