# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 결과 리스트 초기화
        result = []
        # 루트가 None이면 빈 리스트 반환
        if not root:
            return result
        
        # BFS를 위한 큐 초기화 (큐에 노드와 레벨을 함께 저장)
        queue = deque([(root, 0)])
        
        # 현재 레벨을 추적하기 위한 변수
        current_level = -1
        
        # BFS 수행
        while queue:
            # 큐에서 노드와 해당 레벨을 꺼냄
            node, level = queue.popleft()
            
            # 새로운 레벨에 도달하면 결과 리스트에 추가
            if level > current_level:
                result.append(node.val)
                current_level = level
            
            # 오른쪽 자식부터 큐에 추가 (오른쪽 자식이 먼저 탐색되도록 하기)
            if node.right:
                queue.append((node.right, level + 1))
            # 왼쪽 자식 추가하기
            if node.left:
                queue.append((node.left, level + 1))
        
        return result    