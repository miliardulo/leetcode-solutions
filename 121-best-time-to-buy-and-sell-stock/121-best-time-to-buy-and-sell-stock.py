class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mpf: int = 0
        pp: int = prices[0] # purchase price
        for i in prices:
            if i-pp>mpf:
                mpf = i-pp
            elif pp>i:
                pp=i
        return mpf             