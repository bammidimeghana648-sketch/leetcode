class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = candies[0]
        for i in candies:
            if max<i:
                max=i
        res=[]
        for i in range(len(candies)):
            if extraCandies+candies[i]>=max:
                res.append(True)
            else:
                res.append(False)
        return res