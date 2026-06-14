class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        a=1
        for i in range(len(nums)-1,-1,-1):
            a=a*nums[i]
            lst.append(a)
        lst.reverse()
        ans=[]
        ans.append(lst[1])
        a=1
        for i in range(1,len(nums)-1,):
            a=a*nums[i-1]
            ans.append(lst[i+1]*a)
        a=a*nums[-2]
        ans.append(a)
        return ans