class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = (1 + n) * n // 2
        return total - sum(nums)
        