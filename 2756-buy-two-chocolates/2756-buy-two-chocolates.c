int buyChoco(int* prices, int pricesSize, int money){
  int minMoney = -1;
    int n = pricesSize;

    for (int i = 0; i < n-1; i++){
        for (int j = i+1; j < n; j++){
            int diff = money - prices[i] - prices [j];
            if (diff >= 0 && diff > minMoney){
                minMoney = diff;
            }
        }
    }

    if (minMoney == -1){
        return money;
    } 
    else{
        return minMoney;
    }
}