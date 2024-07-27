class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int maxCount = 0;
        int minCount = 0;

        for(int i = 0; i < nums.size(); i ++){
            if (nums[i] < 0){
                minCount += 1;
            }
            if (nums[i] > 0){
                maxCount += 1;
            }
        }

        return max(minCount, maxCount);
    }
};