from memory_profiler import profile


class A(object):  # 没有定义__slots__属性
    def __init__(self, x):
        self.x = x


@profile
def test():
    f = [A(523825) for i in range(100000)]


if __name__ == '__main__':
    test()
