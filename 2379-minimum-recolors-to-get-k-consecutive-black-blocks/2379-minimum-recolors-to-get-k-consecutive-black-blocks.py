class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        bc=0
        ans=float("inf")
        for i in range(len(blocks)):
            if i-k>=0 and blocks[i-k]=='B':
                bc-=1
            if blocks[i]=='B':
                bc+=1
            ans=min(ans,k-bc)
        return ans