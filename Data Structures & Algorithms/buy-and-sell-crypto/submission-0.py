class Solution:
    def maxProfit(self, p: List[int]) -> int:
        rm=p[-1]
        ans=0
        i=len(p)-1
        while(i>=0):
            ans=max(ans,rm-p[i])
            rm=max(rm,p[i])
            i-=1
        return ans