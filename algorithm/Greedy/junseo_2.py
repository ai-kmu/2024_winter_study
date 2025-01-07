class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_r = 0
        
        for i, jump in enumerate(nums):
            if i > max_r:
                return False
            max_r = max(max_r, i + jump)
            if max_r >= len(nums) - 1:
                return True
        return False