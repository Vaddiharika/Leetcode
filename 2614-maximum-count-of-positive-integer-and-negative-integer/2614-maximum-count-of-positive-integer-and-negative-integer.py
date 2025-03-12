class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nc=self.binary(nums,0)
        pc=len(nums)-self.binary(nums,1)
        return max(nc,pc)
    def binary(self,nums,target):
        l,r=0,len(nums)-1
        res=len(nums)
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res