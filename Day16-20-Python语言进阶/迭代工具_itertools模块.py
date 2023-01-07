"""
迭代工具模块
"""

import itertools


# 产生ABCD的全排列
it1 = itertools.permutations('ABCD')
# for it in it1:
#     print(it)

# 产生ABCDE的五选三组合
it2 = itertools.combinations('ABCDE', 3)
# for it in it2:
#     print(it)

# 产生ABCD和123的笛卡尔积
it3 = itertools.product('ABCD', '123')
# for it in it3:
#     print(it)

# 产生ABC的无限循环序列
it4 = itertools.cycle(('A', 'B', 'C'))
# for it in it4:
#     print(it)