
# 使用 Thread 类创建多线程

import threading
import  time


class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码 %s' % threading.current_thread())
            time.sleep(1)

class DrawwingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在画图 %s" % threading.current_thread())
            time.sleep(1)


def main():
    t1 = CodingThread()
    t2 = CodingThread()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()


    # 线程是无序的，不可保证哪个线程先执行完