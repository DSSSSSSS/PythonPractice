def main():
    #list是一种有序的集合，可以随时添加和删除其中的元素。
    #实现是链表
    classmates = ['Michael', 'Bob', 'Tracy']
    len(classmates)
    #索引
    classmates[0]
    classmates[-1]

    classmates.append('Adam')
    classmates.insert(1, 'Jack')
    classmates.pop()
    classmates.pop(1)
    classmates[1] = 'Sarah'
    #list里面的元素的数据类型也可以不同
    L = ['Apple', 123, True]
    #list元素也可以是另一个list
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    
if __name__ == '__main__':
    main()