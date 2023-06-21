class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lw1, lw2 = len(word1), len(word2)
        tb :List[List[int]] = [[0 for _ in range(lw1+1)] for _ in range(lw2+1)]
        for i in range(lw1+1):
            tb[0][i] = i
        for i in range(lw2+1):
            tb[i][0] = i
        for r in range(1,lw2+1):
            for c in range(1,lw1+1):
                tb[r][c] = tb[r-1][c-1] if word1[c-1] == word2[r-1] else min(tb[r-1][c], tb[r][c-1], tb[r-1][c-1]) + 1
        return tb[-1][-1]
        
            