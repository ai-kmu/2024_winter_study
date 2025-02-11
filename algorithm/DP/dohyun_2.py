class Solution(object):
    def countVowelStrings(self, n): 
        dp = [[0] * 6 for _ in range(n + 1)]

        for i in range(6):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(1, 6):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][5]
