/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
        var minPrice = 999999999;
        var maxProfit = 0;

        for (var i = 0; i < prices.length; i++){
            var p = prices[i];
            if (p < minPrice){
                minPrice = p;
            }
            
            var profit = p - minPrice;

            if (profit > maxProfit){
                maxProfit = profit;
            }
        }

        return maxProfit;
};