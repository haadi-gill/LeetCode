class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int minPrice = 999999999;
        int maxProfit = 0;

        for (int i = 0; i < prices.size(); i++){
            int p = prices[i];
            if (p < minPrice){
                minPrice = p;
            }
            
            int profit = p - minPrice;

            if (profit > maxProfit){
                maxProfit = profit;
            }
        }

        return maxProfit;

    }
};