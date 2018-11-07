
# Queue 线程安全队列

from queue import Queue
import time
import threading

# q = Queue(4)
# q.put(25) # 最先添加的是最后一位   队列
# q.put(2)
# print(q.qsize())

# for x in range(4):
#     q.put(x)
#
# for x in range(4):
#     print(q.get())


def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)

def get_value(q):
    while True:
        print(q.get())  # 注意： get() 和 put() 都是阻塞式，默认里面都有一个参数，block = True.   get() = get(block=True)

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()