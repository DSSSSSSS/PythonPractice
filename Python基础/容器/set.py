def main():
    #set 集合 存放不重复的元素
    #要创建一个set，需要提供一个list作为输入集合
    s = set([1, 2, 3])
    s.add(4)
    s.remove(4)
    #两个set可以做数学意义上的交集、并集等操作
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    s1 & s2 #交
    s1 | s2 #并
if __name__ == '__main__':
    main()