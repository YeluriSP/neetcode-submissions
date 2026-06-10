class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if(n!=m):
            return False
        seen={}
        for i in s:
            seen[i]=seen.get(i, 0) + 1
        for i in t:
            a=seen.get(i,0)
            if a ==0:
                return False
            seen[i]-=1
        return True