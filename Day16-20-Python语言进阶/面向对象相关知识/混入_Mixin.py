"""
例子：自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。
"""


class SetOnceMappingMixin:
    """自定义混入类"""

    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + " already set")
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""

    pass


my_dict = SetOnceDict()
try:
    my_dict["username"] = "张三"
    my_dict["username"] = "李四"
except KeyError as e:
    print(e)
print(my_dict)
