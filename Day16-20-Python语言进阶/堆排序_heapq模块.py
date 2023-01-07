"""
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
"""

import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 最大的3个元素
print(heapq.nlargest(3, list1))
# 最小的3个元素
print(heapq.nsmallest(3, list1))
# 列表嵌套字典，根据key寻找最大值或最小值的 N 个元素
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


