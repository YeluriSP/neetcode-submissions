class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> a;
        for (int i=0;i<nums.size();i++){
            a.push_back({nums[i],i});
        }
        sort(a.begin(),a.end());
        int i=0,j=a.size()-1;
        while(i<j){
            if(a[i].first+a[j].first==target){
                return {min(a[i].second,a[j].second),
                max(a[j].second,a[i].second)};
            }
            else if(a[i].first+a[j].first<target){
                i++;
            }
            else{
                j--;
            }
        }
        return {};
    }
};
