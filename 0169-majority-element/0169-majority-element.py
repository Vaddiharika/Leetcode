class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=collections.Counter(nums)
        for key,val in d.items():
            if val>(len(nums)//2):
                return key