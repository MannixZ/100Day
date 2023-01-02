"""
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
注意点：
1.为什么范围用(2, end + 1), end 是 num 的平方；
  - 因为 num 不是素数，所以会存在两个数p和q , 切 q 或 p 必定有一个数少于 num 的平方，所以只需要确保较小的数（q 或 p）不会被 num 整除即可
"""
# from math import sqrt

# num = int(input("请输入一个整数:"))
# end = int(sqrt(num))

# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break

# if is_prime and num != 1:
#     print(f"{num}是素数")
# else:
#     print(f"{num}不是素数")


"""
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
最大公约数：能被两个或多个数同时求余不等于0的最大数；eg: 24, 16 最大公约数是 8
最小公倍数：对两个或多个数求余不等于0的对小数； eg: 24, 16 最小公倍数是 24 * 16 // 8
"""
# x = int(input("x="))
# y = int(input("y="))
#
# if x > y:
#     x, y = y, x
#
# # range(10, 0, -1) 区间设定是从大到小，那么需要使用负数步长
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print(f"最大公约数为{factor}")
#         print(f"最小公约数为{x * y // factor}")
#         break


'''
练习3：打印如下所示的三角形图案。
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''

row = int(input("请输入行数:"))
for i in range(row):
    for _ in range(i + 1):
        # print 默认 end='\n' 换行符，用 end='' ,每行输出 * 后，不会自动换行，而是会继续写 *
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()


for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()