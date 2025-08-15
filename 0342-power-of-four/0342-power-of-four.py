class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<4 and n!=1:
            return False
        while n>=4:
            n/=4
        return n==1