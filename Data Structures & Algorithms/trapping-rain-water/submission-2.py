class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        lm,rm=h[0],h[r]
        ans=0
        while(l<r):
            if(h[l]<=h[r]):
                ans+=min(lm,rm)-h[l]
                l+=1
                lm=max(lm,h[l])
            else:
                ans+=min(lm,rm)-h[r]
                r-=1
                rm=max(rm,h[r])
        return ans