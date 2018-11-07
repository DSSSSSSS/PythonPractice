def max1(l):
    m=l[0]
    L=[]
    for i in l:
        if m<i:
            L.append(i)
            m=i
    return m 
