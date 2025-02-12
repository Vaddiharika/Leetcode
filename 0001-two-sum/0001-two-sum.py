class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i,v in enumerate(nums):
            diff=target-v
            if diff in has:
                return [i,has[diff]]
            else:
                has[v]=i