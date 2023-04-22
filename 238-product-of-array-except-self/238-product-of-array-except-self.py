class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n:int = len(nums)
        lprod:list[int] = [1]*n
        rprod:list[int] = [1]*n
        lprod[0] = 1
        for i in range(1,n):
            lprod[i] = lprod[i-1]*nums[i-1]
        rprod[-1] = 1
        for i in range(-2,-n-1,-1):
            rprod[i] = rprod[i+1]*nums[i+1]
        return [lprod[i]*rprod[i] for i in range(n)]
        