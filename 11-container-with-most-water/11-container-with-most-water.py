class Solution:
    def maxArea(self, h: List[int]) -> int:
        i: int = 0
        j: int = len(h)-1
        maxarea:int = 0
        while i<j:
            maxarea=max(maxarea,min(h[i],h[j])*(j-i))
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return maxarea