class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        i,j=0,len(num)-1
        while i<j:
            re=num[i]+num[j]
            if re==target:
                return [i+1,j+1]
            elif re<target and num[i]<=num[j]:
                i+=1
            elif re<target and num[i]>num[j]:
                j-=1
            elif re>target and num[i]<=num[j]:
                j-=1
            elif re>target and num[i]>num[j]:
                i+=1