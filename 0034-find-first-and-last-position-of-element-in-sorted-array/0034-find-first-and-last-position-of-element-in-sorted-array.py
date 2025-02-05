class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums,target,is_sear_left):
            l=0
            r=len(nums)-1
            idx=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    idx=mid
                    if is_sear_left:
                        r=mid-1
                    else:
                        l=mid+1
            return idx
        left=binary(nums,target,True)
        right=binary(nums,target,False)
        return [left,right]