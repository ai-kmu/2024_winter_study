# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        max_depth = -1

        def dfs(root, depth):
            nonlocal max_depth
            if(root == None): return
            else:
                if depth > max_depth: 
                    ans.append(root.val)
                    max_depth = depth

                dfs(root.right, depth + 1)
                dfs(root.left, depth + 1)

        dfs(root, 0)
        return ans
