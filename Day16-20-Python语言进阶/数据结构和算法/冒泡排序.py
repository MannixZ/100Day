'''
算法：解决问题的方法和步骤

评价算法的好坏：渐近时间复杂度和渐近空间复杂度。

渐近时间复杂度的大O标记：

 - 常量时间复杂度 - 布隆过滤器 / 哈希存储
 - 对数时间复杂度 - 折半查找（二分查找）
 - 线性时间复杂度 - 顺序查找 / 计数排序
 - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
 - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
 - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
 - 几何级数时间复杂度 - 汉诺塔
 - 阶乘时间复杂度 - 旅行经销商问题 - NPC
'''

def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


