import sys


def echo_test1():
    print("echo_test1")


def echo_test2():
    print("echo_test2")


def echo_test3():
    print("echo_test3")


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        self.__dict__.pop(key)
        print('执行我了。')


s = Student('hkey')
s.age = 20
print(s['name'])
print(s['age'])
del s['age']


def main():
    this_module = sys.modules[__name__]
    isExist = hasattr(this_module, "echo_test3")
    if not isExist:
        raise AssertionError
    func = getattr(this_module, "echo_test3")()


if __name__ == '__main__':
    main()
