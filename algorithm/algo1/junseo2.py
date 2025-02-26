from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        
        def backtrack(i, j, index):
            # 단어를 모두 찾았을 경우
            if index == len(word):
                return True
            
            # 범위를 벗어나거나, 현재 문자가 일치하지 않거나, 이미 방문한 경우
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            # 현재 위치의 문자를 저장하고 방문 처리
            temp = board[i][j]
            board[i][j] = "#"  # 방문 표시
            
            # 상, 하, 좌, 우 이동하면서 단어 찾기
            found = (backtrack(i+1, j, index+1) or
                     backtrack(i-1, j, index+1) or
                     backtrack(i, j+1, index+1) or
                     backtrack(i, j-1, index+1))

            # 원래 문자로 복원
            board[i][j] = temp
            return found
        
        # 모든 위치에서 시작 가능
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):  # 단어의 첫 글자부터 탐색
                    return True
        return False