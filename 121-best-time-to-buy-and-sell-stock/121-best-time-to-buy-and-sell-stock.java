class Solution {
    public int maxProfit(int[] prices) {
        Queue<Integer> pq = new PriorityQueue<>();
        int mpf = 0;
        for(int i: prices){
            if(!pq.isEmpty() && i-pq.peek()>mpf) mpf=i-pq.peek();
            pq.add(i);
        }
        return mpf;
    }
}