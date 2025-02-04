class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            min_ind=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_ind]:
                    min_ind=j
            nums[i],nums[min_ind]=nums[min_ind],nums[i]

        """
        Do not return anything, modify nums in-place instead.
        """
        