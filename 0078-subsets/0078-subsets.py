class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sset=[]
        def subset(i):
            if i==len(nums):
                res.append(sset[:])
                return
            sset.append(nums[i])
            subset(i+1)
            sset.pop()
            subset(i+1)
        subset(0)
        return res