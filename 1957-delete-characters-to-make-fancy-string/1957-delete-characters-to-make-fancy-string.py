class Solution:
    def makeFancyString(self, s: str) -> str:
        r=s[0]
        for i in range(1,len(s)-1):
            if s[i-1]==s[i]==s[i+1]:
                continue
            else:
                r+=s[i]
        r+=s[-1]
        return r