class Solution(object):
    def exist(self, board, word):
        y, x = len(board), len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if i < 0 or i >= y or j < 0 or j >= x or board[i][j] != word[idx]:
                return False
            temp, board[i][j] = board[i][j], True
            if (dfs(i - 1, j, idx + 1) or dfs(i + 1, j, idx + 1) 
            or dfs(i, j - 1, idx + 1) or dfs(i, j + 1, idx + 1)):
                return True
            board[i][j] = temp
            return False

        for i in range(y):
            for j in range(x):
                if dfs(i, j, 0):
                    return True
        return False
