from functools import reduce


def main():
    # 高阶函数：一个函数就可以接收另一个函数作为参数
    def add(x, y, f):
        return f(x) + f(y)
    re = add(-5, 6, abs)
    print(re)

    # map
    def f(x):
        return x*x
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    list(r)  # 结果r是一个Iterator，Iterator是惰性序列

    # reduce 减少list 和为一个元素
    def add(x, y):
        return x+y
    reduce(add, [1, 3, 5, 7, 9])
    
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return DIGITS[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))


    #filter filter()把传入的函数依次作用于每个元素，
    # 然后根据返回值是True还是False决定保留还是丢弃该元素。

    def is_odd(n):
        return n % 2 == 1
    #filter return Iterator 需要求值
    list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

    #sorted 排序算法
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)


if __name__ == '__main__':
    main()
