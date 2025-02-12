class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * 5

        for _ in range(n):
            for i in range(3, -1, -1):
                dp[i] += dp[i+1]
                
        return dp[0]
