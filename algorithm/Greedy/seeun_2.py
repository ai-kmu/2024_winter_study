class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx = 0
        for idx, jump in enumerate(nums):
            if idx > maxidx:
                return False
            maxidx = max(maxidx, idx + jump)
            if maxidx >= len(nums) - 1:
                return True
        return False
