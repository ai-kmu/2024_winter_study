class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_n = 0
        for i, num in enumerate(nums):
            if(i > max_n): return False
            max_n = max(max_n, num + i)
        return True
