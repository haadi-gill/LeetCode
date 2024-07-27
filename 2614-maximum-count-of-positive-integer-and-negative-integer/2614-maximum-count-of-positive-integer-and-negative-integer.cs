public class Solution {
    public int MaximumCount(int[] nums) {
       int maxCount = 0;
        int minCount = 0;

        for(int i = 0; i < nums.Length; i ++){
            if (nums[i] < 0){
                minCount += 1;
            }
            if (nums[i] > 0){
                maxCount += 1;
            }
        }

        if (maxCount > minCount){
            return maxCount;
        }
        return minCount;
    }
}