# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 결과를 저장할 리스트
        result = []
        # 노드 방문 순서를 추적하기 위한 스택
        stack = []
        # 현재 처리 중인 노드를 나타내는 변수
        current = root
        
        # current가 None이 아니거나 스택에 노드가 남아있을 때까지 반복
        while current or stack:
            # 왼쪽 서브트리 탐색
            while current:
                # 현재 노드를 스택에 추가 (나중에 되돌아오기 위해)
                stack.append(current)
                # 왼쪽 자식으로 이동
                current = current.left
            
            # 왼쪽 끝에 도달했거나 스택에서 노드를 꺼내 처리
            current = stack.pop()  # 스택에서 가장 마지막에 추가된 노드 꺼내기
            result.append(current.val)  # 해당 노드의 값을 결과 리스트에 추가
            
            # 오른쪽 서브트리로 이동
            current = current.right  # 현재 노드를 오른쪽 자식으로 업데이트
        
        # 최종적으로 중위 순회를 완료한 결과를 반환
        return result