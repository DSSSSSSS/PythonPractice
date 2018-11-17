# 数据封装、继承和多态是面向对象的三大特点
class Alimal(object):
    def __init__(self, name, length):
        self.name = name
        self.passwd = length
        self.__a = 1  # 私有变量

    def __str__(self):
        # 当print(user)的时候，会调用这个函数
        return "name "+str(self.name)+" " + "passwd "+str(self.passwd)

    def setName(self, name):
        # 封装1.对传入参数进行检查
        #   2. 当setNmae内部发生变化时，不用修改外部的代码

        if not isinstance(name, str):
            raise ValueError("参数不是str类型")
        else:
            self.name = name

    def run(self):
        print("alimal is running")


class Dog(Alimal):
    # 继承自alimal
    def run(self):
        # 覆盖父类的同名方法
        print("Dog is running")


def run(Alimal):
    # run函数传入参数只要有run()这个函数就行
    # 在静态语言如c++中，参数必需是alimal或是它的子类
    Alimal.run()


def main():
    alimal = Alimal("123", "1234")
    print(alimal)
    alimal.setName("abc")
    print(alimal)
    alimal.run()
    dog = Dog("dog", "123")
    run(dog)

    print(type(dog))
    a = type(dog)("123", "1234")
    a.run()


if __name__ == '__main__':
    main()
