
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

if __name__ == '__main__':
    main()