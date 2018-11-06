

# Lock版生产者和消费者模式

import threading
import random
import time

gMonney = 1000
gLock = threading.Lock()  # 全局锁
gTotalTime = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMonney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >= gTotalTime:
                gLock.release()
                break
            gMonney += money
            print('%s正在生产了%d元钱，剩余%d元钱'%(threading.current_thread(), money, gMonney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMonney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMonney >= money:
                gMonney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMonney))
            else:

                if gTimes >= gTotalTime:
                    gLock.release()
                    break;
                print("消费者不足消费")
            gLock.release()
            time.sleep(0.5)


def mian():
    for x in range(3):
        t = Consumer(name="消费者线程%d" % x)
        t.start()

    for x in range(5):
        t = Producer(name="生产者线程%d"% x)
        t.start()


if __name__ == '__main__':
    mian()