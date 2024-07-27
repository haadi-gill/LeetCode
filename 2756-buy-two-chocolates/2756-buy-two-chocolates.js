/**
 * @param {number[]} prices
 * @param {number} money
 * @return {number}
 */
var buyChoco = function(prices, money) {
    var minMoney = -1;
    var n = prices.length;

    for (var i = 0; i < n-1; i++){
        for (var j = i+1; j < n; j++){
            var diff = money - prices[i] - prices [j];
            if (diff >= 0 && diff > minMoney){
                minMoney = diff;
            }
        }
    }

    if (minMoney === -1){
        return money;
    } 
    else{
        return minMoney;
    }

};