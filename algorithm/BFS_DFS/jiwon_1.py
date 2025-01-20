class Solution:
    def task(self, node: TreeNode | None, result: list[int]) -> list[int]:
        if node == None:
            return result
        self.task(node.left, result)
        result.append(node.val)
        self.task(node.right, result)
        return result

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        return self.task(root, [])
