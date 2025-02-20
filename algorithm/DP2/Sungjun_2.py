class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1

        table = array = [[0] * m for _ in range(n)]

        for i in range(1, n):
            table[i][0] = i
        
        for i in range(1, m):
            table[0][i] = i

        for i in range(1, n):
            for j in range(1, m):
                if(word1[i-1] == word2[j-1]): 
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(table[i-1][j-1], table[i-1][j], table[i][j-1]) + 1

        return table[n-1][m-1]

        
