class Solution:
    def maxArea(self, h: List[int]) -> int:
        i,j,maxarea = 0, len(h)-1, 0
        while i<j:
            maxarea=max(maxarea,min(h[i],h[j])*(j-i))
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return maxarea