import sys
def echo_test1():
    print("echo_test1")


def echo_test2():
    print("echo_test2")


def echo_test3():
    print("echo_test3")


def main():
    this_module = sys.modules[__name__]
    isExist=hasattr(this_module,"echo_test3")
    print(isExist)
    func = getattr(this_module, "echo_test3")()


if __name__ == '__main__':
    main()
