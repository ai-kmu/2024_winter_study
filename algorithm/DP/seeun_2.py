class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]

        for j in range(5):
            dp[1][j] = 1

        for i in range(1, n + 1):
            for j in range(5):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return sum(dp[n])
