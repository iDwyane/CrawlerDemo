
# 多线程 与 传统方式比较

import time
import threading

# def coding():
#     for x in range(3):
#         print('正在写代码 %s' % x)
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print("正在画图 %s" % x)
#         time.sleep(1)
#

# 需要 大概 6秒
# def main():
#     coding()
#     drawing()



def coding():
    for x in range(3):
        print('正在写代码 %s , %s' % (x, threading.current_thread()))
        time.sleep(1)

def drawing():
    for x in range(3):
        print("正在画图 %s" % x)
        time.sleep(1)


# 需要 大概 3秒
def main():
    t1 = threading.Thread(target=coding) # 注意：这里不是传 coding() ,  而是 coding ,有 () 是把函数的值给他
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    print(threading.enumerate())  # 3 个线程 ：  主线程  以及 t1、t2
if __name__ == '__main__':
    main()