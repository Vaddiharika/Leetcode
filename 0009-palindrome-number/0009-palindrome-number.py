class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rn=0
        d=x
        while x>0:
            ld=x%10
            rn=(rn*10)+ld
            x//=10
        return True if rn==d else False