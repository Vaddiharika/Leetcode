def rever(nums,l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=n-k
        k%=n
        rever(nums,0,k-1)
        rever(nums,k,n-1)
        rever(nums,0,n-1)
    
        