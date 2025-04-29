class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        n=len(nums)
        if n==0:
            return True
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                c+=1
        return c<=1