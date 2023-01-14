def demo():
    print(f'参数')
    result = None
    while True:
        result = yield result


demo = demo()
next(demo)
print(demo.send(10))
print(demo.send(20))