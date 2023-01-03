def str_demo():
    str1 = 'hello,world!'
    # 通过内置函数len计算字符串的长度
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())
    # 获得字符串变大写后的拷贝
    print(str1.upper())
    # 从字符串中查找子串所在位置
    print(str1.find('or'))
    print(str1.find('shit123123'))
    # 与find类似但找不到子串时会引发异常
    print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))
    print(str1.startswith('hel'))
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('d!'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())
    str3 = '  jackfrued@126.com '
    print(str3.strip())


def list_demo():
    list1 = [1, 3, 5, 7, 100]
    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        pass
        # print(index, elem)
    # 在下标为1的位置插入 400
    list1.insert(1, 400)
    # 合并两个列表
    list1.extend([1000, 2000])
    list1 += [3000, 4000]
    # 删除指定位置元素
    list1.pop(1)
    # 清空列表元素
    list1.clear()
    print(list1)


def 列表切片_demo():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # 通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 通过方向切片来获得倒转后的列表拷贝
    fruits5 = fruits[::-1]
    print(fruits5)


def 列表排序_demo():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    # sorted 不会改变传入的列表顺序,而是将 list1 拷贝后再改变顺序
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


def 生成器和生成式_demo():
    import sys
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    # [xxx] 生成式, （xxx） 生成器
    # f = [x ** 2 for x in range(1, 1000)]
    # print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    # print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)


def fib_demo():
    '''
    函数生成器 yield 完成斐波那契数列
    :return:
    '''

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            yield a

    for val in fib(20):
        print(val)


def set_demo():
    # 创建集合
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    # print(set4)
    # 向集合中添加元素
    set1.add(4)
    set1.add(5)
    # 向集合中添加一个列表 [11, 12]
    set1.update([11, 12])
    # 向集合中删除一个元素 5
    set1.discard(5)
    if 4 in set1:
        set1.remove(4)
    set1.pop()
    print(set1)


def 集合运算_demo():
    # 集合的交集、并集、差集、对称差运算
    set1 = {1, 2, 3, 7, 8, 9, 10}
    set2 = {1, 2, 3, 4, 5, 6}
    set3 = {1, 2, 3, 7}
    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 差集
    print(set1 - set2)
    print(set1.difference(set2))
    # 对称差
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))
    # 判断子集和超集
    # 如果一个集合S2中的每一个元素都在集合S1中，且集合S1中可能包含S2中没有的元素，则集合S1就是S2的一个超集，反过来，S2是S1的子集。 S1是S2的超集
    print(set2 <= set1)
    print(set2.issubset(set1))

    print(set3 <= set1)
    print(set3.issubset(set1))

    print(set1 >= set3)
    print(set1.issuperset(set3))

    print(set2 >= set3)
    print(set2.issuperset(set3))


def dict_demo():
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 创建字典的构造器语法
    item1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    item2 = dict(zip(['a', 'b', 'c '], '123'))
    # 创建字典的推导式语法
    item3 = {num: num ** 2 for num in range(1, 10)}
    print(item1, item2, item3)
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores.update(冷面=67, 方齐禾=85)
    print(scores)
    # get方法也是通过键获取对应的值但是可以设置默认值
    scores.get('武则天', 60)
    # 删除字典中的元素
    scores.popitem()
    scores.pop('骆昊')
    # 清空字典
    scores.clear()
    print(scores)

if __name__ == '__main__':
    dict_demo()