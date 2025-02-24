class Solution:
    def exist(self, board, word):
        if not board:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            # 단어를 모두 찾은 경우
            if k == len(word):
                return True
            # 범위를 벗어나거나 문자가 일치하지 않는 경우
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'  # 방문 표시
            
            # 상, 하, 좌, 우로 탐색
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            # 원상복구
            board[i][j] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
