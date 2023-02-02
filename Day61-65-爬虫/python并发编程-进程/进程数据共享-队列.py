import time
from multiprocessing import Process, Queue


def sub_task(content, queue):
    counter = queue.get()
    while counter < 50:
        print(content, end="", flush=True)
        counter += 1
        queue.put(counter)
        time.sleep(0.01)
        queue.get(counter)


def main():
    queue = Queue()
    # multiprocessing.Queue对象的get方法默认在队列为空时是会阻塞的，直到获取到数据才会返回。如果不希望该方法阻塞以及需要指定阻塞的超时时间，可以通过指定block和timeout参数进行设定。
    queue.put(0)
    p1 = Process(target=sub_task, args=("Ping", queue))
    p1.start()
    p2 = Process(target=sub_task, args=("Ping", queue))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    queue.put(50)


if __name__ == "__main__":
    main()
