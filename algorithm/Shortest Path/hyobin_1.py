class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for i, v in enumerate(edges):
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        edge = source
        visited[edge] = True

        queue = [edge]

        while queue:
            edge = queue[0]
            queue.pop(0)

            if edge == destination:
                return True
            
            for i, v in enumerate(graph[edge]):
                if visited[v] == False:
                    visited[v] = True
                    queue.append(v)
    
        return False
