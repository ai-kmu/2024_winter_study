class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def dfs(root):
            if root is None:
                return
            else:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)
        dfs(root)
        return result
