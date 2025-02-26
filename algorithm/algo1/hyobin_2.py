class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        word_len = len(word)
        
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        if any(word_count[ch] > board_count.get(ch, 0) for ch in word_count):
            return False
        
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, idx):
            if idx == word_len:
                return True
            
            if not (0 <= row < rows and 0 <= col < cols) or visited[row][col] or board[row][col] != word[idx]:
                return False
            
            visited[row][col] = True

            found = (dfs(row - 1, col, idx + 1) or
                     dfs(row + 1, col, idx + 1) or
                     dfs(row, col - 1, idx + 1) or
                     dfs(row, col + 1, idx + 1))

            visited[row][col] = False
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
