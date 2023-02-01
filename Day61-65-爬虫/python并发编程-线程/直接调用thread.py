import random
import time
from threading import Thread


def download(*, filename):
    start = time.time()
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')
    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')


def main():
    threads = [
        Thread(target=download, kwargs={'filename': 'Python从入门到住院.pdf'}),
        Thread(target=download, kwargs={'filename': 'MySQL从删库到跑路.avi'}),
        Thread(target=download, kwargs={'filename': 'Linux从精通到放弃.mp4'})
    ]
    start = time.time()
    # 启动三个线程
    for thread in threads:
        thread.start()
    # 等待线程结束
    for thread in threads:
        thread.join()
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')


if __name__ == '__main__':
    main()