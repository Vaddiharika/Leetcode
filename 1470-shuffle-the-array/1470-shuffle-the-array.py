class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp=[]
        for i in range(n):
            temp+=[nums[i]]
            temp+=[nums[i+n]]
        return temp
