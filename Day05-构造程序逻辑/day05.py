'''
1.找出水仙花数
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''
def sxh():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


'''
2.反转正整数，例如 12345 -> 54321
对正整数求模 % 能找到个位数 , 找到十位数可以先对正整数整除 //10 后再求模
'''
def reverse_num():
    num = int(input("请输入正整数："))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


'''
3.CRAPS赌博游戏。
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
'''
def gamble():
    from random import randint
    money = 1000
    while money > 0:
        print(f'你的总资产为:{money}')
        need_go_on = False
        while True:
            debt = int(input("请下注："))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print(f"玩家摇出了{first}点")
        if first == 7 or first == 11:
            print("玩家胜出")
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print("庄家胜出")
            money -= debt
        else:
            need_go_on = True
        while need_go_on:
            need_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print(f"玩家摇出了{current}点")
            if current == 7:
                print("庄家胜出")
                money -= debt
            elif current == first:
                print("玩家胜出")
                money += debt
            else:
                need_go_on = True
    print("你破产了，游戏结束！")


'''
计算斐波那契数列
'''
def fbnq():
    num_count = int(input("请输入需要生成的斐波那契数列个数:"))
    num_list = []
    for i in range(num_count):
        if i == 0 or i == 1:
            num_list.append(1)
        else:
            num_first = num_list[i - 1]
            num_second = num_list[i - 2]
            num_list.append(num_first + num_second)
    print(num_list)


'''
完美数
它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
简单理解就是：能够对因子数求余为0，且相加能够等于自身的
'''
def perfect_num():
    for i in range(1, 100):
        total = 0
        for _ in range(i//2+1):
            if _ == 0:
                continue
            else:
                if i % _ == 0:
                    total += _
        if total == i:
            print(f'完美数：{i}')


'''
输出2-100以内所有的素数。
'''
def shusu_100():
    import math
    for num in range(2, 101):
        is_prime = True
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime == True:
            print(num, end=' ')





if __name__ == '__main__':
    shusu_100()