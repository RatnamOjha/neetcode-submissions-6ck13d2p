class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> s;

        for(int i = 0; i < nums.size(); i++){
            int num = target - nums[i];

            if (s.count(num)){
                return {s[num],i};
            }
            s[nums[i]] = i;
        }
        return{};
    }
};
