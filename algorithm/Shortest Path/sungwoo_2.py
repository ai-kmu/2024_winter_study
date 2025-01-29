class Solution:
    def networkDelayTime(self, times, n, k):
        """
        times : List[List[int]]
        n     : int
        k     : int
        return: int
        """
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        INF = 999999999
        dist = [INF] * (n+1)
        dist[k] = 0
        visited = [False] * (n+1)
        
        for _ in range(n):
            node = -1
            min_dist = INF
            
            for i in range(1, n+1):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    node = i
            
            if node == -1:
                break
            
            visited[node] = True
            
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
        
        answer = max(dist[1:])
        return answer if answer != INF else -1
