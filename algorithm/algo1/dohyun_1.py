class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        y = len(obstacleGrid)
        x = len(obstacleGrid[0])
        dp = [[0] * (x + 1) for _ in range(y + 1)]
        dp[0][1] = 1
        for i in range(1, y + 1):
            for j in range(1, x + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[y][x]
