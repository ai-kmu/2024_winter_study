class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1 for _ in range(5)]
        
        for _ in range(n):
            for i in range(4, 0, -1):
                dp[i-1] = dp[i-1] + dp[i]

        return dp[0]
