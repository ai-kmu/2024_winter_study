class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = list([1 for _ in range(5)] for _ in range(n))

        for i in range(1, n):
            dp[i][0] = sum(dp[i - 1])
            
            for j in range(1, 5):
                dp[i][j] = dp[i][j-1] - dp[i-1][j-1]

        return sum(dp[n - 1])
