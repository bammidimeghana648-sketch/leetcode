class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        f = []
        s = 0
        for i in nums:
            s += i
            f.append(s)
        return f