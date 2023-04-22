class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm:dict[int] = dict()
        for i,v in enumerate(nums):
            if target-v in hm:
                return [hm[target-v], i]
            hm[v] = i
        return []