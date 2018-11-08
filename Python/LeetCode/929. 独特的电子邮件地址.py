#https://leetcode-cn.com/problems/unique-email-addresses/description/
from typing import TypeVar, Iterable, Tuple, Dict, List
class Solution:
    def numUniqueEmails(self, emails:List[str]):
        """
        :type emails: List[str]
        :rtype: int
        """
        l=[]
        for e in emails:
            l1,l2 =e.split("@")
            for i in range(len(l1)):
                if(l1[i]=="+"):
                    l1 =l1[0:i]
                    break
            e=l1.replace(".","")+"@"+l2
            if e not in l:
                l.append(e)
        return len(l)


def main():
    s = Solution()
    re=s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(re)

if __name__ == '__main__':
    main()