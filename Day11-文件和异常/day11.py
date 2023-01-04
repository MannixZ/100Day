"""
w+:如果文件存在则清除原来的文件内容，重新写入，否则创建文件
r+：如果文件存在，则直接覆盖在原来的文件内容上，比如原来文件内容是 wwwww, 写入 rrr, 最终文件内容是 rrrw，如果文件不存在，则报错
a+:追加，追加在原来的内容后面，如果文件不存在，则创建文件
"""

"""
下面的例子演示了如何将1-9999之间的素数分别写入三个文件中（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
"""

from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ("./Day11-文件和异常/a.txt", "./Day11-文件和异常/b.txt", "./Day11-文件和异常/c.txt")
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, "w", encoding="utf-8"))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + "\n")
                elif number < 1000:
                    fs_list[1].write(str(number) + "\n")
                else:
                    fs_list[2].write(str(number) + "\n")
    except IOError as ex:
        print(ex)
        print("写文件时发生错误")
    finally:
        for fs in fs_list:
            fs.close()
    print("操作完成")


if __name__ == "__main__":
    main()
