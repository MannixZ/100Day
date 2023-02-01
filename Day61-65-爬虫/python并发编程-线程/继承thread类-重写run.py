import random
import time
from threading import Thread


class DownloadThread(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        start = time.time()
        print(f"开始下载 {self.filename}.")
        time.sleep(random.randint(3, 6))
        print(f"{self.filename} 下载完成.")
        end = time.time()
        print(f"下载耗时: {end - start:.3f}秒.")


def main():
    threads = [
        DownloadThread("Python从入门到住院.pdf"),
        DownloadThread("MySQL从删库到跑路.avi"),
        DownloadThread("Linux从精通到放弃.mp4"),
    ]
    start = time.time()
    # 启动三个线程
    for thread in threads:
        thread.start()
    # 等待线程结束
    for thread in threads:
        thread.join()
    end = time.time()
    print(f"总耗时: {end - start:.3f}秒.")


if __name__ == "__main__":
    main()
