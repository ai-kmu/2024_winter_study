from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost = [0] + [float('inf')] * (n)
        cost[k] = 0 
        graph = defaultdict(list)
        
        for u, v, t in times:
            graph[u].append((v, t))

        q = deque([k])

        while q:
            node = q.popleft()
            for ne, co in graph[node]:
                if cost[ne] > cost[node] + co:  
                    cost[ne] = cost[node] + co
                    q.append(ne)

        ans = max(cost) 
        return ans if ans != float('inf') else -1
