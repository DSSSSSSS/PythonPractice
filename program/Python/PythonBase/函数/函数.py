import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny #返回多个值，其实返回了一个tuple

def my_abs(x):
    #传入函数类型检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def main():
    #常见内置函数
    abs(100) #绝对值
    max() #返回最大值

    #数据类型转换
    float('12.34')
    int(12.34)

    #函数别名
    a = abs
    a(-1)
    #print(fact(800))


if __name__ == '__main__':
    main()

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    #calc(1, 2)

    #nums = [1, 2, 3]
    #calc(*nums)

#关键字参数，kw是dict，为拷贝传值
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    #extra = {'city': 'Beijing', 'job': 'Engineer'}
    #person('Jack', 24, **extra)

#命名关键字参数
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
#和关键字参数**kw不同，
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)