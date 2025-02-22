class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1) + 1
        l2 = len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]

        for i in range(1, l2):
            dp[0][i] = i

        for i in range(1, l1):
            dp[i][0] = i

        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
