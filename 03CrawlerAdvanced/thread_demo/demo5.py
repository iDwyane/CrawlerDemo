

# Condition版生产者和消费者模式

# 与 Lock 相比，免去反复上锁的操作

import threading
import random
import time

gMonney = 1000
gCondition = threading.Condition()  # 全局锁
gTotalTime = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMonney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTimes >= gTotalTime:
                gCondition.release()
                break
            gMonney += money
            print('%s正在生产了%d元钱，剩余%d元钱'%(threading.current_thread(), money, gMonney))
            gTimes += 1
            gCondition.notify_all()  # 生产钱，唤醒等待的线程
            gCondition.release()
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global gMonney
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            while gMonney < money:
                # 如果生产次数已经为10，则停止
                if gTimes >= gTotalTime:
                    gCondition.release()
                    return

                # 不足消费，继续等待
                print("%s准备消费%d元钱，剩余%d元钱，不足消费" %(threading.current_thread(), money, gMonney))
                gCondition.wait()  # 如果不满足条件，则是等待（不执行下面的语句，但释放锁，给其他线程使用）不用反复上锁，把 gCondition.acquire() 放在 while True 外面


            gMonney -= money
            print("%s 消费了%d元钱，剩余%d元钱" % (threading.current_thread(), money, gMonney))
            gCondition.release()
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