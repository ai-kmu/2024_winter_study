from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        queue, answer = deque(), []
        queue.append(root)
        
        while queue:
            level_size = len(queue)  
            
            for i in range(level_size):
                cur = queue.popleft()
                
                if i == level_size - 1:
                    answer.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return answer
