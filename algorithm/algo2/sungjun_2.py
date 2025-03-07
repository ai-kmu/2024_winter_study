class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        check = [0] * (n + 1)

        for i in nums:
            check[i] = 1
        
        for ans, i in enumerate(check):
            if not i:
                return ans
