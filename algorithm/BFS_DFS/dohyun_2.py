class Solution(object):
    def rightSideView(self, root):
        result = []
        def dfs(root, height):
            if root is None:
                return
            else:
                if height > len(result):
                    result.append(root.val)
                dfs(root.right, height + 1)
                dfs(root.left, height + 1)
        dfs(root, 1)
        return result
