def gcd(x, y):
    '''
    求最大公约数
    :param x:
    :param y:
    :return:
    '''
    (x, y) = (y, x) if x > y else (x, y)  # 固定 x 为小的值，因为需要取最大公约数，遍历的取值范围拿小的就可以
    for factor in (x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    '''
    求最小公倍数
    :param x:
    :param y:
    :return:
    '''
    return x * y // gcd(x, y)


def is_palindrome(num):
    '''判断一个数是不是回文数，就是 12345 是否等于 54321'''
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num, total, num


def foo():
    global a
    a = 200
    print(a)


if __name__ == '__main__':
    a = 100
    foo()
    print(a)