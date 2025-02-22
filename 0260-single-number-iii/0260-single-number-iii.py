import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return nums
        l=[]
        d=collections.Counter(nums)
        for i,j in d.items():
            if j==1:
                l.append(i)
        return l