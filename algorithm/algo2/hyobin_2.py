class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        def cal(sum_nums, nums):
            for num in nums:
                sum_nums -= num
            return sum_nums

        if n == 1:
            return cal(n, nums)

        elif n % 2 == 0:
            sum_nums = (n + 1) * n // 2
            return cal(sum_nums, nums)
        
        else:
            sum_nums = n * (n - 1) // 2 + n
            return cal(sum_nums, nums)
