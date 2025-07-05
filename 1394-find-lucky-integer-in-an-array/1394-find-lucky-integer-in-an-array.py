class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=collections.Counter(arr)
        s=-1
        for i,j in d.items():
            if i==j:
                s=i              
        return s