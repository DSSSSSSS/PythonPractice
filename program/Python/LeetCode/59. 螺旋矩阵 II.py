#https://leetcode-cn.com/problems/spiral-matrix-ii/description/
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        x0=0
        x1=n-1
        y0=0
        y1=n-1
        x=0
        y=0
        direct=0
        l=[[0 for i in range(n)] for j in range(n)]
        for i in range(n*n):
            l[x][y]=i+1
            if direct==0:
                y+=1
                if y==y1:
                    direct=(direct+1)%4
                    x0+=1
                    continue
            if direct==1:
                x+=1
                if x==x1:
                    direct=(direct+1)%4
                    y1-=1
                    continue
            if direct==2:
                y-=1
                if y==y0:
                    direct=(direct+1)%4
                    x1-=1
                    continue
            if direct==3:
                x-=1
                if x==x0:
                    direct=(direct+1)%4
                    y0+=1
                    continue
            
        return l
                                 
def main():
    s =Solution()
    re=s.generateMatrix(4)
    print(re)
if __name__ == '__main__':
    main()