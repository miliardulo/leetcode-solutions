class Solution {
    public int maxProfit(int[] prices) {
        int mpf = 0;
        int prev = prices[0];        
        for(int i=1; i<prices.length; i++){
            if(prices[i]<prev) prev = prices[i];
            else mpf = Math.max(mpf,prices[i]-prev);
        }
        return mpf;
    }
}