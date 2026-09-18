class Solution:
    def findErrorNums(self, lst: List[int]) -> List[int]:
        s = sum(lst)
        n = len(lst)
        sum1=(n*(n+1))//2
        rd=set(lst)
        sum2=sum(rd)
        r=s-sum2
        m=sum1-sum2
        return [r,m]
        