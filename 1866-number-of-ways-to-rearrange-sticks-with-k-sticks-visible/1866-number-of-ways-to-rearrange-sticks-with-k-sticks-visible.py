class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp={}
        dp[(1,1)]=1
        for c in range(2,n+1):
            for v in range(1,k+1):
                dp[(c,v)]=dp.get((c-1,v-1),0)+(c-1)*(dp.get((c-1,v),0))
        return dp[(n,k)]%(10**9+7)