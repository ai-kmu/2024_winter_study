class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root == None:
            return []
        result = []
        queue = [root]
        index = 0
        while index != len(queue):
            currentLevel = len(queue)
            while index != currentLevel:
                item = queue[index]
                if item.left != None:
                    queue.append(item.left)
                if item.right != None:
                    queue.append(item.right)
                index += 1
            result.append(item.val)
        return result
