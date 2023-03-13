import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 一维数组创建
# 方法一
array1 = np.array([1, 2, 3, 4, 5])
# print(array1)

# 方法二
array2 = np.arange(0, 20, 2)
# print(array2)

# 方法三：使用linspace函数，用指定范围均匀间隔的数字创建数组对象
array3 = np.linspace(-5, 5, 10)
# print(array3)

# 方法四：使用numpy.random模块的函数生成随机数创建数组对象
# 产生10个$[0, 1)$范围的随机小数
array4 = np.random.rand(10)
# print(array4)
# 产生10个$[1, 100)$范围的随机整数
array5 = np.random.randint(1, 100, 10)
# print(array5)
# 产生20个$\mu=50$，$\sigma=10$的正态分布随机数
array6 = np.random.normal(50, 10, 20)
# print(array6)


# 二维数组创建
# 方法一：使用array函数，通过嵌套的list创建数组对象
array7 = np.array([[1, 2, 3], ["a", "b", "c"]])
# print(array7)

# 方法二：使用zeros、ones、full函数指定数组的形状创建数组对象
array8 = np.zeros((3, 4))
# print(array8)
array9 = np.ones((3, 4))
# print(array9)
array10 = np.full((3, 4), 10)
# print(array10)

# 方法三：使用eye函数创建单位矩阵
array11 = np.eye(3)
# print(array11)

# 方法四：通过reshape将一维数组变成二维数组
array12 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
# print(array12)

# 方法五：通过numpy.random模块的函数生成随机数创建数组对象
# 产生$[0, 1)$范围的随机小数构成的3行4列的二维数组
array13 = np.random.rand(3, 4)
# print(array13)

# 产生$[1, 100)$范围的随机整数构成的3行4列的二维数组
array14 = np.random.randint(1, 100, (3, 4))
# print(array14)


# 多维数组创建
# 使用随机的方式创建多维数组
array15 = np.random.randint(1, 100, (3, 4, 5))
# print(array15)
# 一维数组调形为多维数组
array16 = np.arange(1, 25).reshape((2, 3, 4))
# print(array16)
# 二维数组调形为多维数组
array17 = np.random.randint(1, 100, (4, 6)).reshape((4, 3, 2))
# print(array17)


# 读取图片获得对应的三维数组
array18 = plt.imread("PNG.png")
# print(array18)


# 数组对象的属性
# size属性：数组元素个数
array19 = np.arange(1, 100, 2)
array20 = np.random.rand(3, 4)
# print(array19.size, array20.size)

# shape属性：数组的形状
# print(array19.shape, array20.shape)

# dtype属性：数组元素的数据类型
# print(array19.dtype, array20.dtype)

# ndim属性：数组的维度
# print(array19.ndim, array20.ndim)

# itemsize属性：数组单个元素占用内存空间的字节数
array21 = np.arange(1, 100, 2, dtype=np.int8)
# print(array19.itemsize, array20.itemsize, array21.itemsize)

# nbytes属性：数组所有元素占用内存空间的字节数
# print(array19.nbytes, array20.nbytes, array21.nbytes)

# flat属性：数组（一维化之后）元素的迭代器
from typing import Iterable

# print(isinstance(array20.flat, np.ndarray), isinstance(array20.flat, Iterable))

# base属性：数组的基对象（如果数组共享了其他数组的内存空间）
array22 = array19[:]
# print(array22.base is array19, array22.base is array21)


# 数组的索引和切片
# 一维数组
array23 = np.arange(1, 10)
# print(array23[0], array23[array23.size - 1])
# print(array23[-array23.size], array23[-1])

# 二维数组
array24 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array24[2])
# print(array24[0][0], array24[-1][-1])
# print(array24[1][1], array24[1, 1])

# array24[1][1] = 10
# print(array24)
# array24[1] = [10, 11, 12]
# print(array24)


# 二维数组切片！
# print(array24[:2, 1:])
# print(array24[2])
# print(array24[1, :])
# print(array24[1:, :])  # 切出来还是二维数组
# print(array24[:, :2]) # 切出来还是二维数组
# print(array24[1, :2])
# print(array24[1:2, :2])
# print(array24[::2, ::2])
print(array24[::-1, ::-1])
