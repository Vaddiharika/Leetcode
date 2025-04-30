class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[count]=arr[count],arr[i]
                count+=1
        