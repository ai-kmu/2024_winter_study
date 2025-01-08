class Solution:
    def canJump(self, nums):
        mx = 0
        for i, length in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i + length)
        return mx >= len(nums) - 1
