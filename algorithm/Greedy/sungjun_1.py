class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [i, map[diff]]
            map[num] = i

        
