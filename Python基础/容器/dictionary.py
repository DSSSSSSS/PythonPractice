def main():
    #在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
    #需要占用大量的内存
    #key必须是不可变对象 字符串、整数、str等都是不可变的，
    # 因此，可以放心地作为key。而list是可变的，就不能作为key

    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    d['Michael']
    #通过key来计算值在的位置，然后直接到这个位置读取

    #when the key is not exist,python will raise a error 也称异常
    #一是通过in判断key是否存在
    'Thomas' in d
    #二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
    d.get('Thomas')
    d.get('Thomas', -1)

    d.pop('Bob')
if __name__ == '__main__':
    main()