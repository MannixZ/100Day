"""
对象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。所有的类都直接或间接的继承自object，所有的元类都直接或间接的继承自type。
"""

import threading


class SingletonMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = threading.RLock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """总统类（单例类）"""

    pass
