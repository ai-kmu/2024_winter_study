class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n-1][m-1]
