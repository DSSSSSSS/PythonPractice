import functools

def lazy_sum(*args):#*args 可变参数
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def main():
    f = lazy_sum(1, 3, 5, 7, 9)
    f()

    #匿名函数
    list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    #偏函数
    int2 = functools.partial(int, base=2)
if __name__ == '__main__':
    main()