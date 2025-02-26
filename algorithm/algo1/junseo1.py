from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 시작점이 장애물일 경우 경로는 없음
        if obstacleGrid[0][0] == 1:
            return 0

        # DP 테이블 초기화
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # 시작 위치는 1개의 방법으로 도달 가능

        # 첫 번째 행 초기화
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # 첫 번째 열 초기화
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # DP 테이블 채우기
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]