class Solution(object):
    def minDistance(self, word1, word2):
        nwd1 = len(word1)
        nwd2 = len(word2)
        dp = [[i + j for i in range(nwd2 + 1)] for j in range(nwd1 + 1)]
        for i in range(1, nwd1 + 1):
            for j in range(1, nwd2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1,
                                   dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1)
        return dp[nwd1][nwd2]
