class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=collections.Counter(nums)
        l=[]
        for key,val in d.items():
            if val>(len(nums)//3):
                l.append(key)
        return l