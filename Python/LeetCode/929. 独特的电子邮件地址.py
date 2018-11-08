#https://leetcode-cn.com/problems/unique-email-addresses/description/
from typing import TypeVar, Iterable, Tuple, Dict, List
class Solution:
    def numUniqueEmails(self, emails:List[str]):
        """
        :type emails: List[str]
        :rtype: int
        """
        for string in emails:
            l =string.split("@")
            l1 = l[0].split(".")
            l2=""
            for i in l1:
                l2+=i
            pos=-1
            for i in range(len(l2)):
                if l2[i]=="+":
                    pos =i
            if pos!=-1:
                l2=l2[0:pos] 
            l=l2+l

def main():
    pass

if __name__ == '__main__':
    main()