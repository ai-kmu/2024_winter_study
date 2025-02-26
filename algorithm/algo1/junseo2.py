from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        
        def backtrack(i, j, index):
            if index == len(word):
                return True
            

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False


            temp = board[i][j]
            board[i][j] = "#"  
            
            found = (backtrack(i+1, j, index+1) or
                     backtrack(i-1, j, index+1) or
                     backtrack(i, j+1, index+1) or
                     backtrack(i, j-1, index+1))


            board[i][j] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):  
                    return True
        return False