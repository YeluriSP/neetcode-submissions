class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        dict_map={}
        i=0
        for s in strs:
            a="".join(sorted(s))
            if a in dict_map:
                idx=dict_map[a]
                ans[idx].append(s)
            else:
                dict_map[a]=i
                idx=i
                i=i+1
                lis=[s]
                ans.append(lis)
        return ans