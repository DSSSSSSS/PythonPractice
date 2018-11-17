#就是这样了

#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

# 思维模式-> 积累
def max1(l):
        m =l[0]
        for i in l:
               if m<i:
                       m=i
                                
        return m
def main():
    l=[1,2]
    l.append(3)
    #容器 放数据 =》总结 
    print(max(l))
    print(max1(l))
if __name__ == '__main__':
    main()    