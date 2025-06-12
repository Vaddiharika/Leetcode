class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)-1):
            diff=abs(nums[i]-nums[i+1])
            if diff>res:
                res=diff
        d=abs(nums[0]-nums[len(nums)-1])
        if d>res:
            res=d
        return res