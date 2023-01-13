"""
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
"""

import glob
import os
import threading

from PIL import Image

PREFIX = "thumbnails"


def generate_thumbnail(infile, size, format="PNG"):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind("/") + 1 :]
    outfile = f"{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}"
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main():
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob("images/*.png"):
        for size in (32, 64, 128):
            # 创建并启动线程
            threading.Thread(
                target=generate_thumbnail, args=(infile, (size, size))
            ).start()


if __name__ == "__main__":
    main()
