
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
    
if __name__ == '__main__':
    main()