'''
练习1：在屏幕上显示跑马灯文字。
'''
def 跑马灯():
    import os
    import time
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('clear')
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]


'''
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
'''
def genertate_code(code_len=4):
    import random
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        # random.randint(0, 100) 生成 0 到 100 之间的数字
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


'''
练习3：设计一个函数返回给定文件名的后缀名。
'''
def get_suffix(filename, has_dot=False):
    '''
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return:  文件的后缀名
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


'''
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
'''
def max2(x:list):
    # x.sort(reverse=True)
    # return x[0], x[1]
    # 思路：先对 x[0] x[1] 大小进行比较，确保 m1的值大于 m2, 后续再遍历列表，如果大于m1，就更新 m1,m2 的值，否则，只更新 m2
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m1, m2 = x[index], m1
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


'''
练习5：计算指定的年月日是这一年的第几天。
'''
def is_leap_year(year):
    '''
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 如年返回 True , 平年返回 False
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    '''
    # [is_leap_year(year)] 返回 [True] = 1 ,[False] = 0
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


'''
练习6：打印杨辉三角。
'''
def 杨辉三角():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


'''
综合案例1： 双色球选号
'''

# randrange(100, 1000, 2) 输出100 到 1000，基数为2的随机一个数
# sample([0, 1, 2], 2) 输出列表中的随机2个数
from random import randrange, randint, sample
class 双色球:


    def display(self, balls):
        '''
        输出列表中的双色球号码
        :return:
        '''
        for index, ball in enumerate(balls):
            if index == len(balls) - 1:
                print('|', end=' ')
            print('%02d' % ball, end=' ')
        print()

    def random_select(self):
        '''
        随机选择一组号码
        :return:
        '''
        red_balls = [x for x in range(1, 34)]
        selected_balls = []
        selected_balls = sample(red_balls, 6)
        selected_balls.sort()
        selected_balls.append(randint(1, 16))
        return selected_balls

    def main(self):
        n = int(input("机选几注: "))
        for _ in range(n):
            self.display(self.random_select())


'''
综合案例2：约瑟夫环问题
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开
'''
def 约瑟夫环_demo():
    persons = [True] * 30
    #  counter 代表被丢的人数，number 记数第九个要被丢的，index 重复遍历 30个人，所以才有后面的 index % 30 ，如果求余等于0，说明已经完成了一圈的计数
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    约瑟夫环_demo()