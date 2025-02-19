class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP =[[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    DP[i][j] = 1
                elif j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i][j-1] + DP[i-1][j]
        
        return DP[m-1][n-1]
