class StreamHasher:
    """哈希摘要生成器"""

    def __init__(self, alg="md5", size=4096) -> None:
        self.size = size
        alg = alg.lower()
        # getattr(对象, 属性)，获取对象属性的值
        self.hasher = getattr(__import__("hashlib"), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b""):
            self.hasher.update(buf)
        return self.hasher.hexdigest()


def main():
    hasher1 = StreamHasher()
    with open("./Day16-20-Python语言进阶/面向对象相关知识/chromedriver.zip", "rb") as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher("sha1")
    with open("./Day16-20-Python语言进阶/面向对象相关知识/chromedriver.zip", "rb") as stream:
        print(hasher2(stream))


if __name__ == "__main__":
    main()
