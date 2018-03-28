from memory_profiler import profile


class A(object):  # 定义了__slots__属性
    __slots__ = ('x')

    def __init__(self, x):
        self.x = x


@profile
def test2():
    f = [A(523825) for i in range(100000)]


if __name__ == '__main__':
    test2()
