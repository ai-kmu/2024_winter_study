class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        data = {}
        for index, num in enumerate(nums):
            if target - num in data:
                return [data[target - num], index]
            data[num] = index
