class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = 0
        for index, num in enumerate(nums):
            if index > target:
                return False
            target = max(target, index + num)
            if target >= len(nums) - 1:
                return True
        return False
