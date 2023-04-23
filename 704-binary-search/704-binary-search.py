class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front:int = 0
        back:int = len(nums)-1
        while front<=back:
            mid:int = front + (back-front)//2
            x:int = nums[mid]
            if x==target:
                return mid
            if x<target:
                front = mid+1
                continue
            back=mid-1
        return -1
            