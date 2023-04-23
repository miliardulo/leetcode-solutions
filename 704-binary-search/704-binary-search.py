class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front:int = 0
        back:int = len(nums)-1
        while front<=back:
            mid:int = front + (back-front)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                front = mid+1
            else:
                back=mid-1
        return -1
            