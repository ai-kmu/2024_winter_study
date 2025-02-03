class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [0] * len(points)
        for i in range(len(points)):
            parent[i] = i
        
        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]
        
        def union_parent(parent, a, b):
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        edges = []
        total_cost = 0
        connected_edges = 0

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))
        
        edges.sort()

        for cost, a, b in edges:
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                total_cost += cost
                connected_edges += 1
                
                if connected_edges == len(points) - 1:
                    break

        return(total_cost)
