class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls :int = 0
        rs :int = sum(nums)
        for i in range(len(nums)):
            rs-=nums[i]
            if ls==rs:
                return i
            ls+=nums[i]
        return -1