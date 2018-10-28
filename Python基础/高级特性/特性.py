
def main():
    #切片 取一个list或tuple、string 的部分元素
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    L[0:3]
    L[:3]
    L[-2:-1]
    #前10个数，每两个取一个
    L[:10:2]
    #只写[:]就可以原样复制一个list


    #迭代 for ..in
    for ch in 'ABC':
        print(ch)

    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    for x, y in [(1, 1), (2, 4), (3, 9)]:
        print(x, y)
    

    #列表生成式
    list(range(1, 11))
    [x * x for x in range(1, 11) if x % 2 == 0]
    [m + n for m in 'ABC' for n in 'XYZ']


    #生成器(generator) 元素是在需要时计算出来的
    g = (x * x for x in range(10))
    for n in g:
        print(n)
    

if __name__ == '__main__':
    main()

#一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'