class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        DP = [[0 for _ in range(5)] for _ in range(n+2)]

        for i in range(1, n+2):
            for j in range(5):
                if i == 1 or j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        
        # print(DP[n+1][4])

        return DP[n+1][4]
