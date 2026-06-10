class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            dict[i]=dict.get(i,0)+1
        # res=[]
        # for i,cnt in dict.items():
        #     res.append([cnt,i])
        # res.sort()
        # ans=[]
        # for i in range(k):
        #     ans.append(res.pop()[1])
        # return ans
        for i,cnt in dict.items():
            freq[cnt].append(i)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res