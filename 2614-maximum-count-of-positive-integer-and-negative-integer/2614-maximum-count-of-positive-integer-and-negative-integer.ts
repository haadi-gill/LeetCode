function maximumCount(nums: number[]): number {
     var maxCount = 0;
        var minCount = 0;

        for(var i = 0; i < nums.length; i ++){
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
};