
def main():
    #高阶函数：一个函数就可以接收另一个函数作为参数
    def add(x, y, f):
        return f(x) + f(y)
    re=add(-5, 6, abs)   
    print(re)
    
if __name__ == '__main__':
    main()