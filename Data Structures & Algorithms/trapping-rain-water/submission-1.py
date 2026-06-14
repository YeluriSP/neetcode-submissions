class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        lm,rm=h[0],h[r]
        ans=0
        while(l<r):
            if(h[l]<=h[r]):
                print(f"{lm},{rm}", end=" ")
                ans+=min(lm,rm)-h[l]
                print(f"loop1->{l},{r},{ans}")
                l+=1
                lm=max(lm,h[l])
            else:
                print(f"{lm},{rm}",end=" ")
                ans+=min(lm,rm)-h[r]
                print(f"loop2->{l},{r},{ans}")
                r-=1
                rm=max(rm,h[r])
        return ans