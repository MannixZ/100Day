'''
说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：

输入：1 -2 3 5 -3 2

输出：8

输入：0 -2 3 5 -1 2

输出：9

输入：-9 -2 -3 -5 -3

输出：-2

说明：这个题目最容易想到的解法是使用二重循环，但是代码的时间性能将会变得非常的糟糕。使用动态规划的思想，仅仅是多用了两个变量，就将原来$O(N^2)$复杂度的问题变成了$O(N)$。
'''


def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()