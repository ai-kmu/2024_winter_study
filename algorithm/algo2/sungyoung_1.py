class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        sub = 1
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j], dp[i] + 1)
                sub = max(sub, dp[j])
                
        return sub
        