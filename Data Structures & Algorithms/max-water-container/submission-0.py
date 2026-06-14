class Solution:
    def maxArea(self, h: List[int]) -> int:
        i,j=0,len(h)-1
        area=0
        while(i<j):
            area=max(area,min(h[j],h[i])*(j-i))
            if(h[i]<=h[j]):
                i+=1
            else:
                j-=1
        return area