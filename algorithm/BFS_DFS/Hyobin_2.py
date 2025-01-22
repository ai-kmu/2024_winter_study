# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:        
        def dfs(node):
            nonlocal level, tmp
            if node:
                if level == tmp:
                    result.append(node.val)
                    level += 1
                tmp += 1
                dfs(node.right)
                dfs(node.left)
                tmp -= 1

        result = []
        level = -1
        tmp = -1

        dfs(root)
        return result
