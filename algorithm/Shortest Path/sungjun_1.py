class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(s, e, visited):
            if s == e: return True
            elif s in visited : return False
            
            visited.add(s)
            for ne in graph[s]:
                if dfs(ne, e, visited) : return True

            return False

        visited = set()
        return dfs(source, destination, visited)
