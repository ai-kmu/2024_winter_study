class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            for idx, value in enumerate(nums):
                if value == temp and idx != i:
                    j = idx
                    return [i, j]
            
